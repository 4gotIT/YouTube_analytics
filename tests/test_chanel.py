from src.chanel import Channel


def test_get_info():
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    assert moscowpython.print_info() == {
        "kind": "youtube#channelListResponse",
        "etag": "sq5b4uoagFnb3cyX3DeVlFhXFQ8",
        "pageInfo": {
            "totalResults": 1,
            "resultsPerPage": 5
        },
        "items": [
            {
                "kind": "youtube#channel",
                "etag": "oEQuoHPTd2IVnUp5TaD9E0StGBw",
                "id": "UC-OVMPlMA3-YCIeg4z5z23A",
                "snippet": {
                    "title": "MoscowPython",
                    "description": "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)",
                    "customUrl": "@moscowdjangoru",
                    "publishedAt": "2012-07-13T09:48:44Z",
                    "thumbnails": {
                        "default": {
                            "url": "https://yt3.ggpht.com/ytc/APkrFKaVrRJTNkDjSnvpVAYDqbQ5S1VMHWaZhOauk5M10Q=s88-c-k-c0x00ffffff-no-rj",
                            "width": 88,
                            "height": 88
                        },
                        "medium": {
                            "url": "https://yt3.ggpht.com/ytc/APkrFKaVrRJTNkDjSnvpVAYDqbQ5S1VMHWaZhOauk5M10Q=s240-c-k-c0x00ffffff-no-rj",
                            "width": 240,
                            "height": 240
                        },
                        "high": {
                            "url": "https://yt3.ggpht.com/ytc/APkrFKaVrRJTNkDjSnvpVAYDqbQ5S1VMHWaZhOauk5M10Q=s800-c-k-c0x00ffffff-no-rj",
                            "width": 800,
                            "height": 800
                        }
                    },
                    "localized": {
                        "title": "MoscowPython",
                        "description": "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)"
                    },
                    "country": "RU"
                },
                "statistics": {
                    "viewCount": "2456697",
                    "subscriberCount": "26700",
                    "hiddenSubscriberCount": false,
                    "videoCount": "720"
                }
            }
        ]
    }


def test_get_attr():
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')

    # получаем значения атрибутов
    assert moscowpython.title == 'MoscowPython'
    assert moscowpython.video_count == 720
    assert moscowpython.url == 'https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A'
    assert type(Channel.get_service()) == object

