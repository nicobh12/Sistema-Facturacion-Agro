from agro_store.crud.repository import ClientRepository, InvoiceService
from agro_store.model.client import Client
from agro_store.model.invoice import Invoice
from agro_store.model.invoice_item import InvoiceItem
from datetime import datetime

def run_demo():
    # config repos
    repo = ClientRepository()
    service = InvoiceService(repo)

    # crear cliente
    client = Client("Cliente Demo", "100200300")
    repo.add_client(client)

    # crear factura demo
    inv = Invoice(datetime.now())
    # aquí podrías añadir InvoiceItem(s) desde productos ya creados
    # pero para demo mínimo añadimos vacía si quieres
    service.create_invoice_for(client.cedula, inv)

    print(f"Cliente creado: {client.name} - {client.cedula}")
    invoices = service.buscar_por_cedula(client.cedula)
    print(f"Facturas encontradas para {client.cedula}: {len(invoices)}")
    for i, f in enumerate(invoices, start=1):
        print(f"  Factura {i}: fecha={f.date}, total={f.total:.2f}")
