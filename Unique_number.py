n=int(input())
s=[]
while n>0:
    r=n%10
    s.append(r)
    n//=10
for i in s:
    if s.count(i)!=1:
        print('Not Unique Number')
        break
else:
    print('Unique Number')