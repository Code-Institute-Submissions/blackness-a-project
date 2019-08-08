import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import datetime


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'Blackness'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_heros')
def get_heros():
    return render_template("hero.html", heros=mongo.db.local_heros.find())
    

@app.route('/get_famous')
def get_famous():
    return render_template("famous.html", famous=mongo.db.Persons_of_Interest.find())
    


@app.route('/get_index')
def get_index():
    return render_template("index.html", famous=mongo.db.local_heros.find())

    
    
@app.route('/add_hero')
def add_hero():
    return render_template('add_hero.html', heros=mongo.db.local_heros.find(), date=datetime.datetime.today())
    

@app.route('/insert_hero', methods=['POST'])
def insert_hero():
    hero = mongo.db.local_heros
    hero.insert_one(request.form.to_dict())
    return redirect(url_for('get_heros'))



@app.route('/get_art')
def get_art():
    return render_template("gallery.html", famous=mongo.db.Persons_of_Interest.find())
    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)