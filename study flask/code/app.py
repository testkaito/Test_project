from flask import Flask
from flask import Blueprint, render_template
# from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

app = Flask(__name__)

#Base.html　: 初期設定Config
#index.html : Homeのページ
#create.html : 新規登録画面

# Create BD
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

#SetUp DB
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime,nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))

#Main
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create')
def create():
    return render_template('create.html')












# @app.route("/<city>")
# def hello_world(city):
#     return f'<p>this is {city}<p>'


# @app.route('/mozi_new/<city>')
# def Mozi_new(city):
#     return  render_template('test.html', city=city)