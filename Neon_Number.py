n=int(input())
s=0
for i in str(n*n):
    s+=int(i)
if n==s:
    print("Neon Number")
else:
    print("Not Neon Number")