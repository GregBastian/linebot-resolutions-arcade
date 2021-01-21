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


class GeneralImages(ExtendedEnum):
    WELCOME_ARCADE = "https://images.pexels.com/photos/1601774/pexels-photo-1601774.jpeg?auto=compress&cs=tinysrgb&h" \
                     "=350"


class AcceptedArcadeLobbyTextMessages(ExtendedEnum):
    GAMES = "games"
    INFO = "info"
    FORTUNE_TELLER = "fortune teller"
    FLAG_QUIZ = "flag quiz"


class AcceptedFortuneTellerTextMessages(ExtendedEnum):
    BACK = "back"
    HELP = "help"
    RAMAL = "ramal"


class GamesNames(ExtendedEnum):
    FORTUNE_TELLER = "Fortune Teller"
    FLAG_QUIZ = "Flag Quiz"


class GamesThumbnail(ExtendedEnum):
    FORTUNE_TELLER = "https://images.pexels.com/photos/6014327/pexels-photo-6014327.jpeg?auto=compress&cs" \
                     "=tinysrgb&h=650&w=940"
    FLAG_QUIZ = "https://images.pexels.com/photos/4468974/pexels-photo-4468974.jpeg?auto=compress&cs" \
                "=tinysrgb&h=650&w=940"


class GamesInfo(ExtendedEnum):
    FORTUNE_TELLER = "Bertanyalah kepada sang peramal mengenai hasil dari resolusi tahun baru kamu pada akhir tahun " \
                     "nanti"
    FLAG_QUIZ = "Uji pengetahuan geografis-mu dengan menebak nama negara berdasarkan bendera yang ditampilkan"


class GamesTextSendMessage(ExtendedEnum):
    FORTUNE_TELLER = AcceptedArcadeLobbyTextMessages.FORTUNE_TELLER.value
    FLAG_QUIZ = AcceptedArcadeLobbyTextMessages.FLAG_QUIZ.value


class GamesBubbleInfo(ExtendedEnum):
    # order of tuple should be game's name, image, info then text message
    FORTUNE_TELLER = (AcceptedArcadeLobbyTextMessages.FORTUNE_TELLER.value.title(),
                      GamesThumbnail.FORTUNE_TELLER.value,
                      GamesInfo.FORTUNE_TELLER.value,
                      GamesTextSendMessage.FORTUNE_TELLER.value)
    FLAG_QUIZ = (AcceptedArcadeLobbyTextMessages.FLAG_QUIZ.value.title(),
                 GamesThumbnail.FLAG_QUIZ.value,
                 GamesInfo.FLAG_QUIZ.value,
                 GamesTextSendMessage.FLAG_QUIZ.value)


class FortuneTellerImage(ExtendedEnum):
    FORTUNE_TELLER_THUMBNAIL = "https://images.pexels.com/photos/6014335/pexels-photo-6014335.jpeg?auto=compress&cs" \
                               "=tinysrgb&h=650&w=940"


class RichMenuNames(ExtendedEnum):
    ARCADE_LOBBY = "arcade lobby rm"
    FORTUNE_TELLER = "fortune teller rm"
    FLAG_QUIZ = "flag quiz rm"


class ImagePlaceHolder(ExtendedEnum):
    IMAGE = "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png"
