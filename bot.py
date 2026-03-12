from pyrogram import Client, filters

API_ID = 35790707
API_HASH = "44753bcac8911c81028f009377368330"
BOT_TOKEN = "8779345278:AAGUeRRmEx0C2MP2q4xDmNQUVlcyh_GRRR4"

CHANNEL_ID = -1003865059298

bot = Client(
    "moviebot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

movies = {}

@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("🎬 Movie Bot Ready\nUse /movie name")

@bot.on_message(filters.command("movie"))
async def movie(client, message):

    name = message.text.split(" ",1)[1].lower()

    if name in movies:
        await message.reply_document(movies[name])
    else:
        await message.reply("❌ Movie not found")

@bot.on_message(filters.chat(CHANNEL_ID) & filters.document)
async def save_movie(client, message):

    name = message.document.file_name.lower()
    file_id = message.document.file_id

    movies[name] = file_id

bot.run()
