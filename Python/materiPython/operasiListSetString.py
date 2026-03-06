# len(), Intinya untuk menghitung jumlah item dalam suatu list, set, atau string
#operasi pada list
my_list = [1, 2, 3, 4, 5]
print(len(my_list)) # Output: 5
#operasi pada set
my_list = set([1, 2, 3, 4, 5])
print(len(my_list)) # Output: 5
#operasi pada string
my_string = "Hello, World!"
print(len(my_string)) # Output: 13


#min max
angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))

#count, untuk menghitung jumlah kemunculan suatu item dalam list atau string
genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6)) # Output: 3

string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring)) # Output: 6

#in and not in
kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat) # Output: True
print('tidak' in kalimat) # Output: False
print('Dicoding' not in kalimat) # Output: False
print('tidak' not in kalimat) # Output: True

#nilai untuk multiple variable
data = ['shirt', 'white', 'L']
apparel, color, size = data

print(data)
print(apparel)
print(color)
print(size)

#sort
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()
print(kendaraan)
kendaraan.sort(reverse=True)
print(kendaraan)
#Metode sort tidak dapat mengurutkan list yang memiliki angka dan string sekaligus di dalamnya   