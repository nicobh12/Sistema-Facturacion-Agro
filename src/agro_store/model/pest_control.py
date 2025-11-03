from dataclasses import dataclass
from .control_product import ControlProduct


@dataclass
class PestControl(ControlProduct):
    withdrawal_period_days: int = 0 # periodo de carencia


    def __init__(self, name: str, price: float, ica_registration: str, application_frequency_days: int, withdrawal_period_days: int):
        super().__init__(name, price, ica_registration, application_frequency_days)
        self.withdrawal_period_days = withdrawal_period_days