import sqlite3

# Hjelpemetode - Sjekker om mailen/brukeren eksisterer i databasen
def verify_email(email):
    
    # Kobler til databasen
    con = sqlite3.connect("test.db")
    cursor = con.cursor()
    
    # Henter alle resultater med gitt epostadresse
    exists = cursor.execute("SELECT * FROM Bruker WHERE Epostadresse =:epostadresse", {"epostadresse": email})

    boolean = False

    # Sjekker om spørringen fikk noen resultater
    if exists.fetchone():
        boolean = True

    # Lukker tilkoblingen
    con.close()
    return boolean


# Hjelpemetode - Sjekker om bruker har oppgitt riktig fulltnavn og passord
def matching_email_password(email, password):
    
    # Kobler til databasen
    con = sqlite3.connect("test.db")
    cursor = con.cursor()
    boolean = False

    # Utfører spørring
    exists = cursor.execute("SELECT * FROM Bruker WHERE Epostadresse =:epostadresse AND Passord =:passord", {"epostadresse": email, "passord": password})
    
    # Sjekker om listen er tom
    if exists.fetchone():
        boolean = True

    # Lukker tilkoblingen
    con.close()
    return boolean


# Hjelpemetode - Registrer ny bruker i databasen
def insert_user(email, password, user_name):

    # Kobler til databasen
    con = sqlite3.connect("test.db")

    # Oppretter markør - Du bruker den til å kjøre queries
    cursor = con.cursor()

    # Definerer spørring - ENDRE BRUKERID - Kan bli problem med ''fulltnavn'' osv.
    # query = '''INSERT INTO Bruker VALUES (5, '?', '?', '?')''', (epostadresse, passord, fulltnavn)

    # Utfører spørring og printer resultatet - Trenger løsning for BrukerID
    cursor.execute('''INSERT INTO Bruker (Epostadresse,Passord,Fulltnavn) VALUES (?, ?, ?)''', (email, password, user_name))
    con.commit()

    # Lukker tilkoblingen
    con.close()
    
    