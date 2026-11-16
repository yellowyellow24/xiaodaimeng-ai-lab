# 🌷 小呆萌 AI 實驗室｜作品與學習筆記網站

這是一個以 **AGENTS.md** 為核心規則的可擴充靜態網站，整理小呆萌系列 AI 課程作品，展示如何使用標準頁面模板及規範持續新增內容。

## 作品內容

- 小呆萌 2.0：RAG 檢索、18 篇時間管理教材、FAISS 與 Groq 的原型紀錄。
- 小呆萌 3.0：Reflection Agent 的 Generate → Reflect → Revise 三階段與測試紀錄。
- 小呆萌 4.0：RAG 與 Reflection 整合的未來規劃（**尚未完成整合**）。

本網站是**可直接瀏覽的作品介紹網站**，不是需要 API Key 才能使用的 AI 聊天服務。

## 為什麼有 `AGENTS.md`？

老師的作業重點是建立一套可重複使用的專案規則，而不只是做出一次性網頁。

請閱讀 [AGENTS.md](AGENTS.md)，其中定義：

1. 專案目的、視覺風格及技術選擇。
2. 資料夾結構、檔案命名、相對路徑。
3. 每篇內容必備的四個段落及狀態標籤。
4. 新增頁面的完整 SOP 和可給 AI 使用的範例指令。
5. 安全規範、品質驗收及 GitHub Pages 部署方式。

## 專案結構

```text
AGENTS.md
README.md
.nojekyll
index.html
assets/style.css
assets/site.js
pages/rag.html
pages/reflection.html
pages/roadmap.html
templates/page-template.html
scripts/validate_site.py
```

## 如何在電腦上預覽

### 最簡單的方法

雙擊 `index.html` 用瀏覽器開啟，或使用 VS Code 的 Live Server。

### 使用 Python 開啟本機伺服器

在專案資料夾執行：

```bash
python3 -m http.server 8000
```

再開啟 `http://localhost:8000`。

### 執行基本檢查

```bash
python3 scripts/validate_site.py
```

不需要安裝第三方套件。

## 如何公開到 GitHub Pages

1. 在 GitHub 建立一個 **Public** Repository，建議名稱：`xiaodaimeng-ai-lab`。
2. 將本專案內的**所有檔案與資料夾直接上傳到 Repository 根目錄**。請注意：GitHub 網頁上傳 `.nojekyll` 這類隱藏檔案時可由專案資料夾拖曳上傳；如果遺漏，這個網站仍能顯示，但建議一併上傳。
3. 到該 Repository 的 **Settings → Pages**。
4. 在 **Build and deployment** 設定：**Source: Deploy from a branch；Branch: main；Folder: /(root)**，儲存。
5. 等候 GitHub Pages 完成發布，從 Pages 頁面按 **Visit site**，實際檢查首頁和內容頁。

**預期的專案網站網址格式**：`https://<你的 GitHub 使用者名稱>.github.io/xiaodaimeng-ai-lab/`。實際以 GitHub Pages 顯示的網址為準。

GitHub 官方說明：https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

## 如何請 AI 新增頁面

請提供 AI 以下指令：

> 先閱讀根目錄 AGENTS.md。我要新增「番茄鐘學習法」介紹頁面，請依照 templates/page-template.html 建立 pages/pomodoro-guide.html，使用原本的共用 CSS 和導覽，補上首頁卡片，並執行 scripts/validate_site.py 確認沒有壞連結。

AI 按照規則擴充後，新頁面會與既有網站保持一致，不必重新解釋版型及結構。

## 期末／課堂作業繳交說明（複製後自行填入連結）

**作品名稱：** 小呆萌 AI 實驗室｜作品與學習筆記網站

**使用的規則檔：** 根目錄 `AGENTS.md`

**GitHub Repository：** `https://github.com/<你的帳號>/xiaodaimeng-ai-lab`

**公開網站：** `https://<你的帳號>.github.io/xiaodaimeng-ai-lab/`

**新增內容方式：** AI 必須先閱讀 `AGENTS.md`，複製 `templates/page-template.html` 產生新頁、填滿規定欄位、更新首頁作品卡片、重用共用樣式，最後驗證連結及網站呈現。

## 內容與隱私聲明

網站內容為課程學習與作品介紹；未收集訪客資料，不包含私人 API 金鑰。作品頁面中標示「規劃中」的功能尚未完成整合，不應誤認為正式服務。
