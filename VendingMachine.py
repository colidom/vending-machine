# Lista de productos disponibles
products = {
    "001": {"name": "Coca Cola", "price": 2.5, "stock": 5},
    "002": {"name": "Agua", "price": 1.5, "stock": 10},
    "003": {"name": "Jugo", "price": 3, "stock": 3},
    "004": {"name": "Gatorade", "price": 2, "stock": 7}
}

# Lista de monedas disponibles
coins = {
    0.50: {"stock": 10},
    1: {"stock": 5},
    2: {"stock": 3},
}

# Función que muestra los productos disponibles y sus precios
def show_products():
    print("PRODUCTOS DISPONIBLES:")
    for code, data in products.items():
        print(f"{code} - {data['name']}: €{data['price']}, stock: {data['stock']}")

# Función que procesa la compra de un producto
def buy_product(money, product_code):
    if product_code not in products:
        print("Producto no disponible")
        return None

    data = products[product_code]
    if data['stock'] == 0:
        print("Producto agotado")
        return None

    price = data['price']
    if money < price:
        print("Dinero insuficiente")
        return None

    change = money - price

# Actualiza el stock de monedas disponibles para dar cambio ["Está fallando cuando debe dar cambio"]
    coins_to_return = {}
    for coin_value in sorted(coins.keys(), reverse=True):
        coin_data = coins[coin_value]
        while change >= coin_value and coin_data['stock'] > 0:
            change -= coin_value
            coin_data['stock'] -= 1
            if coin_value not in coins_to_return:
                coins_to_return[coin_value] = 1
            else:
                coins_to_return[coin_value] += 1

    if change > 0:
        print("No hay suficientes monedas para dar cambio. La compra ha sido cancelada.")
        # Devuelve las monedas que el usuario ingresó
        for coin_value in sorted(coins.keys(), reverse=True):
            coin_data = coins[coin_value]
            while money >= coin_value and coin_data['stock'] > 0:
                money -= coin_value
                coin_data['stock'] -= 1
        return None

    data['stock'] -= 1
    print("Compra exitosa!")
    if coins_to_return:
        print("Monedas de cambio:")
        for coin_value, count in coins_to_return.items():
            print(f"€{coin_value / 1:.2f}: {count}")

    return data['name']

# Función que cuenta el dinero ingresado por el usuario
def count_money():
    money = 0
    while True:
        coin = input("Ingrese una moneda (50, 1, 2): ")
        if coin not in ["50", "100", "200"]:
            print("Moneda no válida")
            continue

        money += int(coin)
        print(f"Dinero ingresado: €{money / 1:.2f}")

        if input("¿Desea ingresar más dinero? (S/N) ").upper() != "S":
            break

    return 

# Función que muestra el stock disponible de cada producto
def show_stock():
    print("STOCK DISPONIBLE:")
    for product, data in products.items():
        print(f"{product}: {data['stock']}")

# Función principal del programa
def vending_machine():
    while True:
        option = input("Seleccione una opción: (P)roductos, (C)omprar, (S)tock, (Q)uit: ")
        if option.upper() == "P":
            show_products()
        elif option.upper() == "C":
            show_products()
            product = input("Seleccione un producto: ")
            money = count_money()
            buy_product(money, product)
        elif option.upper() == "S":
            show_stock()
        elif option.upper() == "Q":
            break
        else:
            print("Opción no válida")

# Ejecución del programa
vending_machine()

