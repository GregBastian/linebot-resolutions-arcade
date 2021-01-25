"""
Created on 18/01/2021

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""
from line_bot_app.responses.flag_quiz_responses.text_message_responses.text_message_responses import \
    flag_quiz_text_message_response_obj

from line_bot_app.responses.flag_quiz_responses.flex_message_responses.flex_message_responses import \
    flag_quiz_flex_responses_obj

from line_bot_app.constants import FlagQuizConstants, AcceptedFlagQuizTextMessages

from line_bot_app.db_models.models import UserFlagGameModel


class FlagQuizTextMessageHandlers:
    def flag_quiz_text_message_handler_function(self, event, line_bot_api):
        message = event.message.text
<<<<<<< HEAD
        idUser = event.source.id_user

        if UserFlagGameModel.get_game_counter_by_user_id(idUser) > FlagQuizConstants.FLAG_QUIZ_TOTAL_QUESTIONS.value:
            flag_quiz_text_message_response_obj.get_final_score_game_when_finish(event, line_bot_api)

        if message in FlagQuizConstants.OPTIONS.value and \
                UserFlagGameModel.get_game_counter_by_user_id(idUser) <= FlagQuizConstants.FLAG_QUIZ_TOTAL_QUESTIONS.value:
=======
        idUser = event.source.user_id
        
        if message in FlagQuizConstants.OPTIONS.value:
>>>>>>> 684372ee3ef468dc1168fb251217ecd7974ce97a
            flag_quiz_flex_responses_obj.get_second_question_and_onwards(event, line_bot_api)

        elif message == AcceptedFlagQuizTextMessages.HELP.value:
            flag_quiz_text_message_response_obj.get_flag_quiz_help(event, line_bot_api)

        elif message == AcceptedFlagQuizTextMessages.BACK.value:
            flag_quiz_text_message_response_obj.get_back_to_arcade_lobby(event, line_bot_api)


flag_quiz_text_message_handler_obj = FlagQuizTextMessageHandlers()
