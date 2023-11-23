from datetime import timedelta
from src.chanel import APIMixin
from csv import writer


class PlayList(APIMixin):

    def __init__(self, id_pl):
        self.id_pl = id_pl
        self.__video = self.get_service().playlists().list(id=self.id_pl, part='contentDetails,snippet').execute()
        self.__title_pl = self.__video['items'][0]['snippet']['title']
        self.__url = f'https://www.youtube.com/playlist?list={self.id_pl}'

    @property
    def title(self):
        return self.__title_pl

    @property
    def url(self):
        return self.__url

    @property
    def total_duration(self):
        pass



if __name__ == '__main__':
    pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
    assert pl.title == "Moscow Python Meetup №81"
    assert pl.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"
    #
    # duration = pl.total_duration
    # assert str(duration) == "1:49:52"
    # assert isinstance(duration, datetime.timedelta)
    # assert duration.total_seconds() == 6592.0
    #
    # assert pl.show_best_video() == "https://youtu.be/cUGyMzWQcGM"

