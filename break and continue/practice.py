for i in range(15):
    print("5 x", i + 1, "=", 5 * (i + 1))
    if i == 12:
        break
    elif i == 9:
        continue


list = [1, 3, 5, 7, 9, 10, 11, 13]

for i in list:
    if i == 10:
        break
    print(i)
