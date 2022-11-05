n=int(input())
a=n*n
k=str(n)
s=""
for i in range (len(k)):
    
    r=a%10
    a=a//10
    
    s+=str(r)
    
if str(n)==s[::-1]:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")