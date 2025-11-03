# SistemaFacturacionAgro (Python)  
Proyecto para la asignatura — sistema de facturación para tienda agrícola.  

## Estructura  
-/SistemaFacturacionAgro  
│ README.md  
│ .gitignore  
│ ├─src  
│ ├─agro_store  
│ │ ├─model # Componente Modelo - cada clase en su archivo  
│ │ │ ├─__init__.py  
│ │ │ ├─product.py  
│ │ │ ├─control_product.py  
│ │ │ ├─pest_control.py  
│ │ │ ├─fertilizer_control.py  
│ │ │ ├─animal_type.py  
│ │ │ ├─antibiotic.py  
│ │ │ ├─client.py  
│ │ │ ├─invoice_item.py  
│ │ │ └─invoice.py  
│ │ └─agro_store_app # App de ejemplo (entrypoint)  
│ └─main.py  
│ └─tests  
└─test_invoice.py # pytest
