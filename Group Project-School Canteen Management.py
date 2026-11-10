# Creating lists
food_names = ["Samosa", "Sandwich", "Burger", "Pizza", "Juice", "Momos"]
food_prices = [15, 40, 50, 80, 30, 60]
customer_name = []
c_feedback = []
c_rating = []
# Creating Dictionary
food_items = {'Samosa': 15, 'Sandwich': 40, 'Burger': 50, 'Pizza': 80, 'Juice': 30, 'Momos': 60}
#Main Menu
while True:
    print("\n=============================")
    print("SCHOOL CANTEEN MANAGEMENT SYSTEM")
    print("=============================")
    print("1. Display Food Menu")
    print("2. Search Food Item")
    print("3. Add New Food Item")
    print("4. Place Order and Customer Bill")
    print("5. Give Feedback")
    print("6. Feedback Summary")
    print("7. Help and Instructions")
    print("8. About the Project")
    print("9. Exit")

    choice = int(input("\nEnter choice: "))

    if choice==1:
        #Displaying Food Menu
        print("\n------FOOD MENU------")
        for i in range(0, len(food_names)):
            print(food_names[i], "= Rs.", food_prices[i])

    elif choice == 2:
        #Searching food items
        name=input("\nEnter food name to search(or done to finish): ")
        name=name.strip().title()
        if name in food_items:
            print("Food item is available.")
            print("Price: Rs.", food_items[name])
        elif name=="Done":
            break
        else:
            print("Food item is not available.")

    elif choice==3:
        #Adding new food item
        new_name=input("\nEnter new food name to add(or done to finish): ")
        new_name=new_name.strip().title()
        found=False
        for item in food_items:
            if item == new_name:
                found = True
                print("Food item already exists!")
            elif new_name=="Done":
                break
            else:
                price = int(input("Enter price: "))
                if price>0:
                    food_names.append(new_name)
                    food_prices.append(price)
                    food_items[new_name]=price
                    print("Food item added successfully!")
                    # Display Updated Menu
                    print("\n------UPDATED FOOD MENU------")
                    for item in food_items:
                        print(item, "-Rs.", food_items[item])
                else:
                    print("Price must be greater than zero!")