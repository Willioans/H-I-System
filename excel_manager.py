"""
📊 GESTOR DE EXCEL
H&I System
Importar datos masivos
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importamos librerías necesarias
import pandas as pd
from base_datos import conectar
from config import formato_precio

def importar_desde_excel(ruta_archivo, tipo_modulo):
    """
    Carga datos desde un archivo Excel a la base de datos
    tipo_modulo: 'bodega', 'tienda', 'ferreteria', etc.
    """
    
    try:
        # Leer el archivo Excel
        df = pd.read_excel(ruta_archivo)
        print(f"📖 Archivo leído correctamente. Filas encontradas: {len(df)}")
        
        conn = conectar()
        cursor = conn.cursor()
        agregados = 0

        # --- LÓGICA SEGÚN EL MÓDULO ---
        if tipo_modulo == "bodega":
            for index, row in df.iterrows():
                try:
                    cursor.execute('''
                        INSERT INTO productos_bodega 
                        (codigo, nombre, cantidad, ubicacion, fecha_vencimiento, costo)
                        VALUES (?,?,?,?,?,?)
                    ''', (
                        str(row['codigo']),
                        str(row['nombre']),
                        int(row['cantidad']),
                        str(row['ubicacion']),
                        str(row.get('vencimiento', '')),
                        float(row['costo'])
                    ))
                    agregados += 1
                except: pass # Si el código ya existe, lo salta

        elif tipo_modulo == "tienda":
            for index, row in df.iterrows():
                try:
                    cursor.execute('''
                        INSERT INTO productos_tienda 
                        (codigo, nombre, talla, color, precio, stock)
                        VALUES (?,?,?,?,?,?)
                    ''', (
                        str(row['codigo']),
                        str(row['nombre']),
                        str(row['talla']),
                        str(row['color']),
                        float(row['precio']),
                        int(row['stock'])
                    ))
                    agregados += 1
                except: pass

        elif tipo_modulo == "ferreteria":
            for index, row in df.iterrows():
                try:
                    cursor.execute('''
                        INSERT INTO ferreteria 
                        (codigo, nombre, unidad, precio, stock)
                        VALUES (?,?,?,?,?)
                    ''', (
                        str(row['codigo']),
                        str(row['nombre']),
                        str(row['unidad']),
                        float(row['precio']),
                        int(row['stock'])
                    ))
                    agregados += 1
                except: pass

        # Aquí podemos agregar el resto de módulos luego...

        conn.commit()
        conn.close()
        print(f"\n✅ PROCESO TERMINADO!")
        print(f"📦 Total agregados: {agregados}")
        print(f"⚠️  Errores o duplicados: {len(df) - agregados}")

    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        print("💡 Asegúrate de que las columnas en el Excel se llamen igual que en el sistema (codigo, nombre, etc.)")


# Función para mostrar menú de importación
def menu_importar(modulo):
    print("\n")
    print("==================================")
    print("       IMPORTAR DESDE EXCEL       ")
    print("==================================")
    print(f"📂 Módulo: {modulo.upper()}")
    print("ℹ️  El Excel debe tener las columnas:")
    
    if modulo == "tienda":
        print("👉 codigo | nombre | talla | color | precio | stock")
    elif modulo == "bodega":
        print("👉 codigo | nombre | cantidad | ubicacion | vencimiento | costo")
    elif modulo == "ferreteria":
        print("👉 codigo | nombre | unidad | precio | stock")
        
    print("")
    ruta = input("📄 Pega la ruta completa del archivo Excel: ")
    
    if ruta:
        importar_desde_excel(ruta, modulo)
