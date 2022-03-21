import sqlite3

# Hjelpemetode - Sjekker om mailen/brukeren eksisterer i databasen
def mailExists(epostadresse):

    # Kobler til databasen
    con = sqlite3.connect("test.db")

    # Oppretter markør - Du bruker den til å kjøre queries
    cursor = con.cursor()

    # Definerer spørring
    query = '''SELECT * FROM Bruker WHERE Epostadresse=?''', (epostadresse)

    # Utfører spørring og printer resultatet
    resultat = cursor.execute(query).fetchone()

    # Lukke tilkoblingen
    con.close()
    
    # Sjekker om listen er tom
    if (resultat != None):
        return True
    else:
        return False


# Hjelpemetode - Sjekker om bruker har oppgitt riktig navn og passord
def isCorrectNameAndPassword(epostadresse, navn, passord):

    # Kobler til databasen
    con = sqlite3.connect("test.db")

    # Oppretter markør - Du bruker den til å kjøre queries
    cursor = con.cursor()

    # Definerer spørring
    queryNavn = '''SELECT Navn FROM Bruker WHERE Epostadresse=?''', (epostadresse)
    queryPassord = '''SELECT Passord FROM Bruker WHERE Epostadresse=?''', (epostadresse)

    # Utfører spørring og printer resultatet
    resultatNavn = cursor.execute(queryNavn).fetchone()
    resultatPassord = cursor.execute(queryPassord).fetchone()

    # Lukke tilkoblingen
    con.close()
    
    # Sjekker om listen er tom
    if (navn == resultatNavn and passord == resultatPassord):
        return True
    else:
        return False


# Hjelpemetode - Registrer ny bruker i databasen
def insertUser(epostadresse, navn, passord):

    # Kobler til databasen
    con = sqlite3.connect("test.db")

    # Oppretter markør - Du bruker den til å kjøre queries
    cursor = con.cursor()

    # Definerer spørring - ENDRE BRUKERID - Kan bli problem med ''navn'' osv.
    query = '''INSERT INTO Bruker VALUES (4, '?', '?', '?')''', (epostadresse, navn, passord)

    # Utfører spørring og printer resultatet
    cursor.execute(query)
    con.commit()

    # Lukke tilkoblingen
    con.close()