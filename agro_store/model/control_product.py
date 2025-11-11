from dataclasses import dataclass
from .product import Product

@dataclass
class ControlProduct(Product):
    ica_registration: str = ""
    application_frequency_days: int = 0

    def __init__(self, name: str, price: float, ica_registration: str, application_frequency_days: int):
        if not ica_registration:
            raise ValueError("ica_registration es obligatorio")
        if application_frequency_days is None or application_frequency_days <= 0:
            raise ValueError("application_frequency_days debe ser > 0")
        super().__init__(name, price)
        self.ica_registration = ica_registration
        self.application_frequency_days = application_frequency_days
