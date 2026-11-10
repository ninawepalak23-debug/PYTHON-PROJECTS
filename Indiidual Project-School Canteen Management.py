food_names = ["Samosa", "Sandwich", "Burger", "Pizza", "Juice", "Momos"]
food_prices = [15, 40, 50, 80, 30, 60]
food_items = {'Samosa': 15, 'Sandwich': 40, 'Burger': 50, 'Pizza': 80, 'Juice': 30, 'Momos': 60}

customer_name = []
c_feedback = []
c_rating = []
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

    choice=int(input("\nEnter choice: "))

    if choice==1:
        #Food Menu
        print("------FOOD MENU------")
        for i in range(0,len(food_names)):
            print(food_names[i],"= Rs.",food_prices[i])

    elif choice==2:
        #Search Food Item
        while True:
            f1=input("\nEnter food name to search for(Enter 'done' to exit): ")
            if f1.strip().title()=="Done":
                break
            elif f1.strip().title() in food_names:
                print("This item is available.")
                print("Price of this item is: Rs.",food_prices[food_names.index(f1.strip().title())])
            else:
                print("Sorry, this item is not available.")

    elif choice==3:
        #Add New Food Item in Menu
        while True:
            fi=input("\nEnter new food item to add: ")
            if fi.strip().title() in food_names:
                print("This item already exists.")
            else:
                food_names.append(fi.strip().title())
                p_nf=int(input("Enter price of new item: "))
                food_prices.append(p_nf)
                print("New item added successfully.")
                food_items[fi.strip().title()]=p_nf
            ch=input("Do you want to item (Y/N): ")
            if ch.strip() in "Yy":
                continue
            else:
                break

    elif choice==4:
        #Place an Order
        order = {}
        c_name=input("\nEnter customer name: ")
        print("\nAvailable food items: ")
        for i in range(0, len(food_names)):
            print(food_names[i], "= Rs.", food_prices[i])
        while True:
            ord=input("\nEnter food item(or done to finish): ")
            n_ord= ord.strip().title()
            if n_ord == "Done":
                break
            elif n_ord in food_names:
                quantity=int(input("Enter quantity of food item: "))
                if quantity>0:
                    print("Item added to order")
                    if n_ord in order:
                        order[n_ord] = order[n_ord] + quantity
                    else:
                        order[n_ord] = quantity
                else:
                    print("Quantity must be greater than 0")
            else:
                print("Sorry, this item is not available.")
        #Customer Bill
        print("\n=====CUSTOMER BILL=====")
        print("Customer Name: ",c_name.strip().title())
        total=0
        for k,v in order.items():
            print(k,"x",v,"=",food_items.get(k),"x",v,"= Rs.",food_items.get(k)*v )
            total=total+food_items.get(k)*v
        if total>=200:
            discount=total*(10/100)
        else:
            discount=0
        print("------------------------------------")
        print("Total Amount: Rs.", total)
        print("Total Discount: Rs.", discount)
        print("Final Amount: Rs.",total-discount)
        print("=======================")

    elif choice==5:
        #Give Feedback
        print("\n======CUSTOMER FEEDBACK======")
        customer = input("\nEnter customer name: ")
        feedback=input("Enter feedback: ")
        rating=eval(input("Enter rating from 1 to 5: "))
        if rating>0 and rating<=5:
            c_rating.append(rating)
            c_feedback.append(feedback)
            customer_name.append(customer)
            print("Thank you for your feedback.")
        else:
            print("Rating must be between 1 and 5")

    elif choice==6:
        #Feedback Summary
        print("\n======FEEDBACK SUMMARY======")
        for i in range(len(customer_name)):
            print("Name:",customer_name[i])
            print("Feedback:",c_feedback[i])
            print("Rating:",c_rating[i])
        print("------------------------------------------------")
        print("Total Feedback Entries:",len(c_feedback))
        if len(c_rating)>0:
            print("Average Rating:", (sum(c_rating)) / len(c_rating))
        else:
            print("No Ratings Available")
    elif choice==7:
        #Help and Instructions
        print("\n======HELP AND INSTRUCTIONS======")
        print("1. Select an option from the main menu.")
        print("2. Use Display Food Menu to see available food. ")
        print("3. Use Search Food to find an item's price. ")
        print("4. Use Add New Food to add a food item. ")
        print("5. Select Place Order to order food. ")
        print("6. Enter 'done' to finish ordering. ")
        print("7. Give feedback and a rating from 1 to 5. ")
        print("8. Select Exit to close the program. ")

    elif choice==8:
        #About the project
        print("\n=========ABOUT THE PROJECT=========")
        print("Project: School Canteen Management System ")
        print("Class: XI A")
        print("Subject: Computer Science ")
        print("Language: Python ")
        print("Purpose: To manage basic canteen activities. ")
        print("Project developed by PALAK NINAWE")
        print("================================")
    elif choice==9:
        #Exit the program
        print("Thank you for using the School Canteen Management System")
        break
    else:
        print("Invalid Choice. Please select option from 1 to 9.")