n=int(input())
m=int(input())
s=0
p=0
for i in range(1,(n//2)+1):
    if n%i==0:
        s+=i
for i in range(1,(m//2)+1):
    if m%i==0:
        p+=i
if p==n and s==m:
    print("Amicable")
else:
    print("Not Amicable")