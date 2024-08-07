import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id
    group_name = update.message.chat.title
    await update.message.reply_text(f'Hello! This is the group chat ID: {chat_id}\nGroup Name: {group_name}')
    logging.info(f'Chat ID: {chat_id}, Group Name: {group_name}')
    print(f'Chat ID: {chat_id}, Group Name: {group_name}')  # Add print for debugging

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id
    group_name = update.message.chat.title
    await update.message.reply_text(f'This is the group chat ID: {chat_id}\nGroup Name: {group_name}')
    logging.info(f'Chat ID: {chat_id}, Group Name: {group_name}')
    print(f'Chat ID: {chat_id}, Group Name: {group_name}')  # Add print for debugging

async def main() -> None:
    # Initialize the bot
    application = Application.builder().token('7356522370:AAFTZrm5OhhUU8UbJVd2c1gKssWVGsdm0ig').build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start polling
    await application.run_polling()

if __name__ == '__main__':
    import nest_asyncio
    import asyncio

    nest_asyncio.apply()
    asyncio.run(main())
