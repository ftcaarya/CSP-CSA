# Enter your code here

STARTING_ITEMS_IN_INVENTORY = 20
num_items = STARTING_ITEMS_IN_INVENTORY

while num_items >= 0:
    
    print(f"We have {num_items} items in inventory.")
    sub = int(input("How many would you like to buy? "))
        
    if sub <= num_items:
        if num_items - sub == 0:
            print("All out!")
            break
        else:
            print(f"Now we have {num_items - sub} left.")
            
        num_items -= sub
    else:
        print("There is not enough in inventory for that purchase.")