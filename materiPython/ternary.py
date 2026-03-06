#Ternary operator adalah sebuah operator yang memungkinkan kita untuk menulis sebuah kondisi dalam satu baris kode
#Operator ini memiliki sintaks sebagai berikut:
#value_if_true if condition else value_if_false

lulus = True
print("selamat") if lulus else print("perbaiki")

#Tuple
lulus = True
#jika salah sebelah kiri, jika benar sebelah kanan
kelulusan = ("Perbaiki, Anda belum lulus.","Selamat, Anda lulus!")[lulus]
print(kelulusan)