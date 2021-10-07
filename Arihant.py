import sqlite3
con = sqlite3.connect('Movies.db')
print("Database connected....")
cur=con.cursor()
cur.execute("INSERT INTO Favourite_Movies(Moviename,Year,Actorname,Actressname,Directorname) VALUES('San Andreas',2015,'Dwayne Johnson','Carla Gugino','Brad Peyton')")
cur.execute("INSERT INTO Favourite_Movies(Moviename,Year,Actorname,Actressname,Directorname) VALUES('3idiots',2009,'Amirkhan','Kareena Kapoor','Rajkumar Hirani')")
cur.execute("INSERT INTO Favourite_Movies(Moviename,Year,Actorname,Actressname,Directorname) VALUES('Shershaah',2021,'Sidharth Malhotra','Kiara Advani','Vishnuvardhan')")
cur.execute("INSERT INTO Favourite_Movies(Moviename,Year,Actorname,Actressname,Directorname) VALUES('The Mechanic',2015,'Jason Statham','Mini Anden',' Simon West')")
cur.execute("INSERT INTO Favourite_Movies(Moviename,Year,Actorname,Actressname,Directorname) VALUES('Commando 3',2019,'Vidyut Jammwal','Adah Sharma','Aditya datt')")
cur.execute("INSERT INTO Favourite_Movies(Moviename,Year,Actorname,Actressname,Directorname) VALUES('Skyscraper',2018,' Dwayne Johnson','Neve Campbell','Rawson Marshall Thurber')")
cur.execute("INSERT INTO Favourite_Movies(Moviename,Year,Actorname,Actressname,Directorname) VALUES('Iron Man',2008,'Robert Downey Jr.','Gwyneth Paltrow','Jon Favreau')")
print("data inserted....")
print("Moviename\t ,Year\t ,Actorname\t ,Actressname\t ,Directorname\n")
cursor=cur.execute("SELECT * FROM Favourite_Movies");
for row in cursor:
    print(row[0], "\t",row[1], "\t",row[2], "\t",row[3],"\t",row[4], "\n")
con.close()