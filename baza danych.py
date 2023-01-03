dane = {
        "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
        "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
        "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
        "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
        "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
        "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
        "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
        "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'}, 
    }


while (True):
    print("S-search  A-Add  D-Deduct X-Exit: ")
    sellect = input(": ")
    sellect = sellect.capitalize()    

    if sellect == "S":
        print("Name  Age  Sex ID ")
        sellect1 = input(": ")
       

        if sellect1 == "ID":
            
            idIn = input("Podaj ID: ")
            for id,key in dane.items():
                while id == idIn:
                    print("ID", id)
                    for seckey in key:
                        print(seckey,key[seckey])
                    break
                   
            else:
                print("Wrong value")

        elif sellect1 == "Name":
            nameIn = input("Podaj name: ")
            for id,key in dane.items():
                for secKey,name in key.items():
                    while name == nameIn:
                        print("For name:",name,id,key)
                        break
                    
        elif sellect1 == "Age":
            nameIn = int(input("Podaj age: "))
            for id,key in dane.items():
                for secKey,name in key.items():
                    while name == nameIn:
                        print("For Age:",name,id,key)
                        break
                    
        elif sellect1 == "Sex":
            nameIn = input("Podaj sex: ")
            for id,key in dane.items():
                for secKey,name in key.items():
                    while name == nameIn:
                        print("For Sex:",name,id,key)
                        break                  

     
    elif sellect == "A":
        id = input("Insert new ID: ")
        name = input("Insert  name: ")
        age = int(input("Insert  age: "))
        sex = ""
        i = 1
        while i == 1 :
            sex = input("Insert  sex: F/M : ")
            if sex == "F" or sex == "f":
                    sex = "Female"
                    i = 0
            elif sex == "M" or sex == "m":
                    sex = "Male"
                    i = 0
            else:
                 print("Wrong value")
           
            

        if sex == "Female" or sex == "Male":
            dane.update({id:{'name': name, 'age': age , 'sex': sex}})
            print(dane.items())
            

        else:
            print("Wrong value")



    elif sellect == "D":
        idIn = input("Podaj ID: ")
        if idIn in dane:
            del dane[idIn]
            print("Id",idIn,"deleted")
            print(dane)
        else:
            print("Wrong value")


    elif sellect == "X":
       
        print("Goodbye")
        break
    else:
        print("Wrong value")




     

          


