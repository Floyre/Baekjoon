a = int(input(""))
i = 0

if((a-1)%3 == 0 or (a-1)%2 == 0):
        i+=1
        a=a-1
while a!=1:
    if(a%3 == 0):
        i = (a/3)
        a = (a-(3*(a/3)))+1
    elif(a%2 == 0):
        i = (a/2)
        a = (a-(2*(a/2)))+1

print(i)