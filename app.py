from flask import Flask
import sqlite3


app = Flask(__name__)

@app.route('/')
def index():
    addScore('mikkel',1)
    addScore('martin',3)
    return_string = '\n'.join([name + ': ' + str(score) for name,score in getScores()])
    return return_string

def addScore(name,score): 
    database_connection = sqlite3.connect('snake.db')
    database_cursor = database_connection.cursor()
    sql_string = f"INSERT INTO highscores VALUES ('{name}', {score});"
    database_cursor.execute(sql_string)
    database_connection.commit()
    database_connection.close()

def getScores():
    database_connection = sqlite3.connect('snake.db')
    database_cursor = database_connection.cursor()
    sql_string = 'SELECT human_name,score FROM highscores ORDER BY score DESC;'
    database_cursor.execute(sql_string)
    top5 = database_cursor.fetchall()[:5]
    database_connection.close()
    return top5