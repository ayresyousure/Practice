# Define the menu as a dictionary
menu = {
    1: {"name": "Café", "price": 4.00},
    2: {"name": "Pão com Queijo", "price": 4.50},
    3: {"name": "Refri", "price": 5.00},
    4: {"name": "Torrada", "price": 2.00},
    5: {"name": "Bala", "price": 1.50},
}

# Take input from the user
user_input = input("Coloque o código do item e depois quantos dele: ")

# Split the input into code and quantity
code, quantity = map(int, user_input.split())

# Look up the item in the menu
if code in menu:
    item = menu[code]
    total_cost = item["price"] * quantity
    print(f"Total: R${total_cost:.2f}")
else:
    print("Código Inválido, tente novamente.")
