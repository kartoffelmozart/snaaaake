import sqlite3

con = sqlite3.connect("snake.db")
cur = con.cursor()


cur.execute('DROP TABLE IF EXISTS highscores;')
cur.execute(
'''
CREATE TABLE highscores (
    human_name VARCHAR(15),
    score INT
);
'''
)
con.close()