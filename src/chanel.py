import json
from dotenv import get_key
from googleapiclient.discovery import build


class Channel:
    """Класс аналитика для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__id = channel_id
        self.channel = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
        self.__title = self.channel['items'][0]['snippet']['title']  # название канала
        self.__description = self.channel['items'][0]['snippet']['description']  # описание канала
        self.__url = f'https://www.youtube.com/channel/{self.id}'
        self.__subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']  # количество подписчиков
        self.__video_count = self.channel['items'][0]['statistics']['videoCount']  # количество видео
        self.__view_count = self.channel['items'][0]['statistics']['viewCount']  # количество видео

    @classmethod
    def get_service(cls):
        """Класс-метод, возвращающий объект для работы с YouTube API"""
        api_key: str = get_key(".env", 'API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.title

    @property
    def description(self):
        return self.description

    @property
    def url(self):
        return self.url

    @property
    def subscriber_count(self):
        return self.subscriber_count

    @property
    def video_count(self):
        return self.video_count

    @property
    def view_count(self):
        return self.view_count

    def to_json(self) -> None:
        attr = {
            'id': self.id,
            'name': self.title,
            'description': self.description,
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count
        }
        with open('data.json', 'a', encoding='utf-8') as data:
            json.dump(attr, data, indent=2, ensure_ascii=False)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))


