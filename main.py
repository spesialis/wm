from wm import wm 
from pyrogram.client import Client
from pyrogram.types import Message
from pyrogram import filters
from env import API_ID, API_HASH, SESSION
import asyncio

bot = Client('wm', api_id=API_ID, api_hash=API_HASH, session_string=SESSION)

@bot.on_message(filters.photo)
async def photo_handler(client: Client, message: Message):
    r = await message.reply('Terminal Running')
    image_path = str(await client.download_media(message))
    result_path = wm.generate(image_path)
    await message.reply_photo(result_path)
    await r.delete()

if __name__ == "__main__":
    event_policy = asyncio.get_event_loop_policy()
    event_loop = event_policy.new_event_loop()
    try:
        bot.run()
    except KeyboardInterrupt:
        pass
    finally:
        event_loop.close()
