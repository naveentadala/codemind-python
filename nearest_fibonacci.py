n=int(input())
a=0
b=1
c=0
while b<n:
    c=a+b
    a=b
    b=c
if n-a < c-n:
    print(a)
elif n-a > c-n:
    print(c)
else:
    print(a,c)