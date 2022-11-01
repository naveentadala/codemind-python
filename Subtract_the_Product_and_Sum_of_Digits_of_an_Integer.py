n=int(input())
p=1
s=0
while n>0:
    r=n%10
    s+=r
    p*=r
    n//=10
print(p-s)