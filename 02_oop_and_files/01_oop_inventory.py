"""01_oop_inventory.py - Two classes working together: items and a warehouse."""


class InventoryItem:
    """Represents a single product item in an inventory system."""

    def __init__(self, item_id: str, name: str, price: float, quantity: int):
        # Store the details on the object with self
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def restock(self, amount: int) -> None:
        self.quantity += amount

    def sell(self, amount: int) -> bool:
        if amount > self.quantity:
            return False
        self.quantity -= amount
        return True

    def value(self) -> float:
        return self.price * self.quantity

    def __str__(self) -> str:
        return f"{self.name} ({self.item_id}): {self.quantity} @ ${self.price:.2f}"


class Warehouse:
    """Holds many InventoryItem objects."""

    def __init__(self, warehouse_name: str):
        self.warehouse_name = warehouse_name
        self.inventory = {}  # maps item_id -> InventoryItem

    def add_item(self, item: InventoryItem) -> None:
        if item.item_id in self.inventory:
            self.inventory[item.item_id].restock(item.quantity)
        else:
            self.inventory[item.item_id] = item

    def get_total_inventory_value(self) -> float:
        total = sum(item.value() for item in self.inventory.values())
        return round(total, 2)

    def display_report(self) -> None:
        print("\n========================================")
        print(f"  WAREHOUSE REPORT: {self.warehouse_name.upper()}")
        print("========================================")

        if not self.inventory:
            print(" No items in inventory.")
        else:
            for item in self.inventory.values():
                print(f"  {item}")

        print("----------------------------------------")
        print(f" TOTAL WAREHOUSE VALUE: ${self.get_total_inventory_value():.2f}")
        print("========================================\n")


if __name__ == "__main__":
    warehouse = Warehouse("Main Store")
    warehouse.add_item(InventoryItem("A1", "Laptop", 899.99, 5))
    warehouse.add_item(InventoryItem("B2", "Mouse", 19.5, 40))
    warehouse.inventory["A1"].sell(2)
    warehouse.inventory["B2"].restock(10)
    warehouse.display_report()
