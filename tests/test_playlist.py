from src.playlist import PlayList
from datetime import timedelta


def test_get_title_from_playlist():
    pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
    assert pl.title == "Moscow Python Meetup №81"


def test_get_url():
    pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
    assert pl.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"


def test_duration():
    pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
    duration = pl.total_duration
    assert str(duration) == "1:49:52"
    assert isinstance(duration, timedelta)
    assert duration.total_seconds() == 6592.0
    assert pl.show_best_video() == "https://youtu.be/cUGyMzWQcGM"
