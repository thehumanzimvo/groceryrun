sizeOfShape = 6
xCentre = 30
yCentre = 9

buns = 5
# for i in range(1, buns+1):
#     for j in range(2):
#         print(i, end='')
#     print('j')

# 79
# 25 down
rows = [i for i in range(1, 80)]
columns = [i for i in range(1, 26)]

for midas in columns:
    for sisyphus in rows:
        if sisyphus%10 == 0:
                print(int(sisyphus/10), end='')
        else:
            print('=', end='')
    print('')