import sqlite3

# Kobler til databasen
con = sqlite3.connect("test.db")

# Oppretter markør - Du bruker den til å kjøre queries
cursor = con.cursor()

# Definerer Bruker-tabellen
cursor.execute('''CREATE TABLE IF NOT EXISTS bruker
                    (BrukerID INTEGER PRIMARY KEY,
                    Epost TEXT,
                    Passord TEXT,
                    FulltNavn TEXT
                    )''')

bruker = '''CREATE TABLE Bruker(
                    BrukerID INTEGER PRIMARY KEY,
                    Epost TEXT,
                    Passord TEXT,
                    Fulltnavn TEXT,
                    FOREIGN KEY (KaffesmakingID) REFERENCES Kaffesmaking(KaffesmakingID)
                )'''

# Definerer Kaffesmaking-tabellen
cursor.execute('''CREATE TABLE IF NOT EXISTS Kaffesmaking
                    (KaffesmakingID INTEGER PRIMARY KEY,
                    Smaksnotat TEXT,
                    Poeng INTEGER NOT NULL,
                    Dato DATE DEFAULT NOW(), # Usikker på NOW() her
                    BrukerID INTEGER,
                    Kaffenavn TEXT,
                    Brennerinavn TEXT,
                    FOREIGN KEY (BrukerID) REFERENCES Bruker(BrukerID),
                    FOREIGN KEY (Kaffenavn) REFERENCES Kaffe(Navn),
                    FOREIGN KEY (Brennerinavn) REFERENCES Kaffe(Brennerinavn))''')


kaffesmaking = '''CREATE TABLE Kaffesmaking(
                    KaffesmakingID INTEGER PRIMARY KEY,
                    Smaksnotater TEXT,
                    AntallPoeng INTEGER,
                    Smaksdato TEXT,
                    FOREIGN KEY (BrukerID) REFERENCES Bruker(BrukerID)
                )'''

# Definerer Kaffe-tabellen
cursor.execute('''CREATE TABLE IF NOT EXISTS Kaffe
                    (Brennerinavn TEXT,
                    Navn TEXT,
                    Brenningsgrad TEXT NOT NULL,
                    Brenningsdato DATE NOT NULL,
                    Beskrivelse TEXT,
                    KiloprisNOK INTEGER,
                    PartiID INTEGER,
                    FOREIGN KEY (Brennerinavn) REFERENCES Brenneri(Navn),
                    FOREIGN KEY (PartiID) REFERENCES Kaffeparti(PartiID))''')


kaffe = '''CREATE TABLE Kaffe(
                    KaffeID INTEGER PRIMARY KEY,
                    Brenningsgrad TEXT,
                    Brenningsdato TEXT,
                    Navn TEXT,
                    Beskrivelse TEXT,
                    Kilopris INTEGER,
                    FOREIGN KEY (KaffepartiID) REFERENCES Kaffeparti(KaffepartiID)
                )'''

#Definerer Brenneri-tabellen
cursor.execute('''CREATE TABLE IF NOT EXISTS Brenneri(
                    Navn TEXT,
                    Sted TEXT,))''')


# Definerer Kaffeparti-tabellen
cursor.execute('''CREATE TABLE IF NOT EXISTS Kaffeparti
                    (PartiID INTEGER,
                    Innhøstingsår YEAR,
                    KiloprisUSD INTEGER,
                    Foredlingsmetode TEXT,
                    GårdID INTEGER,
                    FOREIGN KEY (GårdID) REFERENCES Gård(GårdID),
                    FOREIGN KEY (Foredlingsmetode) REFERENCES Foredlingsmetode(Navn))''')


kaffeparti = '''CREATE TABLE Kaffeparti(
                    KaffepartiID INTEGER PRIMARY KEY,
                    KiloprisGård INTEGER,
                    FOREIGN KEY (GårdID) REFERENCES Gård(GårdID),
                    FOREIGN KEY (ForedlingsmetodeID) REFERENCES Foredlingsmetode(ForedlingsmetodeID)
                )'''

# Definerer Foredlingsmetode-tabellen
cursor.execute('''CREATE TABLE IF NOT EXISTS Foredlingsmetode(
                    Navn TEXT,
                    Beskrivelse TEXT,))''')



foredlingsmetode = '''CREATE TABLE Foredlingsmetode(
                    ForedlingsmetodeID INTEGER PRIMARY KEY,
                    Navn TEXT,
                    Beskrivelse TEXT
                )'''

# Definerer Kaffebønne-tabellen
cursor.execute('''CREATE TABLE IF NOT EXISTS Kaffebønne(
                    Sort TEXT,
                    Art TEXT NOT NULL,))''')


kaffebønne = '''CREATE TABLE Kaffebønne(
                    KaffebønneID INTEGER PRIMARY KEY,
                    Art TEXT,
                    Grense INTEGER
                )'''

# Definerer Gård-tabellen
cursor.execute('''CREATE TABLE IF NOT EXISTS Gård(
                    GårdID INT,
                    NAVN TEXT,
                    Høyde INT,
                    Region TEXT NOT NULL,
                    Land TEXT NOT NULL))''')


gård = '''CREATE TABLE Gård(
                    GårdID INTEGER PRIMARY KEY,
                    Land TEXT,
                    Region TEXT,
                    HøydeOverHavet TEXT
                )'''


# Definerer DyrkesAv-tabellen
cursor.execute('''CREATE TABLE IF NOT EXISTS DyrkesAv(
                    GårdID INT,
                    Bønnesort TEXT, HER STÅR DET INT I SQL-FILA!
                    FOREIGN KEY (GårdID) REFERENCES Gård(GårdID),
                    FOREIGN KEY (Bønnesort) REFERENCES Bønne(Sort))''')




dyrkesAv = '''CREATE TABLE DyrkesAv(
                    FOREIGN KEY (GårdID) REFERENCES Gård(GårdID),
                    FOREIGN KEY (KaffebønneID) REFERENCES Kaffebønne(KaffebønneID)
                )'''

# Definerer DelAVParti-tabellen
cursor.execute('''CREATE TABLE IF NOT EXISTS DelAVParti(
                    PartiID INTEGER,
                    Bønnesort TEXT,
                    FOREIGN KEY (GårdID) REFERENCES Gård(GårdID),
                    FOREIGN KEY (Bønnesort) REFERENCES Bønne(Sort))''')


# Lager tabeller
cursor.execute(bruker)              # Fremmed:  KaffesmakingID
cursor.execute(kaffesmaking)        # Fremmed:  BrukerID
cursor.execute(kaffe)               # Fremmed:  KaffepartiID
cursor.execute(kaffeparti)          # Fremmed:  GårdID, ForedlingsmetodeID
cursor.execute(foredlingsmetode)  
cursor.execute(kaffebønne)
cursor.execute(gård)
cursor.execute(dyrkesAv)            # Fremmed:  GårdID, KaffebønneID


# Commiter endringen
con.commit()

# Brukerhistorie 1
con.execute('''INSERT INTO Kaffesmaking VALUES ('Wow – en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!', 10, 'Vinterkaffe 2022', 'Jacobsen & Svart')''')

#Brukerhistorie 2
con.execute()

# Lukker tilkoblingen
con.close()