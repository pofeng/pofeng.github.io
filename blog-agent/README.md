opencode 文字工作者使用範例
本文位置 : http://github.com/pofeng/pofeng.github.io/blob/master/blog-agent/README.md

把 prompt 寫成檔案，用 @ 呼叫，可要求輸出成檔案
範例: "請依照 @blog-agent/agent-title.md 與 https://pofeng.github.io/ai/2025/06/13/Welcome-to-the-Era-of-Experience.html 產出內容"

本目錄檔案說明: 
agent-conent-generator.md - 文字產出的提示詞與流程
agent-title.md - 上列提示詞的任務2，但要求輸出到檔案 title-hook.md
title-hook.md - 使用 agent-title.md 的產出

可以用自然語言 commit
範例: "將目前目錄向所有的更動，commit 到 github" 

有興趣可以練習看看怎樣寫 skill，不過就像 prompt engineering 一樣，應該很快就可以請 LLM 幫忙寫

vibe coding + vibe writing 建議學習路徑 : google gem -> google aistudio -> opencode (如果將來 google antigravity or Claude Code 開放自己選模型的話，我也會考慮推薦 ) 
