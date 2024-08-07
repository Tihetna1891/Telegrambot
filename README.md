Telegram Bot with Google Sheets Integration
This project involves a Telegram bot that integrates with Google Sheets to automate data management and streamline communication across multiple groups.

Features
Automatic Group Info Logging: Captures and logs group names and chat IDs to Google Sheets when messages are received.
Message Sending: Allows sending messages to specific groups based on stored chat IDs.
Secure Configuration: Uses environment variables to manage sensitive information like bot tokens and credentials.
Tools and Libraries
Python: Programming language used for the bot.
python-telegram-bot: Library for interacting with the Telegram Bot API.
gspread: Library for interacting with Google Sheets.
oauth2client: Library for Google API authentication.
python-dotenv: Library for managing environment variables.
Installation
Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/your-repository.git
cd your-repository
Set Up a Virtual Environment

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies

bash
Copy code
pip install python-telegram-bot gspread oauth2client python-dotenv nest_asyncio
Set Up Google Sheets API

Create a Google Cloud project and enable the Google Sheets API.
Create a service account and download the credentials JSON file.
Share the Google Sheet with the service account email.
Configure Environment Variables

Create a .env file in the project root with the following content:

makefile
Copy code
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
GOOGLE_CREDENTIALS_PATH=path/to/your/credentials.json
Usage
Run the Bot

bash
Copy code
python your_script_name.py

Interact with the Bot
/start: Logs the group name and chat ID to Google Sheets.
/send_message <group_name> <message>: Sends a message to the specified group.

Contributing
Feel free to submit issues or pull requests if you have suggestions or improvements.
