import json
from dotenv import get_key
from googleapiclient.discovery import build


class APIMixin:
    __api_key: str = get_key(".env", 'API_KEY')

    @classmethod
    def get_service(cls):
        """Класс-метод, возвращающий объект для работы с YouTube API"""
        youtube = build('youtube', 'v3', developerKey=cls.__api_key)
        return youtube

class Channel(APIMixin):
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

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def url(self):
        return self.__url

    @property
    def subscriber_count(self):
        return self.__subscriber_count

    @property
    def video_count(self):
        return self.__video_count

    @property
    def view_count(self):
        return self.__view_count

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

    def __str__(self):
        return f'{self.__title} ({self.__url})'

    def __add__(self, other):
        if isinstance(other, Channel):
            return self.__subscriber_count + other.__subscriber_count
        else:
            raise f'{other} не является экземпляром класса Channel'

    def __sub__(self, other):
        if isinstance(other, Channel):
            return int(self.__subscriber_count) - int(other.__subscriber_count)
        else:
            raise f'{other} не является экземпляром класса Channel'

    def __gt__(self, other):
        if not isinstance(other, Channel):
            raise TypeError('f{other} не является экземпляром класса Channel')
        if self.__subscriber_count > other.__subscriber_count:
            return True
        return False

    def __lt__(self, other):
        if not isinstance(other, Channel):
            raise TypeError('f{other} не является экземпляром класса Channel')
        if self.__subscriber_count < other.__subscriber_count:
            return True
        return False

    def __ge__(self, other):
        if not isinstance(other, Channel):
            raise TypeError('f{other} не является экземпляром класса Channel')
        if self.__subscriber_count >= other.__subscriber_count:
            return True
        return False

    def __le__(self, other):
        if not isinstance(other, Channel):
            raise TypeError('f{other} не является экземпляром класса Channel')
        if self.__subscriber_count <= other.__subscriber_count:
            return True
        return False


if __name__ == '__main__':
    # Создаем два экземпляра класса
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    highload = Channel('UCwHL6WHUarjGfUM_586me8w')
    # Используем различные магические методы
    print(moscowpython)  # 'MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'
    print(moscowpython + highload)  # 100100
    print(moscowpython - highload)  # -48300
    print(highload - moscowpython)  # 48300
    print(moscowpython > highload)  # False
    print(moscowpython >= highload)  # False
    print(moscowpython < highload)  # True
    print(moscowpython <= highload)  # True
    print(moscowpython == highload)  # False