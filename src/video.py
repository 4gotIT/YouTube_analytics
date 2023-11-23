import json
from src.chanel import APIMixin
from dotenv import get_key
from googleapiclient.discovery import build


class Video(APIMixin):
    """
    Класс видео
    :param
    id_video - id видео
    """
    def __init__(self, id_video: str):
        self.__id = id_video # id видео
        self.__video = self.get_service().videos().list(id=id_video, part='snippet,statistics').execute()
        self.__url = f'https://www.youtube.com/watch?v={self.id}' # ссылка на видео
        self.__title = self.__video["items"][0]["snippet"]["title"] # название видео
        self.__view_count = self.__video["items"][0]["statistics"]["viewCount"] # количество просмотров
        self.__likes = self.__video["items"][0]["statistics"]["likeCount"] # количество лайков

    @property
    def id(self):
        return self.__id

    def get_info(self) -> dict:
        '''
        Создание списка о видео
        :return:
        data список с данными
        '''
        data = {
            'id': self.__id,
            'title': self.__title,
            'url': self.__url,
            'viewCount': self.__view_count,
            'likeCount': self.__likes
        }
        return data

    @staticmethod
    def to_json_file(data: dict) -> None:
        """
        Запись данных в json файл
        :param
        data: dict
        """
        with open('video.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def __str__(self):
        return f'{self.__title}'


class PLVideo(Video):
    def __init__(self, id_video: str, id_playlist: str):
        super().__init__(id_video)
        self.__id_playlist = id_playlist

    @property
    def id_playlist(self):
        return self.__id_playlist


if __name__ == '__main__':
    # Создаем два экземпляра класса
    video1 = Video('AWX4JnAnjBE')  # 'AWX4JnAnjBE' - это id видео из ютуб  RYiwB9OoRvIfowF9
    video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
    assert str(video1) == 'GIL в Python: зачем он нужен и как с этим жить'
    assert str(video2) == 'MoscowPython Meetup 78 - вступление'

