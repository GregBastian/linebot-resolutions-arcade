# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 18:16:43 2020

@author: Gregorius Ivan Sebastian
@email: ivansebastian60@gmail.com
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


# ==!! IMPORTANT !!==
# If you modified the table design in the database please make sure that you
# edit this class accordingly and vice-versa

class ExtendedModel(db.Model):

    @classmethod
    def as_dict(cls):
        return {
            attribute.name:
                getattr(cls, attribute.name) for attribute in cls.__table__.columns
        }


class ArcadeUserModel(ExtendedModel):
    __tablename__ = "user_arcade"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(33), nullable=False, unique=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    is_playing_game = db.Column(db.String(25), nullable=False)
    flag_game_score = db.Column(db.String(2), nullable=True)

    def __init__(self, id, user_id, date_created):
        self.id = id
        self.user_id = user_id
        self.date_created = date_created
