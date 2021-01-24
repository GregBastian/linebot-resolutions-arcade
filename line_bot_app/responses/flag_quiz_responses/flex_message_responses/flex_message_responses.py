"""
Created on 23/01/2021

@author: Gregorius Ivan Sebastian
"""
from linebot.models import FlexSendMessage, TextSendMessage

from line_bot_app.templates.flex_message_templates.flag_quiz_flex_template.flag_quiz_flex_template \
    import get_flag_quiz_bubble_flex_message

from line_bot_app.db_models.models import UserFlagGameModel, FlagGameQuestionsModel

from line_bot_app.constants import FlagQuizConstants, AcceptedArcadeLobbyTextMessages

import random


class FlexResponses:

    @staticmethod
    def generate_question(event):
        idUser = event.source.user_id
        trueCountryId = random.randint(1, 82)
        falseCountryIds = random.sample([x for x in range(1, 83) if x != trueCountryId], 4)
        trueChoice = random.choice(FlagQuizConstants.OPTIONS.value)
        choices2FlexMessage = {trueChoice: FlagGameQuestionsModel.get_name_by_id(trueCountryId)}
        for pos, el in enumerate(choice for choice in FlagQuizConstants.OPTIONS.value if choice != trueChoice):
            choices2FlexMessage[el] = FlagGameQuestionsModel.get_name_by_id(falseCountryIds[pos])
        UserFlagGameModel.set_selected_option_to_true_by_user_id(idUser, trueChoice)
        return choices2FlexMessage, trueCountryId

    def get_first_question(self, event, line_bot_api):
        choices2FlexMessage, trueCountryId = self.generate_question(event)
        idUser = event.source.user_id
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text=f"{AcceptedArcadeLobbyTextMessages.FLAG_QUIZ.value.title()} "
                                     f"Pertanyaan ke-{FlagQuizConstants.FLAG_QUIZ_TOTAL_QUESTIONS.value}",
                            contents=get_flag_quiz_bubble_flex_message(
                                gameName=AcceptedArcadeLobbyTextMessages.FLAG_QUIZ.value.title(),
                                selectedFlagImage=FlagGameQuestionsModel.get_flag_by_id(trueCountryId),
                                currentQuestionCount=UserFlagGameModel.get_game_counter_by_user_id(idUser),
                                choices=choices2FlexMessage))
        )

    def get_second_question_and_onwards(self, event, line_bot_api):
        message = event.message.text
        idUser = event.source.user_id
        UserFlagGameModel.increment_counter_by_user_id(user_id=idUser, increment_value=1)

        if UserFlagGameModel.check_true_option_by_user_id(idUser, message):
            UserFlagGameModel.increment_score_by_user_id(idUser)
            userTextRightOrWrong = "Tepat! Jawaban Kamu benar..."

        else:
            userTextRightOrWrong = "Ups! Jawaban Kamu kurang tepat..."

        UserFlagGameModel.set_all_options_as_false_by_user_id(idUser)
        choices2FlexMessage, trueCountryId = self.generate_question(event)
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(userTextRightOrWrong),
                FlexSendMessage(alt_text=f"{AcceptedArcadeLobbyTextMessages.FLAG_QUIZ.value.title()} "
                                         f"Pertanyaan ke-{FlagQuizConstants.FLAG_QUIZ_TOTAL_QUESTIONS.value}",
                                contents=get_flag_quiz_bubble_flex_message(
                                    gameName=AcceptedArcadeLobbyTextMessages.FLAG_QUIZ.value.title(),
                                    selectedFlagImage=FlagGameQuestionsModel.get_flag_by_id(trueCountryId),
                                    currentQuestionCount=UserFlagGameModel.get_game_counter_by_user_id(idUser),
                                    choices=choices2FlexMessage))
            ]
        )

    def get_flag_quiz_help(self, event, line_bot_api):
        pass


flag_quiz_flex_responses_obj = FlexResponses()
