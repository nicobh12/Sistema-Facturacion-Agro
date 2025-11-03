from dataclasses import dataclass
from .product import Product


@dataclass
class ControlProduct(Product):
    ica_registration: str = ""
    application_frequency_days: int = 0

    def __init__(self, name: str, price: float, ica_registration: str, application_frequency_days: int):
        super().__init__(name, price)
        self.ica_registration = ica_registration
        self.application_frequency_days = application_frequency_days