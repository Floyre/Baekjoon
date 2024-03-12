import sys

b_alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
s_alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
blank = [' ']

s = list(sys.stdin.readline().rstrip())
code = []

for i in s:
    if i in b_alp: #대문자
        checker = 0
        checker = b_alp.index(i) + 13
        if(checker >= 26):
            checker-=26
        code.append(b_alp[checker])
    elif i in s_alp: #소문자
        checker = 0
        checker = s_alp.index(i) + 13
        if(checker >= 26):
            checker-=26
        code.append(s_alp[checker])
    elif i in blank:
        code.append(blank[0])
    else:
        code.append(i)

code = ''.join(code)
print(code)

# 오답 1 - 문제가 되는 부분을 소문자 부분에서만 해결하고 대문자 부분을 해결하지 않은 상태로 제출하였다.
# 오답 2 - 기존 입력받는 부분이 sys.stdin.readline().strip()이였는데, 첫 글자에 공백이 주어질수도 있는 문제같은 경우는 
#          .strip()이 양 끝 공백을 싹 지워버리기 때문에 문제가 생긴다.

# 첫째 줄에 알파벳 대문자, 소문자, 공백, 숫자로만 이루어진 문자열 S가 주어진다. S의 길이는 100을 넘지 않는다.

