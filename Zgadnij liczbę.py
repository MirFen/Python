import random

search = random.randint(1, 100)
x = 1
a = search - 3
b = search + 3
#print("serch", search)
while x <11:
        print("It's your",x,"chance")
        gus = int(input("Try your self: "))
        if (gus != search) :
            if (gus > search and gus <= b ):
                print(gus,"jest za dużą liczbą ale już blisko")
                
            elif (gus < search and gus >= a):
                print(gus,"jest za małą liczbą ale już blisko")
                
            elif (gus > search ):
                print(gus,"jest za dużą liczbą")
                
            else:
                print(gus,"jest za mała liczba")
                
        else:
            print("congratulation!!")
            break
        x += 1
        if x == 11 :
              print("time out")
