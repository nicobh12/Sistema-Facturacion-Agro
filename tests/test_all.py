import sys, os
import pytest
from datetime import datetime

# 🔧 Asegurar que se pueda importar agro_store sin problemas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ✅ Imports del modelo
from agro_store.model.client import Client
from agro_store.model.product import Product
from agro_store.model.pest_control import PestControl
from agro_store.model.fertilizer_control import FertilizerControl
from agro_store.model.antibiotic import Antibiotic
from agro_store.model.animal_type import AnimalType
from agro_store.model.invoice import Invoice
from agro_store.model.invoice_item import InvoiceItem

# ✅ Imports del CRUD
from agro_store.crud.repository import ClientRepository, InvoiceService


# =====================================================
# 🧾 PRUEBAS DE FACTURACIÓN Y RELACIONES ENTRE CLASES
# =====================================================

def test_invoice_total_sums_line_totals():
    """Verifica que el total de la factura sume correctamente los subtotales."""
    pest = PestControl("Pest", 100.0, "ICA-1", 30, 10)
    antib = Antibiotic("Anti", 200.0, 500, AnimalType.Porcino)
    invoice = Invoice(datetime.today())
    invoice.add_item(InvoiceItem(pest, 2))  # 200
    invoice.add_item(InvoiceItem(antib, 1))  # 200
    assert invoice.total == pytest.approx(400.0)


def test_client_can_have_multiple_invoices():
    """Verifica que un cliente puede tener múltiples facturas asociadas."""
    client = Client("Ana", "999")
    client.invoices.append(Invoice(datetime.now()))
    client.invoices.append(Invoice(datetime.now()))
    assert len(client.invoices) == 2


# =====================================================
# 🧩 PRUEBAS DE VALIDACIONES DE DATOS Y HERENCIA
# =====================================================

def test_client_requires_name_and_cedula():
    """El cliente debe tener nombre y cédula válidos."""
    with pytest.raises(ValueError):
        Client("", "123")
    with pytest.raises(ValueError):
        Client("Nombre", "")


def test_fertilizer_requires_last_application_date():
    """El fertilizante debe tener una fecha de última aplicación válida."""
    with pytest.raises(ValueError):
        FertilizerControl("F", 10.0, "ICA-1", 15, None)


def test_antibiotic_requires_valid_dose_and_animal():
    """El antibiótico debe tener dosis válida y tipo de animal válido."""
    with pytest.raises(ValueError):
        Antibiotic("A", 10.0, 300, AnimalType.Bovino)
    with pytest.raises(ValueError):
        Antibiotic("A", 10.0, 500, None)


# =====================================================
# 🔍 PRUEBAS DE CRUD Y BÚSQUEDA POR CÉDULA
# =====================================================

def test_cliente_y_factura_y_busqueda_por_cedula():
    """Verifica que la búsqueda por cédula retorna las facturas correctas."""
    repo = ClientRepository()
    service = InvoiceService(repo)

    client = Client("Prueba", "111222333")
    repo.add_client(client)

    pest = PestControl("PestY", 50.0, "ICA-999", 30, 10)
    antib = Antibiotic("AntX", 200.0, 450, AnimalType.Porcino)

    inv = Invoice(datetime.now())
    inv.add_item(InvoiceItem(pest, 3))
    inv.add_item(InvoiceItem(antib, 1))

    service.create_invoice_for(client.cedula, inv)

    invoices_found = service.buscar_por_cedula(client.cedula)
    assert len(invoices_found) == 1

    found = invoices_found[0]
    # La factura debe contener los items añadidos
    assert len(found.items) == 2
    # Los productos deben ser instancias correctas (herencia)
    assert any(isinstance(it.product, PestControl) for it in found.items)
    assert any(isinstance(it.product, Antibiotic) for it in found.items)


def test_buscar_por_cedula_inexistente_devuelve_vacio():
    """Si se busca una cédula no registrada, debe devolver lista vacía."""
    repo = ClientRepository()
    service = InvoiceService(repo)
    assert service.buscar_por_cedula("no-existe") == []
