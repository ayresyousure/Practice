# Define the menu as a dictionary
menu = {
    1: {"name": "Cachorro Quente", "price": 4.00},
    2: {"name": "X-Salada", "price": 4.50},
    3: {"name": "X-Bacon", "price": 5.00},
    4: {"name": "Torrada Simples", "price": 2.00},
    5: {"name": "Refrigerante", "price": 1.50},
}

# Take input from the user
user_input = input("Enter the code and quantity (e.g., '1 2' for 2 Cachorro Quente): ")

# Split the input into code and quantity
code, quantity = map(int, user_input.split())

# Look up the item in the menu
if code in menu:
    item = menu[code]
    total_cost = item["price"] * quantity
    print(f"Total: R${total_cost:.2f}")
else:
    print("Invalid code. Please try again.")