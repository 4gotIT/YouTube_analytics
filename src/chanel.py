import json
from dotenv import get_key
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
        self.id = channel_id
        self.name = self.channel['items'][0]['snippet']['title'] # название канала
        self.description = self.channel['items'][0]['snippet']['description'] # описание канала
        self.url = self.channel['items'][0]['snippet']['customUrl'] # ссылка на канал
        self.subscribercount = self.channel['items'][0]['statistics']['subscriberCount']  # количество подписчиков
        self.videocount = self.channel['items'][0]['statistics']['videoCount']  # количество видео
        self.viewcount = self.channel['items'][0]['statistics']['viewCount']  # количество видео

    @classmethod
    def get_service(cls):
        """Класс-метод, возвращающий объект для работы с YouTube API"""
        api_key: str = get_key(".env", 'API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def to_json(self):
        pass

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

ex = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
ex.name = 'fsf'
print(ex.name)
