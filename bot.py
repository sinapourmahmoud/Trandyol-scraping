from dotenv import load_dotenv
import os
from telegram import Update
from telegram.ext import Application,CommandHandler,ContextTypes,MessageHandler,filters

load_dotenv()
token=os.getenv('TOKEN')

class Bot():
    _instance=None
    def __init__(self):
        self.app=Application.builder().token(token).build()
        start_handler=CommandHandler('start',self.start)
        self.app.add_handler(start_handler)

    async def start (update:Update,context:ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id,text="Hello to you",reply_to_message_id=update.effective_message.id)
    def run(self):
        self.app.run_polling()
    


