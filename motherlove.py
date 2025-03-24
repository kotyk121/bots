import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Настройки
TOKEN = "7334051684:AAH7siBB-7mJfM4oBgpeYWKgt0gfFcVDIM8"  # Замініть на токен вашого бота

# Привітальне повідомлення
WELCOME_MESSAGE = (
    "Привіт! 💖\n"
    "Я давид, створив для тебе мамо свій бот. "
    "тут я покажу всю свою любовь до тебе. "
    
)

# Списки повідомлень
COMPLIMENTS = [
    "Мамо, ти — найніжніша і найдобріша людина у світі! 💕",
    "Твоя усмішка, мамо, робить мій день яскравішим! 😊",
    "Мамо, ти — мій приклад і моя гордість! ✨",
    "Ти — найкраща мама, яку тільки можна уявити! 🌟",
    "Мамо, твоя любов — це найбільший скарб у моєму житті! 💖"
]

POEMS = [
    "Мамо, ти — мій світ, моя зоря,\n"
    "Твоя любов зігріває мене щодня.\n"
    "Дякую тобі за все, що ти дала,\n"
    "Ти — мій ангел, моя рідна душа! 💞",

    "Твоя ніжність, мамо, як весняний вітер,\n"
    "Ти — мій спокій у будь-який день.\n"
    "Люблю тебе, моя найдорожча,\n"
    "Ти — моє серце, моя вічна весна! 🌸",

    "Мамо, ти — мій промінь у темряві,\n"
    "Твоя любов — це крила мої.\n"
    "Дякую, що ти завжди поруч,\n"
    "Ти — моя радість, моя любов! 🌼"
]

MESSAGES = [
    "Мамо, я так вдячний за твою любов і турботу. Ти — найкраща! 💕",
    "Кожен день я дякую долі за те, що у мене така мама, як ти! 😊",
    "Мамо, ти завжди знаєш, як мене підтримати. Дякую тобі за все! 🌟",
    "Ти — мій дім, моя фортеця, моя любов. Люблю тебе, мамо! 🏡",
    "Мамо, твої обійми — це найкраще місце у світі! 🤗"
]

GIFTS = [
    "💐 Дарую тобі, мамо, величезний букет твоїх улюблених квітів! Нехай вони радують тебе так само, як ти радуєш мене!",
    "🍰 Ось тобі, мамо, найсмаодший торт! Ти заслуговуєш усе найкраще! 🥳",
    "🕯️ Уявімо, мамо, що ми разом п’ємо чай при свічках. Я так люблю наші розмови! ☕",
    "🌟 Мамо, я дарую тобі зірку з неба! Вона світить так само яскраво, як твоя любов до мене!"
]

# Меню
def get_main_keyboard():
    return ReplyKeyboardMarkup([
        ["💌 Комплімент мамі", "📜 Вірш про маму"],
        ["💬 Тепле повідомлення", "🎁 Подарунок для мами"]
    ], resize_keyboard=True)

# Обробники
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Команда /start від користувача {update.effective_chat.id}")
    context.user_data['menu'] = 'main'
    await update.message.reply_text(WELCOME_MESSAGE, reply_markup=get_main_keyboard())

async def handle_commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Отримано повідомлення: {update.message.text} від {update.effective_chat.id}")
    text = update.message.text.lower()

    # Основне меню
    if "комплімент мамі" in text:
        compliment = random.choice(COMPLIMENTS)
        await update.message.reply_text(compliment)
    elif "вірш про маму" in text:
        poem = random.choice(POEMS)
        await update.message.reply_text(poem)
    elif "тепле повідомлення" in text:
        message = random.choice(MESSAGES)
        await update.message.reply_text(message)
    elif "подарунок для мами" in text:
        gift = random.choice(GIFTS)
        await update.message.reply_text(gift)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_commands))
    print("Бот 'Любов до мами' активовано...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()