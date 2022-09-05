import requests


def get_max_category():
    categories = requests.get('http://127.0.0.1:8000/categories').json()
    return len(categories)


def get_catogories(bot, ai_bot):
    try:
        categories = requests.get('http://127.0.0.1:8000/categories').json()
        for number, category in enumerate(categories, 1):
            bot.send_message(ai_bot.user_id, f"{number} - {category['name']}")
    except:
        bot.send_message(ai_bot.user_id, 'Спробуйте пізніше')


def get_books(category_id, bot, ai_bot):
    categories = requests.get(f'http://127.0.0.1:8000/categories/{category_id}').json()
    for number, book in enumerate(categories['books'], 1):
        bot.send_message(ai_bot.user_id, f"{number} -  {book['title']}")


def get_one_book(category_id, book_number, bot, ai_bot):
    categories = requests.get(f'http://127.0.0.1:8000/categories/{category_id}').json()
    bot.send_message(ai_bot.user_id,
                     f'{categories["books"][book_number - 1]["title"]}')
    bot.send_message(ai_bot.user_id,
                     f'{categories["books"][book_number - 1]["description"]}')
