import json
from dotenv import get_key
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.api_key: str = 'AIzaSyDxVxHK2libki_yT44Wc__Ikjsta-XwnPQ'
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))


