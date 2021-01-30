"""
Created on 27/01/2021

@author: Gregorius Ivan Sebastian
"""
from line_bot_app.responses.keliling_indonesia_responses.text_message_responses.text_message_responses import \
    keliling_indonesia_text_message_response_obj

from line_bot_app.responses.keliling_indonesia_responses.flex_message_responses.flex_message_responses import \
    keliling_indonesiak_flex_responses_obj

from line_bot_app.constants import KelilingIndonesiaConstants, AcceptedKelilingIndonesiaMessages

from line_bot_app.db_models.models import UserKelilingIndonesiaGameModel


class KelilingIndonesiaTextMessageHandler:
    def keliling_indonesia_text_message_handler_function(self, event, line_bot_api):
        message = event.message.text
        idUser = event.source.user_id

        if UserKelilingIndonesiaGameModel.get_game_counter_by_user_id(idUser) >= KelilingIndonesiaConstants.TEBAK_BATIK_TOTAL_QUESTIONS.value:
            keliling_indonesia_text_message_response_obj.get_final_score_game_when_finish(event, line_bot_api)

        elif message in KelilingIndonesiaConstants.OPTIONS.value and \
                UserKelilingIndonesiaGameModel.get_game_counter_by_user_id(
                    idUser) < KelilingIndonesiaConstants.TEBAK_BATIK_TOTAL_QUESTIONS.value:
            keliling_indonesiak_flex_responses_obj.get_second_question_and_onwards(event, line_bot_api)

        elif message == AcceptedKelilingIndonesiaMessages.HELP.value:
            keliling_indonesia_text_message_response_obj.get_keliling_indonesia_help(event, line_bot_api)

        elif message == AcceptedKelilingIndonesiaMessages.BACK.value:
            keliling_indonesia_text_message_response_obj.get_back_to_arcade_lobby(event, line_bot_api)


keliling_indonesia_text_message_handler_obj = KelilingIndonesiaTextMessageHandler()
