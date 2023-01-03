login1 = input("Log ")
login = login1.capitalize()
if (login == "Log"):
        while login == "Log":

            choose = input("* - multiplication / division - subtraction + addition ** exponentiation: ")

            if (choose == "*" or choose == "**" or choose == "/" or choose == "+" or choose == "-" or choose == "%"):
                a = int(input("type parameter a: "))
                b = int(input("type parameter b: "))

                if (choose == "*"):
                        print(a * b)
                elif (choose == "**"):
                    print(a ** b)
                elif (choose == "/"):
                    if (b == 0):
                        print("You type zero")
                    else:
                        print(a / b)
                elif (choose == "-"):
                    print(a - b)
                elif (choose == "+"):
                    print(a + b)
                else:
                    print(a % b)
            else:
                print("Incorect value")
                login = input("Log? ")
       
else:
     print("Incorect value")

