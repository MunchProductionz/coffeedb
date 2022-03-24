import email
import sqlite3
from userStories1 import story_one
#from userStories2 import story_two
from userStories3 import story_three
from userStories4 import search
from userStories5 import unwashed

from users import insert_user, isCorrectNameAndPassword, verify_email

def run():
    print('Velkommen til coffeeDB!')
    prompt = input("Skriv 'Ny bruker' for å opprette ny bruker, eller hva som helst annet for å logge inn: ")
    
    if prompt.lower() == "ny bruker":
        epostadresse = new_user()
    else:
        epostadresse = login()
        
    print("Du er nå logget inn i coffeDB! Velg et av alternativene under:\n")
    
    story = get_story()
    
    while (story != -1):
        run_story(story, epostadresse)
        
        x = input("Trykk enter for å avslutte, eller noe annet for å velge en ny brukerhistorie.")
        if (x == ''):
            story = -1
        else:
            story = get_story()

    print("Du er nå logget ut av coffeeDB. Ha en fin dag!")
            

# Hjelpemetode - hente hvilken brukerhistorie som skal kjøres
def get_story():
    story = ''
    while (story != -1):
        print('> 1 - Input Brukerhistorie 1')
        print('> 2 - Rangering: Brukere')
        print('> 3 - Rangering: Kaffer')
        print('> 4 - Søk')
        print('> 5 - Kaffe, ikke vasket')
    
        print()
        print('La valg av alternativ stå tomt for å avslutte.')
        print()

        story = input('Vennligst velg et av alternativene fra menyen (1-5) over: ')

        print()

        if (story == ''):
            return -1  
            
        if (is_valid_story(story)):
            return story 
        
        print('Ikke et gyldig alternativ')
        print('Vennligst prøv igjen.')
        print() 
         
         
# Hjelpemetode - logge inn         
def login():
    email = input('Vennligst skriv inn epostadressen din: ')
    
    print()

    while (not verify_email(email)):
        
        print("Trykk X for å avslutte")
        email = input("Det var ikke en registrert epostadresse. Vennligst prøv på nytt: ")
        if (email.lower() == "x"):
            run()
            
    print('Vennligst logg inn.')
    
    password = input('Passord: ')
        
    print()

    while (not isCorrectNameAndPassword(email, password)):
        print('Navnet eller passordet du har oppgitt er feil.')
        print('Vennligst prøv igjen.')
        print('Trykk "X" for å gå tilbake.')

        print()

        password = input('Passord: ')

        print()

        if (password.lower() == 'x'):
            run()
            
    return email


# Hjelpemetode - opprett ny bruker
def new_user():
    print("Vennligst fyll ut informasjonen under for å registrere deg i coffeDB")
    email = input("Epostadresse: ")
    while (verify_email(email)):
        print("Det er allerede en bruker registrert med epostadresse '" + email + "'.")
        email = input("Prøv igjen: ")
    name = input("Fullt navn: ")
    while (name == ''):
        name = input("Navn kan ikke være tomt. Vennligst skriv inn navnet du vil registreres med: ")
    password = input("Passord: ")
    while (password == ''):
        password = input("Passord kan ikke være blankt. Vennligst skriv inn et passord: ")
    insert_user(email, password, name)
    print("Bruker registrert med mail '" + email + "' og navn '" + name + "'")
    return email
    
    
# Hjelpemetode - Kjører riktig brukerhistorie
def run_story(historie, epostadresse):
    if (historie == '1'):
        story_one(epostadresse)
    elif (historie == '2'):
        return None
    elif (historie == '3'):
        story_three()
    elif (historie == '4'):
        word = input('Skriv ordet du ønsker å søke på: ')
        search(word)
    elif (historie == '5'):
        unwashed()


# Hjelpemetode - Validerer historie
def is_valid_story(story):
    
    for i in range(1, 6):
        h = str(i)
        if (story == h):
            return True
    
    return False


run()


# Brukerhistorie 1




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

# Brukerhistorie 3
# cursor.execute('''''')
# print(cursor.fetchall())


# Brukerhistorie 4
# cursor.execute('''SELECT Kaffenavn, Brenneri
#                     FROM (SELECT *
#                         FROM Kaffesmaking
#                         WHERE Smaksnotat LIKE “%floral%”)
#                     JOIN
#                         (SELECT *
#                         FROM Kaffe
#                         WHERE Beskrivelse LIKE “%floral%”)
#                     ON 
#                         Kaffenavn = Navn AND Kaffesmaking.Brenneri = Kaffe.Brenneri
#                 ''')
# print(cursor.fetchall())



# Brukerhistorie 5
# cursor.execute('''SELECT Brennerinavn, Kaffenavn
#                     FROM (SELECT PartiID
#                             FROM (SELECT *
#                                     FROM Gård
#                                         WHERE Land = Rwanda OR Land = Colombia)
#                                         JOIN
#                                         (SELECT * 
#                                         FROM Kaffeparti
#                                         WHERE NOT IN (SELECT * FROM Kaffeparti WHERE Foredlingsmetode = “Vasket”)
#                             )
#                             ON
#                             Gård.GårdID = Kaffepart.GårdID
#                         )
#                         NATURAL JOIN
#                         Kaffe
#                 ''')
# print(cursor.fetchall())





# Commiter endringen
# con.commit()

# Lukker tilkoblingen
# con.close()