# Configuration file for the Sphinx documentation builder.
# 本配置用于 Read the Docs 自动构建，无需本地安装即可在线发布。

project = "OpenRocket 中文使用说明"
author = "OpenRocket 项目（原文）；中文翻译整理"
copyright = "2026, OpenRocket Project"
language = "zh"

extensions = [
    "myst_parser",
]

# 启用 MyST 扩展，支持 ::: 围栏与定义列表等语法
myst_enable_extensions = [
    "colon_fence",
    "deflist",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

master_doc = "index"
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_title = "OpenRocket 中文使用说明"
