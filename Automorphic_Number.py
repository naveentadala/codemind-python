n=int(input())
t=n
s=n*n
length=0
while n>0:
    length=length+1
    n//=10
    b=s%(10**length)
if t==b:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")