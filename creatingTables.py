import sqlite3

# Kobler til databasen
con = sqlite3.connect("test.db")

# Oppretter markør - Du bruker den til å kjøre queries
cursor = con.cursor()

# Definerer Bruker-tabellen
bruker = '''CREATE TABLE Bruker(
                    BrukerID INTEGER PRIMARY KEY,
                    Epostadresse TEXT,
                    Passord TEXT,
                    Fulltnavn TEXT,
                    FOREIGN KEY (KaffesmakingID) REFERENCES Kaffesmaking(KaffesmakingID)
                )'''

# Definerer Kaffesmaking-tabellen
kaffesmaking = '''CREATE TABLE Kaffesmaking(
                    KaffesmakingID INTEGER PRIMARY KEY,
                    Smaksnotater TEXT,
                    AntallPoeng INTEGER,
                    Smaksdato TEXT,
                    FOREIGN KEY (BrukerID) REFERENCES Bruker(BrukerID)
                )'''

# Definerer Kaffe-tabellen
kaffe = '''CREATE TABLE Kaffe(
                    KaffeID INTEGER PRIMARY KEY,
                    Brenningsgrad TEXT,
                    Brenningsdato TEXT,
                    Navn TEXT,
                    Beskrivelse TEXT,
                    Kilopris INTEGER,
                    FOREIGN KEY (KaffepartiID) REFERENCES Kaffeparti(KaffepartiID)
                )'''

# Definerer Kaffeparti-tabellen
kaffeparti = '''CREATE TABLE Kaffeparti(
                    KaffepartiID INTEGER PRIMARY KEY,
                    KiloprisGård INTEGER,
                    FOREIGN KEY (GårdID) REFERENCES Gård(GårdID),
                    FOREIGN KEY (ForedlingsmetodeID) REFERENCES Foredlingsmetode(ForedlingsmetodeID)
                )'''

# Definerer Foredlingsmetode-tabellen
foredlingsmetode = '''CREATE TABLE Foredlingsmetode(
                    ForedlingsmetodeID INTEGER PRIMARY KEY,
                    Navn TEXT,
                    Beskrivelse TEXT
                )'''

# Definerer Kaffebønne-tabellen
kaffebønne = '''CREATE TABLE Kaffebønne(
                    KaffebønneID INTEGER PRIMARY KEY,
                    Art TEXT,
                    Grense INTEGER
                )'''

# Definerer Gård-tabellen
gård = '''CREATE TABLE Gård(
                    GårdID INTEGER PRIMARY KEY,
                    Land TEXT,
                    Region TEXT,
                    HøydeOverHavet TEXT
                )'''

# Definerer LagesAv-tabellen
lagesAv = '''CREATE TABLE LagesAv(
                    FOREIGN KEY (KaffeID) REFERENCES Kaffe(KaffeID),
                    FOREIGN KEY (KaffepartiID) REFERENCES Kaffeparti(KaffepartiID)
                )'''

# Definerer Produksjon-tabellen
produksjon = '''CREATE TABLE Produksjon(
                    FOREIGN KEY (KaffepartiID) REFERENCES Kaffeparti(KaffepartiID),
                    FOREIGN KEY (KaffebønneID) REFERENCES Kaffebønne(KaffebønneID),
                    FOREIGN KEY (ForedlingsmetodeID) REFERENCES Foredlingsmetode(ForedlingsmetodeID)
                )'''

# Definerer DyrkesAv-tabellen
dyrkesAv = '''CREATE TABLE DyrkesAv(
                    FOREIGN KEY (GårdID) REFERENCES Gård(GårdID),
                    FOREIGN KEY (KaffebønneID) REFERENCES Kaffebønne(KaffebønneID)
                )'''


# Lager tabeller
cursor.execute(bruker)              # Fremmed:  KaffesmakingID
cursor.execute(kaffesmaking)        # Fremmed:  BrukerID
cursor.execute(kaffe)               # Fremmed:  KaffepartiID
cursor.execute(kaffeparti)          # Fremmed:  GårdID, ForedlingsmetodeID
cursor.execute(foredlingsmetode)  
cursor.execute(kaffebønne)
cursor.execute(gård)
cursor.execute(lagesAv)             # Fremmed:  KaffeID, KaffepartiID
cursor.execute(produksjon)          # Fremmed:  KaffepartiID, KaffebønneID, ForedlingsmetodeID
cursor.execute(dyrkesAv)            # Fremmed:  GårdID, KaffebønneID


# Commiter endringen
con.commit()

# Lukker tilkoblingen
con.close()