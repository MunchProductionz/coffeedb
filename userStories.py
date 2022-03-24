from insertingValues import rebuild
from userStories1 import story_one
from userStories2 import story_two
from userStories3 import story_three
from userStories4 import story_four
from userStories5 import story_five

from users import insert_user, matching_email_password, verify_email

def run():
    
    print()
    print('Velkommen til coffeeDB!')
    prompt = input("Skriv 'Ny bruker' for å opprette ny bruker, eller hva som helst annet for å logge inn: ")
    
    if prompt.lower() == "ny bruker":
        email = new_user()
    else:
        email = login()
        
    print("Du er nå logget inn i coffeDB! Velg et av alternativene under:\n")
    
    story = get_story()
    
    while (story != -1):
        run_story(story, email)
        
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

    while (not matching_email_password(email, password)):
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
        story_two()
    elif (historie == '3'):
        story_three()
    elif (historie == '4'):
        word = input('Skriv ordet du ønsker å søke på: ')
        story_four(word)
    elif (historie == '5'):
        story_five()


# Hjelpemetode - Validerer historie
def is_valid_story(story):
    
    for i in range(1, 6):
        h = str(i)
        if (story == h):
            return True
    
    return False

rebuild()
run()