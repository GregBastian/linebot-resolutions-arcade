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
                    "text": "--Resolution Arcade--",
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
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
            "size": "full",
            "aspectMode": "cover",
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
                # {
                #     "type": "box",
                #     "layout": "vertical",
                #     "margin": "lg",
                #     "spacing": "sm",
                #     "contents": [
                #         {
                #             "type": "box",
                #             "layout": "baseline",
                #             "spacing": "sm",
                #             "contents": [
                #                 {
                #                     "type": "text",
                #                     "text": "Selamat datang ke Resolutions Arcade.",
                #                     "wrap": True,
                #                     "color": "#fb9eae",
                #                     "size": "lg",
                #                 }
                #             ],
                #             "paddingAll": "sm"
                #         },
                #         {
                #             "type": "box",
                #             "layout": "baseline",
                #             "spacing": "sm",
                #             "contents": [
                #                 {
                #                     "type": "text",
                #                     "text": "Mainkan semua permainan yang kamu mau. Semoga kamu menikmati waktumu "
                #                             "disini.",
                #                     "wrap": True,
                #                     "color": "#fb9eae",
                #                     "size": "lg"
                #                 }
                #             ],
                #             "paddingAll": "sm"
                #         },
                #         {
                #             "type": "box",
                #             "layout": "baseline",
                #             "contents": [
                #                 {
                #                     "type": "text",
                #                     "text": "Pintu kami akan selalu terbuka untukmu.",
                #                     "wrap": True,
                #                     "color": "#fb9eae",
                #                     "size": "lg"
                #                 }
                #             ],
                #             "margin": "sm",
                #             "paddingAll": "sm"
                #         },
                #         {
                #             "type": "box",
                #             "layout": "baseline",
                #             "contents": [
                #                 {
                #                     "type": "text",
                #                     "text": "Sincerely, Manager Resolution Arcade",
                #                     "wrap": True,
                #                     "color": "#e92efb",
                #                     "size": "lg"
                #                 }
                #             ],
                #             "margin": "sm",
                #             "paddingAll": "sm"
                #         },
                #         {
                #             "type": "box",
                #             "layout": "baseline",
                #             "contents": [
                #                 {
                #                     "type": "text",
                #                     "text": "[ @198ynrsq ]",
                #                     "wrap": True,
                #                     "color": "#e92efb",
                #                     "size": "md"
                #                 }
                #             ],
                #             "paddingStart": "sm"
                #         }
                #     ]
                # },
                {
                    "type": "spacer"
                }
            ],
            "backgroundColor": "#00284a"
        }
    }
