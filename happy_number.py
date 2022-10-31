def add(x):
    s=0
    while x>0:
        r=x%10
        s+=r*r
        x//=10
    if s>4:
        s=add(s)
    return s
x=int(input())
s=add(x)
print(s==1)