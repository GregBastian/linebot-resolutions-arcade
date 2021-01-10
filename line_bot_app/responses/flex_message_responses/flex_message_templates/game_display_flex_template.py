"""
Created on 10/01/2021

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""
# some future comment
from line_bot_app.constants import ImagePlaceHolder


def get_game_display_flex_message(gameName="game name", gameImage=ImagePlaceHolder.IMAGE.value,
                                  gameTextMessage="game text"):
    return {
        "type": "bubble",
        "size": "kilo",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": gameName,
                    "size": "xl",
                    "weight": "bold",
                    "align": "center",
                    "color": "#f6019d",
                    "wrap": True
                }
            ],
            "backgroundColor": "#920075",
            "borderColor": "#f6019d",
            "borderWidth": "semi-bold",
            "cornerRadius": "none"
        },
        "hero": {
            "type": "image",
            "url": gameImage,
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover"
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
