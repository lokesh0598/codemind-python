n=int(input())
p=1
s=0
for i in str(n):
    p=p*int(i)
    s+=int(i)
print(p-s)