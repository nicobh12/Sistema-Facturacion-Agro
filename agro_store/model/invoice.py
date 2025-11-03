from dataclasses import dataclass, field
from typing import List
import uuid
from .invoice_item import InvoiceItem
from datetime import datetime


@dataclass
class Invoice:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    date: datetime = None
    items: List[InvoiceItem] = field(default_factory=list)


    def __init__(self, date: datetime):
        self.id = str(uuid.uuid4())
        self.date = date
        self.items = []


    def add_item(self, item: InvoiceItem):
        if item is None:
            raise ValueError("item no puede ser None")
        self.items.append(item)


    @property
    def total(self) -> float:
        return sum(i.line_total for i in self.items)