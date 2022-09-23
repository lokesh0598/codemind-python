i=int(input())
j=str(i)[::-1]
j=int(j)
j=j**2
k=str(j)[::-1]

if i**2==int(k):
    print("True")
else:
    print("False")
