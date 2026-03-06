var_list = [1,2,3,4,5,6,7,8,9,10]
for i in var_list:
    print(i)

for i in range(10):
    print(i)

for i in range(1,10,2): #start, stop, step
    print(i)

counter = 1
while counter <= 5:
    print(counter)
    counter += 1    # Increment


for i in range(1, 3):
    for j in range(1, 3):
        print(i,j)

for i in range(2):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 2:
            break  # Menghentikan perulangan dalam jika j = 2

for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))

for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))