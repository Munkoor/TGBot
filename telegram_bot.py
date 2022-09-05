import telebot
from telebot import types
from states import BookCategoryState, MainMenuState, State


bot = telebot.TeleBot("5528928530:AAF-xZS2wlkJgSfN0EqLRbQ617k8j49BkKo")


class AIBot:
    def __init__(self, user_id):
        self.state = MainMenuState(bot=bot, ai_bot=self)
        self.user_id = user_id
        
    def answer(self, message):
        if message == '/info':
            return bot.send_message(self.user_id, self.state.text)
        answer = self.state.answer(message)
        if isinstance(answer, State):
            self.state = answer
            bot.send_message(self.user_id, self.state.text)


bots = [] 


@bot.message_handler(commands=["start"])
def start_using(message):
    markup = types.ReplyKeyboardMarkup(row_width=5)
    itembtn1 = types.KeyboardButton('/info')
    markup.add(itembtn1)
    bot.send_message(message.chat.id,
                     'Вітаємо! В цьому телеграм боті ви зможете інформацію із книжок по '
                     'Python. Нажми /info , щоб почати',
                     reply_markup=markup)
    

@bot.message_handler(content_types=["text"])
def get_message(message):
    if message.chat.id not in [bot.user_id for bot in bots]:
        main_bot = AIBot(message.chat.id)
        bots.append(main_bot)
    else:
        for ai_bot in bots:
            if message.chat.id == ai_bot.user_id:
                main_bot = ai_bot
    main_bot.answer(message.text)


bot.polling()
