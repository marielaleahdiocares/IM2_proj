while True: 
    rows = int(input("Enter number of rows: "))
    column = int(input("Enter number of column: "))

    if rows == 0 or column == 0:
        print ("Program stopped, Bye!")
        break
    

    search = (int(input("Enter number to search: ")))
    
    for i in range(1, rows +1):
        for j in range(1, column +1):
            print (i * j, end ="\t")
        print ()


    print ("\nMultiplication Table:\n")
    found = False

    for i in range (1, rows +1):
        for j in range (1, column + 1):
            val = i * j  
            if val == search:
                print(f"[{val}]", end ="\t")
                found = True
            else:
                print (val, end="\t")
        print() 

    if found: 
        print(f"\n {search} was found in the table.\n")
    else: 
        print(f"\n {search} was not found in the table.\n")