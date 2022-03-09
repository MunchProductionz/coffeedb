import sqlite3

# Kobler til databasen
con = sqlite3.connect("test.db")

# Oppretter markør - Du bruker den til å kjøre queries
cursor = con.cursor()

# Utfør queries
all = cursor.execute("SELECT * FROM sqlite_master")
print(all)

# Lukker tilkoblingen - Ved innsetting av data, bruke con.commit() før con.close()
con.close()