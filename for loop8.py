n=int(input("enter"))
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(n-j):
        print(n-j,end=" ")
    print()