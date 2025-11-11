from dataclasses import dataclass, field
from typing import List
import uuid
from .invoice import Invoice

@dataclass
class Client:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    cedula: str = ""
    invoices: List[Invoice] = field(default_factory=list)

    def __init__(self, name: str, cedula: str):
        if not name:
            raise ValueError("name es obligatorio")
        if not cedula:
            raise ValueError("cedula es obligatoria")
        self.id = str(uuid.uuid4())
        self.name = name
        self.cedula = cedula
        self.invoices = []
