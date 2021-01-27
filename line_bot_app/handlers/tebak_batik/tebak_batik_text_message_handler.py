"""
Created on 27/01/2021

@author: Gregorius Ivan Sebastian
"""
from line_bot_app.responses.tebak_batik_responses.text_message_responses.text_message_responses import \
    tebak_batik_text_message_response_obj

from line_bot_app.responses.tebak_batik_responses.flex_message_responses.flex_message_responses import \
    tebak_batik_flex_responses_obj

from line_bot_app.constants import TebakBatikConstants, AcceptedTebakBatikTextMessages
from line_bot_app.db_models.models import UserBatikGameModel


class TebakBatikTextMessageHandler:
    def tebak_batik_text_message_handler_function(self, event, line_bot_api):
        message = event.message.text
        idUser = event.source.user_id

        if UserBatikGameModel.get_game_counter_by_user_id(idUser) >= TebakBatikConstants.FLAG_QUIZ_TOTAL_QUESTIONS.value:
            tebak_batik_text_message_response_obj.get_final_score_game_when_finish(event, line_bot_api)

        elif message in TebakBatikConstants.OPTIONS.value and \
                UserBatikGameModel.get_game_counter_by_user_id(
                    idUser) < TebakBatikConstants.TEBAK_BATIK_TOTAL_QUESTIONS.value:
            tebak_batik_flex_responses_obj.get_second_question_and_onwards(event, line_bot_api)

        elif message == AcceptedTebakBatikTextMessages.HELP.value:
            tebak_batik_text_message_response_obj.get_flag_quiz_help(event, line_bot_api)

        elif message == AcceptedTebakBatikTextMessages.BACK.value:
            tebak_batik_text_message_response_obj.get_back_to_arcade_lobby(event, line_bot_api)


tebak_batik_text_message_handler_obj = TebakBatikTextMessageHandler()
