number = int(input('Введите число от 3 до 20: '))
list_ = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
parol = []
# not_parol = []
for i in range (len(list_)):
#    if i == 1:
#        continue
    for j in range(i+1, len(list_)):
        if list_[i] + list_[j] == number:
            parol.append((list_[i], list_[j]))
#        else:
#           not_parol.append((list_[i] + list_[j])
print(parol)
#print(not_parol)