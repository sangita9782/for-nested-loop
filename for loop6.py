n=int(input("enter"))
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print(k+1,end=" ")
    print()