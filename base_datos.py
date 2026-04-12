"""
🗄️ MÓDULO DE BASE DE DATOS
H&I System
"""

import sqlite3

def conectar():
    return sqlite3.connect('h&i_system.db')

def inicializar_db():
    conexion = conectar()
    cursor = conexion.cursor()
    
    # ==================================
    # 📦 TABLA BODEGA
    # ==================================
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos_bodega (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT UNIQUE,
            nombre TEXT,
            cantidad INTEGER,
            ubicacion TEXT,
            fecha_vencimiento TEXT,
            costo REAL
        )
    ''')
    
    # ==================================
    # 👕 TABLA TIENDA
    # ==================================
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos_tienda (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT UNIQUE,
            nombre TEXT,
            talla TEXT,
            color TEXT,
            precio REAL,
            stock INTEGER
        )
    ''')

    # ==================================
    # 🔩 TABLA FERRETERIA
    # ==================================
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ferreteria (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT UNIQUE,
            nombre TEXT,
            unidad TEXT,
            precio REAL,
            stock INTEGER
        )
    ''')

    # ==================================
    # 💪 TABLA GIMNASIO
    # ==================================
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS socios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            telefono TEXT,
            plan TEXT,
            pago REAL
        )
    ''')

    # ==================================
    # 🏍️ TABLA REPUESTOS MOTO
    # ==================================
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS repuestos_moto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT UNIQUE,
            nombre TEXT,
            modelo TEXT,
            precio REAL
        )
    ''')

    # ==================================
    # 🚗 TABLA REPUESTOS CARRO
    # ==================================
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS repuestos_carro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT UNIQUE,
            nombre TEXT,
            motor TEXT,
            precio REAL
        )
    ''')

    # ==================================
    # 🍽️ TABLA RESTAURANTE
    # ==================================
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS menu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            categoria TEXT,
            precio REAL
        )
    ''')

    # ==================================
    # 🔐 TABLA DE USUARIOS (LOGIN)
    # ==================================
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE,
            password TEXT,
            nombre TEXT,
            rol TEXT
        )
    ''')

    # ==================================
    # ⚙️ TABLA DE CONFIGURACIÓN
    # ==================================
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS configuracion (
            id INTEGER PRIMARY KEY,
            pais TEXT,
            moneda_simbolo TEXT,
            impuesto_porcentaje REAL
        )
    ''')

    # ==================================
    # 💳 TABLA DE SUSCRIPCIONES Y PAGOS
    # ==================================
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS suscripciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT,
            modulo TEXT,
            fecha_inicio TEXT,
            fecha_fin TEXT,
            estado TEXT
        )
    ''')

    # ==================================
    # 🤝 TABLA DE AFILIADOS
    # ==================================
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS afiliados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT UNIQUE,
            nombre TEXT,
            porcentaje_comision REAL,
            balance REAL
        )
    ''')

    conexion.commit()
    conexion.close()
    print("✅ Base de Datos Actualizada y Lista.")
