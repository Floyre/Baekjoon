# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.

A = list(input())

alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
chk = [0]*26

for i in range(len(A)):
    for j in range(len(alp)):
        if(A[i] == alp[j]):
            chk[j]=chk[j]+1

chk =' '.join(map(str,chk))
print(chk)