"""
Created on 01/01/2021

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""
from flask import Flask, request, abort
import logging

from linebot.exceptions import InvalidSignatureError
from linebot.models import *


def create_app(line_bot_api, handler):
    app = Flask(__name__)

    logging.basicConfig(level=logging.INFO)

    @app.route("/check")
    def homepage_test():
        return {
            "message": "Hello World",
            "type": "json"
        }

    @app.route("/webhook", methods=['POST'])
    def callback():
        # get X-Line-Signature header value
        signature = request.headers['X-Line-Signature']
        # get request body as text
        body = request.get_data(as_text=True)
        app.logger.info("Request body: " + body)
        # handle webhook body
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)
        return 'OK'

    @handler.add(FollowEvent)
    def user_follow_event(event):
        idUser = event.source.user_id
        profile = line_bot_api.get_profile(idUser)
        app.logger.info(f"Received Follow event from {idUser}")



    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(event):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text))

    return app
