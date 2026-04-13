"""
🌐 H&I SYSTEM - VERSION PWA
PROGRESSIVE WEB APPLICATION
✅ Funciona en Celulares y PC
✅ Se puede instalar como App
✅ Sin instaladores, solo abrir y usar
"""

from flask import Flask, render_template_string, request, jsonify
import sqlite3
import hashlib
from datetime import datetime, timedelta

app = Flask(__name__)

# ==============================================
# BASE DE DATOS
# ==============================================
def conectar():
    return sqlite3.connect('h&i_system.db')

def encriptar(texto):
    return hashlib.sha256(texto.encode()).hexdigest()

def init_db():
    conn = conectar()
    c = conn.cursor()
    
    # Tablas
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (id INTEGER PRIMARY KEY, usuario TEXT, password TEXT, nombre TEXT, rol TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS clientes
                 (id INTEGER PRIMARY KEY, codigo TEXT, nombre TEXT, fecha_fin TEXT, estado TEXT)''')
    
    # Insertar Admin
    try:
        c.execute("INSERT INTO usuarios VALUES (NULL, 'admin', ?, 'Administrador', 'SuperAdmin')", 
                  (encriptar("1234"),))
        fecha_fin = (datetime.now() + timedelta(days=365)).strftime("%d/%m/%Y")
        c.execute("INSERT INTO clientes VALUES (NULL, 'ADMIN001', 'ADMINISTRADOR', ?, 'ACTIVO')", 
                  (fecha_fin,))
        conn.commit()
    except:
        pass
    conn.close()

# ==============================================
# PLANTILLA PRINCIPAL (LA INTERFAZ)
# ==============================================
HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>H&I SYSTEM</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: Arial, sans-serif; }
        body { background: #121212; color: white; }
        .screen { display: none; padding: 20px; max-width: 500px; margin: auto; }
        .active { display: block !important; }
        
        .logo { text-align: center; font-size: 24px; margin: 30px 0; color: #00ff88; }
        input, button {
            width: 100%;
            padding: 15px;
            margin: 8px 0;
            border: none;
            border-radius: 8px;
            font-size: 16px;
        }
        button { background: #00ff88; color: #121212; font-weight: bold; cursor: pointer; }
        
        .menu-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-top: 20px;
        }
        .menu-item {
            background: #2a2a2a;
            padding: 25px 10px;
            text-align: center;
            border-radius: 12px;
            font-size: 18px;
            border: 2px solid transparent;
        }
        .menu-item:hover { border-color: #00ff88; }
    </style>
</head>
<body>

    <!-- PANTALLA DE LICENCIA -->
    <div id="licencia" class="screen active">
        <div class="logo">🔐 VERIFICAR LICENCIA</div>
        <form onsubmit="enviarLicencia(event)">
            <input type="text" id="codigo" placeholder="Código de Cliente" required>
            <button type="submit">CONTINUAR</button>
        </form>
    </div>

    <!-- PANTALLA DE LOGIN -->
    <div id="login" class="screen">
        <div class="logo">👤 INICIAR SESIÓN</div>
        <form onsubmit="enviarLogin(event)">
            <input type="text" id="usuario" placeholder="Usuario" required>
            <input type="password" id="clave" placeholder="Contraseña" required>
            <button type="submit">ENTRAR</button>
        </form>
    </div>

    <!-- MENU PRINCIPAL -->
    <div id="menu" class="screen">
        <div class="logo">🚀 H&I SYSTEM</div>
        <div class="menu-grid">
            <div class="menu-item">📦 BODEGA</div>
            <div class="menu-item">👕 TIENDA</div>
            <div class="menu-item">🔩 FERRETERÍA</div>
            <div class="menu-item">💪 GIMNASIO</div>
            <div class="menu-item">🏍️ MOTO</div>
            <div class="menu-item">🚗 CARRO</div>
            <div class="menu-item">🍽️ RESTAURANTE</div>
            <div class="menu-item">👑 ADMIN</div>
        </div>
    </div>

<script>
function mostrar(id) {
    document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
    document.getElementById(id).classList.add('active');
}

function enviarLicencia(e) {
    e.preventDefault();
    const cod = document.getElementById('codigo').value;
    fetch('/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({accion: 'licencia', codigo: cod})
    }).then(res => res.json()).then(data => {
        if(data.ok) mostrar('login');
        else alert('❌ Código incorrecto o inactivo');
    });
}

function enviarLogin(e) {
    e.preventDefault();
    const user = document.getElementById('usuario').value;
    const pass = document.getElementById('clave').value;
    fetch('/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({accion: 'login', usuario: user, clave: pass})
    }).then(res => res.json()).then(data => {
        if(data.ok) mostrar('menu');
        else alert('❌ Usuario o clave incorrectos');
    });
}
</script>

</body>
</html>
"""

# ==============================================
# RUTAS
# ==============================================
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template_string(HTML)
    
    data = request.get_json()
    accion = data.get('accion')
    
    if accion == 'licencia':
        cod = data.get('codigo')
        conn = conectar()
        c = conn.cursor()
        c.execute("SELECT estado FROM clientes WHERE codigo=?", (cod,))
        res = c.fetchone()
        conn.close()
        return jsonify({"ok": res and res[0] == "ACTIVO"})
    
    elif accion == 'login':
        user = data.get('usuario')
        pasw = encriptar(data.get('clave'))
        conn = conectar()
        c = conn.cursor()
        c.execute("SELECT * FROM usuarios WHERE usuario=? AND password=?", (user, pasw))
        res = c.fetchone()
        conn.close()
        return jsonify({"ok": res is not None})

# ==============================================
# EJECUTAR
# ==============================================
if __name__ == '__main__':
    init_db()
    print("🌐 SERVIDOR PWA INICIADO")
    print("👉 Abre tu navegador y entra a la dirección que aparece abajo")
    app.run(host='0.0.0.0', port=8080, debug=True)
