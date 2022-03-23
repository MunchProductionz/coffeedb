import sqlite3

# Brukerhistorie 4
def search(word):

    # Kobler til databasen
    con = sqlite3.connect("test.db")

    # Oppretter markør - Du bruker den til å kjøre queries
    cursor = con.cursor()

    # Definerer spørring
    # query = '''SELECT Kaffenavn, Brenneri
    #                 FROM (SELECT *
    #                     FROM Kaffesmaking
    #                     WHERE Smaksnotat LIKE “%?%”)
    #                 JOIN
    #                     (SELECT *
    #                     FROM Kaffe
    #                     WHERE Beskrivelse LIKE “%?%”)
    #                 ON 
    #                     Kaffenavn = Navn AND Kaffesmaking.Brenneri = Kaffe.Brenneri
    #             ''', (word, word)

    # Utfører spørring
    resultat = cursor.execute('''SELECT Kaffenavn, Brenneri
                                    FROM (SELECT *
                                        FROM Kaffesmaking
                                        WHERE Smaksnotat LIKE “%?%”)
                                    JOIN
                                        (SELECT *
                                        FROM Kaffe
                                        WHERE Beskrivelse LIKE “%?%”)
                                    ON 
                                        Kaffenavn = Navn AND Kaffesmaking.Brenneri = Kaffe.Brenneri
                                ''', (word, word))

    # Printer resultatet
    print(resultat.fetchall())

    # Lukker tilkoblingen
    con.close()
    
    return None

# Spørringer
# cursor.execute("SELECT * FROM Kaffesmaking")
# print(cursor.fetchall())