"""
🔐 SISTEMA DE AUTENTICACIÓN
H&I System
Login y Control de Accesos
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from base_datos import conectar

# Crear usuario ADMIN por defecto
def crear_admin_default():
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (usuario, password, nombre, rol) VALUES (?, ?, ?, ?)",
                       ("admin", "1234", "Administrador", "SuperAdmin"))
        conn.commit()
        print("✅ Usuario Admin creado por defecto")
    except:
        pass # Si ya existe, no hace nada
    conn.close()

def verificar_login(usuario, contraseña):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, rol FROM usuarios WHERE usuario = ? AND password = ?", 
                   (usuario, contraseña))
    resultado = cursor.fetchone()
    conn.close()
    
    if resultado:
        return {"nombre": resultado[0], "rol": resultado[1], "valido": True}
    else:
        return {"valido": False}

def pantalla_login():
    print("\n")
    print("╔══════════════════════════════════════╗")
    print("║           ACCESO RESTRINGIDO         ║")
    print("║           SISTEMA H&I SYSTEM         ║")
    print("╚══════════════════════════════════════╝")
    
    usuario = input("👤 Usuario: ")
    contraseña = input("🔒 Contraseña: ")
    
    datos = verificar_login(usuario, contraseña)
    
    if datos["valido"]:
        print(f"\n✅ Bienvenido {datos['nombre']}! | Nivel: {datos['rol']}")
        print("------------------------------------------")
        return datos
    else:
        print("❌ Usuario o contraseña incorrectos.")
        return None
 
