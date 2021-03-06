"""
Created on 24/01/2021

@author: Gregorius Ivan Sebastian
"""
from linebot.models import TextSendMessage

from line_bot_app.constants import AcceptedFlagQuizTextMessages

from line_bot_app.db_models.models import UserFlagGameModel, RichMenuModel, UserArcadeModel


class FlagQuizTextResponses:

    def get_flag_quiz_help(self, event, line_bot_api):
        help_msg = f"Silahkan uji maupun asah pengetahuanmu mengenai bendera-bendera negara. Disini kamu akan" \
                   f"menebak asal negara mana dari bendera yang ditampilkan. Gunakan tombol-tombol di menu bawah" \
                   f"untuk bermain:\n" \
                   f"1. {AcceptedFlagQuizTextMessages.HELP.value.capitalize()}: menampilkan pesan ini kembali\n" \
                   f"2. {AcceptedFlagQuizTextMessages.OPTIONS.value}: pilih opsi berikut sebagai jawaban\n" \
                   f"3. {AcceptedFlagQuizTextMessages.BACK.value.capitalize()}: kembali ke lobby Resolutions Arcade"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(help_msg))

    def get_final_score_game_when_finish(self, event, line_bot_api):
        message = event.message.text
        idUser = event.source.user_id

        if UserFlagGameModel.check_true_option_by_user_id(idUser, message):
            UserFlagGameModel.increment_score_by_user_id(idUser)
            userTextRightOrWrong = "Tepat! Jawaban Kamu benar..."

        else:
            userTextRightOrWrong = "Ups! Jawaban Kamu kurang tepat..."

        currentScore = UserFlagGameModel.get_score_by_user_id(user_id=idUser)
        userHighScore = UserFlagGameModel.get_hi_score_by_user_id(user_id=idUser)
        if currentScore > userHighScore:
            UserFlagGameModel.set_hi_score_by_user_id(idUser, currentScore)

        line_bot_api.link_rich_menu_to_user(idUser,
                                            RichMenuModel.get_rich_menu_by_pk_id(1))
        UserArcadeModel.set_game_stop_playing_by_user_id(idUser)
        UserFlagGameModel.reset_game_settings_by_user_id(idUser)

        finalMsg = f"---PERMAINAN SELESAI---\n\n"\
                    f"Beriku rincian skor akhir kamu:\n"\
                    f"Skor Akhir: {currentScore}\n" \
                    f"Skor Tertinggi: {UserFlagGameModel.get_hi_score_by_user_id(idUser)}\n\n" \
                    f"Terima kasih telah bermain game ini. Jika ingin mengulang, maka bisa memilih game" \
                    f"ini kembali ketika berada di Arcade Lobby :)"

        goingBackMsg = "Sekarang kamu akan kembali menuju ke Arcade Lobby..."

        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(userTextRightOrWrong),
                TextSendMessage(finalMsg),
                TextSendMessage(goingBackMsg)
            ])

    def get_back_to_arcade_lobby(self, event, line_bot_api):
        idUser = event.source.user_id
        line_bot_api.link_rich_menu_to_user(idUser,
                                            RichMenuModel.get_rich_menu_by_pk_id(1))
        UserArcadeModel.set_game_stop_playing_by_user_id(idUser)
        UserFlagGameModel.reset_game_settings_by_user_id(idUser)

        goodbye_msg = "Selamat tinggal, sampai jumpa kembali! :)"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(goodbye_msg)
        )


flag_quiz_text_message_response_obj = FlagQuizTextResponses()
