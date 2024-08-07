import nest_asyncio
import logging
import asyncio
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
GOOGLE_CREDENTIALS_PATH = os.getenv('GOOGLE_CREDENTIALS_PATH')
# Apply nest_asyncio to allow nested async functions
nest_asyncio.apply()

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_CREDENTIALS_PATH, scope)
client = gspread.authorize(creds)
sheet = client.open("Telegrambot").sheet1

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id
    group_name = update.message.chat.title
    await update.message.reply_text(f'Hello! This is the group chat ID: {chat_id}\nGroup Name: {group_name}')
    logging.info(f'Chat ID: {chat_id}, Group Name: {group_name}')
    print(f'Chat ID: {chat_id}, Group Name: {group_name}')
    
    # Save group name and chat ID to Google Sheets
    existing_group = sheet.find(group_name)
    if existing_group:
        # Update existing group chat ID
        sheet.update_cell(existing_group.row, existing_group.col + 1, chat_id)
    else:
        # Insert new group and chat ID
        sheet.append_row([group_name, chat_id])

async def send_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        group_name = context.args[0]
        message = ' '.join(context.args[1:])
        
        # Fetch group chat ID from Google Sheets
        cell = sheet.find(group_name)
        if cell:
            group_chat_id = sheet.cell(cell.row, cell.col + 1).value
            await context.bot.send_message(chat_id=group_chat_id, text=message)
            await update.message.reply_text(f'Message sent to {group_name}')
        else:
            await update.message.reply_text(f'Group {group_name} not found.')
    except IndexError:
        await update.message.reply_text('Usage: /send_message <group_name> <message>')

async def main() -> None:
    # Initialize the bot
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("send_message", send_message))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, start))  # Log all text messages to capture group info

    # Start polling
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
