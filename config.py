"""
⚙️ CONFIGURACIÓN GLOBAL
H&I System
Manejo de Países y Monedas
"""

# Configuración actual (se puede cambiar)
PAIS_ACTUAL = "Venezuela"
MONEDA_SIMBOLO = "Bs."
MONEDA_NOMBRE = "Bolívares"

# --- LISTA DE PAISES DISPONIBLES ---
PAISES = {
    "VE": {
        "nombre": "Venezuela",
        "moneda": "Bolívares",
        "simbolo": "Bs.",
        "codigo": "VES"
    },
    "MX": {
        "nombre": "México",
        "moneda": "Pesos Mexicanos",
        "simbolo": "$",
        "codigo": "MXN"
    },
    "CO": {
        "nombre": "Colombia",
        "moneda": "Pesos Colombianos",
        "simbolo": "$",
        "codigo": "COP"
    },
    "AR": {
        "nombre": "Argentina",
        "moneda": "Pesos Argentinos",
        "simbolo": "$",
        "codigo": "ARS"
    },
    "CL": {
        "nombre": "Chile",
        "moneda": "Pesos Chilenos",
        "simbolo": "$",
        "codigo": "CLP"
    },
    "PE": {
        "nombre": "Perú",
        "moneda": "Soles",
        "simbolo": "S/",
        "codigo": "PEN"
    },
    "BR": {
        "nombre": "Brasil",
        "moneda": "Reales",
        "simbolo": "R$",
        "codigo": "BRL"
    },
    "US": {
        "nombre": "Estados Unidos",
        "moneda": "Dólares",
        "simbolo": "USD $",
        "codigo": "USD"
    }
}

# Función para formatear precios correctamente
def formato_precio(valor):
    """
    Recibe un número y lo devuelve bonito con el símbolo del país.
    Ejemplo: 10.5 -> "Bs. 10,50" o "$ 10.50" dependiendo del país.
    """
    return f"{MONEDA_SIMBOLO} {valor:,.2f}"

# Función para cambiar el país
def set_pais(codigo_pais):
    global PAIS_ACTUAL, MONEDA_SIMBOLO, MONEDA_NOMBRE
    if codigo_pais in PAISES:
        pais = PAISES[codigo_pais]
        PAIS_ACTUAL = pais["nombre"]
        MONEDA_SIMBOLO = pais["simbolo"]
        MONEDA_NOMBRE = pais["moneda"]
        print(f"✅ País configurado: {PAIS_ACTUAL} ({MONEDA_SIMBOLO})")
    else:
        print("❌ Código de país no válido.")
