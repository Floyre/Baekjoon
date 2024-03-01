A, B, C = map(int, input().split())
parking_time = [0] * 101

for i in range(3):
    start, end = map(int, input().split())
    for j in range(start, end):
        parking_time[j] += 1

total= 0
for time in parking_time:
    if (time == 1):
        total += A * time
    elif (time == 2):
        total += B * time
    elif (time == 3):
        total += C * time

print(total)

# 문제에서 주어진 조건인 '입력으로 주어지는 시간은 1과 100사이 이다.'를 사용해 최초 100개의 배열을 선언해준 뒤,
# 입력받은 입차/출차 시간 만큼의 루프를 돌려 해당되는 시간대에는 변수에 1을 더해주는 방식으로 해당 시간대에 얼마나 많은 차량이 주차되있는지 검사 후 결과를 출력한다.