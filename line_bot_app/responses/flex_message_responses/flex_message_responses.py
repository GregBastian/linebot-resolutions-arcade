"""
Created on 11/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""

from linebot.models import FlexSendMessage

from line_bot_app.responses.flex_message_responses.flex_message_templates.follow_event_flex_template \
    import get_follow_event_flex_message


class FlexResponses:
    def received_follow_event(self, event, line_bot_api):
        idUser = event.source.user_id
        profile = line_bot_api.get_profile(idUser)
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text=f"Welcome, {profile.display_name}",
                            contents=get_follow_event_flex_message(profile.display_name))
        )


flex_responses_obj = FlexResponses()
