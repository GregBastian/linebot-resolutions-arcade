"""
Created on 08/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""

from line_bot_app.responses.fortune_teller_responses.flex_message_responses.flex_message_responses import \
    fortune_teller_flex_responses_obj

from line_bot_app.responses.arcade_lobby_responses.flex_message_responses.flex_message_responses import \
    arcade_lobby_flex_responses_obj

from line_bot_app.responses.arcade_lobby_responses.text_message_responses.text_message_responses import \
    arcade_lobby_text_message_response_obj

from line_bot_app.constants import AcceptedArcadeLobbyTextMessages
from line_bot_app.db_models.models import UserArcadeModel, RichMenuModel


class ArcadeLobbyTextMessageHandlers:
    def arcade_lobby_text_message_handler_function(self, event, line_bot_api):
        message = event.message.text
        idUser = event.source.user_id
        # below are conditions if the user chooses one of the games
        if message == AcceptedArcadeLobbyTextMessages.FORTUNE_TELLER.value:
            UserArcadeModel.set_game_by_user_id(idUser, message)
            line_bot_api.link_rich_menu_to_user(idUser, RichMenuModel.get_rich_menu_by_pk_id(2))
            fortune_teller_flex_responses_obj.show_fortune_teller_quote(event, line_bot_api)

        # below are conditions if the user has not picked a game yet
        elif message == AcceptedArcadeLobbyTextMessages.GAMES.value:
            arcade_lobby_flex_responses_obj.show_games(event, line_bot_api)

        elif message == AcceptedArcadeLobbyTextMessages.INFO.value:
            arcade_lobby_text_message_response_obj.get_arcade_lobby_info(event, line_bot_api)


arcade_lobby_text_message_event_handlers_obj = ArcadeLobbyTextMessageHandlers()
