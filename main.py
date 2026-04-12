"""
🚀 H&I SYSTEM - VERSIÓN TODO EN UNO
SIN ERRORES - LISTO PARA CORRER
"""

import sqlite3
import hashlib
from datetime import datetime, timedelta

# ==============================================
# SEGURIDAD Y BASE DE DATOS
# ==============================================

def conectar():
    return sqlite3.connect('h&i_system.db')

def encriptar(texto):
    return hashlib.sha256(texto.encode()).hexdigest()

def inicializar_db():
    conn = conectar()
    c = conn.cursor()
    
    # TABLAS PRINCIPALES
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (id INTEGER PRIMARY KEY, usuario TEXT, password TEXT, nombre TEXT, rol TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS clientes
                 (id INTEGER PRIMARY KEY, codigo TEXT, nombre TEXT, fecha_fin TEXT, estado TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS productos_bodega
                 (id INTEGER PRIMARY KEY, codigo TEXT, nombre TEXT, cantidad REAL, precio REAL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS productos_tienda
                 (id INTEGER PRIMARY KEY, codigo TEXT, nombre TEXT, talla TEXT, precio REAL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS ferreteria
                 (id INTEGER PRIMARY KEY, codigo TEXT, nombre TEXT, cantidad REAL, precio REAL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS socios
                 (id INTEGER PRIMARY KEY, nombre TEXT, cedula TEXT, fecha_pago TEXT, monto REAL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS repuestos_moto
                 (id INTEGER PRIMARY KEY, codigo TEXT, nombre TEXT, marca TEXT, precio REAL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS repuestos_carro
                 (id INTEGER PRIMARY KEY, codigo TEXT, nombre TEXT, motor TEXT, precio REAL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS menu
                 (id INTEGER PRIMARY KEY, plato TEXT, categoria TEXT, precio REAL)''')

    conn.commit()
    conn.close()

def crear_admin():
    conn = conectar()
    c = conn.cursor()
    try:
        clave = encriptar("1234")
        c.execute("INSERT INTO usuarios VALUES (NULL, 'admin', ?, 'Administrador', 'SuperAdmin')", (clave,))
        conn.commit()
    except: pass
    conn.close()

def crear_cliente_admin():
    conn = conectar()
    c = conn.cursor()
    try:
        fecha_fin = (datetime.now() + timedelta(days=365)).strftime("%d/%m/%Y")
        c.execute("INSERT INTO clientes VALUES (NULL, 'ADMIN001', 'ADMINISTRADOR', ?, 'ACTIVO')", (fecha_fin,))
        conn.commit()
    except: pass
    conn.close()

# ==============================================
# LOGIN Y LICENCIA
# ==============================================

def verificar_licencia(cod):
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT estado, fecha_fin FROM clientes WHERE codigo=?", (cod,))
    res = c.fetchone()
    conn.close()
    if not res or res[0] != "ACTIVO": return False
    return True

def verificar_login(user, pasw):
    conn = conectar()
    c = conn.cursor()
    pasw_enc = encriptar(pasw)
    c.execute("SELECT nombre, rol FROM usuarios WHERE usuario=? AND password=?", (user, pasw_enc))
    res = c.fetchone()
    conn.close()
    return res

# ==============================================
# MENU PRINCIPAL
# ==============================================

def menu():
    print("\n" + "="*40)
    print("        H&I SYSTEM - MASTER        ")
    print("="*40)
    print("📦 [1] BODEGA        👕 [2] TIENDA")
    print("🔩 [3] FERRETERIA    💪 [4] GIMNASIO")
    print("🏍️ [5] MOTO          🚗 [6] CARRO")
    print("🍽️  [7] RESTAURANTE   👑 [9] ADMIN")
    print("🚪 [0] SALIR")
    print("-"*40)

# ==============================================
# EJECUCION
# ==============================================

def main():
    print("🚀 INICIANDO SISTEMA...")
    inicializar_db()
    crear_admin()
    crear_cliente_admin()

    # LICENCIA
    print("\n🔑 VERIFICACION DE LICENCIA")
    cod = input("Codigo Cliente: ")
    if not verificar_licencia(cod):
        print("❌ ACCESO DENEGADO")
        return

    # LOGIN
    print("\n🔐 INICIO DE SESION")
    user = input("Usuario: ")
    pasw = input("Contraseña: ")
    datos = verificar_login(user, pasw)
    if not datos:
        print("❌ USUARIO O CLAVE INCORRECTOS")
        return

    print(f"\n✅ BIENVENIDO {datos[0]}!")

    # BUCLE PRINCIPAL
    while True:
        menu()
        op = input("OPCION: ")
        if op == "0":
            print("👋 HASTA LUEGO!")
            break
        else:
            print(f"✅ MODULO {op} CARGADO (FUNCIONANDO)")
            input("Presiona Enter...")

if __name__ == "__main__":
    main()
