from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///idleize.db'
db = SQLAlchemy(app)

class Game(db.Model):
    game_id = db.Column(db.Integer, primary_key=True)
    game_title = db.Column(db.String(255), nullable=False)
    max_players = db.Column(db.Integer, default = 2)

class GameInstance(db.Model):
    game_code = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, foreign_key = ) # NEED TO ADD FOREIGN KEY TO GAME
    num_players = db.Column(db.Integer)

class Player(db.Model):
    username = db.Column(db.String(255), primary_key=True)
    lat = db.Column(db.Real, default = 0)
    lon = db.Column(db.Real, default = 0)
    game_code = db.Column(db.Integer) # NEED TO ADD FOREIGN KEY TO GAMEiNSTANCE


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)