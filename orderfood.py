# title
print("===== Welcome to the Food Pedia =====")

# menu

def menus():
    print("== Select the menu ==")
    print("1. Order food")
    print("2. See menus")
    print("3. See restos")
    print("4. Exit")

menus()

# for see menus
def show_menu():
    for product in menu_category:
        print(product)
    global choose_menu
    choose_menu = input("Choose menu category: ")

# for see restos
def show_resto():
    for location in resto:
        print(location)

user_choose = int(input("Choose menu (1-4): "))


food = ["Soto", "Chicken Satay", "Fried rice", "Hamburger", "Lasagna"]
menu_category = ["Western Food", "Asian Food", "Drinks"]
western_food = ["Burger", "Lasagna", "Steak"]
asian_food = ["Soto", "Chicken satay", "Fried rice"]
Drinks = ["Tea", "Coffee", "Juice"]
resto = ["Indonesia", "Malaysia", "Singapore"]


# condition 1
if user_choose == 1:
    print("== Order Food ==")
    for item in food:
        print(item)
    choose_food = input("Choose the food: ")   
    input_quantity = input("Input the quantity: ")
    print("Your order: ",choose_food, ", Thank you for the order")
    menus()
# condition 2
elif user_choose == 2:
    print("== Our Menu ==")
    show_menu()

    if choose_menu == "western food":
        print(western_food)
        show_menu()
    elif choose_menu == "asian food":
        print(asian_food)
        show_menu()
    elif choose_menu == "drinks":
        print(Drinks)
        show_menu()

# condition 3
elif user_choose == 3:
    show_resto()
    menus()

# condition 4
elif user_choose == 4:
    i = 0
    while i <= 1:
        print("Thank you for the visit this platform")
        break
    print("Have a nice day")

        
    
    
    


