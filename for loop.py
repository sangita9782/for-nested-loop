n=int(input("enter n"))
for i in range(n):
    for j in range(n-i):
        print(n-j,end=" ")
    print()