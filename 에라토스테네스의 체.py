a,b=map(int,input().split())
list2=[True]*(b+1)
list2[1]=False
for i in range(2,int(b**0.5)+1):
    if list2[i]==True:
        for j in range(i+i,b+1,i):
            list2[j]=False
for i in range(a,b+1):
    if list2[i]==True:
        print(i)