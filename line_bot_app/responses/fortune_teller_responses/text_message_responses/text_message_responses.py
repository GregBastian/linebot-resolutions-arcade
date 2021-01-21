"""
Created on 20/01/2021

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""
from linebot.models import TextSendMessage


class FortuneTellerTextResponses:

    def get_fortune_teller_help(self, event, line_bot_api):
        help_msg = f"Halo, selamat datang ke ruangan saya. Disini saya akan membantu anda" \
                   f"jika anda belum menentukan resolusimu untuk tahun 2012. Gunakan menu dibawah" \
                   f"untuk berinteraksi dengan saya:\n" \
                   f"1. Help: menampilkan pesan ini kembali" \
                   f"2. Ramal: tampilkan pesan ramalan\n" \
                   f"3. Back: kembali ke lobby Resolutions Arcade"
        return line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(help_msg))


fortune_teller_text_message_response_obj = FortuneTellerTextResponses()
