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

    def __init__(self, user_id):
        self.user_id = user_id

    @staticmethod
    def add_user(user_id):
        newUser = UserArcadeModel(user_id=user_id)
        newFlagGameUser = UserFlagGameModel(user_id=user_id)
        newBatikGameUser = UserBatikGameModel(user_id=user_id)
        db.session.add(newUser)
        db.session.add(newFlagGameUser)
        db.session.add(newBatikGameUser)
        db.session.commit()

    @staticmethod
    def reset_fields_by_user_id(user_id):
        userArcade = UserArcadeModel.query.filter_by(user_id=user_id).first()
        userArcade.is_playing_game = False
        userArcade.name_of_game_played = ""
        userArcade.flag_game_score = "0"
        db.session.commit()

    @staticmethod
    def user_isExist_by_user_id(user_id):
        userIsExist = UserArcadeModel.query.filter_by(user_id=user_id).first()
        return bool(userIsExist)

    @staticmethod
    def get_user_by_user_id(user_id):
        userArcade = UserArcadeModel.query.filter_by(user_id=user_id).first()
        return userArcade

    @staticmethod
    def set_game_by_user_id(user_id, gameName):
        userArcade = UserArcadeModel.query.filter_by(user_id=user_id).first()
        userArcade.name_of_game_played = gameName
        userArcade.is_playing_game = True
        db.session.commit()

    @staticmethod
    def get_is_playing_game_by_user_id(user_id):
        userArcade = UserArcadeModel.query.filter_by(user_id=user_id).first()
        return userArcade.is_playing_game

    @staticmethod
    def set_game_stop_playing_by_user_id(user_id):
        userArcade = UserArcadeModel.query.filter_by(user_id=user_id).first()
        userArcade.name_of_game_played = ""
        userArcade.is_playing_game = False
        db.session.commit()


class UserFlagGameModel(db.Model):
    __tablename__ = "user_flag_game_score"
    id_ = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(33), nullable=False, unique=True)
    game_score = db.Column(db.Integer, nullable=False, default=0)
    game_high_score = db.Column(db.Integer, nullable=True, default=0)
    game_question_counter = db.Column(db.Integer, nullable=False, default=1)
    option_A = db.Column(db.Boolean, nullable=False, default=False)
    option_B = db.Column(db.Boolean, nullable=False, default=False)
    option_C = db.Column(db.Boolean, nullable=False, default=False)
    option_D = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, user_id):
        self.user_id = user_id

    @staticmethod
    def add_user(user_id):
        newUserFlagGame = UserFlagGameModel(user_id=user_id)
        db.session.add(newUserFlagGame)
        db.session.commit()

    @staticmethod
    def get_user_by_user_id(user_id):
        userFlagGameModel = UserFlagGameModel.query.filter_by(user_id=user_id).first()
        return userFlagGameModel

    @staticmethod
    def get_score_by_user_id(user_id):
        userGameFlagModel = UserFlagGameModel.query.filter_by(user_id=user_id).first()
        return userGameFlagModel.game_score

    @staticmethod
    def increment_score_by_user_id(user_id):
        userGameFlagModel = UserFlagGameModel.query.filter_by(user_id=user_id).first()
        userGameFlagModel.game_score += 1
        db.session.commit()

    @staticmethod
    def get_hi_score_by_user_id(user_id):
        userFlagGameModel = UserFlagGameModel.query.filter_by(user_id=user_id).first()
        return userFlagGameModel.game_high_score

    @staticmethod
    def set_hi_score_by_user_id(user_id, newScore):
        userFlagGameModel = UserFlagGameModel.query.filter_by(user_id=user_id).first()
        userFlagGameModel.game_high_score = newScore
        db.session.commit()

    @staticmethod
    def get_game_counter_by_user_id(user_id):
        user_flag_game_hi_score = UserFlagGameModel.query.filter_by(user_id=user_id).first()
        return user_flag_game_hi_score.game_question_counter

    @staticmethod
    def increment_counter_by_user_id(user_id=user_id, increment_value=1):
        userFlagGameModel = UserFlagGameModel.query.filter_by(user_id=user_id).first()
        userFlagGameModel.game_question_counter += increment_value
        db.session.commit()

    @staticmethod
    def set_selected_option_to_true_by_user_id(user_id=user_id, option="A"):
        userFlagGameModel = UserFlagGameModel.query.filter_by(user_id=user_id).first()
        if option == 'A':
            userFlagGameModel.option_A = True
        elif option == 'B':
            userFlagGameModel.option_B = True
        elif option == 'C':
            userFlagGameModel.option_C = True
        elif option == 'D':
            userFlagGameModel.option_D = True
        db.session.commit()

    @staticmethod
    def reset_game_settings_by_user_id(user_id=user_id):
        userFlagGameModel = UserFlagGameModel.query.filter_by(user_id=user_id).first()
        userFlagGameModel.game_score = 0
        userFlagGameModel.game_question_counter = 1
        userFlagGameModel.option_A = False
        userFlagGameModel.option_B = False
        userFlagGameModel.option_C = False
        userFlagGameModel.option_D = False
        db.session.commit()

    @staticmethod
    def set_all_options_as_false_by_user_id(user_id=user_id):
        userFlagGameModel = UserFlagGameModel.query.filter_by(user_id=user_id).first()
        userFlagGameModel.option_A = False
        userFlagGameModel.option_B = False
        userFlagGameModel.option_C = False
        userFlagGameModel.option_D = False
        db.session.commit()

    @staticmethod
    def check_true_option_by_user_id(user_id=user_id, option="A"):
        userFlagGameModel = UserFlagGameModel.query.filter_by(user_id=user_id).first()
        if option == "A":
            return userFlagGameModel.option_A
        elif option == "B":
            return userFlagGameModel.option_B
        elif option == "C":
            return userFlagGameModel.option_C
        elif option == "D":
            return userFlagGameModel.option_D


class UserBatikGameModel(db.Model):
    __tablename__ = "user_batik_game_score"
    id_ = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(33), nullable=False, unique=True)
    game_score = db.Column(db.Integer, nullable=False, default=0)
    game_high_score = db.Column(db.Integer, nullable=True, default=0)
    game_question_counter = db.Column(db.Integer, nullable=False, default=1)
    option_A = db.Column(db.Boolean, nullable=False, default=False)
    option_B = db.Column(db.Boolean, nullable=False, default=False)
    option_C = db.Column(db.Boolean, nullable=False, default=False)
    option_D = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, user_id):
        self.user_id = user_id

    @staticmethod
    def add_user(user_id):
        newUserBatikGame = UserBatikGameModel(user_id=user_id)
        db.session.add(newUserBatikGame)
        db.session.commit()

    @staticmethod
    def get_user_by_user_id(user_id):
        userBatikGameModel = UserBatikGameModel.query.filter_by(user_id=user_id).first()
        return userBatikGameModel

    @staticmethod
    def get_score_by_user_id(user_id):
        userBatikGameModel = UserBatikGameModel.query.filter_by(user_id=user_id).first()
        return userBatikGameModel.game_score

    @staticmethod
    def increment_score_by_user_id(user_id):
        userBatikGameModel = UserBatikGameModel.query.filter_by(user_id=user_id).first()
        userBatikGameModel.game_score += 1
        db.session.commit()

    @staticmethod
    def get_hi_score_by_user_id(user_id):
        userBatikGameModel = UserBatikGameModel.query.filter_by(user_id=user_id).first()
        return userBatikGameModel.game_high_score

    @staticmethod
    def set_hi_score_by_user_id(user_id, newScore):
        userBatikGameModel = UserBatikGameModel.query.filter_by(user_id=user_id).first()
        userBatikGameModel.game_high_score = newScore
        db.session.commit()

    @staticmethod
    def get_game_counter_by_user_id(user_id):
        userBatikGameModel = UserBatikGameModel.query.filter_by(user_id=user_id).first()
        return userBatikGameModel.game_question_counter

    @staticmethod
    def increment_counter_by_user_id(user_id=user_id, increment_value=1):
        userBatikGameModel = UserBatikGameModel.query.filter_by(user_id=user_id).first()
        userBatikGameModel.game_question_counter += increment_value
        db.session.commit()

    @staticmethod
    def set_selected_option_to_true_by_user_id(user_id=user_id, option="A"):
        userBatikGameModel = UserBatikGameModel.query.filter_by(user_id=user_id).first()
        if option == 'A':
            userBatikGameModel.option_A = True
        elif option == 'B':
            userBatikGameModel.option_B = True
        elif option == 'C':
            userBatikGameModel.option_C = True
        elif option == 'D':
            userBatikGameModel.option_D = True
        db.session.commit()

    @staticmethod
    def reset_game_settings_by_user_id(user_id=user_id):
        userBatikGameModel = UserBatikGameModel.query.filter_by(user_id=user_id).first()
        userBatikGameModel.game_score = 0
        userBatikGameModel.game_question_counter = 1
        userBatikGameModel.option_A = False
        userBatikGameModel.option_B = False
        userBatikGameModel.option_C = False
        userBatikGameModel.option_D = False
        db.session.commit()

    @staticmethod
    def set_all_options_as_false_by_user_id(user_id=user_id):
        userBatikGameModel = UserBatikGameModel.query.filter_by(user_id=user_id).first()
        userBatikGameModel.option_A = False
        userBatikGameModel.option_B = False
        userBatikGameModel.option_C = False
        userBatikGameModel.option_D = False
        db.session.commit()

    @staticmethod
    def check_true_option_by_user_id(user_id=user_id, option="A"):
        userBatikGameModel = UserBatikGameModel.query.filter_by(user_id=user_id).first()
        if option == "A":
            return userBatikGameModel.option_A
        elif option == "B":
            return userBatikGameModel.option_B
        elif option == "C":
            return userBatikGameModel.option_C
        elif option == "D":
            return userBatikGameModel.option_D


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
        random_number = randint(1, tableEntityLength)

        fortuneTeller = FortuneTellerModel.query.filter_by(
            number=random_number
        ).first()

        return fortuneTeller.quote


class FlagGameQuestionsModel(db.Model):
    __tablename__ = "flag_game_questions"
    id_ = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country_flag_url = db.Column(db.Text(), nullable=False)
    country_name = db.Column(db.String(20), nullable=False)

    @staticmethod
    def get_flag_and_name_by_id(idInput):
        flagGameQuestionsModel = FlagGameQuestionsModel.query.filter_by(id_=idInput).first()
        return {
            "countryFlag": flagGameQuestionsModel.country_flag_url,
            "countryName": flagGameQuestionsModel.country_name
        }

    @staticmethod
    def get_flag_by_id(idInput):
        flagGameQuestionModel = FlagGameQuestionsModel.query.filter_by(id_=idInput).first()
        return flagGameQuestionModel.country_flag_url

    @staticmethod
    def get_name_by_id(idInput):
        flagGameQuestionsModel = FlagGameQuestionsModel.query.filter_by(id_=idInput).first()
        return flagGameQuestionsModel.country_name


class BatikGameQuestionsModel(db.Model):
    __tablename__ = "batik_game_questions"
    id_ = db.Column(db.Integer, primary_key=True, autoincrement=True)
    batik_image_url = db.Column(db.Text(), nullable=False)
    batik_name = db.Column(db.String(20), nullable=False)

    @staticmethod
    def get_batik_and_name_by_id(idInput):
        batikGameQuestionsModel = BatikGameQuestionsModel.query.filter_by(id_=idInput).first()
        return {
            "batikImage": batikGameQuestionsModel.batik_image_url,
            "batikName": batikGameQuestionsModel.batik_name
        }

    @staticmethod
    def get_batik_url_by_id(idInput):
        batikGameQuestionsModel = BatikGameQuestionsModel.query.filter_by(id_=idInput).first()
        return batikGameQuestionsModel.batik_image_url

    @staticmethod
    def get_batik_name_by_id(idInput):
        batikGamesQuestionsModel = BatikGameQuestionsModel.query.filter_by(id_=idInput).first()
        return batikGamesQuestionsModel.country_name


class RichMenuModel(db.Model):
    __tablename__ = "rich_menu_ids"
    id_ = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rich_menu_id = db.Column(db.String(41), nullable=False, unique=True)
    rich_menu_name = db.Column(db.String(40), nullable=False)
    rich_menu_desc = db.Column(db.String(300), nullable=False)

    @staticmethod
    def get_rich_menu_by_pk_id(richMenuId):
        richMenu = RichMenuModel.query.filter_by(
            id_=richMenuId
        ).first()

        return richMenu.rich_menu_id

    @staticmethod
    def get_rich_menu_by_name(richMenuName):
        richMenu = RichMenuModel.query.filter_by(
            rich_menu_name=richMenuName
        ).first()

        return richMenu.rich_menu_name
