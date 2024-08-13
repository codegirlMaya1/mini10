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


#database , filename
app.config['SQLALCHEMY_DATABASE_URI']="mysql+mysqlconnector://root:S05071984@127.0.0.1/gym_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#init db
db = SQLAlchemy(app)
#init ma
ma = Marshmallow(app)
#Product model/class

class Member(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(255), unique=True)
    age         = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name        = name
        self.age         = age

# Product Schema
class MemberSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'age')

# init schema
member_schema  = MemberSchema()
members_schema = MemberSchema(many=True) 

#Show members
@app.route('/member1', methods=['GET'])
def show_member():
    try:
        members_schema.load(request.json)
        id         = request.json['id']
        name       = request.json['name']
        age        = request.json['age']
        new_member = Member(id, name, age)
        member=new_member.query.all()
        return members_schema.jsonify(member)
    except ValidationError as e:
        print(f" Error: {e}")
    

#create a member
@app.route('/member', methods=['POST'])
def add_member():
    
    id         = request.json['id']
    name       = request.json['name']
    age        = request.json['age']
    new_member = Member(id, name, age)
    
    db.session.add(new_member)
    db.session.commit()
    return member_schema.jsonify(new_member)
print("new member added")





     
with app.app_context():
    db.create_all()
         
if __name__=='__main__':
        app.run()
        
     