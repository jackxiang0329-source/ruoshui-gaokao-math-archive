.PHONY: build watermark encrypt clean

# 用法：
#   make build                 编译整个工程
#   make build chapters/导数/期中题目汇总.tex
#                              按相对路径编译指定的章节文件
#   make build 入题思路.tex    仍可按文件名编译（文件名必须唯一）
#   make watermark xxx.pdf 水印文字
#                              直接给指定 PDF 添加满屏斜向水印
#   make encrypt xxx.pdf       直接给指定 PDF 设置编辑权限密码
REQUESTED_TEX := $(word 2,$(MAKECMDGOALS))
PDF_PYTHON := $(shell \
	if python3 -c 'import pypdf, reportlab' >/dev/null 2>&1; then \
		command -v python3; \
	elif [ -x "$$HOME/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3" ]; then \
		printf '%s' "$$HOME/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"; \
	else \
		command -v python3; \
	fi)

build:
	@if [ -z "$(REQUESTED_TEX)" ]; then \
		xelatex -interaction=nonstopmode -halt-on-error elegantbook-cn.tex; \
	else \
		requested='$(REQUESTED_TEX)'; \
		case "$$requested" in \
			*/*) \
				requested="$${requested#./}"; \
				case "$$requested" in \
					chapters/*.tex) ;; \
					*) echo "错误：请传入 chapters 下的 .tex 文件路径"; exit 1 ;; \
				esac; \
				if [ ! -f "$$requested" ]; then \
					echo "错误：文件不存在：$$requested"; \
					exit 1; \
				fi; \
				matches="$$requested"; \
				;; \
			*) \
				matches="$$(find chapters -type f -name "$$requested" -print)"; \
				count="$$(printf '%s\n' "$$matches" | sed '/^$$/d' | wc -l | tr -d ' ')"; \
				if [ "$$count" -eq 0 ]; then \
					echo "错误：chapters 中没有找到 $$requested"; \
					exit 1; \
				elif [ "$$count" -gt 1 ]; then \
					echo "错误：找到多个同名文件，请改用完整相对路径，例如："; \
					printf '  make build %s\n' $$matches; \
					exit 1; \
				fi; \
				;; \
		esac; \
		relpath="$${matches#chapters/}"; \
		relpath="$${relpath%.tex}"; \
		stem="$${relpath##*/}"; \
		outdir="tmp/$$relpath"; \
		mkdir -p "$$outdir"; \
		wrapper="$$outdir/_standalone.tex"; \
		printf '%s\n' \
			'\documentclass[lang=cn,newtx,10pt,scheme=chinese]{elegantbook}' \
			'\definecolor{customcolor}{RGB}{32,178,170}' \
			'\usepackage{cprotect}' \
			'\begin{document}' \
			"\input{$$matches}" \
			'\end{document}' > "$$wrapper"; \
		xelatex -interaction=nonstopmode -halt-on-error \
			-output-directory="$$outdir" -jobname="$$stem" "$$wrapper"; \
		echo "PDF 已生成：$$outdir/$$stem.pdf"; \
	fi

# “make build 文件路径.tex”中的第二个参数会被 make 当作目标，
# 此规则将它标记为空操作，实际编译由 build 完成。
%.tex:
	@:

watermark:
	@if [ -z "$(word 2,$(MAKECMDGOALS))" ] || [ -z "$(word 3,$(MAKECMDGOALS))" ]; then \
		echo "用法：make watermark 文件.pdf 水印文字"; exit 1; \
	elif [ -n "$(word 4,$(MAKECMDGOALS))" ]; then \
		echo "错误：参数过多；水印文字如含空格，请改用不含空格的写法"; exit 1; \
	fi
	@"$(PDF_PYTHON)" scripts/watermark_pdf.py \
		"$(word 2,$(MAKECMDGOALS))" "$(word 3,$(MAKECMDGOALS))"

encrypt:
	@if [ -z "$(word 2,$(MAKECMDGOALS))" ]; then \
		echo "用法：make encrypt 文件.pdf"; exit 1; \
	elif [ -n "$(word 3,$(MAKECMDGOALS))" ]; then \
		echo "错误：encrypt 只接收一个 PDF 文件参数"; exit 1; \
	fi
	@"$(PDF_PYTHON)" scripts/encrypt_pdf.py "$(word 2,$(MAKECMDGOALS))"

# make 会把命令后的参数也解析为目标；在 watermark/encrypt 模式下将其吞掉。
ifneq ($(filter watermark encrypt,$(firstword $(MAKECMDGOALS))),)
PDF_COMMAND_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
.PHONY: $(PDF_COMMAND_ARGS)
$(PDF_COMMAND_ARGS):
	@:
endif

clean:
	$(RM) *.aux *.bbl *.bcf *.blg *.dvi *.fdb_latexmk *.fls *.lof *.log
	$(RM) *.lot *.nav *.out *.run.xml *.snm *.synctex.gz *.toc *.vrb *.xdv
	$(RM) *-blx.bib
