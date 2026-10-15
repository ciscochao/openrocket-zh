# GitHub Issue 草稿：申请将中文《Getting Started》文档收录进 OpenRocket 官方

> 使用说明：登录 GitHub → 打开 https://github.com/openrocket/openrocket → 点 "Issues" → "New issue"
> 标题填下面 Title，正文粘贴 Description（英文，因为 maintainers 主要用英文沟通）。
> 下面的中文只是给你看的注释，不要贴进 Issue。

---

## Title

[Translation] Chinese (zh) translation of the Getting Started guide

## Description (paste this)

Hi OpenRocket team,

I'd like to contribute a **Simplified Chinese translation of the "Getting Started" guide**
(`docs/source/setup/getting_started.rst`).

**What I've done**
- Translated the full Getting Started guide into Simplified Chinese (all sections: user
  interface, rocket components, appearance & decals, studio).
- Published a working version online so you can review it:
  https://openrocket-zh.readthedocs.io/zh-cn/latest/
- The translation is kept in sync with the current English content (I used the live docs as
  the source).

**Why**
There is a growing Chinese-speaking user community, and a native Getting Started guide would
lower the barrier for new users. OpenRocket already lists Chinese contributors for the UI, so
documentation localization is a natural next step.

**How I'd like to help**
Since the docs are currently single-language (English `.rst`), I want to confirm the preferred
way to integrate a translation before opening a PR. A few options:
1. Add a translated file alongside, e.g. `docs/source/setup/getting_started.zh.rst`;
2. Introduce a locale / i18n structure for the docs (Sphinx `gettext` / `locale` dirs);
3. Any structure you already plan to use (I noticed recent Crowdin sync work).

I'm happy to:
- Re-base the translation onto the current `getting_started.rst` (last updated 2026-09-29),
- Move screenshots to local `docs/source/img/` assets instead of remote links,
- Submit a clean PR once the location/format is agreed.

Could you advise on the preferred file location and format? I can also join the Discord if
that's easier to coordinate. Thanks for a great tool!

— [your GitHub username]

---

## 中文注释（不贴进 Issue）

- 目标仓库：`openrocket/openrocket`，分支 `unstable`。
- 目标文件：`docs/source/setup/getting_started.rst`（RST 格式，非 MD）。
- 关键点：先开 Issue 问「放哪里、用什么格式」，不要直接盲提 PR——因为官方文档目前没有多语言结构，maintainers 需要先拍板集成方式。
- 同步建议：把翻译对齐到当前 `.rst` 源文件（截图 2026-09-29 已更新），图片改用本地 `docs/source/img/` 资源，便于合并。
- 另：软件界面翻译走 Crowdin（crowdin.com/project/openrocket），与文档是两条线；文档目前不在 Crowdin 里。
