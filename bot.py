import os
from pyrogram import Client, filters
from database import add_movie,get_movie

BOT_TOKEN=os.getenv("BOT_TOKEN")
API_ID=int(os.getenv("35790707"))
API_HASH=os.getenv("44753bcac8911c81028f009377368330")

bot = Client(
    "moviebot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

@bot.on_message(filters.command("start"))
async def start(client,message):
    await message.reply("🎬 Movie Bot Ready\nUse /movie movie_name")

@bot.on_message(filters.command("movie"))
async def movie(client,message):

    name = message.text.split(" ",1)[1]

    data = get_movie(name)

    if data:
        await message.reply_document(data[0])
    else:
        await message.reply("❌ Movie not found")

# admin command to add movie
@bot.on_message(filters.document)
async def save_movie(client,message):

    name = message.document.file_name

    file_id = message.document.file_id

    add_movie(name,file_id)

    await message.reply("✅ Movie saved in database")

bot.run()
