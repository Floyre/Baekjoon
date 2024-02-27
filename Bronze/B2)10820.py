# 문자열 N개가 주어진다. 이때, 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 개수를 구하는 프로그램을 작성하시오.

M = [] 
while True:
    try:
        line = input()
        if not line:
            break
        l_c, u_c, d_c, s_c = 0, 0, 0, 0  
        for j in line:
            if j.islower():
                l_c +=1
            elif j.isupper():
                u_c +=1
            elif j.isdigit():
                d_c +=1
            elif j.isspace(): #Return Bool
                s_c +=1
        M.append([l_c, u_c, d_c, s_c])  # 리스트에 추가
    except EOFError:
        break


for c in M:
    print(*c)


#'몇'개의 입력을 받아야 하는지 제공되지 않는 점을 간과하여 오답이 많이 나왔다.
# if not 을 통해 입력받은 내용이 없다면 진행할 수 있는 것과, While -> Try -> EOFError의 사용법을 알게 되었다.
# 처음에는 깡 코딩으로 해결하려 했지만 알고 보니 islower, isupper 과 같은 파이썬 내장 함수를 이용화여 푸는 문제였다.

# print(*counts)에서 사용된 * 연산자는 Python에서 'unpacking' 연산자로 사용됩니다. 
# 이 연산자는 리스트, 튜플, 집합, 사전 등의 iterable(반복 가능한 객체)을 함수의 인자로 전달할 때 사용되며, 해당 iterable의 각 요소를 개별 인자로 '풀어서' 전달합니다.