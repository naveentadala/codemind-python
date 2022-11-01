n=int(input())
e=0
o=0
i=0
while n>0:
    r=n%10
    if r%2==0:
        e+=1
    elif r%2!=0:
        o+=1
    n//=10
    i+=1
if i==e:
    print('Even')
elif i==o:
    print('Odd')
elif o+e==i:
    print('Mixed')