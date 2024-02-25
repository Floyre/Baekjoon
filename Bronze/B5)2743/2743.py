num_list_x=[]
num_list_y=[]
for i in range(3):
    a,b= map(int,input().split())
    num_list_x.append(a)
    num_list_y.append(b)

for i in range(3):
    if num_list_x.count(num_list_x[i])==1:
        print(num_list_x[i], end=" ")
for i in range(3):
    if num_list_y.count(num_list_y[i])==1:
        print(num_list_y[i])