import sqlite3

# Brukerhistorie 2
# cursor.execute('''SELECT Navn, Smakinger
#                     FROM (SELECT COUNT(BrukerID) AS Smakinger, Kaffenavn, Brennerinavn
#                         FROM Kaffesmaking
#                         GROUP BY BrukerID)
#                     JOIN
#                         (SELECT BrukerID AS ID, Navn
#                         FROM Bruker)
#                     ON
#                     BrukerID = ID
#                     ORDER BY Smakinger DESC
#                 ''')
# print(cursor.fetchall())

# En bruker skal kunne få skrevet ut en liste over hvilke brukere som
# har smakt flest unike kaffer så langt i år, sortert synkende. Listen skal
# inneholde brukernes fulle navn og antallet kaffer de har smakt.


def numberOfTasted():

    # Kobler til databasen
    con = sqlite3.connect("test.db")

    # Oppretter markør - Du bruker den til å kjøre queries
    cursor = con.cursor()

    # Definerer spørring
    query = '''SELECT Navn, Smakinger
                     FROM (SELECT COUNT(BrukerID) AS Smakinger, Kaffenavn, Brennerinavn
                         FROM Kaffesmaking
                         GROUP BY BrukerID)
                     JOIN
                         (SELECT BrukerID AS ID, Navn
                         FROM Bruker)
                     ON
                     BrukerID = ID
                     ORDER BY Smakinger DESC
                 ''',
    
    # Utfører spørring og printer resultatet
    resultat = cursor.execute(query)
    print(resultat.fetchall())

    # Lukker tilkoblingen
    con.close()

    return None

