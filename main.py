n=int(input("Enter No. of Stone"))
s=0
f=0
for i in range(1,n+1):
    s=s+i
    if n>=s:
        n=n-s
        f=i
    else:
        break
print(f)
        