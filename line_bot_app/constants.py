"""
Created on 01/01/2021

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""
from enum import Enum, auto
import os


class ExtendedEnum(Enum):
    @classmethod
    def names2list(cls):
        return list(map(lambda c: c.name, cls))

    @classmethod
    def values2list(cls):
        return list(map(lambda c: c.value, cls))


class GamesBubbleInfo(ExtendedEnum):
    FORTUNE_TELLER = ("Fortune Teller", "https://images.pexels.com/photos/6014327/pexels-photo-6014327.jpeg?auto"
                                        "=compress&cs=tinysrgb&h=350",
                      "Silahkan mendapatkan insight mengenai kehidupanmu kelak")



class GeneralImages(ExtendedEnum):
    WELCOME_ARCADE = "https://images.pexels.com/photos/1601774/pexels-photo-1601774.jpeg?auto=compress&cs=tinysrgb&h" \
                     "=350"


class GameImages(ExtendedEnum):
    FORTUNE_TELLER = "lmao"


class ImagePlaceHolder(ExtendedEnum):
    IMAGE = "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png"


DATABASE_URL = os.getenv(
    "postgres://bwyfmcorftpnzx:d62ae2e86f370c6db7dccd990b8f8034531aff9324595976fdcfec78a6129a7d@ec2-54-85-80-92.compute-1.amazonaws.com:5432/dc0vqgch21h2ba")
