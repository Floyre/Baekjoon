# 이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
# N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.
# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.
# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.

from itertools import combinations

n, m = map(int,input().split())
total = 0
card = list(map(int, input().split()))
com = list(combinations(card, 3))

for i in com:
    if sum(i) <= m: # 모든 경우의 수 조합 세가지의 총합이 m 이하인가?
        total = max(total, sum(i))  #total에 루프 돌면서 최대값 할당
print(total)

# combinations 라는 파이썬 내장 함수에 대해 알게 되었다.
# https://seu11ee.tistory.com/5

# 시간 복잡도
# https://hanamon.kr/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-time-complexity-%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84/

# 최빈값/근사값
# https://designingdata.tistory.com/68

# combinations 함수 말고도 n n-1 n-2 루프를 통해서도 가능하다.