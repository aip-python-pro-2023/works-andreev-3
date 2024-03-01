import os
from dotenv import load_dotenv
import telebot
from telebot.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage
from quest import QuestRepository

load_dotenv()

storage = StateMemoryStorage()

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode=None, state_storage=storage)


class QuestsSelectStates(StatesGroup):
    Moi = State()
    Diehard = State()


quest_repo = QuestRepository()


@bot.message_handler(state=QuestsSelectStates.Moi)
def send_moi(message: telebot.types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('Выйти', callback_data='quit'))
    bot.send_message(message.chat.id, f'Выбран квест "Мастер Иике-баны"', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda callback: callback.data == 'quit')
def quest_selected_callback(callback: telebot.types.CallbackQuery):
    bot.delete_state(callback.from_user.id)
    bot.send_message(callback.message.chat.id, f'Вы вышли из квеста')


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
    state = bot.get_state(message.from_user.id)
    if state:
        bot.send_message(message.chat.id, state)


@bot.callback_query_handler(func=lambda callback: callback.data.startswith('quest-'))
def quest_selected_callback(callback: telebot.types.CallbackQuery):
    quest_name = callback.data.split('-', 1)[1]
    if quest_name == 'Moi':
        bot.set_state(callback.from_user.id, state=QuestsSelectStates.Moi)
    elif quest_name == 'Diehard':
        bot.set_state(callback.from_user.id, state=QuestsSelectStates.Diehard)
    bot.send_message(callback.message.chat.id, f'Success {quest_name}!')


@bot.message_handler(func=lambda m: True)
def echo_all(message: telebot.types.Message):
    bot.reply_to(message, message.text)


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.infinity_polling()
