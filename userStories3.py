import sqlite3

# Brukerhistorie 3
def story_three():
    
    # Kobler til databasen
    con = sqlite3.connect("test.db")

    # Oppretter markør
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
    
    print("Under følger en oversikt over kaffene som har fått høyest gjennomsnittlig rating i forhold til pris")
    
    for coffee in all_coffees:
        print("Brenneri: " + coffee[0] + ", Kaffenavn: " + coffee[1] + ", Pris: " + str(coffee[2]) + ", Gjennomsnitsscore: " + str(coffee[3]))
    print()
    
    
