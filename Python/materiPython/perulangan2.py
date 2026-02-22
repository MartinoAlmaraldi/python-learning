numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 6:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print("Angka tidak ditemukan.")


count = 0
while count < 3:
    print("Dicoding Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")


n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")


x = 10
if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")


# angka = [1, 2, 3, 4]
# pangkat = []
# for n in angka:
#   pangkat.append(n**2)
# print(pangkat)

angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)

