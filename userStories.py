import sqlite3
from userStories3 import unwashed
from userStories4 import search

from users import insertUser, isCorrectNameAndPassword, mailExists

def run():
    
    # Initialiserer variabler
    fulltnavn = ''
    passord = ''
    historie = ' '

    # Henter epostadresse
    print('Velkommen til coffeeDB.')
    epostadresse = input('Vennligst skriv inn epostadressen din: ')
    
    print()

    # Sjekker om mailen/brukeren eksisterer i databasen
    if (mailExists(epostadresse)):
        
        print('Vennligst logg inn.')
        fulltnavn = input('Fullt navn: ')
        passord = input('Passord: ')
        
        print()

        # "Logger inn" på bruker
        while (not isCorrectNameAndPassword(epostadresse, fulltnavn, passord)):
            print('Navnet eller passordet du har oppgitt er feil.')
            print('Vennligst prøv igjen.')
            print('La navn og passord stå tomme for å gå tilbake.')

            print()

            fulltnavn = input('Fullt navn: ')
            passord = input('Passord: ')

            print()

            # Kaller run() dersom bruker trykker Enter 2 ganger
            if (fulltnavn == '' and passord == ''):
                run()

    # Hvis bruker ikke allerede eksisterer, registrer bruker        
    else:

        print('Du ser ut til å være en ny bruker i databasen.')
        print('Vennligst registrer fulltnavn og passord for brukeren.')

        print()

        fulltnavn = input('Fullt navn: ')
        passord = input('Passord: ')

        print()

        while (fulltnavn == '' and passord == ''):
            print('Navn eller passord kan ikke være en tom streng.')
            print('Vennligst prøv igjen.')

            print()

            fulltnavn = input('Fullt navn: ')
            passord = input('Passord: ')

            print()
        
        insertUser(epostadresse, fulltnavn, passord)

    # Bruker velger ønsket historie, avsluttes ved å inputte tom streng
    while (historie != ''):

        print('Alternativer:')
        print('> 1 - Input Brukerhistorie 1')
        print('> 2 - Rangering: Brukere')
        print('> 3 - Rangering: Kaffer')
        print('> 4 - Søk')
        print('> 5 - Kaffe, ikke vasket')
    
        print()
        print('La valg av alternativ stå tomt for å avslutte.')
        print()

        historie = input('Vennligst velg et av alternativene fra menyen (1-5) over: ')

        print()

        if (not isValidStory(historie)):
            print('Ikke et gyldig alternativ')
            print('Vennligst prøv igjen.')
            print()
        
        elif (historie == ''):
            return None
        else:
            runStory(historie, epostadresse, fulltnavn, passord)
            print()
            input('Trykk enter for å velge nytt alternativ.')
            print()
            



# Hjelpemetode - Kjører riktig brukerhistorie
def runStory(historie, epostadresse, fulltnavn, passord):
    if (historie == '1'):
        return None
    elif (historie == '2'):
        return None
    elif (historie == '3'):
        return None
    elif (historie == '4'):
        word = input('Skriv ordet du ønsker å søke på: ')
        search(word)
    elif (historie == '5'):
        unwashed()

# Hjelpemetode - Validerer historie
def isValidStory(historie):

    if (historie == ''):
        return True

    for i in range(5):
        h = str(i + 1)
        if (historie == h):
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