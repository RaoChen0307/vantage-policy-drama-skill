#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Vantage Markets daily briefing PDF."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

# Register Chinese CID font (built-in, supports Chinese)
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
# Use STSong-Light for regular, and we'll simulate bold with same font
CN_FONT = 'STSong-Light'
CN_FONT_BOLD = 'STSong-Light'  # CID font doesn't have bold variant

output_path = "/home/user/Doubao/chats/38442157651693058/Vantage每日推送_20260921.pdf"

doc = SimpleDocTemplate(output_path, pagesize=A4,
                        leftMargin=20*mm, rightMargin=20*mm,
                        topMargin=20*mm, bottomMargin=20*mm)

styles = getSampleStyleSheet()

title_style = ParagraphStyle('CustomTitle', parent=styles['Title'],
                             fontName=CN_FONT, fontSize=20, leading=28,
                             textColor=HexColor('#1a1a2e'), spaceAfter=6*mm)

subtitle_style = ParagraphStyle('Subtitle', parent=styles['Normal'],
                                fontName=CN_FONT, fontSize=11, leading=16,
                                textColor=HexColor('#666666'), spaceAfter=8*mm)

h1_style = ParagraphStyle('H1', parent=styles['Heading1'],
                          fontName=CN_FONT, fontSize=15, leading=22,
                          textColor=HexColor('#0f3460'), spaceBefore=8*mm, spaceAfter=4*mm,
                          borderPadding=(0, 0, 2, 0))

h2_style = ParagraphStyle('H2', parent=styles['Heading2'],
                          fontName=CN_FONT, fontSize=12, leading=18,
                          textColor=HexColor('#16213e'), spaceBefore=5*mm, spaceAfter=2*mm)

body_style = ParagraphStyle('Body', parent=styles['Normal'],
                             fontName=CN_FONT, fontSize=10, leading=16,
                             textColor=HexColor('#333333'), spaceAfter=2*mm)

bullet_style = ParagraphStyle('Bullet', parent=body_style,
                             leftIndent=8*mm, bulletIndent=2*mm, spaceAfter=1.5*mm)

source_style = ParagraphStyle('Source', parent=body_style,
                             fontSize=9, textColor=HexColor('#888888'),
                             leftIndent=8*mm, spaceAfter=4*mm)

highlight_style = ParagraphStyle('Highlight', parent=body_style,
                                 backColor=HexColor('#fff3cd'), borderPadding=6,
                                 leftIndent=4*mm, rightIndent=4*mm, spaceBefore=2*mm, spaceAfter=3*mm)

story = []

# ============ Title ============
story.append(Paragraph("Vantage Markets 全球重要动态", title_style))
story.append(Paragraph("2026年9月21日 星期一 · 每日推送", subtitle_style))

# ============ Part 1: Policy News ============
story.append(Paragraph("一、今日政策动态（按重要性排序）", h1_style))

news_items = [
    {
        "title": "1. 本周二是 500:1 黄金杠杆最后窗口，周三起降为 100:1",
        "points": [
            "今天周一、周二：XAUUSD247 维持最高 <b>500:1</b> 杠杆",
            "9月23日（周三）起：S&P PMI + 原油库存事件期间，黄金新仓杠杆临时降至 <b>100:1</b>",
            "9月24日（周四）：SNB 利率决议 + 新屋销售，杠杆限制延续",
            "9月25日（周五）：耐用品订单数据，杠杆限制延续",
            "关键规则：<b>现有持仓不受影响</b>，窗口结束后自动恢复 500:1",
        ],
        "source": "Vantage Markets 官方通知，9月18日发布"
    },
    {
        "title": "2. 美联储加息后黄金不跌反涨，现价约 $4,376/盎司",
        "points": [
            "9月19日凌晨纽约金主连收报 <b>$4,415.9</b>，重回 $4,400 上方",
            "周一早盘伦敦金现约 <b>$4,376/盎司</b>，本周初窄幅震荡",
            "油价回落缓解通胀担忧，但美元走强限制涨幅",
        ],
        "source": "新浪财经 / Reuters（9月21日早间）"
    },
    {
        "title": "3. XAUUSD247 黄金返现活动 9月30日截止（仅剩 9 天）",
        "points": [
            "每 10 万美元交易量返 1 美元，周末额外 20% 返现",
            "活动期最高 <b>$1,000</b> 返现",
            "本周三起杠杆临时下调，本周二可能是最后一个高交易量窗口",
        ],
        "source": "Vantage Markets 促销页面"
    },
    {
        "title": "4. 0.88% 利润奖金活动进行中（截止 11月3日）",
        "points": [
            "每日利润超过 $1 的部分，额外获得 <b>0.88%</b> 奖金",
            "每人活动期内最高 <b>$888</b> 奖金",
            "活动期：2026年5月4日 — 11月3日",
        ],
        "source": "Vantage Markets 促销页面"
    },
    {
        "title": "5. Vantage Trading Premier League (TPL) 交易竞赛进行中",
        "points": [
            "入金+交易冲击排行榜，争夺最高 <b>$10,000</b> 奖金",
            "每手交易和每美元入金推动等级提升",
        ],
        "source": "Vantage Markets 促销页面"
    },
    {
        "title": "6. XAUUSD247 500:1 杠杆升级进入第一个完整交易周",
        "points": [
            "9月19日生效，杠杆从 100:1 → 最高 500:1",
            "最大订单量 500 手 → 5,000 手（10倍）",
            "净敞口限额 3,000 → 15,000 手（5倍）",
        ],
        "source": "Vantage Markets 官方通知，9月19日生效"
    },
    {
        "title": "7. 49 只 24/7 美股上线第三天",
        "points": [
            "涵盖 SK hynix、Astera Labs、KLA Corporation 等科技标的",
            "支持 7×24 小时交易",
        ],
        "source": "Vantage Markets 官方通知，9月18日"
    },
    {
        "title": "8. LCID 仅做多 + 四只美股已下架",
        "points": [
            "LCID（Lucid Group）不再支持做空",
            "BLNK / CGC / INO / GPRO 已从所有服务器移除",
        ],
        "source": "Vantage Markets 官方通知，9月18日"
    },
]

for item in news_items:
    story.append(Paragraph(item["title"], h2_style))
    for p in item["points"]:
        story.append(Paragraph(f"• {p}", bullet_style))
    story.append(Paragraph(f"来源：{item['source']}", source_style))

# ============ Page Break ============
story.append(PageBreak())

# ============ Part 2: Script Directions ============
story.append(Paragraph("二、今日短视频剧本方向（3 个）", h1_style))
story.append(Paragraph("自动筛选素材：本周二是 500:1 杠杆最后窗口、美联储加息后黄金不跌反涨、0.88%利润奖金+返现截止。", highlight_style))

directions = [
    {
        "name": "方向 1：《周二之前》— 时间压力/规则漏洞型",
        "fields": [
            ("第一屏压力", "周一早上，交易群里都在传——周三起黄金杠杆要从 500 降回 100"),
            ("主角行动", "主角想赶在周二结束前建好仓位，用 500:1 锁定大杠杆"),
            ("关键证据", "通知里写着「现有持仓不受影响，窗口结束后自动恢复」"),
            ("反转", "主角周二重仓冲进去，结果周三 PMI 数据公布后黄金剧烈波动，新仓因杠杆降到 100:1 保证金差点不够——而他上周五随手开的一笔小仓位，因为在窗口前开的，反而用着 500:1 安然无恙，还吃到了完整涨幅"),
            ("政策改变剧情", "杠杆调整的「新老仓区别对待」规则直接制造了时间窗口内的策略反转"),
            ("广告记忆画面", "日历上 9月23日 被红圈标注，旁边两行字——「新仓 100:1」 vs 「持仓 500:1」"),
            ("结尾回报", "主角把那笔上周五的老仓截图保存，命名为「规则比预测重要」"),
        ]
    },
    {
        "name": "方向 2：《加息那天》— 认知差/反转型",
        "fields": [
            ("第一屏压力", "美联储宣布加息，群里所有人都在喊「黄金要崩了」"),
            ("主角行动", "主角跟着大家一起做空黄金，止损设在 $4,400 上方"),
            ("关键证据", "9月19日凌晨，黄金不跌反涨，直接冲过 $4,400——主角被止损出局"),
            ("反转", "主角复盘发现，他做空的时候，Vantage 上 XAUUSD247 正好升级到 500:1 杠杆，而且周末 24/7 交易时段有人在低位吸筹——他看到的「利空」，正好是别人用新杠杆捡筹码的机会"),
            ("政策改变剧情", "500:1 新杠杆 + 24/7 交易时段，改变了市场资金的行为模式，主角的「常识」失效了"),
            ("广告记忆画面", "主角被止损的弹窗，和屏幕另一侧「500:1」的新杠杆通知，同时出现在一个画面里"),
            ("结尾回报", "主角没有追多，而是设了一个小仓位多单，自语：「加息不跌，说明有人比我知道得更多——但我不赌方向，我赌规则。」"),
        ]
    },
    {
        "name": "方向 3：《888 和 1000》— 竞赛/时间压力型",
        "fields": [
            ("第一屏压力", "主角发现两个活动同时在跑——0.88% 利润奖金最高 $888，黄金返现最高 $1,000"),
            ("主角行动", "他想两个活动都拿满，开始疯狂交易刷利润和交易量"),
            ("关键证据", "他算了一笔账——两个活动要求的交易频率不一样，利润奖金看每日利润，返现看交易量，两头跑反而两边都差一点"),
            ("反转", "主角停止两头跑，专注做一笔高质量的黄金波段交易——单笔利润够拿当天的 0.88% 奖金，交易量也够返现门槛。结果这一笔同时满足了两个活动的要求"),
            ("政策改变剧情", "两个促销活动的不同计算规则，改变了主角的最优交易策略"),
            ("广告记忆画面", "屏幕上两个通知并排——左边「$888 利润奖金」，右边「$1,000 返现」，中间是主角的一笔交易记录"),
            ("结尾回报", "两个奖励都到账了。主角看着总金额笑了一下，把活动规则截图存进相册，备注：「算清楚规则再动手。」"),
        ]
    },
]

for d in directions:
    story.append(Paragraph(d["name"], h2_style))
    for label, content in d["fields"]:
        story.append(Paragraph(f"<b>{label}：</b>{content}", bullet_style))
    story.append(Spacer(1, 3*mm))

# Footer note
story.append(Spacer(1, 8*mm))
story.append(Paragraph("回复编号选择方向（1/2/3），或说明组合需求，即可输出完整分镜剧本。", highlight_style))
story.append(Paragraph("风险提示：本简报为信息整理，不构成投资建议。CFD 交易具有高风险，杠杆可能导致重大损失。条款与条件适用。", source_style))

doc.build(story)
print(f"PDF generated: {output_path}")
