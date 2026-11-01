import os
import asyncio
from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

TOKEN = "9073817246:AAFyn4rlEEQopCU-kpMtJVS4VlvQ9MPNW5M"
CHAT_ID = "ТВОЙ_CHAT_ID"  # Укажи ID своего чата или группы

bot = Bot(token=TOKEN)

async def send_photo():
    try:
        await bot.send_message(chat_id=CHAT_ID, text="Бот работает каждую минуту!")
    except Exception as e:
        print(f"Ошибка отправки: {e}")

async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_photo, 'interval', minutes=1)
    scheduler.start()
    print("Бот успешно запущен :)")
    
    while True:
        await asyncio.sleep(3600)

if __name__ == '__main__':
    asyncio.run(main())
