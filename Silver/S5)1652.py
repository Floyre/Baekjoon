import sys

sleep_row, sleep_colum = 0, 0 # 가로, 세로 열의 수면 가능한 자리 갯수 변수 선언
n = int(sys.stdin.readline()) # n x n 배열 생성을 위한 n 변수 선언
square = [[0]*n] *n # n x n 배열 선언

for i in range(n):
    a = list(sys.stdin.readline().rstrip())
    square[i] = a

for i in range(n): #세로 열 루프
    count = 0
    for j in range(n): # 가로 열 루프
        if square[i][j] == '.': #만약 해당 칸이 빈 공간 ('.')이면 빈공간 카운트에 1 추가
            count += 1
        else: #만약 해당 칸이 짐 ('X')이면 검사
            if count >= 2: # 빈 공간이 2칸 이상였으면 잘 수 있는 공간에 1추가
                sleep_row += 1
            count = 0 
    if count >= 2:
        sleep_row += 1

for j in range(n): #가로 열 루프
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
            
# 0000X = 자리는 1개
# 00X00 = 자리는 2개
# 바보같이 다 맞춰 놓고 입력받는 부분을 구현해놓지 않은 상태로 제출해서 나온 오답이였다.