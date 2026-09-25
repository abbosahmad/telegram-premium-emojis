# Telegram Premium Emojis & UI Toolkit 💎 (O'zbekcha Qo'llanma)

<p align="center">
  <a href="https://pypi.org/project/telegram-premium-emojis/"><img src="https://img.shields.io/pypi/v/telegram-premium-emojis?color=blue&style=for-the-badge&logo=pypi&logoColor=white" alt="PyPI Versiyasi"></a>
  <img src="https://img.shields.io/badge/Catalog-1%2C920%2B_Custom_Emojis-orange?style=for-the-badge" alt="Katalog">
  <img src="https://img.shields.io/badge/Aiogram-3.x_Ready-2ea44f?style=for-the-badge" alt="Aiogram 3">
  <img src="https://img.shields.io/badge/Litsenziya-MIT-green?style=for-the-badge" alt="Litsenziya">
</p>

Telegram botlarda **Telegram Premium Custom Emojilar**, **Aiogram 3 zamonaviy kartochka UI**, inline tugmalarda maxsus custom emoji ikonkalari (`icon_custom_emoji_id`), rangli tugmalar va pack skanerlari bilan ishlash bo'yicha to'liq ochiq kodli vosita va AI Agent Skill.

---

## 📌 Nima uchun bu loyiha yaratildi?

Telegram **Bot API 7.0+ va 8.0+** yangilanishlarida botlar uchun xabarlar ichida harakatlanuvchi premium emojilar (`<tg-emoji>`) va inline tugmalarda custom emoji qo'yish imkoniyatini taqdim etdi.

Ammo ko'pchilik dasturchilar va AI agentlar (ChatGPT, Claude, Cursor) quyidagi muammolarga duch kelmoqda:
1. **Custom emoji ID larini topish qiyin:** Stiker to'plamlaridagi emoji ID larini qanday ajratib olishni bilishmaydi.
2. **Xunuk tugmalar:** Tugma ichiga `icon_custom_emoji_id` qo'yilgandan keyin ham matnga oddiy emoji yozib qo'yish (`text="💎 Balans"`), natijada ikkita bir xil emoji chiqib qoladi.
3. **Buzilgan kartochkalar:** Kenglik uchun bo'sh joy (spacer) qo'yilmagani sababli xabar kartochkalari telefonda juda tor bo'lib qisilib qoladi.
4. **Fallback yo'qligi:** Eski Telegram versiyalarida xabar buzilib ko'rinmasligi uchun fallback unicode emoji qo'yish unutiladi.

Ushbu kutubxona va AI Skill barcha shu muammolarni bir martada professional darajada hal qiladi!

---

## ✨ Asosiy Imkoniyatlar

- **💎 1 920+ Saralangan Emojilar Bazasi:** 7 ta eng mashhur pack (`RestrictedEmoji`, `TgAndroidIcons`, `tgmacicons`, `vector_icons_by_fStikBot`, `NewsEmoji`, `RoboEmoji`, `StatusEmoji`) bo'yicha tozalangan va tekshirilgan ID lar.
- **🎴 Qulay `TelegramCard` Generatori:** Sarlavhasi tashqarida, tanasi iqtibosda, to'liq kenglikdagi ko'rinmas spacer va kengayuvchi imzo bilan ideal kartochka yasaydi.
- **🔘 `build_inline_button` Yordamchisi:** Aiogram 3 da tugma nomini toza saqlash, custom emoji ikonka biriktirish va rang berish (`primary`, `success`, `danger`).

- **🔍 Pack Scanner CLI:** Istalgan ommaviy stiker to'plami nomini kiritib, undagi barcha ishlaydigan custom emoji ID larini avtomatik ajratib oladi.
- **🛡️ Kod Linter / Validator:** Bot kodingizni tekshirib, xato va ortiqcha emojilarni avtomatik topadi.
- **🤖 Universal AI Agent Skill (`SKILL.md`):** Antigravity, Claude Code, Cursor kabi AI larni bot dizayni bo'yicha professional darajaga ko'taradi.

---

## ⚡ Qisqa Qo'llanma (Aiogram 3 Misolida)

```python
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.keyboard import InlineKeyboardBuilder

from telegram_premium_emojis import TelegramCard, CommonIcons, build_inline_button

bot = Bot(token="SIZNING_BOT_TOKENINGIZ", default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message()
async def start_handler(message: types.Message):
    # 1. Chiroyli kartochka yasash
    card = (
        TelegramCard()
        .set_title("PDF Xizmatlari", icon_id=CommonIcons.DOCUMENT)
        .add_line("PDF fayllarni Word va Excel ga o'giring.", icon_id=CommonIcons.SPARKLES)
        .add_line("Maksimal hajm: 100 MB", icon_id=CommonIcons.ATTACH)
        .add_line("Holat: Barcha serverlar faol ishlamoqda", icon_id=CommonIcons.SUCCESS)
        .with_spacer()  # Kartochkani to'liq kenglikka yoyadi
        .set_signature("@osonpdfrobot • Tez va Xavfsiz", expandable=True)
        .build()
    )

    # 2. Custom emoji ikonli tugmalar
    builder = InlineKeyboardBuilder()
    builder.row(
        build_inline_button(
            text="Fayl yuborish",
            callback_data="upload",
            icon_custom_emoji_id=CommonIcons.UPLOAD,
            style="success"  # Yashil rangda ajratib ko'rsatish
        )
    )
    builder.row(
        build_inline_button(
            text="Sozlamalar",
            callback_data="settings",
            icon_custom_emoji_id=CommonIcons.SETTINGS
        ),
        build_inline_button(
            text="Orqaga",
            callback_data="back",
            icon_custom_emoji_id=CommonIcons.BACK,
            style="danger"  # Qizil rangda
        )
    )

    await message.answer(card, reply_markup=builder.as_markup())
```

---

## 📐 Telegram Kartochka Qoidalari

Biz ishlab chiqqan va sinovdan o'tgan standart quyidagicha tuziladi:

```
<b><tg-emoji emoji-id="...">👑</tg-emoji> Sarlavha (Blockquote tashqarisida)</b>

<blockquote><i><tg-emoji emoji-id="...">✨</tg-emoji> Birinchi ma'lumot yoki qator

<tg-emoji emoji-id="...">⚡️</tg-emoji> Ikkinchi ma'lumot yoki qator
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</i></blockquote>

<blockquote expandable><i>✅ @BotUsername orqali tayyorlandi</i></blockquote>
```

### Nima uchun bu tartib eng yaxshisi?
1. **Sarlavha tashqarida bo'lishi:** Sarlavha iqtibos ichiga kirmaydi va alohida ajralib turadi.
2. **Ko'rinmas Spacer (`FULL_WIDTH_SPACER`):** Telegram matn uzunligiga qarab xabarni qisib qo'yadi. Ko'rinmas brayl probeli tufayli kartochka doimo to'liq kenglikda va tartibli turadi.
3. **Kengayuvchi Imzo (`expandable`):** Asosiy xabarga xalaqit bermagan holda pastda bot brendini ko'rsatadi.

---

## 📚 Eng Ko'p Ishlatiladigan 20 ta Custom Emoji ID

To'liq 920+ ro'yxat [`catalog/catalog.md`](catalog/catalog.md) yoki [`catalog/all_emojis.json`](catalog/all_emojis.json) faylida.

| Maqsadi | Emoji | Custom Emoji ID | HTML Kodi |
|---|---|---|---|
| **Orqaga** | ⬅️ | `5877536313623711363` | `<tg-emoji emoji-id="5877536313623711363">⬅️</tg-emoji>` |
| **Bosh Menyu** | 🏠 | `5807868868886009920` | `<tg-emoji emoji-id="5807868868886009920">🏠</tg-emoji>` |
| **Tasdiqlash** | ✅ | `5920052658743283381` | `<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji>` |
| **Bekor qilish** | ❌ | `5258226313285607065` | `<tg-emoji emoji-id="5258226313285607065">❌</tg-emoji>` |
| **Olmos / Token** | 💎 | `5807465992363710697` | `<tg-emoji emoji-id="5807465992363710697">💎</tg-emoji>` |
| **Yulduz / Tarif** | ⭐️ | `5874948844935974490` | `<tg-emoji emoji-id="5874948844935974490">⭐️</tg-emoji>` |
| **Tezlik / Yashin**| ⚡️ | `5843553939672274145` | `<tg-emoji emoji-id="5843553939672274145">⚡️</tg-emoji>` |
| **Toj / VIP** | 👑 | `5807868868886009920` | `<tg-emoji emoji-id="5807868868886009920">👑</tg-emoji>` |
| **Hujjat** | 📄 | `5258477770735885832` | `<tg-emoji emoji-id="5258477770735885832">📄</tg-emoji>` |
| **Papka** | 📁 | `5875206779196935950` | `<tg-emoji emoji-id="5875206779196935950">📁</tg-emoji>` |
| **Yuklab olish** | ⬇️ | `5258336354642697821` | `<tg-emoji emoji-id="5258336354642697821">⬇️</tg-emoji>` |
| **Yuklash** | ⬆️ | `5260652420052032852` | `<tg-emoji emoji-id="5260652420052032852">⬆️</tg-emoji>` |
| **Ogohlantirish** | ⚠️ | `5258474669769497337` | `<tg-emoji emoji-id="5258474669769497337">⚠️</tg-emoji>` |
| **Ma'lumot** | ℹ️ | `5258503720928288433` | `<tg-emoji emoji-id="5258503720928288433">ℹ️</tg-emoji>` |
| **Sozlamalar** | ⚙️ | `5258420634785947640` | `<tg-emoji emoji-id="5258420634785947640">⚙️</tg-emoji>` |

---

## 🛠️ CLI Buyruqlari

### 1. Istalgan stiker/emoji to'plamini skan qilish:
```bash
python -m telegram_premium_emojis.scanner TgAndroidIcons TajalyanEmoji --token BOT_TOKENINGIZ
```

### 2. Bot kodingizni tekshirish (Linter):
```bash
python -m telegram_premium_emojis.validator .
```

---

## 🤖 AI Agent Skill (`SKILL.md`)

Ushbu repozitoriy ichida tayyor [`SKILL.md`](SKILL.md) fayli mavjud. Uni Antigravity, Claude yoki Cursor kabi AI agentingizga qo'shib qo'ysangiz, AI bot kodini yozayotganda avtomatik ravishda eng to'g'ri custom emoji teglari, tugma qoidalari va zamonaviy kartochka andozalarini qo'llaydi!

---

## 📄 Litsenziya

MIT Litsenziyasi © 2026 Abbos & OsonPDF Hamjamiyati.
