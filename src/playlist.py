import json
import isodate
from datetime import timedelta, datetime
from src.chanel import APIMixin
from csv import writer


class PlayList(APIMixin):

    def __init__(self, id_pl):
        self.__id_pl = id_pl

        self.__video: dict = self.get_service().playlists().list(
            id=self.__id_pl,
            part='contentDetails,snippet').execute()
        self.__video_response: dict = self.get_service().videos().list(
            part='contentDetails,statistics',
            id=','.join(self.id_videos)).execute()

        self.__title_pl: str = self.__video['items'][0]['snippet']['title']
        self.__url: str = f'https://www.youtube.com/playlist?list={self.__id_pl}'

        # print(json.dumps(self.__video, ensure_ascii=False, indent=2))

    @property
    def title(self):
        return self.__title_pl

    @property
    def url(self):
        return self.__url

    @property
    def id_videos(self) -> list:
        """
        Получает id каждого видео из плейлиста
        :return: Список id видео
        """
        playlists: dict = self.get_service().playlistItems().list(
            playlistId=self.__id_pl,
            part='contentDetails',
            maxResults=50).execute()

        list_video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlists['items']]

        return list_video_ids

    @property
    def total_duration(self) -> object:
        result = timedelta()

        if 'items' not in self.__video_response:
            raise KeyError('Ключа нет')

        for video in self.__video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            result += timedelta(seconds=duration.total_seconds())

        return result

    def show_best_video(self):
        max_likes = 0
        max_likes_video_id = ''
        for item in self.__video_response['items']:
            video_id = item['id']
            like_count = int(item['statistics']['likeCount'])
            if like_count > max_likes:
                max_likes = like_count
                max_likes_video_id = video_id
        return f'https://youtu.be/{max_likes_video_id}'



if __name__ == '__main__':
    pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
    assert pl.title == "Moscow Python Meetup №81"
    assert pl.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"
    duration = pl.total_duration
    assert str(duration) == "1:49:52"
    assert isinstance(duration, timedelta)
    assert duration.total_seconds() == 6592.0
    assert pl.show_best_video() == "https://youtu.be/cUGyMzWQcGM"

