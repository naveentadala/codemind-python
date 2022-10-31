def self_dividing(x):
    s=x
    while x>0:
        r=x%10
        if r==0:
            return 0
        if s%r!=0:
            return 0
        x=x//10
    else:
            return 1
x=int(input())
y=int(input())
for i in range(x,y+1):
    if self_dividing(i)==1:
        print(i,end=' ')