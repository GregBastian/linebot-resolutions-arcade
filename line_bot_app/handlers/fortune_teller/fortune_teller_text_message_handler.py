"""
Created on 18/01/2021

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""
from line_bot_app.responses.fortune_teller_responses.text_message_responses.text_message_responses import \
    fortune_teller_text_message_response_obj

from line_bot_app.responses.fortune_teller_responses.flex_message_responses.flex_message_responses import \
    fortune_teller_flex_responses_obj

from line_bot_app.responses.arcade_lobby_responses.flex_message_responses.flex_message_responses import \
    arcade_lobby_flex_responses_obj

from line_bot_app.constants import AcceptedFortuneTellerTextMessages, RichMenuNames

from line_bot_app.db_models.models import UserArcadeModel, RichMenuModel


class FortuneTellerTextMessageHandlers:
    def fortune_teller_text_message_handler_function(self, event, line_bot_api):
        message = event.message.text
        idUser = event.source.user_id
        if message == AcceptedFortuneTellerTextMessages.RAMAL.value:
            fortune_teller_flex_responses_obj.show_fortune_teller_quote(event, line_bot_api)

        elif message == AcceptedFortuneTellerTextMessages.HELP.value:
            fortune_teller_text_message_response_obj.get_fortune_teller_help(event, line_bot_api)

        elif message == AcceptedFortuneTellerTextMessages.BACK.value:
            line_bot_api.link_rich_menu_to_user(idUser,
                                                RichMenuModel.get_rich_menu_by_name(RichMenuNames.ARCADE_LOBBY.value))
            UserArcadeModel.set_game_stop_playing_by_user_id(idUser)
            arcade_lobby_flex_responses_obj.show_games(event, line_bot_api)


fortune_teller_text_message_handler_obj = FortuneTellerTextMessageHandlers()
