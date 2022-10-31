n=int(input())
x=0
for i in range(1,n):
    if n%i==0:
        x+=i
if x==n:
    print('True')
else:
    print('False')