# 다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다. c는 1로, d는 2로, ..., C를 8로 바꾼다.
# 1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.
# 연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.

num = list(map(int, input().split(" ")))
if(num == sorted(num)):
    print("ascending")
elif(num == sorted(num,reverse=True)):
    print("descending")
else:
    print("mixed")

# sorted라는 파이썬 내장 함수에 대해 알게 되었다.
# 복잡하게 할 필요 없이 파이썬 내장 함수인 sorted를 이용해 비교하면 쉽게 풀 수 있는 문제다.