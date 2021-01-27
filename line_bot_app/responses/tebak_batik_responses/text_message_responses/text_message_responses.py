"""
Created on 24/01/2021

@author: Gregorius Ivan Sebastian
"""
from linebot.models import TextSendMessage

from line_bot_app.constants import AcceptedTebakBatikTextMessages

from line_bot_app.db_models.models import UserBatikGameModel, RichMenuModel, UserArcadeModel


class TebakBatikTextResponses:

    def get_tebak_batik_help(self, event, line_bot_api):
        help_msg = f"Apakah kamu tahu semua tentang batik-batik di Indonesia? Ukur pengetahuanmu" \
                   f"mengenai batik-batik di Indonesia di kuis ini. Gunakan tombol-tombol di menu" \
                   f"bawah ini untuk bermain:\n" \
                   f"1. {AcceptedTebakBatikTextMessages.HELP.value.capitalize()}: menampilkan pesan ini kembali\n" \
                   f"2. {AcceptedTebakBatikTextMessages.OPTIONS.value}: pilih opsi berikut sebagai jawaban\n" \
                   f"3. {AcceptedTebakBatikTextMessages.BACK.value.capitalize()}: kembali ke lobby Resolutions Arcade"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(help_msg))

    def get_final_score_game_when_finish(self, event, line_bot_api):
        message = event.message.text
        idUser = event.source.user_id

        if UserBatikGameModel.check_true_option_by_user_id(idUser, message):
            UserBatikGameModel.increment_score_by_user_id(idUser)
            userTextRightOrWrong = "Tepat! Nama batik yang kamu pilih benar..."

        else:
            userTextRightOrWrong = "Ups! Nama batik yang kamu pilih kurang tepat..."

        currentScore = UserBatikGameModel.get_score_by_user_id(user_id=idUser)
        userHighScore = UserBatikGameModel.get_hi_score_by_user_id(user_id=idUser)
        if currentScore > userHighScore:
            UserBatikGameModel.set_hi_score_by_user_id(idUser, currentScore)

        line_bot_api.link_rich_menu_to_user(idUser,
                                            RichMenuModel.get_rich_menu_by_pk_id(1))
        UserArcadeModel.set_game_stop_playing_by_user_id(idUser)
        UserBatikGameModel.reset_game_settings_by_user_id(idUser)

        finalMsg = f"---PERMAINAN SELESAI---\n\n"\
                    f"Beriku rincian skor akhir kamu:\n"\
                    f"Skor Akhir: {currentScore}\n" \
                    f"Skor Tertinggi: {UserBatikGameModel.get_hi_score_by_user_id(idUser)}\n\n" \
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
        UserBatikGameModel.reset_game_settings_by_user_id(idUser)

        goodbye_msg = "Selamat tinggal, sampai jumpa kembali! :)"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(goodbye_msg)
        )


tebak_batik_text_message_response_obj = TebakBatikTextResponses()
