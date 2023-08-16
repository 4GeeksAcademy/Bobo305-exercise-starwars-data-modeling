import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template, request, redirect, url_for

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
           'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)



class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    username=db.Column(db.String(250), unique = True, nullable = False )
    password = db.Column(db.String(250), nullable = False)
    favorite_Character = db.Column(db.String(250))
    favorite_Planets = db.Column(db.String(250))


class Character(db.Model):
    __tablename__ = 'Character'
    id = db.Column(db.Integer, primary_key = True)
    name =db.Column(db.String(250), ForeignKey('Favorite.Character'), unique = True, nullable = False )
    birth_year = db.Column(db.Integer, nullable = False)
    homeworld = db.Column(db.String(250), nullable =False)
    skin_Color = db.Column(db.String(250), nullable =False )
    eye_Color = db.Column(db.String(250), nullable =False )
    mass = db.Column(db.Integer, nullable =False )
    height = db.Column(db.Integer, nullable =False )


class Planets(db.Model):
    __tablename__ = 'Planets'
    id = db.Column(db.Integer, primary_key = True)
    name =db.Column(db.String(250),ForeignKey('Favorite.Planet'), unique = True, nullable = False)
    Population = db.Column(db.Integer, nullable =False)
    Terrain = db.Column(db.Integer, nullable =False)
    Diameter = db.Column(db.Integer, nullable =False) 
    

class Favorites(db.Model):
    __tablename__ = 'Favorite'
    id = db.Column(db.Integer, primary_key = True)
    Planet =db.Column(db.String(250), ForeignKey('user.favorite_Planets'), unique = True, nullable = False)
    Character =db.Column(db.String(250), ForeignKey('user.favorite_Character'),unique = True, nullable = False)



        



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(db, 'diagram.png')
