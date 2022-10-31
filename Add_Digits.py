a=int(input())
t=a
L=0
s=0
while a>0:
    L+=1
    a//=10
while L>1:
    while t>0:
        b = t%10
        s+=b
        t//=10
    t = s
    st =str(s)
    L = len(st)
    s = 0
print(t)