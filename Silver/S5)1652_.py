import sys

sleep_row, sleep_colum = 0, 0
n = int(sys.stdin.readline())
square = [[0]*n] *n

for i in range(n):
    count = 0
    for j in range(n):
        if square[i][j] == '.':
            count += 1
        else:
            if count >= 2:
                sleep_row += 1
            count = 0
    if count >= 2:
        sleep_row += 1

for j in range(n):
    count = 0 
    for i in range(n):
        if square[i][j] == '.':
            count += 1
        else:
            if count >= 2:
                sleep_colum += 1
            count = 0
    if count >= 2:
        sleep_colum += 1
            
print(sleep_row, sleep_colum)
            
# 2칸씩 구하는 게 아니라 그냥 한 "줄" 에 두칸 "이상"의 "연속"되는 빈칸을 구하는 문제였다.