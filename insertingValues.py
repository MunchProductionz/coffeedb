import sqlite3

# Kobler til databasen
con = sqlite3.connect("test.db")

# Oppretter markør - Du bruker den til å kjøre queries
cursor = con.cursor()


# Innsetting av verdier

# Tabell            Antall attributter
# Bruker            4
# Brenneri          2
# Gård              4
# Kaffebønne        2
# Foredlingsmetode  2
# Kaffeparti        4
# Kaffe             7
# Kaffesmaking      7
# DyrkesAv          2
# DelAvParti        2


# Fjern gamle verdier
cursor.execute("DELETE FROM Bruker")
cursor.execute("DELETE FROM Brenneri")
cursor.execute("DELETE FROM Gård")
cursor.execute("DELETE FROM Kaffebønne")
cursor.execute("DELETE FROM Foredlingsmetode")
cursor.execute("DELETE FROM Kaffeparti")
cursor.execute("DELETE FROM Kaffe")
cursor.execute("DELETE FROM Kaffesmaking")
cursor.execute("DELETE FROM DyrkesAv")
cursor.execute("DELETE FROM DelAvParti")
con.commit()


# Bruker
# cursor.execute('''INSERT INTO Bruker VALUES (1, 'bruker1@mail.com', '123', 'Bruker 1')''')
# cursor.execute('''INSERT INTO Bruker VALUES (2, 'bruker2@mail.com', '456', 'Bruker 2')''')
# cursor.execute('''INSERT INTO Bruker VALUES (3, 'bruker3@mail.com', '789', 'Bruker 3')''')
cursor.execute('''INSERT INTO Bruker VALUES (4, 'bruker4@mail.com', '111', 'Bruker 4')''')
con.commit()

# Brenneri
# cursor.execute('''INSERT INTO Brenneri VALUES ('Bergen Brenneri', 'Bergen')''')
# cursor.execute('''INSERT INTO Brenneri VALUES ('Oslo Brenneri', 'Oslo')''')
# cursor.execute('''INSERT INTO Brenneri VALUES ('Trondheim Brenneri', 'Trondheim')''')
cursor.execute('''INSERT INTO Brenneri VALUES ('Jacobsen & Svart', 'Trondheim')''')
con.commit()

# Gård
# cursor.execute('''INSERT INTO Gård VALUES (1, '1000', 'Bergen', 'Norge')''')
# cursor.execute('''INSERT INTO Gård VALUES (2, '2000', 'Oslo', 'Norge')''')
# cursor.execute('''INSERT INTO Gård VALUES (3, '3000', 'Trondheim', 'Norge')''')
cursor.execute('''INSERT INTO Gård VALUES (4, '1500', 'Santa Ana', 'El Salvador')''')
con.commit()

# Kaffebønne
# cursor.execute('''INSERT INTO Kaffebønne VALUES ('Magnum', 'coffea arabica')''')
# cursor.execute('''INSERT INTO Kaffebønne VALUES ('Mocca', 'coffea robusta')''')
# cursor.execute('''INSERT INTO Kaffebønne VALUES ('Royal', 'coffea liberica')''')
cursor.execute('''INSERT INTO Kaffebønne VALUES ('Bourbon', 'coffea arabica')''')
con.commit()

# Foredlingsmetode
# cursor.execute('''INSERT INTO Foredlingsmetode VALUES ('Bærtørket', 'Hengt til tørk')''')
# cursor.execute('''INSERT INTO Foredlingsmetode VALUES ('Vasket', 'Skylt i rist')''')
# cursor.execute('''INSERT INTO Foredlingsmetode VALUES ('Plukket', 'Hentet rett fra plantene')''')
cursor.execute('''INSERT INTO Foredlingsmetode VALUES ('Bærtørket', '')''')
con.commit()

# Kaffeparti
# cursor.execute('''INSERT INTO Kaffeparti VALUES (1, 10, 'Bærtørket', 1)''')
# cursor.execute('''INSERT INTO Kaffeparti VALUES (2, 20, 'Vasket', 2)''')
# cursor.execute('''INSERT INTO Kaffeparti VALUES (3, 30, 'Plukket', 3)''')
cursor.execute('''INSERT INTO Kaffeparti VALUES (4, 8, 'Bærtørket', 4)''')
con.commit()

# Kaffe
# cursor.execute('''INSERT INTO Kaffe VALUES ('Bergen Brenneri', 'Nescafe', 'mørk', '2022-01-01', 'Helt ok', 100, 1)''')
# cursor.execute('''INSERT INTO Kaffe VALUES ('Oslo Brenneri', 'Espresso', 'middels', '2022-02-02', 'Middels god', 200, 2)''')
# cursor.execute('''INSERT INTO Kaffe VALUES ('Trondheim Brenneri', 'Evergood', 'lys', '2022-03-03', 'Ganske god', 300, 3)''')
cursor.execute('''INSERT INTO Kaffe VALUES ('Jacobsen & Svart', 'Vinterkaffe 2022', 'lys', '2022-01-20', 'En velsmakende og kompleks kaffe for mørketiden', 600, 4)''')
con.commit()

# Kaffesmaking
# cursor.execute('''INSERT INTO Kaffesmaking VALUES (1, 'Grei kvalitet', 3, '2022-01-02', 1, 'Nescafe', 'Bergen Brenneri')''')
# cursor.execute('''INSERT INTO Kaffesmaking VALUES (2, 'Smakfulle bønner', 6, '2022-02-03', 2, 'Espresso', 'Oslo Brenneri')''')
# cursor.execute('''INSERT INTO Kaffesmaking VALUES (3, 'Bemerkelsesverdig smak', 9, '2022-03-04', 3, 'Evergood', 'Trondheim Brenneri')''')
cursor.execute('''INSERT INTO Kaffesmaking VALUES (4, 'Wow - en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!', 10, '2022-03-21', 4, 'Vinterkaffe 2022', 'Jacobsen & Svart')''')
con.commit()

# DyrkesAv
# cursor.execute('''INSERT INTO DyrkesAv VALUES (1, 'Magnum')''')
# cursor.execute('''INSERT INTO DyrkesAv VALUES (2, 'Mocca')''')
# cursor.execute('''INSERT INTO DyrkesAv VALUES (3, 'Royal')''')
# con.commit()

# DelAvParti
# cursor.execute('''INSERT INTO DelAvParti VALUES (1, 'Magnum')''')
# cursor.execute('''INSERT INTO DelAvParti VALUES (2, 'Mocca')''')
# cursor.execute('''INSERT INTO DelAvParti VALUES (3, 'Royal')''')
# con.commit()


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