import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in args:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        name, quantity_str = arg.split(":", 1)
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            quantity = int(quantity_str)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
            continue
        inventory[name] = quantity
    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = parse_inventory(sys.argv[1:])
    print(f"Got inventory: {inventory}")
    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")
    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(item_list)} items: {total_quantity}")
    for name in inventory:
        parcent = round(inventory[name] / total_quantity * 100, 1)
        print(f"Item {name} represents {parcent}%")
    most_name = ""
    most_qty = -1
    least_name = ""
    least_qty = -1
    for name in inventory:
        qty = inventory[name]
        if qty > most_qty:
            most_name, most_qty = name, qty
        if least_qty == -1 or qty < least_qty:
            least_name, least_qty = name, qty
    print(f"Item most abundant: {most_name} with quantity {most_qty}")
    print(f"Item least abundant: {least_name} with quantity {least_qty}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
