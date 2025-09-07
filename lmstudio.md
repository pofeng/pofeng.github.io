( by gpt-oss-20b ) 

以下是 **LM Studio** 在載入語言模型時常見的「Advanced Options」項目，以及每一項所代表的功能、目的與使用情境。  
（下列說明基於 2025‑09 版 LM Studio，若你使用的是不同版本或不同前端（如 LM Studio Lite / Desktop），某些選項名稱可能略有差異，但概念相同。）

| 選項 | 簡短說明 | 為什麼要用？ | 何時該啟用／關閉 |
|------|----------|--------------|-------------------|
| **GPU Offload** (或 “Offload to GPU”) | 將模型權重（weight tensors）自動切分到 GPU 記憶體，而非僅在 CPU 上運算。 | 在擁有多張 GPU 或大型 GPU 時，能減少 CPU‑GPU 之間的資料搬移，提高吞吐量；亦可讓單卡 GPU 的記憶體空間被更多模型佔用。 | *啟用*：你有足夠 GPU VRAM（至少 >4 GB）並想利用其加速；<br>*關閉*：GPU 記憶體不足或你只想在 CPU 上跑，避免不必要的 GPU 資源占用。 |
| **CPU Pool Size** | 指定為「CPU‑only」模式下使用多少個核心（threads）來進行模型計算。 | 在沒有 GPU 或 GPU 無法使用時，透過多執行緒加速推論；同時可避免單核心過載造成的熱 throttling。 | *啟用*：在 CPU‑only 模式或「CPU offload」不開啟時。<br>設定值通常為 1–(核心數)，但若你想保留 CPU 用於其他任務，可設低一些（如 2 或 4）。 |
| **Memory‑map (mmap)** | 將模型檔案使用「記憶體映射」方式載入，而不是一次性讀取到 RAM。 | 大型 LLM（>10 GB）可在啟動時不佔用完整 RAM，僅在需要時才從磁碟載入所需片段；減少系統記憶體壓力。 | *啟用*：模型超過 8–12 GB 或你系統 RAM 不足。<br>*關閉*：若你有充足 RAM，mmap 可能略遲於直接載入（尤其在 SSD 非極速時）。 |
| **Number of Experts** (多專家模型) | 在 Mixture‑of‑Experts (MoE) 結構中設定同時活躍的「expert」數量。 | MoE 模型允許同一層只啟用部分子模組（experts），可在保持表現的同時減少 FLOPs；此參數控制每次前向傳播要載入多少 experts。 | *較大值*：提升推論準確度、速度（因更多專家可並行處理）。<br>*較小值*：節省記憶體與算力，適合資源有限的環境。 |
| **Tensor Parallelism** (張量平行) | 將單一層權重分割到多個 GPU/CPU core 上，同時進行計算。 | 適用於超大模型（> 30 B）或需要跨卡運算；可在保持完整精度的同時加速推論。 | *啟用*：你有 2+ 卡 GPU 或多 CPU core 且想充分利用。<br>*關閉*：單卡環境或模型已小到不需平行。 |
| **Quantization** (量化) | 將浮點權重轉換為低位元表示（如 int8、bfloat16）。 | 減少記憶體佔用與加速推論，特別是 GPU 只支援 FP32/FP16 的情況。 | *啟用*：記憶體瓶頸或想在舊硬體上跑；<br>*關閉*：若你追求最高精度且有足夠 VRAM。 |
| **Cache Size / KV Cache** | 設定 Key‑Value cache 的最大容量（token數）。 | 在長序列推論時避免頻繁重計算；較大的 KV cache 可提升速度，但佔用更多記憶體。 | *增大*：你需要處理 1k+ token 長文本。<br>*減小*：短句或記憶體受限。 |
| **Batch Size** | 每次推論允許同時輸入的 prompt 數量。 | 大 batch 可以提升 GPU utilisation，但同時佔用更多 VRAM；適合服務化部署。 | *大值*：多使用者並發、GPU 充足。<br>*小值*：單一或少量請求、記憶體有限。 |
| **Thread Affinity / Scheduler** | 控制每個執行緒的 CPU 核心綁定，或選擇不同的線程調度器（如 OpenMP vs. TBB）。 | 能減少 cache miss、提升多核心效能。 | 需要微調性能時使用；一般預設即可。 |
| **Mixed Precision** (混合精度) | 在 FP32/FP16 之間自動切換，以加速推論並降低記憶體需求。 | 近年 GPU（尤其 RTX 30 系列、A100）對 FP16 有硬件支援，能提升速度。 | *啟用*：若你有支持 FP16 的 GPU；<br>*關閉*：舊 GPU 或對精度敏感。 |
| **Dynamic Batch** (動態批次) | 允許模型根據實際輸入長度自動調整 batch 大小，避免過大造成記憶體溢出。 | 適用於不規則 prompt 長度的情境。 | 常見於 API 或聊天機器人部署。 |
| **Offload to Disk** (磁碟卸載) | 在 GPU VRAM 不足時，把一部分張量暫存到硬碟（NVMe）或 SSD，必要時再載入。 | 允許在極低記憶體環境下仍能跑大型模型。 | *啟用*：GPU 記憶體 < 模型大小；<br>*關閉*：避免磁碟 I/O 延遲。 |
| **Cache Reuse** (重複使用 KV cache) | 在連續對話中保持前一次推論的 KV cache，減少重新計算。 | 對聊天機器人非常重要，可顯著降低 latency。 | 只在持久會話模式下啟用。 |

---

## 如何根據硬體與需求選擇

| 硬體/場景 | 推薦配置 (大致) |
|-----------|----------------|
| **桌面 PC**（RTX 3060，12 GB VRAM） | GPU Offload：關；CPU Pool Size：8–16；mmap：關；Quantization：int8 或 bf16；Cache Size：512 tokens；Batch Size：1–4 |
| **工作站**（A100，40 GB VRAM） | GPU Offload：開啟並分配 30‑35 GB；CPU Pool Size：自動；mmap：關；Quantization：fp16 或 bf16；Number of Experts：依模型 MoE 參數；Batch Size：8–32 |
| **伺服器**（多卡，NVMe SSD） | GPU Offload + Tensor Parallelism：開啟；CPU Pool Size：全部核心；mmap：開啟；Offload to Disk：可選；Cache Reuse：開啟；Batch Size：大於 32 |
| **低端筆電**（集成顯示卡，4 GB RAM） | GPU Offload：關；CPU Pool Size：2–4；mmap：開啟；Quantization：int8；Number of Experts：1；Cache Size：256 tokens；Batch Size：1 |

---

## 小技巧

1. **先測試**：在正式部署前，先用 `--profile` 或 LM Studio 的「Performance Test」功能跑一次，觀察 GPU/CPU 使用率、記憶體佔用與 latency。
2. **逐步調整**：不要同時改動多個參數。先決定是否使用 GPU Offload，再微調 CPU Pool Size；之後再考慮 mmap 或 Quantization。
3. **監控工具**：Linux 可用 `nvidia-smi`, `htop`; Windows 用 Task Manager 或 GPU-Z；查看實際記憶體占用與核心利用率。
4. **保存設定**：LM Studio 允許將「Profile」存檔，以便不同模型或任務快速切換。

---

### 總結

- **GPU Offload / Tensor Parallelism** → 利用 GPU 資源
- **CPU Pool Size** → 控制 CPU 多執行緒
- **mmap / Offload to Disk** → 節省 RAM/VRAM，降低 I/O 成本
- **Number of Experts** → 調節 MoE 模型的效能與記憶體
- 其餘選項（Quantization、Cache Size、Batch Size 等）則是為了在不同硬體與任務需求下取得最佳平衡。

希望這份簡介能幫你快速了解 LM Studio 的進階載入設定，並在實際使用中做出最適合的選擇！如果還有更具體的模型或環境想討論，隨時告訴我。
