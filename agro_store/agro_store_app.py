from datetime import datetime
from agro_store.model.client import Client
from agro_store.model.pest_control import PestControl
from agro_store.model.fertilizer_control import FertilizerControl
from agro_store.model.antibiotic import Antibiotic
from agro_store.model.animal_type import AnimalType
from agro_store.model.invoice import Invoice
from agro_store.model.invoice_item import InvoiceItem




def main():
    client = Client("Juan Perez", "12345678")


    pest = PestControl("AntiPlaga X", 120.0, "ICA-001", 30, 14)
    fert = FertilizerControl("FertiMax", 80.0, "ICA-020", 15, datetime.now())
    antib = Antibiotic("AntibioPlus", 250.0, 450, AnimalType.Bovino)


    invoice = Invoice(datetime.now())
    invoice.add_item(InvoiceItem(pest, 2))
    invoice.add_item(InvoiceItem(antib, 1))


    client.invoices.append(invoice)


    print(f"Cliente: {client.name} - Cédula: {client.cedula}")
    print(f"Factura fecha: {invoice.date}")
    print(f"Total: {invoice.total:.2f}")


    input("Pausa para debugging - pon un breakpoint en esta línea")




if __name__ == '__main__':
    main()