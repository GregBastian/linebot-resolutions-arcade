"""
Created on 19/01/2021

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""

from line_bot_app.constants import ImagePlaceHolder


def get_fortune_teller_bubble_flex_message(fortuneTellerThumbnail=ImagePlaceHolder.IMAGE.value,
                                           fortuneTellerQuote="Lorem ipsum dolor sit amet"):
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
            "url": fortuneTellerThumbnail,
            "size": "full",
            "aspectRatio": "14:13",
            "aspectMode": "cover"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "Sang Peramal Berkata:",
                    "weight": "bold",
                    "size": "lg",
                    "color": "#b537f2",
                    "margin": "sm"
                },
                {
                    "type": "text",
                    "text": fortuneTellerQuote,
                    "size": "md",
                    "weight": "regular",
                    "wrap": True,
                    "offsetTop": "sm",
                    "color": "#f66dc2",
                    "margin": "sm"
                }
            ],
            "backgroundColor": "#023788"
        },
        "styles": {
            "header": {
                "backgroundColor": "#f6019d"
            }
        }
    }
