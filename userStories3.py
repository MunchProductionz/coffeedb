import sqlite3

# Brukerhistorie 3
def story_three():

    # Kobler til databasen
    con = sqlite3.connect("test.db")

    
    # Oppretter markør - Brukes til å kjøre queries
    cursor = con.cursor()

    #Definerer spørring
    all_coffees = cursor.execute('''
        SELECT
            Kaffe.Brennerinavn,
            Kaffesmaking.Kaffenavn,
            Kaffe.KiloprisNOK,
            AVG(Kaffesmaking.Poeng) AS Gjennomsnitt_poeng
        FROM
            Kaffesmaking
            INNER JOIN Kaffe WHERE Kaffesmaking.Kaffenavn=Kaffe.Navn
        GROUP BY
            Kaffesmaking.Kaffenavn
        ORDER BY
            Gjennomsnitt_poeng/KiloprisNOK DESC
    ''').fetchall()

    # Lukker tilkoblingen 
    con.close()        
    
    return all_coffees

s = story_three()

# Printer hver linje
for coffee in s:
    print(coffee)