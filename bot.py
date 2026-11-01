import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, ChatMemberHandler
from apscheduler.schedulers.asyncio import AsyncIOScheduler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = '9073817246:AAFyn4rlEEQopCU-kpMtJVS4VlvQ9MPNW5M'
PHOTO_PATH = 'photo.jpg'

active_chats = set()

async def send_scheduled_photo(context: ContextTypes.DEFAULT_TYPE):
    for chat_id in list(active_chats):
        try:
            with open(PHOTO_PATH, 'rb') as photo:
                await context.bot.send_photo(chat_id=chat_id, photo=photo)
            print(f"Фото отправлено в чат {chat_id}")
        except Exception as e:
            print(f"Ошибка отправки в чат {chat_id}: {e}")
            if "Forbidden" in str(e) or "chat not found" in str(e):
                active_chats.discard(chat_id)

async def track_chat_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = update.my_chat_member
    if not result:
        return
    chat = result.chat
    new_status = result.new_chat_member.status
    if new_status in ['member', 'administrator']:
        active_chats.add(chat.id)
        print(f"Бот добавлен в чат: {chat.title} ({chat.id})")
    elif new_status in ['left', 'kicked']:
        active_chats.discard(chat.id)
        print(f"Бот удален из чата: {chat.id}")

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(ChatMemberHandler(track_chat_member, ChatMemberHandler.MY_CHAT_MEMBER))

    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_scheduled_photo, 'interval', seconds=60, args=[application])
    
    scheduler.start()
    print("Бот запущен в облаке и ждет добавления в группы...")
    application.run_polling()

if __name__ == '__main__':
    main()
