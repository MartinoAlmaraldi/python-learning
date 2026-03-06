var = -1
if var < 0:
    raise ValueError("Bilangan negatif tidak diperbolehkan")
else:
    for i in range(var):
        print(i+1)

for i in range(1, 3):    
    for j in range(1, 3):    
        print(i,j) 