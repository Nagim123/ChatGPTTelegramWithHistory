from typing import Callable
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


class TelegramBot() :
    def __init__(self, token : str, on_message: Callable[[int, str], None]) -> None:
        self.token = token
        self.t_bot = telebot.TeleBot(token)
        @self.t_bot.message_handler()
        def _(message) :
            on_message(message.chat.id, message.text)
        self.keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    def send_message(self, chat_id : int, content : str) -> None :
        self.t_bot.send_message(chat_id, content, parse_mode="MARKDOWN", reply_markup=self.keyboard)

    def update_buttons(self, button_list: list):
        self.keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        for button_name in button_list:
            self.keyboard.add(KeyboardButton(button_name))

    def start_bot(self) -> None :
        self.t_bot.infinity_polling()