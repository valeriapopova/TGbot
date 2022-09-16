import telebot
from flask import Flask, request, Response
from werkzeug.exceptions import BadRequestKeyError

from config import Configuration
from settings import token


app = Flask(__name__)
app.config.from_object(Configuration)


@app.route('/telegram/post', methods=['POST'])
def send_mess():
    if request.method == 'POST':
        try:
            json_file = request.get_json(force=False)
            chat_id = json_file['chat_id']
            bot = telebot.TeleBot(token)
            name = json_file['data'][0]['name']
            phone = json_file['data'][1]['phone']
            bot.send_message(chat_id, f'Новый лид!!! имя {name} , номер телефона {phone}')
            # bot.polling()
            return Response("Сообщение отправлено", 201)

        except BadRequestKeyError:
            return Response("Пустое значение", 400)



