x=int(input())
a=0
b=1
c=0
while b<x:
    c=a+b
    a=b
    b=c
print(x==c)