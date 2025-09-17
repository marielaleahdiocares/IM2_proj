mydict = {}

size = int(input("Enter Matrix size: "))

for i in range(size):
    item = input(f"Shopping items {i}: ")
    mydict[i] = item

print(f"\n You have {size} items in your cart")

while True: 
    option= input("\n[A] Add [C]hange  [R]emove [D]isplay [S]earch [*] Exit: ").upper()

    if option == "D":
        print("\nKey\tItem") 
        for key in mydict:
            print(f"{key}\t{mydict[key]}")
    
    elif option == "S":
        search = input("Enter item name: ")
        found = False
        for key, value in mydict.items():
            if value.lower()==search.lower():
                print(f"Found {value} item ")
                found = True
        if not found:
            print("I'm sorry not in the cart")
    
    elif option == "R":
        key =int(input('Enter key to remove: '))
        if key in mydict:
            print(f"The key {key} with value {mydict[key]} has been deleted")
            del mydict[key]
        else:
            print ("Key not found")
    
    elif option == "C":
        key = int(input("Enter key to change: "))
        if key in mydict:
            print(f"Found {mydict[key]} item")
            new_item = input("Enter new item: ")
            mydict [key] = new_item
            print(f"The key {key} has been updated to {new_item}")
        else:
            print ("I'm sorry not in the cart")

    elif option == "A":
        new_key = max(mydict.keys(), default=-1) + 1 
        new_item = input("Enter new item to add: ")
        mydict[new_key] = new_item
        print(f"Item '{new_item}' added with key {new_key}")

    elif option == "*":
        print("Bye!")
        break

        