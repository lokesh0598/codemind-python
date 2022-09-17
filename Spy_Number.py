n=int(input())
p=1
s=0
for i in str(n):
    p*=int(i)
    s+=int(i)
if p==s:
    print("Spy Number")
else:
    print("Not Spy Number")
