from dataclasses import dataclass
from .product import Product


@dataclass
class InvoiceItem:
    product: Product
    quantity: int

    def __init__(self, product: Product, quantity: int):
        if product is None:
            raise ValueError("product no puede ser None")
        if quantity <= 0:
            raise ValueError("quantity debe ser mayor que 0")
        self.product = product
        self.quantity = quantity


    @property
    def line_total(self) -> float:
        return self.product.price * self.quantity