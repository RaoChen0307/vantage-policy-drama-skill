# Vantage Markets 政策短视频自动化方案

自动搜集 Vantage Markets 全球重要动态，筛选高价值政策信息，并将其转化为 AI 短视频剧本方向的完整自动化工作流。

## 功能特性

- **每日自动推送**：每天 7:08 自动抓取 Vantage Markets 促销/通知页面及公开市场数据
- **智能筛选**：从过去 24 小时动态中筛选 5-8 条最有价值信息，按重要性排序
- **政策→剧本引擎**：自动将杠杆调整、新品上线、促销活动等转化为 3 个差异化短视频剧本方向
- **金融合规硬门**：内置 6 条合规规则（不承诺收益、杠杆双向呈现风险、数字零误差等）
- **PDF 导出**：支持将每日推送整理为 PDF 报告

## 目录结构

```
vantage-policy-automation/
├── README.md                          # 项目说明
├── .gitignore                         # Git 忽略规则
├── skills/
│   └── vantage-policy-drama/
│       └── SKILL.md                   # 金融政策短视频剧本生成 Skill
├── scripts/
│   └── generate_pdf.py                # PDF 生成脚本（reportlab + 中文字体）
├── docs/
│   └── 方案说明.md                     # 完整方案推导过程
└── examples/
    └── 剧本方向示例.md                 # 剧本方向输出示例
```

## 快速开始

### 1. 安装 Skill

将 `skills/vantage-policy-drama/` 目录复制到你的 Skill 目录：

```bash
cp -r skills/vantage-policy-drama/ ~/.doubao/agent_mode/workspace/.user_skills/
```

### 2. 创建定时任务

使用 cron 表达式 `8 7 * * *`（每天 7:08）创建定时任务，任务内容参考 `docs/方案说明.md`。

### 3. 生成 PDF

```bash
pip install reportlab
python scripts/generate_pdf.py
```

## 信息来源

| 来源 | URL |
|---|---|
| Vantage 通知中心 | https://www.vantagemarkets.io/notifications/ |
| Vantage 促销页面 | https://www.vantagemarkets.io/en/promotions/ |
| 亚太区通知镜像 | https://www.vantage-markets-apac.com/en/notifications/ |

> 注意：`secure.vantagemarkets.com` 为登录态域名，定时任务使用公开域名获取信息。

## 剧本生成规则

### 输入门（自动筛选）
从 5-8 条政策中优先选取：
1. 数字变化大（杠杆 100→500、订单量 10 倍）
2. 时间敏感（促销即将截止、产品当天下架）
3. 影响面广（49 只新品上线、全服务器变更）
4. 有冲突潜力（仅做多限制、股票移除）

### 故事引擎映射

| 政策类型 | 推荐故事引擎 |
|---|---|
| 杠杆/额度提升 | 逆袭 / 危机处理 |
| 新产品上线 | 机会争夺 / 隐藏身份 |
| 股票下架/限制 | 时间压力 / 规则漏洞 |
| 促销/返现活动 | 竞赛 / 误会反转 |
| 交易模式变更 | 策略转变 / 认知差 |

### 金融合规硬门（HARD GATE）
1. 不承诺收益（禁止"稳赚""必涨""翻倍"）
2. 杠杆双向呈现（必须暗示杠杆也放大亏损）
3. 数字零误差（杠杆比例、手数、金额与原始政策一致）
4. 促销标注 T&C（返现/奖金结尾有"*条款与条件适用"）
5. 不暗示内幕（政策是公开信息）
6. 风险提示（结尾必须有"交易有风险，投资需谨慎"）

## 剧本方向输出格式

每个方向包含：
- 方向名称
- 第一屏压力（静音可懂）
- 主角行动
- 关键证据（政策数字自然植入）
- 反转
- 政策如何改变剧情
- 广告记忆画面
- 结尾回报

## 技术栈

- **定时调度**：cron（每天 7:08）
- **PDF 生成**：reportlab + STSong-Light 中文字体
- **Skill 格式**：Markdown 规则型 Skill
- **数据获取**：web.fetch + general_search

## 已知限制

- `secure.vantagemarkets.com` 需要登录态，定时任务使用公开域名
- PDF 中文字体使用 reportlab 内置 CID 字体 STSong-Light（不支持 CFF/PostScript outlines 的 TTC）
- 剧本方向生成后需用户选择编号，再输出完整分镜剧本

## 许可证

MIT
