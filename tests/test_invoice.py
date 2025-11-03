import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import datetime
from agro_store.model.pest_control import PestControl
from agro_store.model.antibiotic import Antibiotic
from agro_store.model.animal_type import AnimalType
from agro_store.model.invoice import Invoice
from agro_store.model.invoice_item import InvoiceItem
from agro_store.model.client import Client

def test_invoice_total_sums_line_totals():
    pest = PestControl("Pest", 100.0, "ICA-1", 30, 10)
    antib = Antibiotic("Anti", 200.0, 500, AnimalType.Porcino)
    invoice = Invoice(datetime.today())
    invoice.add_item(InvoiceItem(pest, 2)) # 200
    invoice.add_item(InvoiceItem(antib, 1)) # 200
    assert invoice.total == pytest.approx(400.0)

def test_antibiotic_dose_validation_throws():
    with pytest.raises(ValueError):
        Antibiotic("X", 10.0, 350, AnimalType.Bovino)

def test_client_can_have_multiple_invoices():
    client = Client("Ana", "999")
    client.invoices.append(Invoice(datetime.now()))
    client.invoices.append(Invoice(datetime.now()))
    assert len(client.invoices) == 2

    