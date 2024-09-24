from back_end import *


def printMeny():
    print("------------------- Kalkulator -------------------")
    print("| 1. Kalkulator                                  |")
    print("| 2. Avslutt                                     |")
    print("--------------------------------------------------")
    menyvalg = input("Velg operasjon fra menyen: ")
    utfoerMenyvalg(menyvalg)


def utfoerMenyvalg(valgtTall):
    if valgtTall == "1":
        calculator()
        pause_og_fortsett()
    elif valgtTall == "2":
        bekreftelse = input("Er du sikker på at du vil avslutte? J/N ")
        if (bekreftelse == "J" or bekreftelse == "j"):
            exit()
        else:
            printMeny()
    else:
        nyttForsoek = input("*** Ugyldig valg. Velg et tall mellom 1-2. Trykk for å fortsette *** ")
        print(nyttForsoek)
        printMeny()


def pause_og_fortsett():
    input("-- Trykk en tast for å fortsette --")
    printMeny()


printMeny()

