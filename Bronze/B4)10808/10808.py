A = list(input())

alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
chk = [0]*26

for i in range(len(A)):
    for j in range(len(alp)):
        if(A[i] == alp[j]):
            chk[j]=chk[j]+1

chk =' '.join(map(str,chk))
print(chk)