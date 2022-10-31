x=int(input())
a=0
b=1
x-=2
print(a,b,end=' ')
while x>0:
    c=a+b
    x-=1
    a=b
    b=c
    print(c,end=' ')