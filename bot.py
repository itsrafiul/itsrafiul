from telegram import Update, Bot
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

BOT_TOKEN = 'bot7793433237:AAGsxA8eyWT-KG4CDjcALNPAyguAWTGIBaw'
FORWARD_TO_CHANNEL = '@seed343g'

def forward_to_channel(update: Update, context: CallbackContext):
    if update.message:
        context.bot.forward_message(
            chat_id=FORWARD_TO_CHANNEL,
            from_chat_id=update.message.chat_id,
            message_id=update.message.message_id
        )

updater = Updater(BOT_TOKEN)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.all, forward_to_channel))

print("Bot is running 24/7 on Render!")
updater.start_polling()
updater.idle()
