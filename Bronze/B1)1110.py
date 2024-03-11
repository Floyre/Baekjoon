# 만약 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다
# 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.

# 1. if(a<10): - [0,9] -> 0+9 = 9
# 2. 9 + 9 = 18
import sys
new_num = [0]*2

count = 1
num = int(sys.stdin.readline()) # 0보다 크거나 같고, 99보다 작거나 같은 정수가 주어진다.
initnum = num

while(True):
    num = str(num)
    num = list(num) # 입력받은 정수를 [0,0] 또는 [0] 으로 분리
    num = list(map(int,num))
    
    if(len(num) < 2): # 만약 입력받은 num이 10 미만이라면
        num.insert(0,0)
    
    temp = list(str(sum(num)))
    temp = list(map(int,temp))
    
    new_num[0] = num[1] # 새로운 수의 십의 자리 수(new_num[0])는 주어진 수(num)의 가장 오른쪽 자리 수 (num[1])
    
    if(len(temp) < 2): # 만약 주어진 수(num)의 십의 자리 수(num[0])과 일의 자리 수(num[1])를 더한 값이 10 미만이라면
        new_num[1] = temp[0]
    else:
        new_num[1] = temp[1]
    # 여기서 새로운 수가 생성됨 new_num[0] , new_num[1]
    
    new_num = ''.join(map(str,new_num))
    new_num = int(new_num)  
    
    if(initnum == new_num):
        break
    
    num = new_num
    new_num = [0]*2
    count +=1

print(count)