"""
Created on 10/01/2021

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""
# some future comment
from line_bot_app.constants import ImagePlaceHolder, GamesBubbleInfo


def get_game_bubble_flex_message(gameName="game name", gameInfo="Lorem ipsum dolor sit amet",
                                 gameImage=ImagePlaceHolder.IMAGE.value, gameTextMessage="game text"):
    return {
        "type": "bubble",
        "size": "kilo",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "gameName",
                    "size": "xl",
                    "weight": "bold",
                    "align": "center",
                    "color": "#f6019d",
                    "wrap": True
                }
            ],
            "backgroundColor": "#920075",
            "borderColor": "#f6019d",
            "borderWidth": "bold",
            "cornerRadius": "md"
        },
        "hero": {
            "type": "image",
            "url": gameImage,
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": gameInfo,
                    "color": "#eecbe6",
                    "wrap": True
                }
            ],
            "backgroundColor": "#00218a"
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
                {
                    "type": "button",
                    "style": "primary",
                    "height": "md",
                    "action": {
                        "type": "message",
                        "label": "PLAY",
                        "text": gameTextMessage
                    },
                    "color": "#535eeb"
                }
            ],
            "flex": 0,
            "backgroundColor": "#00218a"
        }
    }


def get_games_display_carousel_flex_message():
    carouselContents = []
    for gameName, gameInfo, gameImage, gameTextMessage in GamesBubbleInfo.values2list():
        carouselContents.append(get_game_bubble_flex_message(gameName=gameName, gameInfo=gameInfo, gameImage=gameImage,
                                                             gameTextMessage=gameTextMessage))

    return {
        "type": "carousel",
        "contents": carouselContents
    }
