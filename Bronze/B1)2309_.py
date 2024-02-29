from itertools import combinations

input_list = [0]*9
for i in range(9):
    input_list[i] = int(input())
com = list(combinations(input_list,7))

success = []
j=0
for i in com:
    if sum(i) == 100:
        success = sorted(com[j])
    j+=1

for i in range(7):
    print(success[i])

#2798 블랙잭 문제와 비슷하게 combinations 함수를 사용하여 총합 100이 가능한 배열을 찾으면 되는 문제이다.