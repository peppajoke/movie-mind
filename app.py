from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
 
 # endpoints:
 # log watched movie input: movie_id, user_id, love|like|hate
 # get recs input: (optional) genre scary|funny|cool|serious

 # TMDB
 # ask for popular or whatever other "good" movies
 # index all data by id into source of truth database
 # 