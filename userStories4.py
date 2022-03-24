import sqlite3

# Brukerhistorie 4
def story_four(word):

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
    
    resultat = cursor.execute(('''
                      SELECT Kaffenavn, Brenneri
                      FROM Kaffesmaking INNER JOIN KAFFE
                      WHERE Smaksnotat LIKE :descr OR Beskrivelse LIKE :descr
                       '''), {"descr": "%"+word+"%"}).fetchall()
    
    result = cursor.execute(('''SELECT * FROM Kaffesmaking WHERE Smaksnotat LIKE :descr'''), {"descr": "%"+word+"%"}).fetchall()

    # Printer resultatet
     
    print(cursor.execute(('''SELECT * FROM Kaffesmaking WHERE Smaksnotat LIKE :descr'''), {"descr": "%"+word+"%"}).fetchall())
    print(resultat)

    # Lukker tilkoblingen
    con.close()
    
    return None

story_four("rei")
# Spørringer
# cursor.execute("SELECT * FROM Kaffesmaking")
# print(cursor.fetchall())