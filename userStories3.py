import sqlite3

# Brukerhistorie 3
def unwashed():

    # Kobler til databasen
    con = sqlite3.connect("test.db")

    # Oppretter markør - Du bruker den til å kjøre queries
    cursor = con.cursor()

    # Definerer spørring - FYLL INN
    query = ''

    # Utfører spørring og printer resultatet
    resultat = cursor.execute(query)
    print(resultat.fetchall())

    # Lukker tilkoblingen
    con.close()
    
    return None