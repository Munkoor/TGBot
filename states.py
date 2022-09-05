from abc import ABC, abstractmethod
from libs import *


class State(ABC):
    def __init__(self, bot, ai_bot):
        self.bot = bot
        self.ai_bot = ai_bot
    text = ""

    @abstractmethod
    def answer(self, message):
        pass


class BookCategoryState(State):
    text = '''
1 Продивитися всі категорії книг
2 Головне меню:'''

    def answer(self, message):
        if message == '1':
            get_catogories(bot=self.bot, ai_bot=self.ai_bot)
            return WorkCategoryState(self.bot, self.ai_bot)
        elif message == '2':
            return MainMenuState(self.bot, self.ai_bot)
        else:
            self.bot.send_message(self.ai_bot.user_id, 'Некорректна команда')


class WorkCategoryState(State):
    text = '''
Оберіть категорію:
(q - повернутися в головне меню)
'''

    def answer(self, message):
        if message == 'q':
            return MainMenuState(self.bot, self.ai_bot)

        category_id = int(message)
        try:
            get_books(bot=self.bot, ai_bot=self.ai_bot, category_id=category_id)
            return ChooseOneBookState(self.bot, self.ai_bot, category_id)
        except:
            self.bot.send_message(self.ai_bot.user_id, 'Такої категорії немає')
            return WorkCategoryState(self.bot, self.ai_bot)


class ChooseOneBookState(State):
    text = '''
    Оберіть книгу, опис якої ви хочете прочитати:
    (q - повернутися в головне меню)
    '''

    def __init__(self, bot, ai_bot, category_id):
        super().__init__(bot, ai_bot)
        self.category_id = category_id

    def answer(self, message):
        if message == 'q':
            return MainMenuState(self.bot, self.ai_bot)

        book_number = int(message)
        try:
            get_one_book(bot=self.bot,
                         ai_bot=self.ai_bot,
                         book_number=book_number,
                         category_id=self.category_id)
        except:
            self.bot.send_message(self.ai_bot.user_id, 'Такої книги немає')
            return WorkCategoryState(self.bot, self.ai_bot)


class MainMenuState(State):
    text = '''Ви в головному меню! 
Доступні дії:
1 - Перейти в меню категорий книг:'''

    def answer(self, message):
        if message == '1':
            return BookCategoryState(self.bot, self.ai_bot)
        else:
            self.bot.send_message(self.ai_bot.user_id, 'Некорректна команда')
