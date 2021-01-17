# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 18:16:43 2020

@author: Gregorius Ivan Sebastian
@email: ivansebastian60@gmail.com
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from random import randint

db = SQLAlchemy()


# ==!! IMPORTANT !!==
# If you modified the table design in the database please make sure that you
# edit this class accordingly and vice-versa

class UserArcadeModel(db.Model):
    __tablename__ = "user_arcade"
    id_ = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(33), nullable=False, unique=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    is_playing_game = db.Column(db.Boolean, nullable=False, default=False)
    name_of_game_played = db.Column(db.String(25), nullable=False, default="")
    flag_game_score = db.Column(db.String(2), nullable=True, default="0")

    def __init__(self, user_id):
        self.user_id = user_id

    @staticmethod
    def add_user(user_id):
        newUser = UserArcadeModel(user_id=user_id)
        db.session.add(newUser)
        db.session.commit()

    @staticmethod
    def reset_fields_by_user_id(user_id):
        userArcade = UserArcadeModel.query.filter_by(user_id=user_id)
        userArcade.is_playing_game = False
        userArcade.name_of_game_played = ""
        userArcade.flag_game_score = "0"


    @staticmethod
    def user_isExist_by_user_id(user_id):
        userIsExist = UserArcadeModel.query.filter_by(user_id=user_id)
        return bool(userIsExist)

    @staticmethod
    def get_user_by_user_id(user_id):
        userArcade = UserArcadeModel.query.filter_by(user_id=user_id)
        return userArcade

    @staticmethod
    def set_game_by_user_id(user_id, gameName):
        userArcade = UserArcadeModel.query.filter_by(user_id=user_id)
        userArcade.name_of_game_played = gameName
        userArcade.is_playing_game = True
        db.session.commit()

    @staticmethod
    def get_is_playing_game_by_user_id(user_id):
        userArcade = UserArcadeModel.query.filter_by(user_id=user_id)
        return userArcade.is_playing_game


class FortuneTellerModel(db.Model):
    __tablename__ = "fortune_teller_quotes"
    id_ = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.Integer)
    quote = db.Column(db.Text(), nullable=False)

    def __init__(self, id_, number, quote):
        self.id_ = id_
        self.number = number
        self.quote = quote

    @staticmethod
    def get_quote_by_number(number):
        fortuneTeller = FortuneTellerModel.query.filter_by(
            number=number
        ).first()

        return fortuneTeller.quote

    @staticmethod
    def get_random_quote():
        tableEntityLength = FortuneTellerModel.query.count()
        random_number = randint(1, len(tableEntityLength))

        fortuneTeller = FortuneTellerModel.query.filter_by(
            number=random_number
        ).first()

        return fortuneTeller.quote

    # class FlagGameModel(db.Model):
    #     __tablename__ = "fortune_teller_quotes"
    #     id_ = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #     number = db.Column(db.Integer)
    #     quote = db.Column(db.Text(), nullable=False)