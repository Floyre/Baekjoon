import time

a = int(input(""))
i = 0

start = time.perf_counter()
if((a-1)%3 == 0 or (a-1)%2 == 0):
        i+=1
        a=a-1
while a!=1:
    if(a%3 == 0):
        i+=1
        a=a/3
    elif(a%2 == 0):
        i+=1
        a=a/2
print(i)
end = time.perf_counter()

print(f"{end - start:.5f} sec")
