    # Tabla de CONFIGURACIÓN DEL SISTEMA
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS configuracion (
            id INTEGER PRIMARY KEY,
            pais TEXT,
            moneda_simbolo TEXT,
            impuesto_porcentaje REAL
        )
    ''')
