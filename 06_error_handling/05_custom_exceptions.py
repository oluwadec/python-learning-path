"""05_custom_exceptions.py - Make exceptions with meaningful names."""


class ShopError(Exception):
    """Base class for shopping errors."""


class OutOfStockError(ShopError):
    def __init__(self, item: str):
        super().__init__(f"'{item}' is out of stock")
        self.item = item


class InvalidQuantityError(ShopError):
    pass


STOCK = {"pen": 5, "book": 0}


def buy(item: str, quantity: int) -> str:
    if quantity <= 0:
        raise InvalidQuantityError("quantity must be positive")
    if STOCK.get(item, 0) < quantity:
        raise OutOfStockError(item)
    STOCK[item] -= quantity
    return f"Bought {quantity} {item}(s)"


for item, qty in [("pen", 2), ("book", 1), ("pen", 0)]:
    try:
        print(buy(item, qty))
    except ShopError as error:      # catches both custom errors
        print("Shop error:", error)
