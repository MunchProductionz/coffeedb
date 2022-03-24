import sqlite3
from functions import select
from creatingTables import buildTables
from insertingValues import reset
from datetime import date


def story_one(email):
    con = sqlite3.connect("test.db")
    cursor = con.cursor()
    if (not verify_user(email, cursor)):
        return "Ingen bruker registert med denne epostadressen."
    
    print("Du kan nå registrere en ny kaffesmaking.\n")
    roastery = get_roastery(cursor)
    coffee = get_coffee(roastery, cursor)
    points = get_points()
    note = input("Fyll inn din vurdering av kaffen: ")
    userID = get_user_ID(email, cursor)
    today = date.today()

    cursor.execute('''INSERT INTO Kaffesmaking (Smaksnotat,Poeng,Dato,BrukerID,Kaffenavn,Brennerinavn) VALUES (?,?,?,?,?,?)''', ( note, points, today, userID, coffee, roastery))
    con.commit()

    # print(cursor.execute("SELECT * FROM Kaffesmaking").fetchall())

    con.close()
    
    print("Din smaking av kaffen '" + coffee + "' fra brenneriet '" + roastery + "' er registrert med poengscore " + points + " og smaksnotat '" + note + "' er registrert.\n")

def get_roastery(cursor):
    roastery = input("Skriv inn navn på brenneriet: ")
    valid_input = verify_roaster(roastery, cursor)
    while (not valid_input):
        roastery = input("Det var ikke et registrert brenneri. Vennligst skriv inn et gydlig brenneri: ")
        valid_input = verify_roaster(roastery, cursor)
    return roastery

def get_coffee(roastery, cursor):
    coffee = input("Skriv inn navn på kaffen: ")
    valid_input = verify_coffee(roastery, coffee, cursor)
    while (not valid_input):
        coffee = input("Det var ikke en registrert kaffe. Vennligst skriv inn et gydlig kaffenavn: ")
        valid_input = verify_coffee(roastery, coffee, cursor)
    return coffee

def get_points():
    points = input("Ranger kaffen fra 1 til 10: ")
    while (not points.isdigit()):
        points = input("Poengvurderingen må være et tall. Vennligst ranger kaffen fra 1 til 10: ")
    return points

def get_user_ID(email, cursor):
    query = '''
    SELECT
        BrukerID
    FROM 
        Bruker
    WHERE
        Epostadresse =:email
    '''
    
    userID = cursor.execute(query, {"email": email}).fetchone()[0]
    return userID
    

def verify_user(email, cursor):
    exists = cursor.execute("SELECT BrukerID FROM Bruker WHERE Epostadresse =:epostadresse", {"epostadresse": email})

    boolean = False

    if exists.fetchone():
        boolean = True

    return boolean

def verify_roaster(roastery, cursor):
    exists = cursor.execute("SELECT Navn FROM Brenneri WHERE Navn = ?", [roastery])

    boolean = False

    if exists.fetchone():
        boolean = True
        
    return boolean

def verify_coffee(roastery, name, cursor):
    if (not verify_roaster(roastery, cursor)):
        return False
    exists = cursor.execute("SELECT Brennerinavn, Navn FROM Kaffe WHERE Brennerinavn =:brennerinavn AND Navn =:navn", {"brennerinavn": roastery, "navn": name})

    boolean = False

    if exists.fetchone():
        boolean = True
    return boolean

reset()
#story_one("bruker1@mail.com")