import os
import mysql.connector
from mysql.connector import Error
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields
from marshmallow import ValidationError



db_name="gym_db"
user="root"
password="S05071984"
host="127.0.0.1"

# init app
app = Flask(__name__)
conn=mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
        )


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql+mysqlconnector://root:S05071984@127.0.0.1/admin_db"
ma=Marshmallow(app)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

class Members(db.Model):
    __tablename__='members'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255))
    age=db.Column(db.String)
    workoutsession=db.relationship('workoutsessions', backref=("members"))
    
    class WorkoutSessions(db.Model):
     __tablename__='workoutsessions'
     session_id=db.Column(db.Integer,primary_key=True)
     member_id=db.Column(db.Integer)
     session_date=db.Column(db.Date)
     session_time=db.Column(db.String)
     activity=db.Column(db.String(255))
     id=db.Column(db.Integer)
     


class MembersSchema(ma.Schema):
    id = fields.String(required=True)
    name= fields.String(required =True)
    age=fields.String(required=True)
    
    class Meta:
        fields = ('id', 'name', 'age')
    
member_schema = MembersSchema()
members_schema = MembersSchema(many=True)

@app.route('/members', methods=['GET']) #http://127.0.0.1:5000/members
def get_members():
         member_data=member_schema.load(request.json)
         new_member=(member_data['id'], member_data['name'], member_data['age'])
         member=new_member.query.all()
         db.session.add(new_member)
         db.session.commit()
         print("New member added")
         return members_schema.jsonify(member)
       
    

