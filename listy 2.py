imiona = ["Arkadiusz", "Wiola", "Antek"]
counter = 0


while counter <= 2:
    imie = input()
    imie = imie.capitalize()
    if imie in imiona:
        print("Masz dostęp")
        break
    else:
        print("Nie masz dostępu")
        counter += 1
        print("próba nr", counter)
        continue
else:
    print("Koniec prób. Program zostanie zakończony")


    
