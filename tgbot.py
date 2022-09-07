import telebot


from settings import token

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, f'Привет, я буду отправлять тебе информацию о новых лидах, id нашего чата --> {message.chat.id}')



bot.polling()