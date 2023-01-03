imiona = ["Arkadiusz", "Wiola", "Antek"]
counter = 0


while counter <= 3:
    imie = input()

if imie in imiona:
    print("Masz dostęp")
else:
    print("Nie masz dostępu")
    counter += 1
    print("próba nr", counter)
break
 print("Niepoprawna odpowiedź")

