from abc import ABC
from dataclasses import dataclass, field
import uuid

@dataclass
class Product(ABC):
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    price: float = 0.0

    def __init__(self, name: str, price: float):
        if not name:
            raise ValueError("name es obligatorio")
        if price is None or price < 0:
            raise ValueError("price es obligatorio y debe ser >= 0")
        self.id = str(uuid.uuid4())
        self.name = name
        self.price = price
