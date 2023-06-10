d = []
for i in range(10):   
    d.append([])
    for j in range(10):
        d[i].append(0)

for i in range(10):
    a = input().split()
    for j in range(10):
        d[i][j] = int(a[j])

x = 1
y = 1
d[x][y] = 9
while True:
    if   y < 9 and d[x][y+1]%2 == 0:
        y += 1
    elif x < 9 and d[x+1][y]%2 == 0:
        x += 1
    else:
        break

    if d[x][y] == 2 or ( x * y == 81):
        d[x][y] = 9
        break
    else:
        d[x][y] = 9


for i in range(10):
    for j in range(10):
        print(d[i][j], end=" ")
    print('')

