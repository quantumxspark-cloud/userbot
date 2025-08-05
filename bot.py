from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import datetime

# 🔐 Bot credentials
API_ID = 21747701
API_HASH = "f204eca5ea3ea9067da3386a45b7d677"
BOT_TOKEN = "8486038388:AAGlUPQOFvk6MPnRyUqs95bYXfUHnsGOOGg"

# 🤖 Create bot client
app = Client("welcome_id_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# 🚀 Start command handler
@app.on_message(filters.command("start"))
async def start_handler(client: Client, message: Message):
    user = message.from_user
    chat_id = user.id

    # Use @username if available, else use first name
    username_display = f"@{user.username}" if user.username else user.first_name

    # 📅 Current date & time
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    day = now.strftime("%A")
    time = now.strftime("%I:%M %p")

    # 💬 Final message
    welcome_text = (
        f"👋 Welcome {username_display}\n\n"
        f"🗓 Date: {date}\n"
        f"📅 Day: {day}\n"
        f"⏰ Time: {time}\n\n"
        f"🆔 Chat ID: `{chat_id}`\n"
        f"🔗 Username: {username_display}\n\n"
        f"👨‍💻 DEVELOPER: @HEHE_SPARK ⚡"
    )

    await message.reply_text(welcome_text)

# ▶️ Run the bot
app.run()