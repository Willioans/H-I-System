"""
🌐 H&I SYSTEM - VERSION WEB
Accede desde el navegador
"""

from flask import Flask, render_template_string, request
import sqlite3
import hashlib
from datetime import datetime

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
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (usuario TEXT, password TEXT, nombre TEXT, rol TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS clientes
                 (codigo TEXT, nombre TEXT, estado TEXT)''')
    
    # Insertar admin
    try:
        c.execute("INSERT INTO usuarios VALUES (?, ?, ?, ?)",
                 ('admin', encriptar('1234'), 'Administrador', 'SuperAdmin'))
        c.execute("INSERT INTO clientes VALUES (?, ?, ?)",
                 ('ADMIN001', 'ADMIN', 'ACTIVO'))
        conn.commit()
    except:
        pass
    conn.close()

# ==============================================
# PLANTILLA HTML (LA PAGINA WEB)
# ==============================================
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>H&I SYSTEM WEB</title>
    <style>
        body { font-family: Arial; background: #1a1a1a; color: white; text-align: center; padding-top: 50px; }
        .box { background: #333; padding: 30px; margin: auto; width: 300px; border-radius: 10px; }
        input { width: 100%; padding: 10px; margin: 10px 0; }
        button { background: #00aa00; color: white; padding: 10px 20px; border: none; font-size: 16px; }
        .menu { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 20px; }
        .item { background: #444; padding: 20px; border-radius: 8px; }
    </style>
</head>
<body>

    {% if not paso_licencia %}
        <div class="box">
            <h1>🔐 LICENCIA</h1>
            <form method="post">
                <input type="text" name="codigo" placeholder="Código de Cliente" required>
                <button type="submit" name="accion" value="licencia">VERIFICAR</button>
            </form>
        </div>

    {% elif not paso_login %}
        <div class="box">
            <h1>👤 INICIAR SESIÓN</h1>
            <form method="post">
                <input type="text" name="usuario" placeholder="Usuario" required>
                <input type="password" name="clave" placeholder="Contraseña" required>
                <button type="submit" name="accion" value="login">ENTRAR</button>
            </form>
        </div>

    {% else %}
        <h1>✅ BIENVENIDO AL SISTEMA H&I</h1>
        <div class="box menu">
            <div class="item">📦 BODEGA</div>
            <div class="item">👕 TIENDA</div>
            <div class="item">🔩 FERRETERIA</div>
            <div class="item">💪 GIMNASIO</div>
            <div class="item">🏍️ MOTO</div>
            <div class="item">🚗 CARRO</div>
            <div class="item">🍽️ RESTAURANTE</div>
            <div class="item">👑 ADMIN</div>
        </div>
    {% endif %}

</body>
</html>
"""

# ==============================================
# RUTAS
# ==============================================
@app.route('/', methods=['GET', 'POST'])
def index():
    paso_licencia = False
    paso_login = False
    
    if request.method == 'POST':
        accion = request.form.get('accion')
        
        if accion == 'licencia':
            cod = request.form.get('codigo')
            conn = conectar()
            c = conn.cursor()
            c.execute("SELECT * FROM clientes WHERE codigo=? AND estado='ACTIVO'", (cod,))
            if c.fetchone():
                paso_licencia = True
            conn.close()
            return render_template_string(HTML, paso_licencia=paso_licencia, paso_login=False)
        
        elif accion == 'login':
            user = request.form.get('usuario')
            pasw = encriptar(request.form.get('clave'))
            conn = conectar()
            c = conn.cursor()
            c.execute("SELECT * FROM usuarios WHERE usuario=? AND password=?", (user, pasw))
            if c.fetchone():
                paso_licencia = True
                paso_login = True
            conn.close()
            return render_template_string(HTML, paso_licencia=paso_licencia, paso_login=paso_login)
    
    return render_template_string(HTML, paso_licencia=False, paso_login=False)

# ==============================================
# EJECUTAR
# ==============================================
if __name__ == '__main__':
    init_db()
    print("🌐 SERVIDOR INICIADO...")
    print("👉 Abre tu navegador y ve a: http://127.0.0.1:5000")
    app.run(debug=True)
