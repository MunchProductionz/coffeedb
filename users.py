import sqlite3

# Hjelpemetode - Sjekker om mailen/brukeren eksisterer i databasen
def mailExists(epostadresse):

    # Kobler til databasen
    con = sqlite3.connect("test.db")

    # Oppretter markør - Du bruker den til å kjøre queries
    cursor = con.cursor()

    # Definerer spørring
    # query = '''SELECT * FROM Bruker WHERE Epostadresse = ?''', (epostadresse,)

    # Utfører spørring og printer resultatet
    resultat = cursor.execute('''SELECT * FROM Bruker WHERE Epostadresse = ?''', (epostadresse,)).fetchone()

    # Lukker tilkoblingen
    con.close()
    
    # Sjekker om listen er tom
    if (resultat != None):
        return True
    else:
        return False


# Hjelpemetode - Sjekker om bruker har oppgitt riktig fulltnavn og passord
def isCorrectNameAndPassword(epostadresse, passord, fulltnavn):

    # Kobler til databasen
    con = sqlite3.connect("test.db")

    # Oppretter markør - Du bruker den til å kjøre queries
    cursor = con.cursor()

    # Definerer spørring
    # queryFulltnavn = '''SELECT Fulltnavn FROM Bruker WHERE Epostadresse=?''', (epostadresse)
    # queryPassord = '''SELECT Passord FROM Bruker WHERE Epostadresse=?''', (epostadresse)

    # Utfører spørring og printer resultatet
    resultatFulltnavn = cursor.execute('''SELECT Fulltnavn FROM Bruker WHERE Epostadresse=?''', (epostadresse,)).fetchone()[0]   # Henter fulltnavn
    resultatPassord = cursor.execute('''SELECT Passord FROM Bruker WHERE Epostadresse=?''', (epostadresse,)).fetchone()[0]       # Henter passord

    # Lukke tilkoblingen
    con.close()
    
    # Sjekker om listen er tom
    if (fulltnavn == resultatFulltnavn and passord == resultatPassord):
        return True
    else:
        return False


# Hjelpemetode - Registrer ny bruker i databasen
def insertUser(epostadresse, passord, fulltnavn):

    # Kobler til databasen
    con = sqlite3.connect("test.db")

    # Oppretter markør - Du bruker den til å kjøre queries
    cursor = con.cursor()

    # Definerer spørring - ENDRE BRUKERID - Kan bli problem med ''fulltnavn'' osv.
    # query = '''INSERT INTO Bruker VALUES (5, '?', '?', '?')''', (epostadresse, passord, fulltnavn)

    # Utfører spørring og printer resultatet - Trenger løsning for BrukerID
    cursor.execute('''INSERT INTO Bruker VALUES (5, ?, ?, ?)''', (epostadresse, passord, fulltnavn))
    con.commit()

    # Lukke tilkoblingen
    con.close()