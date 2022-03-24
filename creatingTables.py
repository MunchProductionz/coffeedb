import sqlite3

# Definerer Bruker-tabellen
bruker = '''CREATE TABLE IF NOT EXISTS Bruker(
                    BrukerID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Epostadresse TEXT UNIQUE,
                    Passord TEXT NOT NULL,
                    Fulltnavn TEXT NOT NULL
                )'''

# Definerer Brenneri-tabellen
brenneri = '''CREATE TABLE IF NOT EXISTS Brenneri(
                    Navn TEXT PRIMARY KEY,
                    Sted TEXT
                )'''

# Definerer Gård-tabellen
gård = '''CREATE TABLE IF NOT EXISTS Gård(
                    GårdID INTEGER PRIMARY KEY,
                    Navn TEXT,
                    Høyde TEXT,
                    Region TEXT NOT NULL,
                    Land TEXT NOT NULL
                )'''

# Definerer Kaffebønne-tabellen
kaffebønne = '''CREATE TABLE IF NOT EXISTS Kaffebønne(
                    Sort TEXT PRIMARY KEY,
                    Art TEXT NOT NULL
                )'''

# Definerer Foredlingsmetode-tabellen
foredlingsmetode = '''CREATE TABLE IF NOT EXISTS Foredlingsmetode(
                    Navn TEXT PRIMARY KEY,
                    Beskrivelse TEXT
                )'''

# Definerer Kaffeparti-tabellen
kaffeparti = '''CREATE TABLE IF NOT EXISTS Kaffeparti(
                    PartiID INTEGER PRIMARY KEY,
                    KiloprisUSD INTEGER,
                    Foredlingsmetode TEXT NOT NULL,
                    GårdID INTEGER NOT NULL,
                    FOREIGN KEY (Foredlingsmetode) REFERENCES Foredlingsmetode(Navn),
                    FOREIGN KEY (GårdID) REFERENCES Gård(GårdID)
                )'''

# Definerer Kaffe-tabellen
kaffe = '''CREATE TABLE IF NOT EXISTS Kaffe(
                    Brennerinavn TEXT,
                    Navn TEXT,
                    Brenningsgrad TEXT NOT NULL,
                    Brenningsdato DATE NOT NULL,
                    Beskrivelse TEXT,
                    KiloprisNOK INTEGER,
                    PartiID INTEGER NOT NULL,
                    PRIMARY KEY(Brennerinavn, Navn),
                    FOREIGN KEY (Brennerinavn) REFERENCES Brenneri(Navn)
                    FOREIGN KEY (PartiID) REFERENCES Kaffeparti(PartiID)
                )'''

# Definerer Kaffesmaking-tabellen
kaffesmaking = '''CREATE TABLE IF NOT EXISTS Kaffesmaking(
                    KaffesmakingID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Smaksnotat TEXT,
                    Poeng INTEGER NOT NULL,
                    Dato DATE,
                    BrukerID INTEGER,
                    Kaffenavn TEXT,
                    Brenneri TEXT,
                    FOREIGN KEY (BrukerID) REFERENCES Bruker(BrukerID),
                    FOREIGN KEY (Kaffenavn) REFERENCES Kaffe(Navn),
                    FOREIGN KEY (Brenneri) REFERENCES Brenneri(Brennerinavn)
                )'''

# Definerer DyrkesAv-tabellen
dyrkesAv = '''CREATE TABLE IF NOT EXISTS DyrkesAv(
                    GårdID INTEGER,
                    Bønnesort TEXT,
                    FOREIGN KEY (GårdID) REFERENCES Gård(GårdID),
                    FOREIGN KEY (Bønnesort) REFERENCES Kaffebønne(Sort)
                )'''

# Definerer DelAvParti-tabellen
delAvParti = '''CREATE TABLE IF NOT EXISTS DelAvParti(
                    PartiID INTEGER,
                    Bønnesort TEXT,
                    FOREIGN KEY (PartiID) REFERENCES Kaffeparti(PartiID),
                    FOREIGN KEY (Bønnesort) REFERENCES Kaffebønne(Sort)
                )'''


def buildTables():
    
    # Kobler til databasen og oppretter markør
    con = sqlite3.connect("test.db")
    cursor = con.cursor()

    # Dropper alle tabeller
    cursor.execute("DROP TABLE Bruker")
    cursor.execute("DROP TABLE Brenneri")
    cursor.execute("DROP TABLE Gård")
    cursor.execute("DROP TABLE Kaffebønne")
    cursor.execute("DROP TABLE Foredlingsmetode")
    cursor.execute("DROP TABLE Kaffeparti")         
    cursor.execute("DROP TABLE Kaffe")
    cursor.execute("DROP TABLE Kaffesmaking")
    cursor.execute("DROP TABLE DyrkesAv")
    cursor.execute("DROP TABLE DelAvParti")           
    print('Gamle tabeller har blitt fjernet.')


    # Bygger alle tabeller
    cursor.execute(bruker)
    cursor.execute(brenneri)
    cursor.execute(gård)
    cursor.execute(kaffebønne)
    cursor.execute(foredlingsmetode)
    cursor.execute(kaffeparti)          # Fremmed:  Foredlingsmetode, Gård
    cursor.execute(kaffe)               # Fremmed:  Brenneri, Kaffeparti
    cursor.execute(kaffesmaking)        # Fremmed:  Bruker, Kaffe, Brenneri
    cursor.execute(dyrkesAv)            # Fremmed:  Gård, Kaffebønne
    cursor.execute(delAvParti)          # Fremmed:  Kaffeparti, Kaffebønne 
    print('Nye tabeller har blitt bygd.')

    # Commiter endringen
    con.commit()

    # Lukker tilkoblingen
    con.close()