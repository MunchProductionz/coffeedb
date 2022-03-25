import sqlite3

def story_two():

    # Kobler til databasen
    con = sqlite3.connect("test.db")

    # Oppretter markør
    cursor = con.cursor()

    # Definerer spørring
    query = cursor.execute('''SELECT Fulltnavn, Smakinger
                     FROM (SELECT COUNT(DISTINCT Kaffenavn) AS Smakinger, BrukerID, Kaffenavn, Brenneri
                         FROM Kaffesmaking
                         WHERE Strftime('%Y', Dato) = '2022'
                         GROUP BY BrukerID)
                     JOIN
                         (SELECT BrukerID AS ID, Fulltnavn
                         FROM Bruker)
                     ON
                     BrukerID = ID
                     
                     ORDER BY Smakinger DESC
                 ''').fetchall()
    
    # Lukker tilkoblingen
    con.close()
    print("Her er en sortert liste med brukere som har smakt flest antall unike kaffer i år: ")
    for user in query:
        print("Navn: " + user[0] + ", Unike kaffer: " + str(user[1]))
    print()