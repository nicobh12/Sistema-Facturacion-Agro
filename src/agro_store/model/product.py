from abc import ABC, abstractmethod
from dataclasses import dataclass, field
import uuid


@dataclass
class Product(ABC):
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    price: float = 0.0

    def __init__(self, name: str, price: float):
        self.id = str(uuid.uuid4())
        self.name = name
        self.price = price