from pyrogram.client import Client 
from env import API_ID, API_HASH
import asyncio

token = input('token: ')
bot = Client('wm', bot_token=token, api_id=API_ID, api_hash=API_HASH)

async def main():
    await bot.start()
    print(await bot.export_session_string())
    await bot.stop()

if __name__ == "__main__":
    event_policy = asyncio.get_event_loop_policy()
    event_loop = event_policy.new_event_loop()
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    finally:
        event_loop.close()
