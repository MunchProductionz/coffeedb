import sqlite3

# Brukerhistorie 3
def story_three():
    
    # Kobler til databasen
    con = sqlite3.connect("test.db")

    # Oppretter markør - Du bruker den til å kjøre queries
    cursor = con.cursor()
    
    # Definerer spørring
    query = '''
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
    '''
    
    all_coffees = cursor.execute(query).fetchall()
    con.close()        
    
    for coffee in all_coffees:
        print(coffee)
    print()
    
    