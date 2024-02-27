
N, M = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

C = A + B
C.sort()

answer = ' '.join(map(str,C))
print(answer)

#불필요한 Sorting 함수 사용 아닌 Python 자체 내장 sort 함수를 사용하여 푸는 문제.
#' '.join을 통해 리스트를 하나의 문자열로 만든다. .join 함수는 정수형이 아닌 문자열에서만 사용 가능하므로 map(str,C) 를 통해 변환해 준다.