import array

#List sebagai array
x = [1, 2, 3, 4, 5]
print(x)

#Array dengan modul array
x = array.array("i",[1, 2, 3, 4, 5])
print(x)
print(type(x))

var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr)

var_arr = [0 for i in range(10)]
print(var_arr)

var_arr = [0 for i in range(10)]
for i in range(10):
    var_arr[i] = i

print(var_arr)