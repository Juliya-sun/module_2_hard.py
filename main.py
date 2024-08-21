number = int(input('Введите число от 3 до 20: '))
a = number
list_ = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
parol = []
not_parol = []
for i in list_:
    if i == 1:
        continue
    is_parol = True
    for j in range(2, 21):
        if i // j == 0:
            is_parol = False
            break
    if is_parol:
        parol.append([i])
    else:
        not_parol.append(i)
print(parol)