"""
Created on 01/01/2021

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""
from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
import logging
import os

from linebot.exceptions import InvalidSignatureError
from linebot.models import *

from line_bot_app.handlers.follow_event_handler import user_follow_event_handlers_obj
from line_bot_app.handlers.arcade_lobby.arcade_lobby_text_message_handler import arcade_lobby_text_message_event_handlers_obj


def create_app(line_bot_api, handler):
    app = Flask(__name__)
    db = SQLAlchemy(app)

    logging.basicConfig(level=logging.INFO)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    from line_bot_app.db_models.models import UserArcadeModel
    db.init_app(app)
    db.create_all()


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
        app.logger.info(f"Received Follow Event from {idUser}")
        user_follow_event_handlers_obj.user_follow_event_handler_function(event, line_bot_api)

    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(event):
        idUser = event.source.user_id
        message = event.message.text

        if isinstance(event.source, SourceUser):
            # if still in lobby condition from database
            app.logger.info(f"Received Message Event from {idUser} with text message '{message}'")
            arcade_lobby_text_message_event_handlers_obj.arcade_lobby_text_message_handler_function(event, line_bot_api, message)

    return app
