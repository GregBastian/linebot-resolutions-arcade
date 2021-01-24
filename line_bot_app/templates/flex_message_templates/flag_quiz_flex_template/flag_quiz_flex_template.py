"""
Created on 23/01/2021

@author: Gregorius Ivan Sebastian
"""
from line_bot_app.constants import ImagePlaceHolder

from line_bot_app.constants import FlagQuizConstants


def get_flag_quiz_bubble_flex_message(gameName="Flag Quiz", selectedFlagImage=ImagePlaceHolder.IMAGE.value,
                                      currentQuestionCount=0, choices=None):
    if choices is None:
        choices = {}

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
            "borderWidth": "bold",
            "cornerRadius": "md"
        },
        "hero": {
            "type": "image",
            "url": selectedFlagImage,
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
                    "text": f"Pertanyaan {currentQuestionCount}/{FlagQuizConstants.FLAG_QUIZ_TOTAL_QUESTIONS.value}",
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
                            "text": "Bendera milik negara manakah ini?",
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
                                    "text": choices.get('A', 'UTOPIA'),
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
                                    "text": choices.get('B', 'UTOPIA'),
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
                                    "text": choices.get('C', 'UTOPIA'),
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
                                    "text": choices.get('D', 'UTOPIA'),
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
