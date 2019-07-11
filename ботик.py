import telebot;
bot = telebot.TeleBot('794843638:AAFEGpd8vy2DmBuNBkXNSniVpBcY4Oh2Jf4');

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привіт', 'Пока')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привіт, ти написав мені /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привіт':
        bot.send_message(message.chat.id, 'Ну Привіт')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Гуд Бай')

bot.polling()