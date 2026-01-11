# 通用規則

## 語言偏好
- 使用繁體中文回答所有問題
- 程式碼和文件也使用繁體中文

## 項目概述

這是一個使用 Jekyll 構建的 GitHub Pages 個人網站，採用 minimal-mistakes 主題。

### 技術棧
- **靜態網站生成器**: Jekyll (Ruby)
- **主題**: minimal-mistakes v4.24.0
- **標記語言**: Markdown (Kramdown)
- **模板引擎**: Liquid
- **CSS 框架**: Tailwind CSS (部分頁面)
- **字體**: Noto Sans TC (Google Fonts)

## 構建命令

### 本地開發
```bash
bundle install                    # 安裝依賴
bundle exec jekyll serve           # 本地開發伺服器 (http://localhost:4000)
bundle exec jekyll build           # 構建生產版本
```

### 依賴管理
```bash
bundle update                      # 更新所有 gem 依賴
bundle exec jekyll doctor          # 檢查 Jekyll 配置問題
```

注意：此項目沒有測試套件或 linter。

## 代碼風格指南

### Markdown 文章 (_posts/)

#### Front Matter 格式
```yaml
---
title: "文章標題"
date: YYYY-MM-DD
categories:
  - 分類名稱
tags:
  - 標籤1
  - 標籤2
---
```

#### 命名約定
- 文章檔案格式: `YYYY-MM-DD-title.md`
- 標題使用連字符分隔，單詞首字母大寫
- 日期必須符合 ISO 8601 格式

#### Markdown 規範
- 使用標準 Markdown 語法
- 章節使用 `###` (三級標題) 作為主要章節分隔
- 使用 `---` 分隔主要章節
- 列表使用 `-` (減號) 標記
- 強調文字使用粗體 `**文字**`
- 內部連結使用相對路徑
- 外部連接使用完整 URL

### HTML/Liquid 頁面

#### Front Matter
所有 HTML 頁面必須包含 front matter:
```yaml
---
layout: single
title: "頁面標題"
author_profile: true
permalink: /路徑/
---
```

#### Liquid 模板語法
- 變數輸出: `{{ variable }}`
- 邏輯標籤使用縮排 (4 空格或 1 tab):
  ```liquid
  {% for item in items %}
      {{ item.name }}
  {% endfor %}
  ```
- 條件判斷:
  ```liquid
  {% if condition %}
      內容
  {% endif %}
  ```
- 過濾器使用管道符: `{{ site.posts | sort: "date" }}`

#### HTML 規範
- 使用 Tailwind CSS 樣式
- 字體使用 Noto Sans TC
- 響應式設計優先 (使用 `md:`, `lg:` 等斷點前綴)
- 使用語義化 HTML 標籤 (`<header>`, `<main>`, `<section>`, `<article>`)
- 外部資源使用 CDN:
  - Tailwind CSS: `https://cdn.tailwindcss.com`
  - Lucide Icons: `https://unpkg.com/lucide@latest`
  - Google Fonts: `https://fonts.googleapis.com/css2?...`

#### JavaScript 規範
- 使用 `document.addEventListener('DOMContentLoaded', ...)` 確保 DOM 加載完成
- 錯誤處理使用 `.catch()`
- 使用模板字串進行字串拼接
- 使用 `const` 和 `let`，避免 `var`
- 函數使用箭頭函數語法
- DOM 查詢使用 `querySelector` 和 `querySelectorAll`

### 目錄結構

```
_posts/              # 博客文章 (YYYY-MM-DD-title.md)
a/                   # 工具目錄 (HTML 工具頁面)
u/                   # 醫療工具目錄 (eGFR, PEF, QR Code)
notebooks/           # Jupyter notebooks
.agent/              # 工作流程配置
```

### 配置文件 (_config.yml)

- 主題: `mmistakes/minimal-mistakes@4.24.0`
- 語言: `zh-TW` (繁體中文)
- 標記語言: `kramdown`
- 預設皮膚: `dark`

### 程式碼組織原則

1. **一致性**: 遵循現有代碼風格
2. **可讀性**: 使用有意義的變數和函數名稱
3. **簡潔性**: 優先使用 Jekyll 內建功能
4. **維護性**: 將常用邏輯抽取為 includes 或 layouts
5. **可訪問性**: 確保 HTML 符合 WCAG 標準

### 導入和依賴

- Ruby gems 在 `Gemfile` 中定義
- Jekyll plugins 在 `_config.yml` 的 `plugins` 列表中聲明
- 前端依賴使用 CDN，不使用 npm/yarn

### 常用 Jekyll 功能

#### Liquid 過濾器
```liquid
{{ site.pages | where: "layout", "single" }}  # 篩選
{{ file.path | relative_url }}                 # 相對 URL
{{ content | smartify }}                       # 智能引號
```

#### 網站變數
- `site.posts`: 所有文章
- `site.static_files`: 靜態文件
- `page.title`: 當前頁面標題
- `author.name`: 作者名稱

### 錯誤處理

- JavaScript 使用 try-catch 或 Promise.catch()
- 檢查變數是否存在再使用:
  ```liquid
  {% if page.custom_field %}
      {{ page.custom_field }}
  {% endif %}
  ```

### 圖片和媒體

- 優先使用相對路徑
- 使用適當的 alt 文字描述
- 圖片路徑參考 minimal-mistakes 文檔

### Git 忽略規則

- `*.sw*`: Vim 交換文件
- `vendor/`: Ruby gem 安裝目錄
- `.sass-cache/`: SASS 緩存
- `Gemfile.lock`: 可選（通常在 .gitignore 中）

### 部署

- 自動部署至 GitHub Pages
- 推送到 `main` 分支會觸發構建
- 確保 `_config.yml` 中的 `url` 和 `baseurl` 正確配置

### 常見模式

#### 文件列表頁面
使用 Jekyll Liquid 遍歷 `site.static_files` 並按目錄分組顯示（參考 `list.html` 和 `a/index.html`）

#### 動態標題獲取
使用 JavaScript fetch 獲取 HTML 標題並動態更新連結文字

#### 工具頁面結構
- 使用 Tailwind CSS 建立兩列佈局
- 左側: 控制面板
- 右側: 結果顯示區域
- 響應式設計 (md: 以上為橫向，以下為縱向)
