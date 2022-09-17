n=int(input())
c=0
t=0
for i in str(n):
    if int(i)%2==0:
        c+=1
    else:
        t+=1
if c>0 and t==0:
    print("Even")
elif c==0 and t>0:
    print("Odd")
else:
    print("Mixed")
    
    