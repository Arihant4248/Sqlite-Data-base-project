import sqlite3
con = sqlite3.connect('Movies.db')
print("Database connected....")
cur=con.cursor()
cur.execute("CREATE TABLE Favourite_Movies(Moviename TEXT NOT NULL,Year INTEGER NOT NULL,Actorname TEXT NOT NULL,Actressname TEXT NOT NULL,Directorname TEXT NOT NULL)")
print("Table created...")