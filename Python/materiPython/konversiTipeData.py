print(float(5)) #int to float
print(int(3.6)) #float to int, akan dibulatkan ke bawah
print(str(100)) #int to string
print(bool(1)) #0 = false, 1 = true
print(int("10")) #string to int, harus berupa angka dalam string
print(float("3.14")) #string to float, harus berupa angka dalam string


print(set([1,2,3])) #list to set, akan menghilangkan duplikasi jika ada
print(tuple({5,6,7})) #set to tuple, urutan tidak terjamin karena set tidak berurutan
print(list('hello')) #string to list, akan memecah string menjadi karakter-karakter individual dalam list

# Konversi ke dictionary, menggunakan dict()
# Setiap sublist harus memiliki 2 elemen
# Elemen pertama menjadi key dan elemen kedua menjadi value
print(dict([['age',2],[3,4]])) #list of lists to dictionary
print(dict([(3,26),(4,44)])) #list of tuples to dictionary