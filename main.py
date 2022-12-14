#print("Введите количество строк и столбцов: ")
b = input()
a = list(map(int, b.split()))
m = a[0]
n = a[1]
if m < 1 or m > 100 or n < 1 or n > 100:
	print(0)
	exit()
mas = [0] * m
for i in range(m):
    mas[i] = [0] * n
if m % 2 == 0:
    Z = 1
    for i in range(0, m - 1, 2):
        for l in range(n):
            mas[i][l] = mas[i+1][l] = Z
            Z = Z + 1
else:
    Z = 1
    for i in range(0, m - 2, 2):
        for l in range(n):
            mas[i][l] = mas[i + 1][l] = Z
            Z = Z + 1
    for l in range(0, n - 1, 2):
        mas[m-1][l] = mas[m-1][l+1] = Z
        Z = Z + 1

for xx in mas:
    st = ' '.join(str(x) for x in xx)
    print(st)