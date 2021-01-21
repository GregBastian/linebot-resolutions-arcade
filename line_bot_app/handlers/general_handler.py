"""
Created on 18/01/2021

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""
from line_bot_app.db_models.models import UserArcadeModel

from line_bot_app.constants import AcceptedArcadeLobbyTextMessages

from line_bot_app.handlers.arcade_lobby.arcade_lobby_text_message_handler import \
    arcade_lobby_text_message_event_handlers_obj

from line_bot_app.handlers.fortune_teller.fortune_teller_text_message_handler import \
    fortune_teller_text_message_handler_obj


class ArcadeGeneralHandler:
    def general_text_message_handler_function(self, event, line_bot_api):
        idUser = event.source.user_id
        userArcade = UserArcadeModel.get_user_by_user_id(idUser)
        if userArcade.is_playing_game:
            # below are conditions to check what game the user is playing
            if UserArcadeModel.name_of_game_played == AcceptedArcadeLobbyTextMessages.FORTUNE_TELLER.value:
                fortune_teller_text_message_handler_obj.fortune_teller_text_message_handler_function(event,
                                                                                                     line_bot_api)
            elif UserArcadeModel.name_of_game_played == AcceptedArcadeLobbyTextMessages.FLAG_QUIZ.value:
                pass

        else:
            arcade_lobby_text_message_event_handlers_obj.arcade_lobby_text_message_handler_function(event, line_bot_api)


arcade_general_handler_obj = ArcadeGeneralHandler()
