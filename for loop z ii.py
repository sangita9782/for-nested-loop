for i in range(1,6):
    for j in range(1,6-i+1):
        print(" ",end=" ")
    for k in range(i,-1,-1):
        print(k,end=" ")
    for m in range(2,i+1):
        print(m,end=" ")
    print()