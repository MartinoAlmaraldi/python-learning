#immutable data types, data yang tidak bisa diubah setelah dibuat
#contoh: string, tuple, frozenset, int, float, bool. Cuma membuat id baru jika kita membuat variabel baru dengan nilai yang sama
var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))

#formatted string
name = "John"
print(f"Hello, {name}!")
#str.format()
print("Hello, {}!".format(name))
