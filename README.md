# API telegram bot для оповещения о новых лидах

[![Telegram](https://img.shields.io/badge/-Telegram-141130?style=for-the-badge&logo=Telegram)]( https://t.me/LeadsFromVkBot)

Метод, позвляющий получать оповещения о новых лидах (перенаправленные)


***/telegram*** доступ к api excel

___POST___

_/telegram_ - Отправляет новые лиды в телеграм чат

*Parameters*
chat_id - принимает на вход chat_id, узнать его можно у бота @LeadsFromVk написав /start

```
Привет, я буду отправлять тебе информацию о новых лидах, id нашего чата --> 3909888
```

json - данные которые нужно записать в таблицу

```
{
 "data": [{"name": name}, {"phone": phone}]
}
```


Responses 201 сообщение отправлено

