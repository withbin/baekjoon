'''
    1 1 #0
    2 1 1#0
    3 1 1 1 #1
    4 1 2 1 
    5 1 2 1 1 #1            # 1 1 2 2 3 3 4 4 5 5
    6 1 2 2 1               # 1 2 3 4 5 6 7 8 9 10
    7 1 2 2 1 1 #2
    8 1 2 2 2 1
    9 1 2 3 2 1
    10 1 2 3 2 1 1 #2
    11 1 2 3 2 2 1
    12 1 2 3 3 2 1
    13 1 2 3 3 2 1 1 #3

x=5
2+4 두번째 집단
집단 크기에서 -x 끝에서 2번째
2보다 작으니까 4
x=7
2+4+6 세번째 집단
집단 크기에서 -x 끝에서 6번째
3보다 크니까 5
x=13
2+4+6+8 네번째 집단
집단 크기에서 -x 끝에서 8번째
3보다 크니까 5'''
a=int(input())
for i in range(0,a):
    lo1, lo2 =map(int,input().split())
    x=lo2-lo1
    b=2
    big=0
    count=0
    while x>big:
        big=big+b
        b=b+2
        count=count+1
    big=big-x+1
    if big<=count:
        print(count*2)
    else:
        print(count*2-1)