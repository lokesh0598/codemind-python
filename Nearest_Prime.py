
t=int(input())
for _ in range(t):
    n=int(input())
    b=0
    if True:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                b+=1
    if b==0:
        print(n)
    else:
        k=a=n
        count=0
        while count<=2:
            for i in range(1,n+2):
                if (n+1)%i==0:
                    count+=1
            if count==2:
                x=n+1
        
                break
            n+=1
            count=0

        c=0
        while c<=2:
            for j in range(1,a):
                 if (a-1)%j==0:
                    c+=1
            if c==2:
                y=a-1
        
                break
            a-=1
            c=0

        if (x-k)<(k-y):
            print(x)
        else:
            print(y)

            