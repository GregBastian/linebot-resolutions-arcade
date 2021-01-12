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

class UserArcade(db.Model):
    __tablename__ = "user_ektp"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.String(33), nullable=False, unique=True)

    jenisKartu = db.Column(db.String(10), nullable=False)
    nomorKartu = db.Column(db.String(20), nullable=False)
    nama = db.Column(db.String(60), nullable=False)
    tglLahir = db.Column(db.String(60), nullable=False)
    gambarKartu = db.Column(db.Text(), nullable=False)
    isVerified = db.Column(db.String(255), nullable=False)
    kategoriUser = db.Column(db.String(45), nullable=False)
    dateCreated = db.Column(db.DateTime, nullable=False, default=datetime.now)
    dateLastModified = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __init__(self, nomorHape, jenisKartu, nomorKartu,
                 nama, tglLahir, gambarKartu, isVerified,
                 kategoriUser):
        self.nomorHape = nomorHape
        self.jenisKartu = jenisKartu
        self.nomorKartu = nomorKartu
        self.nama = nama
        self.tglLahir = tglLahir
        self.gambarKartu = gambarKartu
        self.isVerified = isVerified
        self.kategoriUser = kategoriUser

    def as_dict(self):
        return {
            attribute.name:
                getattr(self, attribute.name) for attribute in self.__table__.columns
        }
