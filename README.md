# API telegram bot для оповещения о новых лидах

[![Telegram](https://img.shields.io/badge/-Telegram-141130?style=for-the-badge&logo=Telegram)]( https://t.me/LeadsFromVkBot)

Метод, позвляющий получать оповещения о новых лидах (перенаправленные)


***/telegram*** доступ к api

___POST___

_/telegram_ - Отправляет новые лиды в телеграм чат

*Parameters*


```
Привет, я буду отправлять тебе информацию о новых лидах, id нашего чата --> 3909888
```

json - данные(лиды из вк) которые нужно отправить

```
{
 "data": [{"name": name}, {"phone": phone}],
 "chat_id" - принимает на вход chat_id, узнать его можно у бота @LeadsFromVk написав /start
}
```


Responses 201 сообщение отправлено

______рекомендуемый пример запроса___

```
def post_to_tg(res, chat_id, host):
    chat_id_data = {'chat_id': chat_id}
    res.update(chat_id_data)
    url_for_tg = f'http://{host}:5001/telegram'
    response = requests.post(url_for_tg, json=res)
    return response
```
