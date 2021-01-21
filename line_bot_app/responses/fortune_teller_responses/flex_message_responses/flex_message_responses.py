"""
Created on 11/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""

from linebot.models import FlexSendMessage

from line_bot_app.constants import FortuneTellerImage

from line_bot_app.db_models.models import FortuneTellerModel

from line_bot_app.templates.flex_message_templates.fortune_teller_flex_templates.fortune_teller_flex_template \
    import get_fortune_teller_bubble_flex_message


class FortuneTellerFlexResponses:
    def show_fortune_teller_quote(self, event, line_bot_api):
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text=f"Ramalanmu dari sang Fortune Teller",
                            contents=get_fortune_teller_bubble_flex_message(
                                FortuneTellerImage.FORTUNE_TELLER_THUMBNAIL.value,
                                FortuneTellerModel.get_random_quote()
                                ))
        )


fortune_teller_flex_responses_obj = FortuneTellerFlexResponses()
