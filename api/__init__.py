from flask import Flask
from flask_cors import CORS
import db.setup as db


# con = sqlite3.connect("tutorial.db")
# cur = con.cursor()
# cur.execute("CREATE TABLE movie(title, year, score)")


app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return 'My First API !!'


@app.route('/movie', methods=['GET', 'POST'])
def test_write():
    movie = db.Movie("2", "2", "2")

    cursor, connection = db.connect()
    db.create_movie(cursor, movie)

    connection.commit()

    return movie.to_dict(), 200