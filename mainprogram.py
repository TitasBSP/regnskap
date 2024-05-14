# Dette programmet krever brukeren til å installere tabulate, det kan gjøres via å skrive inn "pip install tabulate" på CMD.
# Tabulate en er utvidelse fra Python-biblioteket som lar Python lage tabeller
from tabulate import tabulate
import time 

############################################################## VARIABLES #########################################################################

# Definere hovedkategorien
head = ["", "", "Lovbruddstyper"]

# Definere underkategoriene og dataen i en tabell
mydata = [

    ["År", "Regnskap / Bokføring", "Årsregnskap"],
    ["2017", "9631", "9863"], 
    ["2018", "8593", "12217"], 
    ["2019", "8363", "14920"], 
    ["2020", "8128", "14929"],
    ["2021", "8514", "15425"],
    ["2022", "8534", "18010"]

]

# Lage liste over mulige valg for år
aarsliste = str([2017, 2018, 2019, 2020, 2021, 2022])
choice = ""

# Samle regnskapsvariabler med riktig data
regnskap2017 = 9631
regnskap2018 = 8593
regnskap2019 = 8363
regnskap2020 = 8128
regnskap2021 = 8514
regnskap2022 = 8534

# Samle årsregnskapsvariabler med riktig data
aarsregnskap2017 = 9863
aarsregnskap2018 = 12217
aarsregnskap2019 = 14920
aarsregnskap2020 = 14929
aarsregnskap2021 = 15425
aarsregnskap2022 = 18010

# Lage variabel for main loop
start_screen = True

# KILDER:
# https://www.geeksforgeeks.org/how-to-make-a-table-in-python/

######################################################### MAIN INTERFACE #######################################################################

# Overskrift
print("___________________________________________________")
print("| Velkommen til regnskapskriminalitetsprogrammet! |")
print("```````````````````````````````````````````````````")

time.sleep(2)

# Kalle skrivekommandoen for tabellen og kategoriene
print(tabulate(mydata, headers=head, tablefmt="grid"))
print()

time.sleep(1)

# Beskrivelse
print("\nDette programmet er laget for å finne differansen mellom antall lovbrudd i kategoriene - Bokføring og Årsregnskap - i to forskjellige år" )
    
time.sleep(2)

############################################################# MAIN LOOP #######################################################################

while start_screen:

    # Man får først velge om man vil enten finne differanse for bokføring eller årsregnskap
    choice = input("\nHvilken statistikk vil du finne differanse for? (Enten - bokføring - eller - årsregnskap -): ")

    if choice == "bokføring":
            aar1 = input("\nVennligst skriv inn det første året du ønsker å sammenligne: ")
            # Choice1 blir konvertert til aar1
            choice1 = aar1

            # Dersom choice1 finnes i aarsliste, fortsetter programmet
            if choice1 in aarsliste:
                aar2 = input("\nVennligst skriv inn det andre året du ønsker å sammenligne: ")
                # Choice2 blir konvertert til aar2
                choice2 = aar2

                # Dersom choice2 finnes i aarsliste, fortsetter programmet
                if choice2 in aarsliste:
                    print("\nKalkulerer...\n")
                    time.sleep(1)

                    # Choice1 blir konvertert til dataen istedenfor å være året
                    if choice1 == str(2017):
                        choice1 = regnskap2017

                    elif choice1 == str(2018):
                        choice1 = regnskap2018

                    elif choice1 == str(2019):
                        choice1 = regnskap2019

                    elif choice1 == str(2020):
                        choice1 = regnskap2020

                    elif choice1 == str(2021):
                        choice1 = regnskap2021

                    elif choice1 == str(2022):
                        choice1 = regnskap2022

                    # Choice2 blir konvertert til dataen istedenfor å være året
                    if choice2 == str(2017):
                        choice2 = regnskap2017

                    elif choice2 == str(2018):
                        choice2 = regnskap2018

                    elif choice2 == str(2019):
                        choice2 = regnskap2019

                    elif choice2 == str(2020):
                        choice2 = regnskap2020

                    elif choice2 == str(2021):
                        choice2 = regnskap2021

                    elif choice2 == str(2022):
                        choice2 = regnskap2022

                    # Kalkulasjonen for programmet
                    alter1 = int(choice1) - int(choice2)
                    alter2 = int(choice2) - int(choice1)

                    # Hvis choice1 er større enn choice2, blir det største tallet satt først, så blir den subtrahert
                    if choice1 > choice2:
                        print(f"Differansen i kriminalitet for temaet - Regnskap / Bokføring - mellom årene {aar1} og {aar2} er {alter1}")
                        print(f"---- {choice1} - {choice2} = {alter1} ----\n")
                        time.sleep(3)
                        print(tabulate(mydata, headers=head, tablefmt="grid"))
                        print()
                        time.sleep(2)

                    # Hvis choice2 er større enn choice1, blir det største tallet satt først, så blir den subtrahert
                    elif choice1 < choice2:
                        print(f"Differansen i kriminalitet for temaet - Regnskap / Bokføring - mellom årene {aar1} og {aar2} er {alter2}")
                        print(f"---- {choice2} - {choice1} = {alter2} ----\n")
                        time.sleep(3)
                        print(tabulate(mydata, headers=head, tablefmt="grid"))
                        print()
                        time.sleep(2)

                # Dersom det blir satt inn et år som er større eller mindre enn 2017 til 2022, får man at året er ugyldig.
                else:
                    print(f"Året {choice2} er ikke gyldig. Vennligst velg et år fra listen: {aarsliste}\n")

            else:
                print(f"Året {choice1} er ikke gyldig. Vennligst velg et år fra listen: {aarsliste}\n")

    if choice == "årsregnskap":

            aar1 = input("\nVennligst skriv inn det første året du ønsker å sammenligne: ")
            # Choice1 blir konvertert til aar1
            choice1 = aar1

            # Dersom choice1 finnes i aarsliste, fortsetter programmet
            if choice1 in aarsliste:
                aar2 = input("\nVennligst skriv inn det andre året du ønsker å sammenligne: ")
                # Choice2 blir konvertert til aar2
                choice2 = aar2

                # Dersom choice2 finnes i aarsliste, fortsetter programmet
                if choice2 in aarsliste:
                    print("\nKalkulerer...\n")
                    time.sleep(1)

                    # Choice1 blir konvertert til dataen istedenfor å være året
                    if choice1 == str(2017):
                        choice1 = aarsregnskap2017

                    elif choice1 == str(2018):
                        choice1 = aarsregnskap2018

                    elif choice1 == str(2019):
                        choice1 = aarsregnskap2019

                    elif choice1 == str(2020):
                        choice1 = aarsregnskap2020

                    elif choice1 == str(2021):
                        choice1 = aarsregnskap2021

                    elif choice1 == str(2022):
                        choice1 = aarsregnskap2022

                    # Choice2 blir konvertert til dataen istedenfor å være året
                    if choice2 == str(2017):
                        choice2 = aarsregnskap2017

                    elif choice2 == str(2018):
                        choice2 = aarsregnskap2018

                    elif choice2 == str(2019):
                        choice2 = aarsregnskap2019

                    elif choice2 == str(2020):
                        choice2 = aarsregnskap2020

                    elif choice2 == str(2021):
                        choice2 = aarsregnskap2021

                    elif choice2 == str(2022):
                        choice2 = aarsregnskap2022

                    # Kalkulasjonen for programmet
                    alter1 = int(choice1) - int(choice2)
                    alter2 = int(choice2) - int(choice1)

                    # Hvis choice1 er større enn choice2, blir det største tallet satt først, så blir den subtrahert
                    if choice1 > choice2:
                        print(f"Differansen i kriminalitet for temaet - Regnskap / Bokføring - mellom årene {aar1} og {aar2} er {alter1}")
                        print(f"---- {choice1} - {choice2} = {alter1} ----\n")
                        time.sleep(3)
                        print(tabulate(mydata, headers=head, tablefmt="grid"))
                        print()
                        time.sleep(2)

                    # Hvis choice2 er større enn choice1, blir det største tallet satt først, så blir den subtrahert
                    elif choice1 < choice2:
                        print(f"Differansen i kriminalitet for temaet - Regnskap / Bokføring - mellom årene {aar1} og {aar2} er {alter2}")
                        print(f"---- {choice2} - {choice1} = {alter2} ----\n")
                        time.sleep(3)
                        print(tabulate(mydata, headers=head, tablefmt="grid"))
                        print()
                        time.sleep(2)

                # Dersom det blir satt inn et år som er større eller mindre enn 2017 til 2022, får man at året er ugyldig.
                else:
                    print(f"Året {choice2} er ikke gyldig. Vennligst velg et år fra listen: {aarsliste}\n")

            else:
                print(f"Året {choice1} er ikke gyldig. Vennligst velg et år fra listen: {aarsliste}\n")