n=int(input())
t=0
while n>9:
    for i in str(n):
        t=t+int(i)
    n=t
    t=0
print(n)