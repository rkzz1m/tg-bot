import os
import asyncio
from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

TOKEN = "9073817246:AAFyn4rlEEQopCU-kpMtJVS4VlvQ9MPNW5M"
CHAT_ID = "ТВОЙ_CHAT_ID"  # Твой ID чата

bot = Bot(token=TOKEN)

async def send_my_photo():
    try:
        # Пока отправляем тестовую картинку по прямой ссылке, чтобы бот точно работал
        # Потом заменим на твою, когда скинешь её боту
        photo_url = "https://picsum.photos/600/400"
        await bot.send_photo(
            chat_id=CHAT_ID, 
            photo=photo_url, 
            caption="Бот шлет картинку каждую минуту :)"
        )
    except Exception as e:
        print(f"Ошибка отправки фото: {e}")

async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_my_photo, 'interval', minutes=1)
    scheduler.start()
    print("Бот с отправкой картинок запущен :)")
    
    while True:
        await asyncio.sleep(3600)

if __name__ == '__main__':
    asyncio.run(main())
