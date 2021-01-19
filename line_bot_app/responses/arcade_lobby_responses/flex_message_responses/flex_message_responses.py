"""
Created on 11/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""

from linebot.models import FlexSendMessage, TextSendMessage

from line_bot_app.templates.flex_message_templates.follow_event_flex_template \
    import get_follow_event_flex_message

from line_bot_app.templates.flex_message_templates.arcade_lobby_flex_templates.game_display_flex_template \
    import get_games_display_carousel_flex_message


class FlexResponses:
    def received_follow_event(self, event, line_bot_api):
        idUser = event.source.user_id
        profile = line_bot_api.get_profile(idUser)

        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text=f"Selamat Datang, {profile.display_name}",
                            contents=get_follow_event_flex_message(profile.display_name))
        )

    def show_games(self, event, line_bot_api):
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(text="Silahkan pilih permainan yang tersedia"),
                FlexSendMessage(alt_text="Daftar Permainan",
                                contents=get_games_display_carousel_flex_message())
            ]
        )


flex_responses_obj = FlexResponses()