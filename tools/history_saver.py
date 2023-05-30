import os

class HistorySaver:

    def __init__(self) -> None:
        self.last_history_number = len(os.listdir("history"))
        self.current_history = self.get_free_history_name()

    def get_free_history_name(self) -> str:
        return f"history_{self.last_history_number}"

    def save_history(self, messages: list):
        save_file = open(f"history/{self.current_history}.txt", "w")
        save_file.write(str(messages))
        save_file.close()

    def load_history(self, name: str) -> list:
        save_file = open(f"history/{name}.txt", "r")
        messages = eval(save_file.read())
        save_file.close()
        self.current_history = name
        return messages
    
    def get_most_recent(self, number: int) -> list[str]:
        latest_files = []
        for cur_path, dirnames, filenames in os.walk("history"):
            for filename in filenames:
                latest_files.append(os.path.join(cur_path, filename))
        latest_files.sort(key=lambda x: os.path.getmtime(x))
        latest_files = latest_files[:number]
        return [file.replace('history\\', '').replace(".txt", "") for file in latest_files]
        