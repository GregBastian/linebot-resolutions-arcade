"""
Created on 23/01/2021

@author: Gregorius Ivan Sebastian
"""
from line_bot_app.constants import ImagePlaceHolder

from line_bot_app.constants import TebakBatikConstants


def get_tebak_batik_bubble_flex_message(gameName="Tebak Batik", selectedBatikImage=ImagePlaceHolder.IMAGE.value,
                                      currentQuestionCount=0, choices=None):
    if choices is None:
        choices = {}

    return {
        "type": "bubble",
        "size": "mega",
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
            "borderWidth": "bold",
            "cornerRadius": "md"
        },
        "hero": {
            "type": "image",
            "url": selectedBatikImage,
            "size": "full",
            "aspectRatio": "21:14",
            "gravity": "center",
            "aspectMode": "cover"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": f"Pertanyaan {currentQuestionCount}/{TebakBatikConstants.TEBAK_BATIK_TOTAL_QUESTIONS.value}",
                    "weight": "bold",
                    "size": "lg",
                    "wrap": True,
                    "color": "#bdbdfd"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Asal daerah motif batik diatas?",
                            "size": "md",
                            "margin": "none",
                            "wrap": True,
                            "color": "#bdbdfd"
                        }
                    ],
                    "margin": "sm"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "lg",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "A)",
                                    "size": "md",
                                    "margin": "none",
                                    "flex": 0,
                                    "weight": "bold",
                                    "color": "#eecbe6"
                                },
                                {
                                    "type": "text",
                                    "text": choices.get('A', 'BATIK LOREM IPSUM'),
                                    "size": "md",
                                    "margin": "md",
                                    "color": "#eecbe6"
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "B)",
                                    "size": "md",
                                    "margin": "none",
                                    "flex": 0,
                                    "weight": "bold",
                                    "color": "#eecbe6"
                                },
                                {
                                    "type": "text",
                                    "text": choices.get('B', 'BATIK LOREM IPSUM'),
                                    "size": "md",
                                    "margin": "md",
                                    "color": "#eecbe6"
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "C)",
                                    "size": "md",
                                    "margin": "none",
                                    "flex": 0,
                                    "weight": "bold",
                                    "color": "#eecbe6"
                                },
                                {
                                    "type": "text",
                                    "text": choices.get('C', 'BATIK LOREM IPSUM'),
                                    "size": "md",
                                    "margin": "md",
                                    "color": "#eecbe6"
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "D)",
                                    "size": "md",
                                    "margin": "none",
                                    "flex": 0,
                                    "weight": "bold",
                                    "color": "#eecbe6"
                                },
                                {
                                    "type": "text",
                                    "text": choices.get('D', 'BATIK LOREM IPSUM'),
                                    "size": "md",
                                    "margin": "md",
                                    "color": "#eecbe6"
                                }
                            ]
                        }
                    ]
                }
            ],
            "margin": "sm",
            "backgroundColor": "#023788"
        },
        "styles": {
            "header": {
                "backgroundColor": "#f6019d"
            }
        }
    }
