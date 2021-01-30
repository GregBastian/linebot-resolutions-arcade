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


class FollowEventImage(ExtendedEnum):
    WELCOME_ARCADE = "https://images.pexels.com/photos/1601774/pexels-photo-1601774.jpeg?auto=compress&cs=tinysrgb&h" \
                     "=350"


class AcceptedArcadeLobbyTextMessages(ExtendedEnum):
    GAMES = "games"
    INFO = "info"
    FORTUNE_TELLER = "fortune teller"
    FLAG_QUIZ = "flag quiz"
    TEBAK_BATIK = "tebak batik"
    KELILING_INDONESIA = "tebak lokasi"


class AcceptedFortuneTellerTextMessages(ExtendedEnum):
    BACK = "back"
    HELP = "help"
    RAMAL = "ramal"


class FlagQuizConstants(ExtendedEnum):
    OPTIONS = ('A', 'B', 'C', 'D')
    FLAG_QUIZ_TOTAL_QUESTIONS = 10


class AcceptedFlagQuizTextMessages(ExtendedEnum):
    BACK = "back"
    OPTIONS = ('A', 'B', 'C', 'D')
    HELP = "help"


class TebakBatikConstants(ExtendedEnum):
    OPTIONS = ('A', 'B', 'C', 'D')
    TEBAK_BATIK_TOTAL_QUESTIONS = 10


class AcceptedTebakBatikTextMessages(ExtendedEnum):
    OPTIONS = ('A', 'B', 'C', 'D')
    BACK = "back"
    HELP = "help"


class AcceptedKelilingIndonesiaMessages(ExtendedEnum):
    OPTIONS = ('A', 'B', 'C', 'D')
    BACK = "back"
    HELP = "help"


class KelilingIndonesiaConstants(ExtendedEnum):
    OPTIONS = ('A', 'B', 'C', 'D')
    DAFTAR_PROVINSI = (
        'Maluku', 'Jawa Timur', 'Jambi', 'Banten', 'Sulawesi Tenggara', 'Kalimantan Tengah', 'Sumatera Utara',
        'Sulawesi Barat', 'Di Yogyakarta', 'Gorontalo', 'Sulawesi Tengah', 'Papua Barat', 'Kepulauan Riau',
        'Kalimantan Barat', 'Nusa Tenggara Barat', 'Jawa Tengah', 'Papua', 'Kalimantan Timur', 'Maluku Utara',
        'Dki Jakarta', 'Jawa Barat', 'Sulawesi Selatan', 'Riau', 'Nusa Tenggara Timur', 'Sumatera Barat', 'Bengkulu',
        'Aceh', 'Bali', 'Lampung', 'Sumatera Selatan', 'Kalimantan Utara', 'Kepulauan Bangka Belitung',
        'Sulawesi Utara', 'Kalimantan Selatan')
    KELILING_INDONESIA_TOTAL_QUESTIONS = 5


class GamesNames(ExtendedEnum):
    FORTUNE_TELLER = "Fortune Teller"
    FLAG_QUIZ = "Flag Quiz"
    TEBAK_BATIK = "Tebak Batik"
    KELILING_INDONESIA = "Tebak Lokasi"


class GamesThumbnail(ExtendedEnum):
    FORTUNE_TELLER = "https://images.pexels.com/photos/6014327/pexels-photo-6014327.jpeg?auto=compress&cs" \
                     "=tinysrgb&h=650&w=940"
    FLAG_QUIZ = "https://images.pexels.com/photos/4468974/pexels-photo-4468974.jpeg?auto=compress&cs" \
                "=tinysrgb&h=650&w=940"
    TEBAK_BATIK = "https://images.pexels.com/photos/4610857/pexels-photo-4610857.jpeg?auto=compress&cs" \
                  "=tinysrgb&h=650&w=940"
    KELILING_INDONESIA = "https://images.pexels.com/photos/758742/pexels-photo-758742.jpeg?auto=compress&cs" \
                         "=tinysrgb&h=650&w=940"


class GamesInfo(ExtendedEnum):
    FORTUNE_TELLER = "Bertanyalah kepada sang peramal mengenai hasil dari resolusi tahun baru kamu pada akhir tahun " \
                     "nanti"
    FLAG_QUIZ = "Uji pengetahuan geografis-mu dengan menebak nama negara berdasarkan bendera yang ditampilkan"
    TEBAK_BATIK = "Ukur kemampuanmu untuk mengetahui asal daerah dari motif-motif batik dari seluruh Indonesia"
    KELILING_INDONESIA = "Anda sudah merasa mengetahui semua daerah di Indonesia? Buktikan dengan skor sempurna disini"


class GamesTextSendMessage(ExtendedEnum):
    FORTUNE_TELLER = AcceptedArcadeLobbyTextMessages.FORTUNE_TELLER.value
    FLAG_QUIZ = AcceptedArcadeLobbyTextMessages.FLAG_QUIZ.value
    TEBAK_BATIK = AcceptedArcadeLobbyTextMessages.TEBAK_BATIK.value
    KELILING_INDONESIA = AcceptedArcadeLobbyTextMessages.KELILING_INDONESIA.value


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
    TEBAK_BATIK = (AcceptedArcadeLobbyTextMessages.TEBAK_BATIK.value.title(),
                   GamesThumbnail.TEBAK_BATIK.value,
                   GamesInfo.TEBAK_BATIK.value,
                   GamesTextSendMessage.TEBAK_BATIK.value)
    KELILING_INDONESIA = (AcceptedArcadeLobbyTextMessages.KELILING_INDONESIA.value.title(),
                          GamesThumbnail.KELILING_INDONESIA.value,
                          GamesInfo.KELILING_INDONESIA.value,
                          GamesTextSendMessage.KELILING_INDONESIA.value)


class FortuneTellerImage(ExtendedEnum):
    FORTUNE_TELLER_THUMBNAIL = "https://images.pexels.com/photos/6014335/pexels-photo-6014335.jpeg?auto=compress&cs" \
                               "=tinysrgb&h=650&w=940"


class RichMenuNames(ExtendedEnum):
    ARCADE_LOBBY = "arcade lobby rm"
    FORTUNE_TELLER = "fortune teller rm"
    FLAG_QUIZ = "flag quiz rm"


class ImagePlaceHolder(ExtendedEnum):
    IMAGE = "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png"


class KelilingIndonesiaGameThumbnails(ExtendedEnum):
    THUMBNAIL_1 = "https://images.pexels.com/photos/1743165/pexels-photo-1743165.jpeg?auto=compress&cs=tinysrgb&h=650" \
                  "&w=940 "
    THUMBNAIL_2 = "https://images.pexels.com/photos/654/clouds-cloudy-agriculture-farm.jpg?auto=compress&cs=tinysrgb" \
                  "&h=650&w=940 "
    THUMBNAIL_3 = "https://images.pexels.com/photos/931007/pexels-photo-931007.jpeg?auto=compress&cs=tinysrgb&h=650&w" \
                  "=940 "
    THUMBNAIL_4 = "https://images.pexels.com/photos/2032110/pexels-photo-2032110.jpeg?auto=compress&cs=tinysrgb&h=650" \
                  "&w=940 "
    THUMBNAIL_5 = "https://images.pexels.com/photos/2583847/pexels-photo-2583847.jpeg?auto=compress&cs=tinysrgb&h=650" \
                  "&w=940 "
    THUMBNAIL_6 = "https://images.pexels.com/photos/1657984/pexels-photo-1657984.jpeg?auto=compress&cs=tinysrgb&h=650" \
                  "&w=940 "
    THUMBNAIL_7 = "https://images.pexels.com/photos/1697494/pexels-photo-1697494.jpeg?auto=compress&cs=tinysrgb&h=650" \
                  "&w=940"
    THUMBNAIL_8 = "https://images.pexels.com/photos/1454932/pexels-photo-1454932.jpeg?auto=compress&cs=tinysrgb&h=650" \
                  "&w=940 "
    THUMBNAIL_9 = "https://images.pexels.com/photos/1081915/pexels-photo-1081915.jpeg?auto=compress&cs=tinysrgb&h=650" \
                  "&w=940"
    THUMBNAIL_10 = "https://images.pexels.com/photos/739285/pexels-photo-739285.jpeg?auto=compress&cs=tinysrgb&h=650" \
                   "&w=940 "
    THUMBNAIL_11 = "https://images.pexels.com/photos/1722321/pexels-photo-1722321.jpeg?auto=compress&cs=tinysrgb&h" \
                   "=650&w=940 "
    THUMBNAIL_12 = "https://images.pexels.com/photos/1700742/pexels-photo-1700742.jpeg?auto=compress&cs=tinysrgb&h" \
                   "=650&w=940 "
    THUMBNAIL_13 = "https://images.pexels.com/photos/1551491/pexels-photo-1551491.jpeg?auto=compress&cs=tinysrgb&h" \
                   "=650&w=940 "
    THUMBNAIL_14 = "https://images.pexels.com/photos/2246950/pexels-photo-2246950.jpeg?auto=compress&cs=tinysrgb&h" \
                   "=650&w=940"
    THUMBNAIL_15 = "https://images.pexels.com/photos/1551493/pexels-photo-1551493.jpeg?auto=compress&cs=tinysrgb&h" \
                   "=650&w=940"
    THUMBNAIL_16 = "https://images.pexels.com/photos/3068249/pexels-photo-3068249.jpeg?auto=compress&cs=tinysrgb&h" \
                   "=650&w=940"
    THUMBNAIL_17 = "https://images.pexels.com/photos/639/clouds-rainy-rain-asia.jpg?auto=compress&cs=tinysrgb&h" \
                   "=650&w=940"
    THUMBNAIL_18 = "https://images.pexels.com/photos/2861894/pexels-photo-2861894.jpeg?auto=compress&cs=tinysrgb&h" \
                   "=650&w=940"
    THUMBNAIL_19 = "https://images.pexels.com/photos/3290667/pexels-photo-3290667.jpeg?auto=compress&cs=tinysrgb&h" \
                   "=650&w=940"
    THUMBNAIL_20 = "https://images.pexels.com/photos/2020377/pexels-photo-2020377.jpeg?auto=compress&cs=tinysrgb&h" \
                   "=650&w=940"
