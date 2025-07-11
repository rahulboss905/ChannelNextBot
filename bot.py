
import logging
import os
from pymongo import MongoClient
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Load environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")

# MongoDB setup
client = MongoClient(MONGO_URI)
db = client["ChannelBotDB"]
users_collection = db["users"]

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id
    name = user.first_name

    # Store or update user in MongoDB
    users_collection.update_one(
        {"user_id": user_id},
        {"$set": {"name": name}},
        upsert=True
    )

    await update.message.reply_text(f"ðŸ‘‹ Hello, {name}! Welcome to the bot.")

# /info command handler
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user = users_collection.find_one({"user_id": user_id})

    if user:
        await update.message.reply_text(f"ðŸ“‹ Your info:\nName: {user.get('name')}\nUser ID: {user_id}")
Name: {user.get('name')}
User ID: {user_id}")
    else:
        await update.message.reply_text("âš ï¸ You are not registered. Use /start first.")

# Main entry point
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("info", info))

    logger.info("Bot is polling...")
    app.run_polling()

if __name__ == "__main__":
    main()
