import sqlite3
from creatingTables import buildTables

# Innsetting av verdier

# Tabell            Antall attributter
# Bruker            4
# Brenneri          2
# Gård              4
# Kaffebønne        2
# Foredlingsmetode  2
# Kaffeparti        5
# Kaffe             7
# Kaffesmaking      7
# DyrkesAv          2
# DelAvParti        2


def reset():

    # Kobler til databasen og oppretter markør
    con = sqlite3.connect("coffeeDB.db")
    cursor = con.cursor()


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
    print('Gamle verdier i tabellene er fjernet.')

    # Bruker
    cursor.execute('''INSERT INTO Bruker VALUES (1, 'bruker1@mail.com', '123', 'Bruker 1')''')
    cursor.execute('''INSERT INTO Bruker (Epostadresse, Passord, Fulltnavn) VALUES ('bruker2@mail.com', '456', 'Bruker 2')''')
    cursor.execute('''INSERT INTO Bruker (Epostadresse, Passord, Fulltnavn) VALUES ('bruker3@mail.com', '789', 'Bruker 3')''')
    cursor.execute('''INSERT INTO Bruker (Epostadresse, Passord, Fulltnavn) VALUES ('bruker4@mail.com', '111', 'Bruker 4')''')
    con.commit()

    # Brenneri
    cursor.execute('''INSERT INTO Brenneri VALUES ('Bergen Brenneri', 'Bergen')''')
    cursor.execute('''INSERT INTO Brenneri VALUES ('Oslo Brenneri', 'Oslo')''')
    cursor.execute('''INSERT INTO Brenneri VALUES ('Trondheim Brenneri', 'Trondheim')''')
    cursor.execute('''INSERT INTO Brenneri VALUES ('Jacobsen & Svart', 'Trondheim')''')
    con.commit()

    # Gård
    cursor.execute('''INSERT INTO Gård VALUES (1, 'Sagmo Gård', '1000', 'Bergen', 'Colombia')''')
    cursor.execute('''INSERT INTO Gård VALUES (2, 'Storvik Gård' , '2000', 'Oslo', 'Norge')''')
    cursor.execute('''INSERT INTO Gård VALUES (3, 'Bø Gård', '3000', 'Trondheim', 'Rwanda')''')
    cursor.execute('''INSERT INTO Gård VALUES (4, 'Nombre de Dios', '1500', 'Santa Ana', 'El Salvador')''')
    con.commit()

    # Kaffebønne
    cursor.execute('''INSERT INTO Kaffebønne VALUES ('Magnum', 'coffee arabica')''')
    cursor.execute('''INSERT INTO Kaffebønne VALUES ('Mocca', 'coffee robusta')''')
    cursor.execute('''INSERT INTO Kaffebønne VALUES ('Royal', 'coffee liberica')''')
    cursor.execute('''INSERT INTO Kaffebønne VALUES ('Bourbon', 'coffee arabica')''')
    con.commit()

    # Foredlingsmetode
    cursor.execute('''INSERT INTO Foredlingsmetode VALUES ('Bærtørket', 'Hengt til tørk')''')
    cursor.execute('''INSERT INTO Foredlingsmetode VALUES ('Vasket', 'Skylt i rist')''')
    cursor.execute('''INSERT INTO Foredlingsmetode VALUES ('Plukket', 'Hentet rett fra plantene')''')
    con.commit()

    # Kaffeparti
    cursor.execute('''INSERT INTO Kaffeparti VALUES (1, 2020, 10, 'Bærtørket', 1)''')
    cursor.execute('''INSERT INTO Kaffeparti VALUES (2, 2021, 20, 'Vasket', 2)''')
    cursor.execute('''INSERT INTO Kaffeparti VALUES (3, 2022, 30, 'Plukket', 3)''')
    cursor.execute('''INSERT INTO Kaffeparti VALUES (4, 2021, 8, 'Bærtørket', 4)''')
    con.commit()

    # Kaffe
    cursor.execute('''INSERT INTO Kaffe VALUES ('Bergen Brenneri', 'Nescafe', 'mørk', '2022-01-01', 'Helt ok', 100, 1)''')
    cursor.execute('''INSERT INTO Kaffe VALUES ('Oslo Brenneri', 'Espresso', 'middels', '2022-02-02', 'Middels god', 200, 2)''')
    cursor.execute('''INSERT INTO Kaffe VALUES ('Trondheim Brenneri', 'Evergood', 'lys', '2022-03-03', 'Ganske god, med en floral smak', 300, 3)''')
    cursor.execute('''INSERT INTO Kaffe VALUES ('Jacobsen & Svart', 'Vinterkaffe 2022', 'lys', '2022-01-20', 'En velsmakende og kompleks kaffe for mørketiden', 600, 4)''')
    con.commit()

    # Kaffesmaking
    cursor.execute('''INSERT INTO Kaffesmaking (Smaksnotat,Poeng,Dato,BrukerID,Kaffenavn,Brenneri) VALUES ('Grei kvalitet', 3, '2022-01-02', 1, 'Nescafe', 'Bergen Brenneri')''')
    cursor.execute('''INSERT INTO Kaffesmaking (Smaksnotat,Poeng,Dato,BrukerID,Kaffenavn,Brenneri) VALUES ('Smakfulle bønner', 6, '2022-02-03', 2, 'Espresso', 'Oslo Brenneri')''')
    cursor.execute('''INSERT INTO Kaffesmaking (Smaksnotat,Poeng,Dato,BrukerID,Kaffenavn,Brenneri) VALUES ('Gode bønner', 4, '2022-02-03', 2, 'Espresso', 'Oslo Brenneri')''')
    cursor.execute('''INSERT INTO Kaffesmaking (Smaksnotat,Poeng,Dato,BrukerID,Kaffenavn,Brenneri) VALUES ('Ganske grei kvalitet', 5, '2022-02-03', 2, 'Nescafe', 'Bergen Brenneri')''')
    cursor.execute('''INSERT INTO Kaffesmaking (Smaksnotat,Poeng,Dato,BrukerID,Kaffenavn,Brenneri) VALUES ('Bemerkelsesverdig smak', 9, '2021-03-04', 3, 'Evergood', 'Trondheim Brenneri')''')
    cursor.execute('''INSERT INTO Kaffesmaking (Smaksnotat,Poeng,Dato,BrukerID,Kaffenavn,Brenneri) VALUES ('Wow - en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!', 10, '2022-03-21', 4, 'Vinterkaffe 2022', 'Jacobsen & Svart')''')
    con.commit()

    # DyrkesAv
    cursor.execute('''INSERT INTO DyrkesAv VALUES (1, 'Magnum')''')
    cursor.execute('''INSERT INTO DyrkesAv VALUES (2, 'Mocca')''')
    cursor.execute('''INSERT INTO DyrkesAv VALUES (3, 'Royal')''')
    con.commit()

    # DelAvParti
    cursor.execute('''INSERT INTO DelAvParti VALUES (1, 'Magnum')''')
    cursor.execute('''INSERT INTO DelAvParti VALUES (2, 'Mocca')''')
    cursor.execute('''INSERT INTO DelAvParti VALUES (3, 'Royal')''')
    con.commit()

    print('Nye verdier er lagt til i tabellene.')

    # Lukker tilkoblingen
    con.close()


def rebuild():

    # Bygger nye tabeller
    buildTables()

    # Setter inn standard-data
    reset()

    print('Tabellene er ferdig gjenopprettet.')

#reset()
# rebuild()