for i in range(1,5):
    for j in range(1,5-i+1):
        print(" ",end=" ")
    for k in range(1,i+i):
        print("*",end=" ")
    print()