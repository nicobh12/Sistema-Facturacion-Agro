from dataclasses import dataclass
from datetime import datetime
from .control_product import ControlProduct

@dataclass
class FertilizerControl(ControlProduct):
    last_application_date: datetime = None

    def __init__(self, name: str, price: float, ica_registration: str, application_frequency_days: int, last_application_date: datetime):
        if last_application_date is None or not isinstance(last_application_date, datetime):
            raise ValueError("last_application_date es obligatorio y debe ser datetime")
        super().__init__(name, price, ica_registration, application_frequency_days)
        self.last_application_date = last_application_date
