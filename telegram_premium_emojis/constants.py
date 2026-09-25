"""
Telegram Premium Emojis — Curated Constants & Icon Enums
"""
from enum import Enum

# Telegram full-width invisible Braille whitespace spacer.
# Forces mobile & desktop Telegram clients to render blockquote cards at full width.
FULL_WIDTH_SPACER = "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"


class CommonIcons:
    """Most frequently used Telegram custom emoji IDs for navigation and actions."""
    # Navigation
    BACK = "5877536313623711363"        # ⬅️
    FORWARD = "5258215850745275216"     # ➡️
    HOME = "5807868868886009920"        # 🏠
    NEXT = "5875506366050734240"        # ⏩
    CANCEL = "5258226313285607065"      # ❌
    CLOSE = "5260342697075416641"       # ✖️
    REFRESH = "5260687119092817530"     # 🔄
    TRASH = "5258130763148172425"       # 🗑

    # Status / Indicators
    SUCCESS = "5920052658743283381"     # ✅
    ERROR = "5258226313285607065"       # ❌
    WARNING = "5258474669769497337"     # ⚠️
    INFO = "5258503720928288433"        # ℹ️
    PENDING = "5258419835922030550"     # ⏳
    LOCK = "5258476306152038031"        # 🔒
    UNLOCK = "5258514780469075716"      # 🔓

    # Finance & Engagement
    DIAMOND = "5807465992363710697"     # 💎
    STAR = "5874948844935974490"        # ⭐️
    LIGHTNING = "5843553939672274145"   # ⚡️
    CROWN = "5807868868886009920"       # 👑
    COIN = "5258368777350816286"        # 🪙
    CARD = "5258260149037965799"        # 💳
    FIRE = "6008118472066732010"        # 🔥

    # Statistics & Gamification
    CHART_BAR = "5877485980901971030"   # 📊 Stats / Analytics
    CHART_UP = "5776219138917668486"    # 📈 Growth / Rank
    TROPHY = "5961051261204696786"      # 🏆 / 🥇 Total score (XP) & Trophy/Medal
    TARGET = "5920052658743283381"      # 🎯 Solved / Goal
    ROCKET = "5875506366050734240"      # 🚀 Boost / Level-up
    ID_BADGE = "5258477770735885832"    # 🆔 / 🪪 ID Badge
    MEDAL_GOLD = "5961051261204696786"  # 🥇 1st place
    MEDAL_SILVER = "5447203607294265305"# 🥈 2nd place
    MEDAL_BRONZE = "5453902265922376865"# 🥉 3rd place

    # Content & Documents
    DOCUMENT = "5258477770735885832"    # 📄
    FOLDER = "5875206779196935950"      # 📁
    EDIT = "5839380464116175529"        # ✏️
    ATTACH = "5260730055880876557"      # 📎
    SEARCH = "5260341314095947411"      # 🔍
    DOWNLOAD = "5258336354642697821"    # ⬇️
    UPLOAD = "5260652420052032852"      # ⬆️
    SETTINGS = "5258420634785947640"    # ⚙️
    PROFILE = "5771887475421090729"     # 👤
    HELP = "5258503720928288433"        # ❓
    ROBOT = "5258093637450866522"       # 🤖
    SPARKLES = "5877318502947229960"    # ✨


# Mapping of fallback emoji char for each icon
ICON_FALLBACKS = {
    CommonIcons.BACK: "⬅️",
    CommonIcons.FORWARD: "➡️",
    CommonIcons.HOME: "🏠",
    CommonIcons.NEXT: "⏩",
    CommonIcons.CANCEL: "❌",
    CommonIcons.CLOSE: "✖️",
    CommonIcons.REFRESH: "🔄",
    CommonIcons.TRASH: "🗑",
    CommonIcons.SUCCESS: "✅",
    CommonIcons.ERROR: "❌",
    CommonIcons.WARNING: "⚠️",
    CommonIcons.INFO: "ℹ️",
    CommonIcons.PENDING: "⏳",
    CommonIcons.LOCK: "🔒",
    CommonIcons.UNLOCK: "🔓",
    CommonIcons.DIAMOND: "💎",
    CommonIcons.STAR: "⭐️",
    CommonIcons.LIGHTNING: "⚡️",
    CommonIcons.CROWN: "👑",
    CommonIcons.COIN: "🪙",
    CommonIcons.CARD: "💳",
    CommonIcons.FIRE: "🔥",
    CommonIcons.CHART_BAR: "📊",
    CommonIcons.CHART_UP: "📈",
    CommonIcons.TROPHY: "🏆",
    CommonIcons.TARGET: "🎯",
    CommonIcons.ROCKET: "🚀",
    CommonIcons.ID_BADGE: "🆔",
    CommonIcons.MEDAL_GOLD: "🥇",
    CommonIcons.MEDAL_SILVER: "🥈",
    CommonIcons.MEDAL_BRONZE: "🥉",
    CommonIcons.DOCUMENT: "📄",
    CommonIcons.FOLDER: "📁",
    CommonIcons.EDIT: "✏️",
    CommonIcons.ATTACH: "📎",
    CommonIcons.SEARCH: "🔍",
    CommonIcons.DOWNLOAD: "⬇️",
    CommonIcons.UPLOAD: "⬆️",
    CommonIcons.SETTINGS: "⚙️",
    CommonIcons.PROFILE: "👤",
    CommonIcons.HELP: "❓",
    CommonIcons.ROBOT: "🤖",
    CommonIcons.SPARKLES: "✨",
}

