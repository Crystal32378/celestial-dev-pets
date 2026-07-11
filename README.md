# Celestial Dev Pets — 日月地

一組非官方、粉絲創作的桌面開發寵物包：

- **Helios 日**：旗艦型太陽寵物
- **Luna 月**：精簡高效型月亮寵物
- **Terra 地**：輕量可靠型地球寵物

> 本專案未使用 OpenAI Logo 或官方品牌素材，亦不代表 OpenAI 的官方產品、合作、背書或授權。

## 三隻本尊

| Helios 日 | Luna 月 | Terra 地 |
|---|---|---|
| ![Helios spritesheet](assets/helios.png) | ![Luna spritesheet](assets/luna.png) | ![Terra spritesheet](assets/terra.png) |

**Current release:** `v0.1 — Static Sprite Prototype`

## 目前真的包含什麼

每隻寵物都有一張：

- 192 × 192 px spritesheet
- 3 × 3 格
- 每格 64 × 64 px
- PNG 與 lossless WebP
- 已處理為透明背景
- 9 個靜態狀態姿勢

## 狀態編號

```text
0 1 2   idle / waiting / running
3 4 5   review / jumping / waving
6 7 8   failed / happy / glow
```

| 狀態 | 用途 |
|---|---|
| `idle` | 待機 |
| `waiting` | 等待或思考 |
| `running` | 執行任務 |
| `review` | 審查程式碼或內容 |
| `jumping` | 短暫動作 |
| `waving` | 打招呼 |
| `failed` | 錯誤 |
| `happy` | 任務成功彩蛋 |
| `glow` | 高光、完成或特殊狀態 |

## 檔案結構

```text
celestial-dev-pets/
├─ assets/
│  ├─ helios.webp
│  ├─ helios.png
│  ├─ luna.webp
│  ├─ luna.png
│  ├─ terra.webp
│  └─ terra.png
├─ pets/
│  ├─ helios-pet.json
│  ├─ luna-pet.json
│  └─ terra-pet.json
├─ manifest.json
├─ preview.html
├─ TECH_NOTES.md
├─ LICENSE
└─ README.md
```

## 預覽

直接用瀏覽器開啟 `preview.html`，可以切換三隻寵物與九種狀態。

## 關於 JSON 相容性

目前沒有一套可假設所有 Codex 或 VS Code 寵物擴充功能都支援的通用 JSON 格式。

這一包提供的是：

1. 清楚、穩定的自訂 JSON schema
2. 可直接驗證素材切格是否正確的 `preview.html`
3. 可供實際目標專案撰寫 adapter 的基礎資料

請先確認目標 extension 或 repo 的 schema，再將欄位映射過去。

## 一個重要限制

目前每個狀態只有 **一個 frame**，因此它們是「狀態姿勢」，不是逐格動畫。

例如：

```json
"running": {
  "frames": [2],
  "loop": true
}
```

這會顯示奔跑姿勢，但不會自行產生奔跑動畫；`fps` 也不會讓單張圖動起來。

真正的動畫版本需要：

- 每個狀態增加 2–6 個 frame，或
- 由程式加入漂浮、縮放、位移、粒子等 tween 效果

## Roadmap

- [x] v0.1 — 3 × 3 static sprite prototype
- [ ] v0.2 — multi-frame animation
- [ ] v0.3 — adapter for a real editor extension or desktop runtime
- [ ] v0.4 — task-state integration
- [ ] v1.0 — installable release

## 角色設定

### Helios 日

陽光開朗的算力太陽神。工作完成時亮得像在搶會議室投影機的主導權。

錯誤狀態：`timeout`

### Luna 月

冷靜高效的夜班小編。半夜還在線，但不代表你應該半夜改需求。

錯誤狀態：`rate_limit`

### Terra 地

穩重可靠的端側小地球。背著包、長著樹，也逃不過記憶體不足。

錯誤狀態：`out_of_memory`

## 授權

程式、設定檔與本包內容依 `LICENSE` 所示授權。

---

Made with caffeine, celestial bodies, and a healthy distrust of red error messages.
