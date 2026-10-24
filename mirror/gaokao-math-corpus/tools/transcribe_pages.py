"""Submit a paper's page images to one Codex transcription session.

Usage (run from the repository root)::

    uv run python tools/transcribe_pages.py work/2024-I \
        --year 2024 --volume I --proxy http://127.0.0.1:???? \
        --bypass-codex-sandbox

All selected images are submitted in page order to one agent session.  By
default the selected range is the complete image directory; ``--start-page``
and ``--end-page`` are available only for an intentional partial rerun.
Use ``--dry-run`` to inspect the generated prompt and command without calling
Codex.  The script may read the Windows system proxy, but a local proxy can be
provided explicitly with ``--proxy``.
"""

from __future__ import annotations

import argparse
import ctypes
from ctypes import wintypes
import os
import re
import subprocess
import sys
from pathlib import Path


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
DEFAULT_MODEL = "gpt-5.5"
DEFAULT_REASONING_EFFORT = "low"
PROXY_ENV_VARS = ("HTTPS_PROXY", "HTTP_PROXY", "ALL_PROXY")


class WinHttpCurrentUserIeProxyConfig(ctypes.Structure):
    _fields_ = [
        ("fAutoDetect", wintypes.BOOL),
        ("lpszAutoConfigUrl", ctypes.c_wchar_p),
        ("lpszProxy", ctypes.c_wchar_p),
        ("lpszProxyBypass", ctypes.c_wchar_p),
    ]


def natural_key(path: Path) -> list[int | str]:
    parts = re.split(r"(\d+)", path.stem)
    key: list[int | str] = []
    for part in parts:
        if part.isdigit():
            key.append(int(part))
        elif part:
            key.append(part.lower())
    key.append(path.suffix.lower())
    return key


def two_digit(value: int) -> str:
    if value < 1 or value > 99:
        raise ValueError(f"page/item numbers must be between 1 and 99, got {value}")
    return f"{value:02d}"


def collect_images(image_dir: Path) -> list[Path]:
    images = [
        path
        for path in image_dir.iterdir()
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
    ]
    return sorted(images, key=natural_key)


def infer_paper_scheme_id(year: int) -> str:
    if 2021 <= year <= 2023:
        return "new_gaokao_legacy"
    if 2024 <= year <= 2026:
        return "new_gaokao_current"
    raise ValueError(
        "Cannot infer paper_scheme_id for this year. "
        "Pass --paper-scheme-id explicitly."
    )


def canonical_paper_title(year: int, volume: str) -> str:
    return f"{year}年普通高等学校招生全国统一考试 数学 ({volume}卷)"


def parse_windows_proxy_server(proxy_server: str) -> dict[str, str]:
    if not proxy_server:
        return {}
    if "=" not in proxy_server:
        proxy = proxy_server
        if "://" not in proxy:
            proxy = f"http://{proxy}"
        return {
            "HTTP_PROXY": proxy,
            "HTTPS_PROXY": proxy,
            "ALL_PROXY": proxy,
        }

    proxies: dict[str, str] = {}
    for part in proxy_server.split(";"):
        if "=" not in part:
            continue
        scheme, value = part.split("=", 1)
        scheme = scheme.strip().lower()
        value = value.strip()
        if not value:
            continue
        if "://" not in value:
            value = f"http://{value}"
        if scheme == "http":
            proxies["HTTP_PROXY"] = value
        elif scheme == "https":
            proxies["HTTPS_PROXY"] = value
        elif scheme in {"socks", "socks5"}:
            proxies["ALL_PROXY"] = value
    if "HTTPS_PROXY" in proxies and "HTTP_PROXY" not in proxies:
        proxies["HTTP_PROXY"] = proxies["HTTPS_PROXY"]
    if "HTTP_PROXY" in proxies and "HTTPS_PROXY" not in proxies:
        proxies["HTTPS_PROXY"] = proxies["HTTP_PROXY"]
    if "ALL_PROXY" not in proxies:
        proxies["ALL_PROXY"] = proxies.get("HTTPS_PROXY") or proxies.get("HTTP_PROXY", "")
    return {key: value for key, value in proxies.items() if value}


def parse_wininet_connection_settings(data: bytes | bytearray) -> dict[str, str]:
    if len(data) < 16:
        return {}
    proxy_length = int.from_bytes(bytes(data[12:16]), "little", signed=False)
    if proxy_length <= 0 or len(data) < 16 + proxy_length:
        return {}
    proxy_bytes = bytes(data[16 : 16 + proxy_length])
    try:
        proxy_server = proxy_bytes.decode("utf-8")
    except UnicodeDecodeError:
        proxy_server = proxy_bytes.decode("latin-1", errors="ignore")
    return parse_windows_proxy_server(proxy_server)


def read_windows_system_proxy() -> dict[str, str]:
    if sys.platform != "win32":
        return {}
    proxies: dict[str, str] = {}
    try:
        import winreg

        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Internet Settings",
        ) as key:
            proxy_enabled, _ = winreg.QueryValueEx(key, "ProxyEnable")
            if proxy_enabled:
                proxy_server, _ = winreg.QueryValueEx(key, "ProxyServer")
                proxies.update(parse_windows_proxy_server(str(proxy_server)))
    except OSError:
        pass

    try:
        import winreg

        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Internet Settings\Connections",
        ) as key:
            for value_name in ("DefaultConnectionSettings", "SavedLegacySettings"):
                try:
                    settings, _ = winreg.QueryValueEx(key, value_name)
                except OSError:
                    continue
                proxies.update(parse_wininet_connection_settings(settings))
    except OSError:
        pass

    try:
        config = WinHttpCurrentUserIeProxyConfig()
        ok = ctypes.windll.winhttp.WinHttpGetIEProxyConfigForCurrentUser(
            ctypes.byref(config)
        )
        if ok and config.lpszProxy:
            proxies.update(parse_windows_proxy_server(config.lpszProxy))
    except (AttributeError, OSError):
        pass

    return proxies


def build_subprocess_env(
    *,
    explicit_proxy: str | None,
    use_system_proxy: bool,
) -> tuple[dict[str, str], str]:
    env = os.environ.copy()
    if explicit_proxy:
        proxy = explicit_proxy if "://" in explicit_proxy else f"http://{explicit_proxy}"
        for name in PROXY_ENV_VARS:
            env[name] = proxy
            env[name.lower()] = proxy
        return env, "explicit"

    if any(env.get(name) or env.get(name.lower()) for name in PROXY_ENV_VARS):
        return env, "environment"

    if use_system_proxy:
        system_proxy = read_windows_system_proxy()
        if system_proxy:
            env.update(system_proxy)
            env.update({key.lower(): value for key, value in system_proxy.items()})
            return env, "windows-system"

    return env, "none"


def format_page_list(page_images: list[tuple[int, Path]]) -> str:
    return "\n".join(
        f"- 第 {page_number} 页：{image_path.name}"
        for page_number, image_path in page_images
    )


def build_prompt(
    *,
    year: int,
    volume: str,
    paper_scheme_id: str,
    page_images: list[tuple[int, Path]],
    target_root: Path,
) -> str:
    page_summary = format_page_list(page_images)
    page_numbers = ", ".join(str(page_number) for page_number, _ in page_images)
    title = canonical_paper_title(year, volume)

    return f"""你正在为“新高考数学试题知识库”执行页面转录任务。

必须先遵守并读取这些项目规则：
- AGENTS.md
- docs/TRANSCRIPTION_RULES.md
- docs/DATA_FORMAT.md
- config/agents/transcription.yml
- config/status.yml
- config/paper_schemes/{paper_scheme_id}.yml

任务对象：
- 年份：{year}
- 卷种：{volume}
- paper_scheme_id：{paper_scheme_id}
- 规范试卷标题：{title}
- 本次处理页序号：{page_numbers}
- 本次提交图片：
{page_summary}
- 目标试卷目录：{target_root.as_posix()}

执行规则：
1. 按图片文件名的自然顺序处理本次提交的所有页面。
2. 本次提交的图片是一份完整的试卷。
3. 直接修改目标文件，不要在最终回复中重复输出完整题目。
4. 数据清洗阶段不得添加答案、解析、知识点、难度、解题方法或手工分值。
5. 创建题目文件使用两位题号，例如 items/01.md，题目 ID 如 {year}-{volume}-01。
6. 图片和表格都使用原图裁剪，文件名使用两位编号，例如 01-fig-01.png、01-table-01.png。先确定源页面图片中的像素裁剪框，再只使用 `uv run python tools/crop_asset.py SOURCE OUTPUT --box LEFT TOP RIGHT BOTTOM` 执行一次裁剪；不要自行寻找其他截图或裁剪方法。裁剪范围应只包含题目所需图形或表格，并保留必要标注。
7. 遇到无法确认的文字、公式、图形或表格，使用 [待确认：...] 并写入 uncertain_notes，不得猜测。
8. 题目正文、选项和说明文字统一使用西文风格标点符号，例如 `, . ; : ? ! ( )`；数学公式按 LaTeX 习惯处理。
9. Markdown 正文中的 LaTeX 命令必须使用单反斜杠，例如 `\\dfrac`, `\\sqrt`, `\\mathbb`；不得写成 `\\\\dfrac`, `\\\\sqrt`, `\\\\mathbb`。
10. YAML front matter 中含 LaTeX 的选项或字段优先使用单引号字符串，例如 `A: '$\\dfrac{{1}}{{2}}$'`，避免为了 YAML 双引号转义写出双反斜杠。
11. 本次提交的是整份试卷，完整建立或更新该试卷的 paper.yml、items/ 和 assets/。
12. paper.yml 的 title 必须使用上方“规范试卷标题”, 由年份和卷种生成；不要从页面 OCR 或社区排版标题读取。

最终回复只报告：
- 修改了哪些文件；
- 本次检查结果；
- 待确认事项。
"""


def build_codex_command(
    *,
    codex_bin: str,
    workspace: Path,
    prompt_file: bool,
    images: list[Path],
    output_file: Path,
    model: str | None,
    reasoning_effort: str | None,
    profile: str | None,
    sandbox: str,
    bypass_codex_sandbox: bool,
    extra_args: list[str],
) -> list[str]:
    cmd = [
        codex_bin,
        "exec",
        "-C",
        str(workspace),
        "--output-last-message",
        str(output_file),
    ]
    if bypass_codex_sandbox:
        cmd.append("--dangerously-bypass-approvals-and-sandbox")
    else:
        cmd.extend(["--sandbox", sandbox])
    if model:
        cmd.extend(["--model", model])
    if reasoning_effort:
        cmd.extend(["-c", f'model_reasoning_effort="{reasoning_effort}"'])
    if profile:
        cmd.extend(["--profile", profile])
    cmd.extend(extra_args)
    for image in images:
        cmd.extend(["--image", str(image)])
    cmd.append("-" if prompt_file else "")
    return [part for part in cmd if part]


def response_indicates_execution_failure(response_path: Path) -> bool:
    if not response_path.exists():
        return False
    text = response_path.read_text(encoding="utf-8", errors="replace")
    failure_markers = [
        "未能执行",
        "拒绝访问",
        "sandbox 初始化失败",
        "sandbox initialization failed",
        "orchestrator_helper_launch_failed",
    ]
    return any(marker in text for marker in failure_markers)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Submit all selected paper page images to one codex exec session. "
            "By default, the whole image directory is treated as one paper."
        )
    )
    parser.add_argument("image_dir", type=Path, help="Directory containing page images.")
    parser.add_argument("--year", type=int, required=True, help="Paper year, e.g. 2024.")
    parser.add_argument("--volume", choices=["I", "II"], required=True, help="Paper volume.")
    parser.add_argument(
        "--paper-scheme-id",
        choices=["new_gaokao_legacy", "new_gaokao_current"],
        help="Defaults from --year when omitted.",
    )
    parser.add_argument(
        "--workspace",
        type=Path,
        default=Path.cwd(),
        help="Repository root passed to codex exec -C.",
    )
    parser.add_argument(
        "--target-root",
        type=Path,
        help="Target paper directory. Defaults to corpus/papers/{year}/{volume}.",
    )
    parser.add_argument(
        "--log-dir",
        type=Path,
        default=Path("work/transcription_runs"),
        help="Directory for prompts and final agent messages.",
    )
    parser.add_argument("--codex-bin", default="codex", help="Codex executable.")
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help="Codex model for page transcription. Defaults to the smallest sufficient configured model.",
    )
    parser.add_argument(
        "--reasoning-effort",
        default=DEFAULT_REASONING_EFFORT,
        choices=["low", "medium", "high"],
        help="Reasoning effort for OCR-style transcription. Defaults to low.",
    )
    parser.add_argument("--profile", help="Optional codex config profile.")
    parser.add_argument(
        "--proxy",
        help=(
            "Proxy URL for nested codex exec, e.g. http://127.0.0.1:7890. "
            "If omitted, existing proxy environment variables or the Windows system proxy are used."
        ),
    )
    parser.add_argument(
        "--no-system-proxy",
        action="store_true",
        help="Do not read the Windows system proxy when proxy environment variables are absent.",
    )
    parser.add_argument(
        "--sandbox",
        default="workspace-write",
        choices=["read-only", "workspace-write", "danger-full-access"],
        help="Sandbox mode for each codex exec run.",
    )
    parser.add_argument(
        "--bypass-codex-sandbox",
        action="store_true",
        help=(
            "Pass --dangerously-bypass-approvals-and-sandbox to nested codex exec. "
            "Use only when the local Windows sandbox helper prevents nested agent execution."
        ),
    )
    parser.add_argument(
        "--start-page",
        type=int,
        default=1,
        help="1-based start page index for partial reruns.",
    )
    parser.add_argument(
        "--end-page",
        type=int,
        help="1-based inclusive end page index for partial reruns.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned commands and write prompts, but do not run codex exec.",
    )
    parser.add_argument(
        "--extra-codex-arg",
        action="append",
        default=[],
        help="Extra argument passed through to codex exec. Repeat for multiple args.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    workspace = args.workspace.resolve()
    image_dir = args.image_dir.resolve()
    if not image_dir.is_dir():
        raise SystemExit(f"Image directory does not exist: {image_dir}")

    images = collect_images(image_dir)
    if not images:
        raise SystemExit(f"No supported images found in {image_dir}")

    start = args.start_page
    end = args.end_page or len(images)
    if start < 1 or end < start or end > len(images):
        raise SystemExit(
            f"Invalid page range {start}..{end}; image count is {len(images)}"
        )

    paper_scheme_id = args.paper_scheme_id or infer_paper_scheme_id(args.year)
    target_root = args.target_root or Path("corpus/papers") / str(args.year) / args.volume
    target_root_display = target_root.as_posix()

    log_dir = args.log_dir if args.log_dir.is_absolute() else workspace / args.log_dir
    run_root = log_dir / f"{args.year}-{args.volume}"
    prompt_dir = run_root / "prompts"
    response_dir = run_root / "responses"
    prompt_dir.mkdir(parents=True, exist_ok=True)
    response_dir.mkdir(parents=True, exist_ok=True)
    subprocess_env, proxy_source = build_subprocess_env(
        explicit_proxy=args.proxy,
        use_system_proxy=not args.no_system_proxy,
    )
    print(
        f"model={args.model or '-'} reasoning_effort={args.reasoning_effort or '-'} proxy_source={proxy_source}"
    )

    selected_page_images = [
        (page_number, images[page_number - 1])
        for page_number in range(start, end + 1)
    ]
    page_label = (
        f"pages-{two_digit(start)}-{two_digit(end)}"
        if start != 1 or end != len(images)
        else "all-pages"
    )
    prompt = build_prompt(
        year=args.year,
        volume=args.volume,
        paper_scheme_id=paper_scheme_id,
        page_images=selected_page_images,
        target_root=Path(target_root_display),
    )
    prompt_path = prompt_dir / f"{page_label}.md"
    response_path = response_dir / f"{page_label}.md"
    prompt_path.write_text(prompt, encoding="utf-8")

    selected_images = [image_path for _, image_path in selected_page_images]
    cmd = build_codex_command(
        codex_bin=args.codex_bin,
        workspace=workspace,
        prompt_file=True,
        images=selected_images,
        output_file=response_path,
        model=args.model,
        reasoning_effort=args.reasoning_effort,
        profile=args.profile,
        sandbox=args.sandbox,
        bypass_codex_sandbox=args.bypass_codex_sandbox,
        extra_args=args.extra_codex_arg,
    )
    print(
        f"[pages {start}-{end}] images="
        + ", ".join(image_path.name for image_path in selected_images)
    )
    print(" ".join(cmd))
    if args.dry_run:
        return 0

    result = subprocess.run(
        cmd,
        input=prompt.encode("utf-8"),
        cwd=workspace,
        env=subprocess_env,
        check=False,
    )
    if result.returncode != 0:
        print(
            f"codex exec failed for pages {start}-{end} with exit code {result.returncode}",
            file=sys.stderr,
        )
        return result.returncode
    if response_indicates_execution_failure(response_path):
        print(
            f"codex exec response indicates execution failure for pages {start}-{end}; stopping.",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
