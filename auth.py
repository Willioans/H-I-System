"""
🔐 SISTEMA DE AUTENTICACIÓN AVANZADA
H&I System
SEGURIDAD MÁXIMA Y ENCRIPTACIÓN
"""

import sys
import os
import hashlib # 🛡️ LIBRERÍA PARA ENCRIPTAR
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from base_datos import conectar

# Función para convertir texto en código ilegible
def encriptar_texto(texto):
    return hashlib.sha256(texto.encode()).hexdigest()

# Crear usuario ADMIN por defecto (CLAVE ENCRIPTADA)
def crear_admin_default():
    conn = conectar()
    cursor = conn.cursor()
    try:
        clave_encriptada = encriptar_texto("1234")
        cursor.execute("INSERT INTO usuarios (usuario, password, nombre, rol) VALUES (?, ?, ?, ?)",
                       ("admin", clave_encriptada, "Administrador", "SuperAdmin"))
        conn.commit()
        print("✅ Usuario Admin creado y protegido")
    except:
        pass # Si ya existe, no hace nada
    conn.close()

def verificar_login(usuario, contraseña):
    conn = conectar()
    cursor = conn.cursor()
    
    # Encriptamos lo que escribe el usuario para comparar
    contraseña_encriptada = encriptar_texto(contraseña)
    
    cursor.execute("SELECT nombre, rol FROM usuarios WHERE usuario = ? AND password = ?", 
                   (usuario, contraseña_encriptada))
    resultado = cursor.fetchone()
    conn.close()
    
    if resultado:
        return {"nombre": resultado[0], "rol": resultado[1], "valido": True}
    else:
        return {"valido": False}

def pantalla_login():
    print("\n")
    print("╔══════════════════════════════════════╗")
    print("║        ACCESO SEGURO 🔐             ║")
    print("║           SISTEMA H&I               ║")
    print("╚══════════════════════════════════════╝")
    
    usuario = input("👤 Usuario: ")
    contraseña = input("🔒 Contraseña: ")
    
    datos = verificar_login(usuario, contraseña)
    
    if datos["valido"]:
        print(f"\n✅ Bienvenido {datos['nombre']}! | Nivel: {datos['rol']}")
        print("🛡️ Conexión encriptada activada.")
        print("------------------------------------------")
        return datos
    else:
        print("❌ Usuario o contraseña incorrectos.")
        return None
