import numpy 
matriks = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
            
print(matriks)
#ini agak makan memori


matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
print(matriks)  
#biar lebih efisien memori dan lebih cepat, bisa juga untuk array
import sys
var_list= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var_array= numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])

print("Ukuran keseluruhan elemen list dalam bytes = ",sys.getsizeof(var_list)*len(var_list))
print("Ukuran keseluruhan elemen NumPy dalam bytes = ", var_array.size*var_array.itemsize)
