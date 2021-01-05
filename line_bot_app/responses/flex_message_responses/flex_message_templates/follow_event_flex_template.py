# some future comment


def get_follow_event_flex_message(profileName="user"):
    return {
        "type": "bubble",
        "size": "giga",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "--Resolutions Arcade--",
                    "weight": "bold",
                    "size": "xxl",
                    "color": "#e3e4e6",
                    "offsetStart": "sm",
                    "align": "center"
                }
            ],
            "backgroundColor": "#00284a"
        },
        "hero": {
            "type": "image",
            "url": "https://images.pexels.com/photos/1601774/pexels-photo-1601774.jpeg?auto=compress\u0026cs=tinysrgb\u0026h=350",
            "size": "full",
            "aspectMode": "cover",
            "action": {
                "type": "uri",
                "uri": "http://linecorp.com/"
            },
            "animated": True,
            "aspectRatio": "20:13"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": f"Hello, {profileName}!",
                    "weight": "bold",
                    "size": "xxl",
                    "color": "#e3e4e6",
                    "offsetStart": "sm"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "lg",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "Selamat datang ke Resolutions Arcade.",
                                    "wrap": True,
                                    "color": "#fb9eae",
                                    "size": "lg",
                                    "flex": 5,
                                    "margin": "none"
                                }
                            ],
                            "paddingAll": "sm"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "Mainkan semua permainan yang kamu mau. Semoga kamu menikmati waktumu disini.",
                                    "wrap": True,
                                    "color": "#fb9eae",
                                    "size": "lg",
                                    "flex": 5
                                }
                            ],
                            "paddingAll": "sm"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "Pintu kami akan selalu terbuka untukmu.",
                                    "wrap": True,
                                    "color": "#fb9eae",
                                    "size": "lg",
                                    "flex": 5
                                }
                            ],
                            "margin": "sm",
                            "paddingAll": "sm"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "Sincerely, Manager Resolutions Arcade",
                                    "wrap": true,
                                    "color": "#e92efb",
                                    "size": "lg",
                                    "flex": 5
                                }
                            ],
                            "margin": "sm",
                            "paddingAll": "sm"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "[ @198ynrsq ]",
                                    "wrap": True,
                                    "color": "#e92efb",
                                    "size": "md",
                                    "flex": 5
                                }
                            ],
                            "paddingStart": "sm"
                        }
                    ]
                },
                {
                    "type": "spacer"
                }
            ],
            "backgroundColor": "#00284a"
        }
    }
