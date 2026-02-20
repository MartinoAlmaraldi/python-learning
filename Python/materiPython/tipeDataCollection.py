#List, List Python tidak mengharuskan memiliki tipe data yang sama di dalamnya, sedangkan array sebaliknya. 
variable_list = [1, "Dicoding", True, 3.14]
print(type(variable_list))


#Slicing list
sl = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(sl[0:5:2])
print(sl[1:])
print(sl[:3])

#Tuple, Tuple adalah tipe data yang tidak bisa diubah setelah dibuat (immutable). 
#Tuple menggunakan tanda kurung () sedangkan list menggunakan tanda kurung siku [].
a = (1, "Dicoding", 1+3j)
print(type(a))

#Set, Set adalah tipe data yang tidak berurutan (unordered) dan tidak mengizinkan duplikasi.
s = {1,2,7,2,3,13,3}
print(s)
print(type(s))
#print(s[0]) #akan error karena set tidak berurutan

#method union & intersection pada set
set1 = {1, 2, 3}
set2 = {3, 4, 5}

#union
union = set1.union(set2)
print("Union: ", union)

#intersection
intersection = set1.intersection(set2)
print("Intersection: ", intersection)

#Dictionary, Dictionary adalah tipe data yang menyimpan pasangan key-value.
d = {'name': 'Tino', 'Age': 20, 'isStudent': True}
d['Job'] = 'Engineer' #menambahkan key-value baru ke dalam dictionary
print(d)
print(type(d))
print(d['name']) # Ga bisa indexing seperti list, harus menggunakan key untuk mengakses value
del d['isStudent'] #menghapus key-value dari dictionary
d['name'] = 'Martino' 
print(d)

