n=int(input())
s=[]
while n>0:
    r=n%10
    n=n//10
    s.append(r)
print(max(s))