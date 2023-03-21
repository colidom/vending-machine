# ******************
# MAQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path


def read_operations(input_path: str) -> list:
    with open(input_path, "r") as f:
        return [line.strip().split() for line in f]


def manage_order(operation: list, products: dict[str, tuple], vending_money: int) -> int:
    product_code = operation[1]
    ordered_qty = int(operation[2])
    inserted_money = int(operation[3])

    if product_code not in products:
        return vending_money

    stock, price = products[product_code]

    if ordered_qty > stock or ordered_qty * price > inserted_money:
        return vending_money

    change = inserted_money - price * ordered_qty
    vending_money += inserted_money - change
    products[product_code] = (stock - ordered_qty, price)

    return vending_money


def modify_product(operation: list, product: tuple, op_type: str) -> tuple[int, int]:
    restocked_qty = int(operation[2])
    if op_type == "R":
        return (product[0] + restocked_qty, product[1])
    return (product[0], restocked_qty)


def create_product(operation: list) -> tuple[int, int]:
    restocked_qty = int(operation[2])
    return restocked_qty, 0


def update_product(operation: list, products: dict[str, tuple], op_type: str) -> dict[str, tuple]:
    prod_code = operation[1]
    if prod_code in products:
        products[prod_code] = modify_product(operation, products[prod_code], op_type)
    elif op_type == "R":
        products[prod_code] = create_product(operation)
    return products


def restock_money(operation: list, money: int) -> int:
    money += int(operation[1])
    return money


def write_status_file(file_path: str, products: dict, vending_money: int):
    with open(file_path, "w") as f:
        f.write(f"{vending_money}\n")

        prod_codes = sorted(products.keys())
        for prod_code in prod_codes:
            stock, price = products[prod_code]
            f.write(f"{prod_code} {stock} {price}\n")


def run(operations_path: str) -> bool:
    status_path = "data/vending/status.dat"

    operations = read_operations(operations_path)
    products: dict = {}
    vending_money = 0

    for operation in operations:
        op_type = operation[0]
        match op_type:
            case "O":
                vending_money = manage_order(operation, products, vending_money)
            case "R" | "P":
                update_product(operation, products, op_type)
            case "M":
                vending_money = restock_money(operation, vending_money)
            case _:
                print(f"Operación {op_type} desconocida")
                continue

    write_status_file(status_path, products, vending_money)

    return filecmp.cmp(status_path, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    operations_path = "data/vending/operations.dat"
    run(operations_path)
