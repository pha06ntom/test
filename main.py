
from telebot import types,telebot

bot = telebot.TeleBot("token")  #вставить token из телеграмма

db = {'ФИО': 'Иванов Иван', 'Адрес': 'ул.Ленина, д.7', 'Работа': 'Школа №34'}

@bot.message_handler(commands=["start"]) #управитель сообщениями
def start(m, res=False): # m - сообщение, res - отдых
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Кнопки
    item1 = types.KeyboardButton("ФИО")
    item2 = types.KeyboardButton("Адрес")
    item3 = types.KeyboardButton("Работа")

    markup.add(item1)
    markup.add(item2)
    markup.add(item3)

    bot.send_message(m.chat.id, f'Здравствуйте, что Вас интересует', reply_markup=markup)  #сообщение при входе

@bot.message_handler(content_types=["text"])
def handler_text(message):

    if message.text.strip() == 'ФИО':
        answer = db['ФИО']
    elif message.text.strip() == 'Адрес':
        answer = db['Адрес']
    elif message.text.strip() == 'Работа':
        answer = db['Работа']
    else:
        ansxer = 'Такой команды нет'
    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True, interval=0)   # Запуск бота без остановочно



