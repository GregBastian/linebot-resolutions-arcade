"""
Created on 30/01/2021

@author: Gregorius Ivan Sebastian
"""

from line_bot_app.constants import ImagePlaceHolder

from line_bot_app.constants import KelilingIndonesiaConstants


def get_keliling_indonesia_bubble_flex_message(gameName="Keliling Indonesia",
                                               randomThumbnail=ImagePlaceHolder.IMAGE.value,
                                               trueKotaKabupatenName="UTOPIA",
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
            "url": randomThumbnail,
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
                    "text": f"Pertanyaan {currentQuestionCount}/{KelilingIndonesiaConstants.KELILING_INDONESIA_TOTAL_QUESTIONS.value}",
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
                            "text": f"Di provinsi manakah {trueKotaKabupatenName} berada?",
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
                                    "text": f"Provinsi {choices.get('A', 'Provinsi Utopia')}",
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
                                    "text": f"Provinsi {choices.get('B', 'Provinsi Utopia')}",
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
                                    "text": f"Provinsi {choices.get('C', 'Provinsi Utopia')}",
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
                                    "text": f"Provinsi {choices.get('D', 'Provinsi Utopia')}",
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
