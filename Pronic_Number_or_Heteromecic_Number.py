n=int(input())
p=0
for i in range(2,n):
    
    if i*i+1*i==n:
        p=i
if p*(p+1)==n:
    print("YES")
else:
    print("NO")