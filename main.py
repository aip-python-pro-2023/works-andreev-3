import os
from dotenv import load_dotenv
import telebot
from telebot.types import ReplyKeyboardRemove

from quest import QuestRepository

load_dotenv()

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode=None)

quest_repo = QuestRepository()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    bot.send_message(message.chat.id, "Howdy, how are you doing?", reply_markup=ReplyKeyboardRemove())


@bot.message_handler(commands=['quests'])
def quests_list(message: telebot.types.Message):
    quests = quest_repo.get_all()
    keyboard = telebot.types.InlineKeyboardMarkup()
    for quest in quests:
        keyboard.add(telebot.types.InlineKeyboardButton(quest.get_name(), callback_data=f'quest-{quest.quest_id}'))
    quests_data = "\n".join([f'* {quest.get_name()}' for quest in quests])
    response = telebot.formatting.escape_markdown(f'Список квестов: \n\n{quests_data}')
    bot.send_message(message.chat.id, response, parse_mode='MarkdownV2', reply_markup=keyboard)


@bot.message_handler(func=lambda m: True)
def echo_all(message: telebot.types.Message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
