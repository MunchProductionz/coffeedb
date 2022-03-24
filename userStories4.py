import sqlite3

# Brukerhistorie 4
def story_four(word):

    # Kobler til databasen
    con = sqlite3.connect("test.db")

    # Oppretter markør
    cursor = con.cursor()

    # Utfører spørring
    resultat = cursor.execute(('''
                      SELECT Kaffenavn, Brenneri
                      FROM Kaffesmaking NATURAL JOIN Kaffe
                      WHERE Smaksnotat LIKE :descr
                      UNION
                      SELECT Navn, Brennerinavn
                      FROM Kaffe
                      WHERE Beskrivelse LIKE :descr
                       '''), {"descr": "%"+word+"%"}).fetchall()

    # Printer resultatet
    print(f'Her er en liste over brennerinavn og kaffenavn som inneholder ordet "' + word + '":')
    for res in resultat:
        print("Brennerinavn: " + res[0] + ", Kaffenavn: " + str(res[1]))
    print()

    # Lukker tilkoblingen
    con.close()