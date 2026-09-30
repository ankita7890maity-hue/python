rows=4
for i in range(1, rows + 1):
    
    for j in range(i):
        print(i, end="")
    
    for j in range(2 * rows - 2 * i):
        print(" ", end="")

    for j in range(i):
        print(i, end="")  
    print()    