n=int(input())
t=0
while n>9:
    for i in str(n):
        t=t+int(i)**2
    n=t
    t=0
if n==1 or n==7:
    print("True")
else:
    print("False")