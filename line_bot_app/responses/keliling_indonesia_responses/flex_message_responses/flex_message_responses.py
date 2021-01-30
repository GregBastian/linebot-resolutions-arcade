"""
Created on 23/01/2021

@author: Gregorius Ivan Sebastian
"""
from linebot.models import FlexSendMessage, TextSendMessage

from line_bot_app.templates.flex_message_templates.kelilling_indonesia_templates.keliling_indonesia_flex_template import \
    get_keliling_indonesia_bubble_flex_message

from line_bot_app.db_models.models import UserKelilingIndonesiaGameModel, IndonesiaLocationGameQuestionsModel

from line_bot_app.constants import AcceptedArcadeLobbyTextMessages, KelilingIndonesiaConstants, \
    KelilingIndonesiaGameThumbnails

import random

import logging


class FlexResponses:

    @staticmethod
    def generate_question(event):
        idUser = event.source.user_id
        trueKotaKabupatenId = random.randint(1, 514)
        trueKotaKabupaten = IndonesiaLocationGameQuestionsModel.get_nama_kota_or_kabupaten_by_id(trueKotaKabupatenId)
        trueProvinsi = IndonesiaLocationGameQuestionsModel.get_provinsi_by_id(trueKotaKabupatenId)
        trueChoice = random.choice(KelilingIndonesiaConstants.OPTIONS.value)
        choices2FlexMessage = {trueChoice: trueProvinsi}
        falseChoices = random.sample([provinsi for provinsi in KelilingIndonesiaConstants.DAFTAR_PROVINSI.value
                                      if provinsi != trueProvinsi], 3)
        for pos, el in enumerate(choice for choice in KelilingIndonesiaConstants.OPTIONS.value if choice != trueChoice):
            choices2FlexMessage[el] = falseChoices[pos]
        UserKelilingIndonesiaGameModel.set_selected_option_to_true_by_user_id(idUser, trueChoice)
        return choices2FlexMessage, trueKotaKabupatenId, trueKotaKabupaten

    def get_first_question(self, event, line_bot_api):
        choices2FlexMessage, trueKotaKabupatenId, trueKotaKabupaten = self.generate_question(event)
        idUser = event.source.user_id
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text=f"{AcceptedArcadeLobbyTextMessages.KELILING_INDONESIA.value.title()} "
                                     f"Pertanyaan ke-{KelilingIndonesiaConstants.KELILING_INDONESIA_TOTAL_QUESTIONS.value}",
                            contents=get_keliling_indonesia_bubble_flex_message(
                                gameName=AcceptedArcadeLobbyTextMessages.KELILING_INDONESIA.value.title(),
                                randomThumbnail=random.choice(KelilingIndonesiaGameThumbnails.values2list()),
                                trueKotaKabupatenName=trueKotaKabupaten,
                                currentQuestionCount=UserKelilingIndonesiaGameModel.get_game_counter_by_user_id(idUser),
                                choices=choices2FlexMessage))
        )

    # continue from this point
    def get_second_question_and_onwards(self, event, line_bot_api):
        message = event.message.text
        idUser = event.source.user_id
        UserKelilingIndonesiaGameModel.increment_counter_by_user_id(user_id=idUser, increment_value=1)

        if UserKelilingIndonesiaGameModel.check_true_option_by_user_id(idUser, message):
            UserKelilingIndonesiaGameModel.increment_score_by_user_id(idUser)
            userTextRightOrWrong = "Tepat! Tampaknya kamu memang jago nih..."

            else:
            userTextRightOrWrong = "Ups! Sepertinya kamu salah lokasi...""

        UserKelilingIndonesiaGameModel.set_all_options_as_false_by_user_id(idUser)
        choices2FlexMessage, trueKotaKabupatenId, trueKotaKabupaten = self.generate_question(event)

        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(userTextRightOrWrong),
                FlexSendMessage(alt_text=f"{AcceptedArcadeLobbyTextMessages.KELILING_INDONESIA.value.title()} "
                                         f"Pertanyaan ke-{KelilingIndonesiaConstants.KELILING_INDONESIA_TOTAL_QUESTIONS.value}",
                                contents=get_keliling_indonesia_bubble_flex_message(
                                    gameName=AcceptedArcadeLobbyTextMessages.KELILING_INDONESIA.value.title(),
                                    randomThumbnail=random.choice(KelilingIndonesiaGameThumbnails.values2list()),
                                    trueKotaKabupatenName=trueKotaKabupaten,
                                    currentQuestionCount=UserKelilingIndonesiaGameModel.get_game_counter_by_user_id(
                                        idUser),
                                    choices=choices2FlexMessage))
            ]
        )


keliling_indonesia_flex_responses_obj = FlexResponses()
