import datetime

RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
PURPLE = "\033[35m"
CYAN   = "\033[36m"
RESET  = "\033[0m"


print(CYAN + " Welcome to the Inventory System ".upper().center(50, "★") + RESET)

def login():
    security = 0
    while security < 3:
        user_email = input("\n[ID] Please enter your email: ")
        user_password = input("[PASS] Enter your password: ")
        
        if user_email == "mabwans73@gmail.com" and user_password == "0":
      
            print(GREEN + "\nAccess Granted: Administrator Control Center".title() + RESET)
            print(GREEN + "You may now proceed to manage the inventory.\n" + RESET)
            break
        else:
            security += 1
            remaining = 3 - security
        
            if user_email != "mabwans73@gmail.com" and user_password != "0":
                print(RED + f" ERROR: INVALID CREDENTIALS ({remaining} Left) ".center(40, "-") + RESET)
            elif user_email != "mabwans73@gmail.com":
                print(RED + f" ERROR: INVALID EMAIL ({remaining} Left) ".center(40, "-") + RESET)
            else:
                print(RED + f" ERROR: INVALID PASSWORD ({remaining} Left) ".center(40, "-") + RESET)

    if security == 3:
        print(RED + "\nSecurity Alert: System Terminated".upper().center(50, "!") + RESET)
        exit()
            
print(BLUE + "\n[USER LOGIN]" + RESET)
check_enter = input("Are you a Guest (G) or an Authorized User (U): ").upper()

if check_enter == "G":
    print(YELLOW + "Logged in as Guest: Temporary Access Enabled." + RESET)
    user_key = "guest"
else:
    login()
    user_key = "authorized user"

def get_inventory_data():
    product_names = []
    product_prices = []
    while True: 
        try: 
            many_products = int(input(PURPLE + "\nHow many items would you like to add? " + RESET))
            current_step = 1 
            break
        except ValueError:
            print(RED + "INPUT ERROR: Please enter numbers only." + RESET)

    while current_step <= many_products:
        name = input(f"\nItem #{current_step} - Name: ")
        try:
            price = float(input(f"Item #{current_step} - Unit Price ($): "))
            product_names.append(name)
            product_prices.append(price)
            current_step += 1
        except ValueError:
            print(RED + "DATA ERROR: Please enter a numeric price." + RESET)
    return product_names, product_prices
    
product_names, product_prices = get_inventory_data()

print(CYAN + "\n Inventory Update Complete \n".title().center(40, "-") + RESET)

view_lists_request = input("Generate product report? (Y/N): ").lower()
if view_lists_request == "y":
    print(BLUE + "\n" + " Product Report ".center(40, "=") + RESET)
    for i, name in enumerate(product_names):
        price = product_prices[i]
   
        print(f"Index: {i + 1} | Product: {YELLOW}{name}{RESET} | Price: {GREEN}${price:.2f}{RESET}")
else:
    print("Operation complete. Thank you.")

view_total = sum(product_prices)
print("-" * 40)
print(f"SUBTOTAL: {CYAN}${view_total:.2f}{RESET}")

if len(product_names) >= 3 or view_total >= 50:
    discount = 0.85 * view_total
    print(GREEN + f"DISCOUNT APPLIED: 15%" + RESET)
    print(YELLOW + f"GRAND TOTAL: ${discount:.2f}" + RESET)
else:
    print(f"GRAND TOTAL: ${view_total:.2f}")



now = datetime.datetime.now().strftime("\n%Y-%m-%d | %I:%M %p")
print(f"Issued on: {now}")

print(f"ACCOUNT TYPE: {PURPLE}{user_key.upper()}{RESET}")