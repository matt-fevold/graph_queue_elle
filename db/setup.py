import sqlite3

# cursor.execute("insert into people values (?, ?)", (who, age))

class Movie:
    def __init__(self, title, year, score):
        self.title = title
        self.year = year
        self.score = score

    def to_dict(self):
        return {
            "title": self.title,
            "year": self.year,
            "score": self.score,
        }

def connect():
    connection = sqlite3.connect("tutorial.db")
    cursor = connection.cursor()
    return cursor, connection

# if __name__ == '__main__':
#
#     cursor = connect()
#

def create_test_table(cursor):
    cursor.execute("CREATE TABLE movie(title, year, score)")

def create_movie(cursor, movie):
    cursor.execute("insert into movie(title, year, score) values (?,?,?)", (movie.title, movie.year, movie.score))
