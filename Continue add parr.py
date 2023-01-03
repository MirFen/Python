i = 0
s = 0
while i < 3:
    value = int(input("Tap the value: "))
    if (value > 0):
        s += value
    else:
        print("incorect value")
        continue
    i += 1
print("suma to:", s)


