import sqlite3

# Brukerhistorie 5
def unwashed():

    # Kobler til databasen
    con = sqlite3.connect("test.db")

    # Oppretter markør - Du bruker den til å kjøre queries
    cursor = con.cursor()

    # Definerer spørring
    query = '''SELECT Brennerinavn, Kaffenavn
                    FROM (SELECT PartiID
                            FROM (SELECT *
                                    FROM Gård
                                    WHERE Land = Rwanda OR Land = Colombia)
                                    JOIN
                                    (SELECT * 
                                    FROM Kaffeparti
                                    WHERE Beskrivelse NOT IN (SELECT * FROM Kaffeparti WHERE Foredlingsmetode = “Vasket”)
                                    )
                                    ON
                                    Gård.GårdID = Kaffeparti.GårdID
                        )
                        NATURAL JOIN
                        Kaffe
                '''

    # Utfører spørring og printer resultatet
    resultat = cursor.execute(query)
    print(resultat.fetchall())

    # Lukker tilkoblingen
    con.close()
    
    return None