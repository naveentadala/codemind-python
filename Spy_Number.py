n=int(input())
s=0
d=1
while n>0:
    r=n%10
    s=s+r
    d=d*r
    n=n//10
if s==d:
    print("Spy Number")
else:
    print("Not Spy Number")