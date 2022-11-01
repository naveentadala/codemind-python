def pal(x):
    i=0
    k=x
    while x>0:
        r=x%10
        i=i*10+r
        x//=10
    if i==k:
        return 1
    else:
        return 0
x=int(input())
y=int(input())
for i in range(x,y+1):
    if pal(i)==1:
        print(i,end=' ')
            
