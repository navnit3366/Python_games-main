from random import randint
a,b,c,d = randint(0,9),randint(0,9),randint(0,9),randint(0,9)
print("Загадано 4-значное число")

spisok = []
listik = []

spisok.append(a)
spisok.append(b)
spisok.append(c)
spisok.append(d)

for i in range(9):
    bull = 0
    cow = 0
    q = int(input("Введите число 0 - 9: "))
    w = int(input("Введите число 0 - 9: "))
    e = int(input("Введите число 0 - 9: "))
    r = int(input("Введите число 0 - 9: "))
    listik.append(q)
    listik.append(w)
    listik.append(e)
    listik.append(r)
    print(listik)

    if listik[0] == spisok[0]:
        bull += 1
    elif listik[0] != spisok[0] and (listik[0] == spisok[2] or listik[0] == spisok[1] or listik[0] == spisok[3]):
        cow += 1
    else:
        cow = 0
        bull = 0
    if listik[1] == spisok[1]:
        bull += 1
    elif listik[1] != spisok[1] and (listik[1] == spisok[2] or listik[1] == spisok[0] or listik[1] == spisok[3]):
        cow += 1
    else:
        cow = 0
        bull = 0
    if listik[2] == spisok[2]:
        bull += 1
    elif listik[2] != spisok[2] and (listik[2] == spisok[3] or listik[2] == spisok[1] or listik[2] == spisok[0]):
        cow += 1
    else:
        cow = 0
        bull = 0
    if listik[3] == spisok[3]:
        bull += 1
    elif listik[3] != spisok[3] and (listik[3] == spisok[2] or listik[3] == spisok[1] or listik[3] == spisok[0]):
        cow += 1
    else:
        cow = 0
        bull = 0
    print(bull,cow)
    if bull == 4:
        print("Вы победили")
        break
    elif bull != 4:
        print("Вы потеряли попытку")
        listik = []
if bull != 4:
    print("Вы проиграли!((")
    print("Загаданное число было:")
    print(a, b, c, d)

