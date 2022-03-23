import sqlite3
from functions import select
from creatingTables import buildTables
from insertingValues import reset
from datetime import date


def story_one():
    
    con = sqlite3.connect("test.db")
    cursor = con.cursor()
    
    roastery = get_roastery(cursor)
    coffee = get_coffee(roastery, cursor)
    
    points = int(input("Ranger kaffen fra 1 til 10: "))
    note = input("Fyll inn din vurdering av kaffen: ")

    userID = 1
    today = date.today()

    cursor.execute('''INSERT INTO Kaffesmaking (Smaksnotat,Poeng,Dato,BrukerID,Kaffenavn,Brennerinavn) VALUES (?,?,?,?,?,?)''', ( note, points, today, userID, coffee, roastery))
    con.commit()

    print(cursor.execute("SELECT * FROM Kaffesmaking").fetchall())

    con.close()

def get_roastery(cursor):
    roastery = input("Skriv inn navn på brenneriet: ")
    valid_input = check_roaster(roastery, cursor)
    while (not valid_input):
        roastery = input("Det var ikke et registrert brenneri. Vennligst skriv inn et gydlig brenneri: ")
        valid_input = check_roaster(roastery, cursor)
    return roastery

def get_coffee(roastery, cursor):
    coffee = input("Skriv inn navn på kaffen: ")
    valid_input = check_coffee(roastery, coffee)
    while (not valid_input):
        coffee = input("Det var ikke en registrert kaffe. Vennligst skriv inn et gydlig kaffenavn: ")
        valid_input = check_coffee(roastery, coffee, cursor)

def check_user(epostadresse, fulltnavn):
    con = sqlite3.connect("test.db")
    cursor = con.cursor()
    exists = cursor.execute("SELECT BrukerID FROM Bruker WHERE Epostadresse =:epostadresse AND Fulltnavn =:fulltnavn", {"epostadresse": epostadresse, "fulltnavn": fulltnavn})

    boolean = False

    if exists.fetchone():
        boolean = True

    con.close()
    return boolean

def check_roaster(brenneri, cursor):
    exists = cursor.execute("SELECT Navn FROM Brenneri WHERE Navn = ?", [brenneri])

    boolean = False

    if exists.fetchone():
        boolean = True
        
    return boolean

def check_coffee(brenneri, navn, cursor):
    if (not check_roaster(brenneri, cursor)):
        return False
    exists = cursor.execute("SELECT Brennerinavn, Navn FROM Kaffe WHERE Brennerinavn =:brennerinavn AND Navn =:navn", {"brennerinavn": brenneri, "navn": navn})

    boolean = False

    if exists.fetchone():
        boolean = True
    return boolean

reset()
buildTables()
reset()

story_one()