from telegram import Update
from telegram.ext import Application,CommandHandler,ContextTypes,MessageHandler,filters



async def start (update:Update,context:ContextTypes.DEFAULT_TYPE):

    await context.bot.send_message(chat_id=update.effective_chat.id,text="Hello to you",reply_to_message_id=update.effective_message.id)


async def echo(update:Update,context:ContextTypes.DEFAULT_TYPE):
    text=update.effective_message.text
    await context.bot.send_message(chat_id=update.effective_chat.id,text=text,reply_to_message_id=update.effective_message.id)


def main():
    app=Application.builder().token(token).build()
    start_handler=CommandHandler('start',start)
    echo_handler=MessageHandler(filters.TEXT&(~filters.COMMAND),echo)
    app.add_handler(start_handler)
    app.add_handler(echo_handler)
    app.run_polling()

if __name__=='__main__':
    main()
