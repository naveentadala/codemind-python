def rev(x):
    i=0
    while x>0:
        r=x%10
        i=i*10+r
        x=x//10
    return i
x=int(input())
r=rev(x)
k=0
i=0
while r>0:
    s=r%10
    if s<9:
        k+=1
    if s<9 and k==1:
        s=9
    i=i*10+s
    r=r//10
print(i)