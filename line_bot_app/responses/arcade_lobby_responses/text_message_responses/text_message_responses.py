"""
Created on 20/01/2021

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""
from linebot.models import TextSendMessage


class ArcadeLobbyTextResponses:
    def get_arcade_lobby_info(self, event, line_bot_api):
        help_msg = f"Halo, selamat datang ke Resolutions Arcade!\n\n" \
                   f"Tampilkan games dengan menekan tombol 'Show Games'.Jika ingin bermain sebuah game maka bisa " \
                   f"dengan menekan tombol play pada window game masing-masing, dan jika sudah selesai bermain, " \
                   f"maka kamu bisa menekan tombol 'back' untuk kembali ke lobi ini.\n\n" \
                   f" Have fun!"
        return line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(help_msg))


arcade_lobby_text_message_response_obj = ArcadeLobbyTextResponses()
