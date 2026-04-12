"""
👑 PANEL DE ADMINISTRADOR MASTER
H&I System
CONTROL TOTAL DE CLIENTES Y LICENCIAS
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from base_datos import conectar
from config import formato_precio
from datetime import datetime, timedelta

def agregar_cliente():
    print("\n🆕 AUTORIZAR NUEVO CLIENTE")
    print("---------------------------")
    
    cod = input("📝 Código de Cliente (ej: CLI001): ")
    nom = input("🏢 Nombre de la Empresa: ")
    pais = input("🌍 País: ")
    
    print("\n📦 Módulos disponibles:")
    print("1=Bodega, 2=Tienda, 3=Ferretería, 4=Gimnasio, 5=Moto, 6=Carro, 7=Restaurante")
    modulos = input("🔧 ¿Cuáles puede usar? (Separa con comas ej: 1,2,7): ")
    
    dias = int(input("📅 ¿Cuántos días de licencia? "))
    
    # Calcular fechas
    fecha_ini = datetime.now().strftime("%d/%m/%Y")
    fecha_fin = (datetime.now() + timedelta(days=dias)).strftime("%d/%m/%Y")

    # Guardar en BD
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO clientes 
            (codigo_cliente, nombre_empresa, pais, modulos_permitidos, fecha_activacion, fecha_vencimiento, estado)
            VALUES (?,?,?,?,?,?,?)
        ''', (cod, nom, pais, modulos, fecha_ini, fecha_fin, "ACTIVO"))
        
        conn.commit()
        print("\n✅ CLIENTE AUTORIZADO EXITOSAMENTE!")
        print(f"📅 Desde: {fecha_ini}")
        print(f"📅 Hasta: {fecha_fin}")
        print(f"🔓 Acceso permitido a: {modulos}")
        
    except Exception as e:
        print(f"\n❌ ERROR: El código ya existe o hubo un problema. Detalle: {e}")
    
    conn.close()

def ver_clientes():
    print("\n📋 LISTA DE TODOS LOS CLIENTES")
    print("-------------------------------")
    
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes ORDER BY id DESC")
    
    lista = cursor.fetchall()
    
    if not lista:
        print("⚠️ No hay clientes registrados aún.")
    else:
        for c in lista:
            estado_icon = "🟢" if c[6] == "ACTIVO" else "🔴"
            print(f"{estado_icon} ID:{c[0]} | Código:{c[1]} | Empresa:{c[2]}")
            print(f"   📅 Expira: {c[5]} | Estado: {c[6]}")
            print("   ------------------------------------")
    
    conn.close()

def cambiar_estado():
    print("\n🔧 CAMBIAR ESTADO DE CLIENTE")
    print("------------------------------")
    
    cod = input("Código del cliente: ")
    nuevo_estado = input("Nuevo estado (ACTIVO / SUSPENDIDO / VENCIDO): ").upper()
    
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE clientes SET estado = ? WHERE codigo_cliente = ?", (nuevo_estado, cod))
    conn.commit()
    
    if cursor.rowcount > 0:
        print(f"✅ Cliente {cod} ahora está: {nuevo_estado}")
    else:
        print("❌ Cliente no encontrado.")
    
    conn.close()

def iniciar_admin():
    while True:
        print("\n")
        print("==================================")
        print("    PANEL DE ADMINISTRACIÓN       ")
        print("          MODO DIOS 👑          ")
        print("==================================")
        print("1. ➕ Autorizar Nuevo Cliente")
        print("2. 📋 Ver Todos los Clientes")
        print("3. 🛡️  Cambiar Estado (Bloquear)")
        print("4. 🚪 Salir al Menú Principal")
        
        op = input("\n👉 Elige una opción: ")
        
        if op == "1":
            agregar_cliente()
        elif op == "2":
            ver_clientes()
        elif op == "3":
            cambiar_estado()
        elif op == "4":
            print("🔙 Volviendo al menú principal...")
            break
        else:
            print("❌ Opción incorrecta.")
            
        input("\nPresiona Enter para continuar...")
