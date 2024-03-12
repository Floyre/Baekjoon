# https://www.acmicpc.net/problem/2816

import sys

n = int(sys.stdin.readline())
choosen = 0
temp = 0
ch = [0] * n
btn = []

for i in range(n):
    ch[i] = sys.stdin.readline().rstrip()

while(True):
    if(ch[0] == "KBS1"): # KBS1 Allocation Check
        break
    else:
        if(ch[choosen] != "KBS1"):
            choosen+=1
            btn.append(1)
        elif(ch[choosen] == "KBS1"):
            while(True):
                if(ch[0] == ("KBS1")):
                    break
                else:
                    temp = ch[choosen-1]
                    ch[choosen-1] = ch[choosen]
                    ch[choosen] = temp
                    btn.append(4)
                    choosen -=1
                    
choosen = 0
temp = 0

while(True):
    if(ch[1] == "KBS2"): # KBS2 Allocation Check
        break
    else:
        if(ch[choosen] != "KBS2"):
            choosen+=1
            btn.append(1)
        elif(ch[choosen] == "KBS2"):
            while(True):
                if(ch[1] == ("KBS2")):
                    break
                else:
                    temp = ch[choosen-1]
                    ch[choosen-1] = ch[choosen]
                    ch[choosen] = temp
                    btn.append(4)
                    choosen -=1
                    
btn = ''.join(map(str,btn))
print(btn)

