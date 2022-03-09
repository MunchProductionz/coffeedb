import sqlite3

# Kobler til databasen
con = sqlite3.connect("test.db")

# Oppretter markør - Du bruker den til å kjøre queries
cursor = con.cursor()

# Utfør queries
cursor.execute("SELECT * FROM sqlite_master")


# Lukker tilkoblingen - Ved innsetting av data, bruke con.commit() før con.close()
con.close()


# Eksempler på queries
#Ikke gjør dette:      cursor.execute("SELECT * FROM person WHERE navn = '%s'" % navn)           
#Gjør heller dette:    cursor.execute("SELECT * FROM person WHERE navn = ?", (navn))              
#Eller dette:          cursor.execute("SELECT * FROM person WHERE navn =:navn", {"navn" = navn}) 

# Nyttige metoder
#fetchone()     -   Returnerer neste resultatet i resultatsettet            (Hvis ingen elementer: None)
#fetchall()     -   Returnerer hele resultatsettet som en liste av tupler   (Hvis ingen elementer: None)
#fetchmany(i)   -   Returnerer en liste av i tupler fra resultatsettet
