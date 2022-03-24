import sqlite3

# Brukerhistorie 5
def story_five():

    # Kobler til databasen
    con = sqlite3.connect("test.db")

    # Oppretter markør
    cursor = con.cursor()

    # Definerer spørring
    query = '''SELECT Brennerinavn, Kaffe.Navn
                FROM (Kaffe NATURAL JOIN Kaffeparti) INNER JOIN Gård ON Kaffeparti.GårdID = Gård.GårdID
                WHERE (Land = "Rwanda" OR Land = "Colombia") AND Foredlingsmetode != "Vasket"'''

    # Utfører spørring og printer resultatet
    resultat = cursor.execute(query)
    
    # Printer resultatet
    print("Her er en liste over brennerinavn og kaffenavn fra Rwanda eller Colombia som ikke er vasket:")
    for res in resultat:
        print("Brennerinavn: " + res[0] + ", Kaffenavn: " + str(res[1]))
    print()

    # Lukker tilkoblingen
    con.close()