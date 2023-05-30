from tools.config_loader import ConfigLoader
from tools.openai_bot import OpenAIChatBot
from tools.telegram_bot import TelegramBot
from tools.history_saver import HistorySaver

def process_message(user_id: int, message: str):
    """
    Process messages from user.
    """
    
    global chatbot, openaibot, history_saver
    if(message[0] == '/'):
        # Command.
        args = message.split(' ')
        if args[0] == '/load_history':
            if len(args) == 2:
                try:
                    openaibot.set_history(history_saver.load_history(args[1]))
                    chatbot.send_message(user_id, "History loaded succesfully. Continue dialogue.")
                except Exception as e:
                    print(e)
                    chatbot.send_message(user_id, "Error. Check console")
            else:
                chatbot.send_message(user_id, f"Invalid syntax: /load_history <history_name>")
        elif args[0] == '/start':
            chatbot.send_message(user_id, "Здарова мужик)")
        elif args[0] == '/new':
            chatbot.send_message(user_id, "New conversation started!")
            history_saver = HistorySaver()
        else:
            chatbot.send_message(user_id, f"Unknown command \{args[0]}")
    else:
        response = openaibot.submit(message)
        history_saver.save_history(openaibot.get_history())
        recent_files = history_saver.get_most_recent(5)
        commands = [f"/load_history {rf}" for rf in recent_files]
        chatbot.update_buttons(commands)
        chatbot.send_message(user_id, response)

# Load config.json with tokens and personality data.
config_data = ConfigLoader()

# Set up history saver
history_saver = HistorySaver()

# Load Open AI GPT bot.
openaibot = OpenAIChatBot(config_data.get_openai_token(), max_history=50)

# Load and start chatsystem bot.
chatbot = TelegramBot(config_data.get_telegram_token(), process_message)

chatbot.start_bot()