import openai


class OpenAIChatBot:
    """
    Class to send requests to Open AI API and create bots.
    """

    def __init__(self, token: str, max_history: int = 50) -> None:
        """
        Initialize Open AI API using secret key.
        """

        openai.api_key = token
        self._messages = [{"role": "system", "content": "You are helpful assistant."}]
        self._max_history = max_history

    def _update(self, role: str, content: str) -> None:
        """
        Process message history.
        """
        
        self._messages.append({"role":role, "content":content})
        if len(self._messages) > self._max_history:
            self._messages.pop(1)
        
    def _get_response(self) -> str:
        """
        Get response from ChatGPT system.
        """
        
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self._messages
        )
        return chat_completion.choices[0].message.content

    def submit(self, user_input) -> str:
        """
        Submit user input and get response from bot.
        """

        self._update("user", user_input)
        response = self._get_response()
        self._update("assistant", response)
        return response
    
    def get_history(self) -> list:
        return self._messages

    def set_history(self, new_history: list) -> None:
        self._messages = [{"role": "system", "content": "You are helpful assistant."}]
        self._messages += new_history