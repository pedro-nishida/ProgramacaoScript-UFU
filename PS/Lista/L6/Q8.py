n = int(input())
i = 0
j = 0
while j < n:

    while i < n:

        if i != j:
            print("*",end=" ")
        else:
            print("+",end=" ")
        i += 1    
    
    j += 1
    i = 0
    print("")
