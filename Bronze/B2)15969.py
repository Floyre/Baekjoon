n = int(input())
score = list(map(int, input().split()))
print(max(score) - min(score))

# 복잡하게 연산자 사용해가며 계산할 필요 없이 그냥 파이썬의 내장 함수를 사용하여 풀면 되는 문제였다.
# 많은 알고리즘 문제에서 내장 함수를 사용하면 편하게 풀 수 있으니 활용하는 것이 중요한 것 같다.