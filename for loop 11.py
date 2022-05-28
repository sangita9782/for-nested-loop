n=int(input("enter"))
a=1
for i in range(0,n):
    for j in range(0,i):
       print(a,end=" ")
       a=a+1
    print()