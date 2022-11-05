a,b=map(int,input().split())
if a>b:
    g=a
else:
    g=b
for i in range(1,g):
    if a%i==b%i==0:
        h=i
lcm=a*b//h
print(lcm)