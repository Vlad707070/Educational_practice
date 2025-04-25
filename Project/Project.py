import random
import telebot
import requests

BOT_TOKEN = '7750673944:AAED3LaAqPnZUSD1eqv9e4Bxz4r7FIApo2I'
WEATHER_TOKEN = '93bfe38d71334ee98552e1aaa275f509'
GIPHY_API_KEY = "M40G6BpmxLfyHfhERwNEWWifpBAWKYk5"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "Привет! Я бот с погодой и полезными штуками")
    main_control_menu(message.chat.id)

def main_control_menu(chat_id):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Погода", "Факт")
    markup.row("Анекдот","GIF")
    markup.row("Стикер", "Привет", "Пока")
    bot.send_message(chat_id, "Выбери действие:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def processing_messages_from_the_user(message):
    text = message.text
    chat_id = message.chat.id

    if text == "Погода":
        the_name_of_the_city_from_the_user(chat_id)
    elif text == "Факт":
        sending_facts_to_the_user(chat_id)
    elif text == "Анекдот":
        sending_jokes_to_the_user(chat_id)
    elif text == "Стикер":
        sending_stickers_to_the_user(chat_id)
    elif text == "Привет":
        send_greetings(chat_id)
    elif text == "Пока":
        sending_a_goodbye(chat_id)
    elif text == "GIF":
        bot.send_message(chat_id, "Какой GIF вы хотите увидеть?")
        bot.register_next_step_handler(message, send_gif)

def the_name_of_the_city_from_the_user(chat_id):
    bot.send_message(chat_id, "Напиши название города:")
    bot.register_next_step_handler_by_chat_id(chat_id, weather_for_the_requested_city)

def weather_for_the_requested_city(message):
    city = message.text
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_TOKEN}&units=metric&lang=ru"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        bot.send_message(message.chat.id, f"Погода в {city}: {desc}, {temp}°C")
    else:
        bot.send_message(message.chat.id, "Не удалось найти город. Попробуй ещё раз.")

def get_random_gif(query):
    url = f"https://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={query}&limit=50"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    if data["data"]:
        gif = random.choice(data["data"])
        return gif["images"]["original"]["url"]
    else:
        return None


def send_gif(message):
    query = message.text
    gif_url = get_random_gif(query)
    if gif_url:
        bot.send_animation(message.chat.id, gif_url)
    else:
        bot.send_message(message.chat.id, "Не удалось найти GIF по запросу.")

def sending_stickers_to_the_user(chat_id):
    stickers = [
        "CAACAgIAAxkBAAEOasVoAAE4EchVEkjdOlzmCglXA-QmD0UAAn4oAALlrJFIOui6JVAenew2BA",
        "CAACAgIAAxkBAAEOoQFoCnPera9SLu_j1f5OzTbFwEG8owACshwAAtuhmEhiwTogMJddoTYE",
        "CAACAgIAAxkBAAEOoQNoCnPpFAjkgcpXURGstWRlPXxiUwACdSgAAlO9QEr3x-3VRiwHpzYE",
        "CAACAgIAAxkBAAEOoQVoCnP-ipKpXkYyUxe_RShfcExQqQACFSoAAj70MUks_ObYEZZlijYE"
    ]
    bot.send_sticker(chat_id, random.choice(stickers))

def sending_jokes_to_the_user(chat_id):
    jokes = [
        "Почему программисты путают Хэллоуин и Рождество? Потому что Oct 31 = Dec 25.",
        "Если программа не работает, значит, это фича, а не баг.",
        "Программист — это человек, который решает проблему, которую вы не знали, способом, который вы не поймёте.",
        "Код — это как шутка: если надо объяснять, значит она плохая.",
        "Программисты не ошибаются, они просто создают неожиданные возможности."
    ]
    bot.send_message(chat_id, random.choice(jokes))

def sending_facts_to_the_user(chat_id):
    facts = [
        "Python назван не в честь змеи, а в честь шоу Monty Python.",
        "Первым программистом была женщина — Ада Лавлейс.",
        "День программиста — 256-й день года (13 сентября или 12 в високосный).",
        "Программисты часто используют утёнка для поиска ошибок (метод резиновой уточки).",
        "Термин «баг» появился, когда мотылёк застрял в реле старого компьютера."
    ]
    bot.send_message(chat_id, random.choice(facts))

def send_greetings(chat_id):
    greetings = [
        "Привет! Рад тебя видеть!",
        "Здарова, друг! Чем сегодня займёмся?",
        "Здравствуйте! Чем могу помочь?",
        "Привет-привет! Готов к приключениям?",
        "Хэй! День будет классным!"
    ]
    bot.send_message(chat_id, random.choice(greetings))

def sending_a_goodbye(chat_id):
    goodbyes = [
        "Пока! Увидимся позже!",
        "До скорого!",
        "Было приятно пообщаться!",
        "Прощай! Хорошего дня!",
        "Удачи и хорошего настроения!"
    ]
    bot.send_message(chat_id, random.choice(goodbyes))

bot.polling(none_stop=True)