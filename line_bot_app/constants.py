"""
Created on 01/01/2021

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""
from enum import Enum, auto
from os import getenv


class ExtendedEnum(Enum):
    @classmethod
    def names2list(cls):
        return list(map(lambda c: c.name, cls))

    @classmethod
    def values2list(cls):
        return list(map(lambda c: c.value, cls))


class GameNames(ExtendedEnum):
    FORTUNE_TELLER = "Fortune Teller"


class GameImages(ExtendedEnum):
    FORTUNE_TELLER = "lmao"


class Images(ExtendedEnum):
    IMAGE = "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png"
    FORTUNE_TELLER = "lmao"


ENV = getenv.get("ENVIRONMENT", "LOCAL")
if ENV == "ENVIRONMENT":
    GAME_IMAGES = ImagePlaceholder.IMAGE.value
else:
    IMAGES = Game
