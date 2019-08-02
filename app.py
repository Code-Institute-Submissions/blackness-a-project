import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'Blackness'
app.config["MONGO_URI"] = os.getenv('MONGO_URI',)

@app.route('/')
def hello():
    return 'Hello world'
    
if __name__== '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)