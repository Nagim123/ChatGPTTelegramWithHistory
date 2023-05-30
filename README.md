# ChatGPTTelegramWithHistory
Telegram bot that has access to ChatGPT and also saves history.

## How to use
1. Install requirements.
```console
pip install -r requirements.txt
```

2. Insert your **OpenAI API** and **Telegram bot** tokens in ```config.json``` file. 
```
{
    "telegram_token": "TELEGRAM TOKEN HERE",
    "open_ai_token": "OPEN AI TOKEN HERE"
}
```

3. Run code.
```console
python main.py
```

4. Go to Telegram and chat with bot.

## History saving and loading
All chat histories are saved in ```history``` folder. You can rename chat history files manually if you want to organize them.
<br/>
You can load history via command or using button (shown in picture below).
<br/>
<br/>
Picture:
<br/>
![History button picture](https://github.com/Nagim123/ChatGPTTelegramWithHistory/blob/master/picture.png)
<br/>
## Bot commands
1. ```/new``` - start new chat session.
2. ```/load_history <history_name>``` - load chat history.
3. ```/start``` - "Здарова мужик)".
