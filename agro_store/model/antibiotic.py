from dataclasses import dataclass
from .product import Product
from .animal_type import AnimalType

@dataclass
class Antibiotic(Product):
    dose_kg: int = 0
    treated_animal: AnimalType = None

    def __init__(self, name: str, price: float, dose_kg: int, treated_animal: AnimalType):
        if treated_animal is None:
            raise ValueError("treated_animal es obligatorio")
        super().__init__(name, price)
        if dose_kg < 400 or dose_kg > 600:
            raise ValueError("La dosis debe estar entre 400 y 600 Kg.")
        self.dose_kg = dose_kg
        self.treated_animal = treated_animal
