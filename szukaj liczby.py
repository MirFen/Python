generator= (element for element in range (100,471) if (element % 7 == 0 and element % 5 != 0))
for item in generator:
    print(item)
    
