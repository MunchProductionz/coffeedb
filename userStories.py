import sqlite3

# Kobler til databasen
con = sqlite3.connect("test.db")

# Oppretter markør - Du bruker den til å kjøre queries
cursor = con.cursor()


# Spørringer
cursor.execute("SELECT * FROM Kaffesmaking")
print(cursor.fetchall())

# Brukerhistorie 1




# Brukerhistorie 2
# cursor.execute('''SELECT Navn, Smakinger
#                     FROM (SELECT COUNT(BrukerID) AS Smakinger, Kaffenavn, Brennerinavn
#                         FROM Kaffesmaking
#                         GROUP BY BrukerID)
#                     JOIN
#                         (SELECT BrukerID AS ID, Navn
#                         FROM Bruker)
#                     ON
#                     BrukerID = ID
#                     ORDER BY Smakinger DESC
#                 ''')
# print(cursor.fetchall())

# Brukerhistorie 3
# cursor.execute('''''')
# print(cursor.fetchall())


# Brukerhistorie 4
# cursor.execute('''SELECT Kaffenavn, Brenneri
#                     FROM (SELECT *
#                         FROM Kaffesmaking
#                         WHERE Smaksnotat LIKE “%floral%”)
#                     JOIN
#                         (SELECT *
#                         FROM Kaffe
#                         WHERE Beskrivelse LIKE “%floral%”)
#                     ON 
#                         Kaffenavn = Navn AND Kaffesmaking.Brenneri = Kaffe.Brenneri
#                 ''')
# print(cursor.fetchall())



# Brukerhistorie 5
# cursor.execute('''SELECT Brennerinavn, Kaffenavn
#                     FROM (SELECT PartiID
#                             FROM (SELECT *
#                                     FROM Gård
#                                         WHERE Land = Rwanda OR Land = Colombia)
#                                         JOIN
#                                         (SELECT * 
#                                         FROM Kaffeparti
#                                         WHERE NOT IN (SELECT * FROM Kaffeparti WHERE Foredlingsmetode = “Vasket”)
#                             )
#                             ON
#                             Gård.GårdID = Kaffepart.GårdID
#                         )
#                         NATURAL JOIN
#                         Kaffe
#                 ''')
# print(cursor.fetchall())





# Commiter endringen
con.commit()

# Lukker tilkoblingen
con.close()