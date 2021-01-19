"""
Created on 18/01/2021

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""
from line_bot_app.db_models.models import UserArcadeModel

from line_bot_app.handlers.arcade_lobby.arcade_lobby_text_message_handler import \
    arcade_lobby_text_message_event_handlers_obj


class ArcadeGeneralHandler:
    def general_text_message_handler_function(self, event, line_bot_api):
        idUser = event.source.user_id
        if UserArcadeModel.get_is_playing_game_by_user_id(idUser):
            # if the user is playing a game
            pass

        else:
            arcade_lobby_text_message_event_handlers_obj.arcade_lobby_text_message_handler_function(event, line_bot_api)


arcade_general_handler_obj = ArcadeGeneralHandler()
