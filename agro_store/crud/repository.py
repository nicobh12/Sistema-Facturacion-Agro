from typing import List, Dict
from agro_store.model.client import Client
from agro_store.model.invoice import Invoice
from agro_store.model.invoice_item import InvoiceItem
from agro_store.model.product import Product

class ClientRepository:
    """Repo en memoria para clientes y sus facturas"""
    def __init__(self):
        self._clients_by_cedula: Dict[str, Client] = {}

    def add_client(self, client: Client):
        if client is None:
            raise ValueError("client no puede ser None")
        if not client.cedula:
            raise ValueError("cedula es obligatoria")
        self._clients_by_cedula[client.cedula] = client

    def get_by_cedula(self, cedula: str) -> Client | None:
        return self._clients_by_cedula.get(cedula)

    def list_all(self) -> List[Client]:
        return list(self._clients_by_cedula.values())

class InvoiceService:
    """Servicios relacionados con facturas"""
    def __init__(self, client_repo: ClientRepository):
        self.client_repo = client_repo

    def create_invoice_for(self, cedula: str, invoice: Invoice):
        client = self.client_repo.get_by_cedula(cedula)
        if client is None:
            raise ValueError(f"No existe cliente con cédula {cedula}")
        if invoice is None:
            raise ValueError("invoice no puede ser None")
        client.invoices.append(invoice)

    def buscar_por_cedula(self, cedula: str) -> List[Invoice]:
        client = self.client_repo.get_by_cedula(cedula)
        if client is None:
            return []
        return client.invoices
