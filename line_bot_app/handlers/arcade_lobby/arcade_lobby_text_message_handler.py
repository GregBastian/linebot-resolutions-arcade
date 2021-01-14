"""
Created on 08/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""

from line_bot_app.responses.arcade_lobby_responses.flex_message_responses.flex_message_responses import \
    flex_responses_obj

from line_bot_app.constants import AcceptedTextMessages


class ArcadeLobbyTextMessageHandlers:
    def arcade_lobby_text_message_handler_function(self, event, line_bot_api, message=""):
        if message == AcceptedTextMessages.GAMES:
            # returns TEXT message and FLEX message
            flex_responses_obj.show_games(event, line_bot_api)
        
        elif message == AcceptedTextMessages.HELP.value:
            pass


arcade_lobby_text_message_event_handlers_obj = ArcadeLobbyTextMessageHandlers()
