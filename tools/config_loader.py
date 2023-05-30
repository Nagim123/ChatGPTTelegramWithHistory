import json

class ConfigLoader:
    """
    Class that loads and parse information from config.json file.
    """
    
    def __init__(self) -> None:
        config_file = open("config.json", 'r')
        self._config_data = json.loads(config_file.read())
        self._telegram_token = self._config_data["telegram_token"]
        self._openai_token = self._config_data["open_ai_token"]
        config_file.close()

    def get_personality(self) -> str:
        """
        Get character description for bot.
        """
        
        return self._personality
    
    def get_telegram_token(self) -> str:
        """
        Get chat system's token.
        """

        return self._telegram_token
    
    def get_openai_token(self) -> str:
        """
        Get token for Open AI API.
        """

        return self._openai_token