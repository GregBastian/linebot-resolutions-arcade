"""
Created on 23/01/2021

@author: Gregorius Ivan Sebastian
"""
from linebot.models import FlexSendMessage, TextSendMessage

from line_bot_app.templates.flex_message_templates.flag_quiz_flex_template.flag_quiz_flex_template \
    import get_flag_quiz_bubble_flex_message

from line_bot_app.db_models.models import UserBatikGameModel, BatikGameQuestionsModel, RichMenuModel, UserArcadeModel

from line_bot_app.constants import AcceptedArcadeLobbyTextMessages, TebakBatikConstants

import random


class FlexResponses:

    @staticmethod
    def generate_question(event):
        idUser = event.source.user_id
        trueBatikId = random.randint(1, 75)
        falseCountryIds = random.sample([x for x in range(1, 76) if x != trueBatikId], 4)
        trueChoice = random.choice(TebakBatikConstants.OPTIONS.value)
        choices2FlexMessage = {trueChoice: BatikGameQuestionsModel.get_batik_name_by_id(trueBatikId)}
        for pos, el in enumerate(choice for choice in TebakBatikConstants.OPTIONS.value if choice != trueChoice):
            choices2FlexMessage[el] = BatikGameQuestionsModel.get_batik_name_by_id(falseCountryIds[pos])
        UserBatikGameModel.set_selected_option_to_true_by_user_id(idUser, trueChoice)
        return choices2FlexMessage, trueBatikId 

    def get_first_question(self, event, line_bot_api):
        choices2FlexMessage, trueBatikId = self.generate_question(event)
        idUser = event.source.user_id
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text=f"{AcceptedArcadeLobbyTextMessages.FLAG_QUIZ.value.title()} "
                                     f"Pertanyaan ke-{TebakBatikConstants.FLAG_QUIZ_TOTAL_QUESTIONS.value}",
                            contents=get_flag_quiz_bubble_flex_message(
                                gameName=AcceptedArcadeLobbyTextMessages.FLAG_QUIZ.value.title(),
                                selectedFlagImage=BatikGameQuestionsModel.get_batik_url_by_id(trueBatikId),
                                currentQuestionCount=UserBatikGameModel.get_game_counter_by_user_id(idUser),
                                choices=choices2FlexMessage))
        )

    def get_second_question_and_onwards(self, event, line_bot_api):
        message = event.message.text
        idUser = event.source.user_id
        UserBatikGameModel.increment_counter_by_user_id(user_id=idUser, increment_value=1)

        if UserBatikGameModel.check_true_option_by_user_id(idUser, message):
            UserBatikGameModel.increment_score_by_user_id(idUser)
            userTextRightOrWrong = "Tepat! Nama batik yang kamu pilih benar..."

        else:
            userTextRightOrWrong = "Ups! Nama batik yang kamu pilih kurang tepat..."

        UserBatikGameModel.set_all_options_as_false_by_user_id(idUser)
        choices2FlexMessage, trueBatikId = self.generate_question(event)

        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(userTextRightOrWrong),
                FlexSendMessage(alt_text=f"{AcceptedArcadeLobbyTextMessages.FLAG_QUIZ.value.title()} "
                                         f"Pertanyaan ke-{TebakBatikConstants.FLAG_QUIZ_TOTAL_QUESTIONS.value}",
                                contents=get_flag_quiz_bubble_flex_message(
                                    gameName=AcceptedArcadeLobbyTextMessages.FLAG_QUIZ.value.title(),
                                    selectedFlagImage=BatikGameQuestionsModel.get_batik_url_by_id(trueBatikId),
                                    currentQuestionCount=UserBatikGameModel.get_game_counter_by_user_id(idUser),
                                    choices=choices2FlexMessage))
            ]
        )


tebak_batik_flex_responses_obj = FlexResponses()
