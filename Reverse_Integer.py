n=int(input())
r=0
x=0
if n<0:
    n=abs(n)
    while n>0:
        x=n%10
        r=r*10+x
        n=n//10
    print(-r)
else:
    while n>0:
        x=n%10
        r=r*10+x
        n=n//10
    print(r)

    