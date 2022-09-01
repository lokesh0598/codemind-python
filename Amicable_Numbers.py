n=int(input())
m=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
add=0
for j in range(1,m):
    if m%j==0:
        add+=j
if (sum==m) or (add==n):
    print("Amicable")
else:
    print("Not Amicable")