a = int(input())
b = list(map(int,input().split()))
c = [0]*a

for i in range(1,a):
    # (B의 현재 항 * 현재 항의 위치) - 이전 A 항들의 합계 = A의 현재 항
    d = d + b[i]
    c[i] = d / i

print(c)
# 수열 A 가 1,3,2,6,8 이라면 수열 B는 1/1, (1+3)/2, (1+3+2)/3 