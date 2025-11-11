from datetime import datetime
from agro_store.model.client import Client
from agro_store.model.pest_control import PestControl
from agro_store.model.fertilizer_control import FertilizerControl
from agro_store.model.antibiotic import Antibiotic
from agro_store.model.animal_type import AnimalType
from agro_store.model.invoice import Invoice
from agro_store.model.invoice_item import InvoiceItem


def main():
    print("=== INICIO DE LA APLICACIÓN AGRO STORE ===")

    # 🧍‍♂️ Crear cliente
    client = Client("Juan Perez", "12345678")
    print(f"Cliente creado: {client.name} ({client.cedula})")

    breakpoint()  # 🔹 Captura 1: Cliente creado

    # 🌾 Crear productos
    pest = PestControl("AntiPlaga X", 120.0, "ICA-001", 30, 14)
    fert = FertilizerControl("FertiMax", 80.0, "ICA-020", 15, datetime.now())
    antib = Antibiotic("AntibioPlus", 250.0, 450, AnimalType.Bovino)

    print("\nProductos creados:")
    print(f" - {pest.name}, ${pest.price}")
    print(f" - {fert.name}, ${fert.price}")
    print(f" - {antib.name}, ${antib.price}")

    breakpoint()  # 🔹 Captura 2: Productos creados

    # 🧾 Crear factura
    invoice = Invoice(datetime.now())
    invoice.add_item(InvoiceItem(pest, 2))
    invoice.add_item(InvoiceItem(antib, 1))
    invoice.add_item(InvoiceItem(fert, 3))

    print(f"\nFactura creada con {len(invoice.items)} ítems.")
    print(f"Total parcial: ${invoice.total:.2f}")

    breakpoint()  # 🔹 Captura 3: Factura con productos

    # 🧩 Asociar factura al cliente
    client.invoices.append(invoice)

    print(f"\nFactura asociada al cliente {client.name}.")
    print(f"Total factura: ${invoice.total:.2f}")
    print(f"Fecha: {invoice.date}")

    breakpoint()  # 🔹 Captura 4: Factura asociada

    # ✅ Resultado final
    print("\n=== RESUMEN FINAL ===")
    print(f"Cliente: {client.name} - Cédula: {client.cedula}")
    print(f"Factura fecha: {invoice.date}")
    print(f"Total: ${invoice.total:.2f}")

    breakpoint()  # 🔹 Captura 5: Resumen final


if __name__ == "__main__":
    main()
