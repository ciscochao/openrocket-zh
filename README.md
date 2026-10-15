# OpenRocket 中文使用说明（入门指南）

本仓库是 [OpenRocket](https://openrocket.readthedocs.io/) 官方文档《Getting Started》的**中文翻译版**，整理为可被 [Read the Docs](https://readthedocs.org/) 直接构建的 Sphinx 文档项目，方便中文用户在线阅读。

- 原文：OpenRocket 23.09 官方文档《Getting Started》（英文）
- 翻译：社区贡献（中文）
- 图片：全部直接引用官方原始资源 `openrocket.readthedocs.io/_images/...`，**未作任何改动**

## 目录结构

```
openrocket-zh/
├── .readthedocs.yaml      # Read the Docs 构建配置
├── requirements.txt       # 构建依赖（sphinx / myst-parser / sphinx-rtd-theme）
├── README.md
├── LICENSE                # 版权与署名说明
└── docs/
    ├── conf.py            # Sphinx 配置
    ├── index.rst          # 文档首页 / 目录
    └── getting_started.md # 中文翻译正文（MyST Markdown）
```

## 本地预览（可选）

```bash
pip install -r requirements.txt
sphinx-build -b html docs docs/_build/html
# 用浏览器打开 docs/_build/html/index.html
```

## 发布到 Read the Docs（让更多人看到）

1. 把这个仓库推送到你的 GitHub（新建一个公开仓库，例如 `openrocket-zh`）。
2. 用 GitHub 账号登录 [Read the Docs](https://readthedocs.org/)，点击 **Import a Project** → 选择该仓库。
3. Read the Docs 会自动读取 `.readthedocs.yaml` 并构建，几分钟后即可获得一个永久网址，例如 `https://openrocket-zh.readthedocs.io/`。
4. 之后每次向仓库 `main` 分支推送更新，文档会自动重新构建。

> 提示：如果你希望这份翻译被 OpenRocket 官方收录，可以向官方仓库提交翻译贡献（upstream PR）。本仓库的结构已尽量贴近官方 Sphinx 项目，便于后续合并。

## 版权与署名

- 原文版权归 **OpenRocket 项目** 所有。
- 本中文翻译版在保留署名、注明出处的前提下共享，非官方出品，仅供学习参考。
- 如官方内容更新，请以英文原版为准。
