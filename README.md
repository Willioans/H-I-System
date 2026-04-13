<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>H&I SYSTEM</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: Arial, sans-serif; }
        body { background: #121212; color: white; min-height: 100vh; }
        .screen { display: none; padding: 20px; max-width: 450px; margin: auto; padding-top: 80px; }
        .active { display: block !important; }
        
        .titulo { 
            text-align: center; 
            font-size: 28px; 
            margin-bottom: 30px; 
            color: #00ff88; 
            text-shadow: 0 0 10px #00ff88;
        }
        input {
            width: 100%;
            padding: 15px;
            margin: 10px 0;
            border: none;
            border-radius: 8px;
            background: #2a2a2a;
            color: white;
            font-size: 16px;
        }
        button {
            width: 100%;
            padding: 15px;
            margin-top: 15px;
            background: #00ff88;
            color: #121212;
            border: none;
            border-radius: 8px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 0 15px rgba(0,255,136,0.3);
        }
        .menu-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-top: 20px;
        }
        .modulo {
            background: #1e1e1e;
            padding: 25px 10px;
            text-align: center;
            border-radius: 12px;
            font-size: 17px;
            border: 2px solid #333;
            transition: 0.3s;
        }
        .modulo:hover {
            border-color: #00ff88;
            box-shadow: 0 0 15px rgba(0,255,136,0.2);
        }
    </style>
</head>
<body>

    <div id="pantalla-licencia" class="screen active">
        <h1 class="titulo">🔐 VERIFICAR LICENCIA</h1>
        <input type="text" id="codigo" placeholder="Código de Cliente">
        <button onclick="verificarLicencia()">CONTINUAR</button>
    </div>

    <div id="pantalla-login" class="screen">
        <h1 class="titulo">👤 INICIAR SESIÓN</h1>
        <input type="text" id="usuario" placeholder="Usuario">
        <input type="password" id="clave" placeholder="Contraseña">
        <button onclick="verificarLogin()">ENTRAR</button>
    </div>

    <div id="pantalla-menu" class="screen">
        <h1 class="titulo">🚀 H&I SYSTEM</h1>
        <div class="menu-grid">
            <div class="modulo">📦 BODEGA</div>
            <div class="modulo">👕 TIENDA</div>
            <div class="modulo">🔩 FERRETERÍA</div>
            <div class="modulo">💪 GIMNASIO</div>
            <div class="modulo">🏍️ MOTO</div>
            <div class="modulo">🚗 CARRO</div>
            <div class="modulo">🍽️ RESTAURANTE</div>
            <div class="modulo">👑 ADMIN</div>
        </div>
    </div>

<script>
const usuarios = [
    { usuario: "admin", password: "1234", nombre: "Administrador", rol: "SuperAdmin" }
];

const clientes = [
    { codigo: "ADMIN001", nombre: "ADMINISTRADOR", estado: "ACTIVO" }
];

function mostrarPantalla(id) {
    document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
    document.getElementById(id).classList.add('active');
}

function verificarLicencia() {
    const cod = document.getElementById('codigo').value.trim().toUpperCase();
    const valido = clientes.some(c => c.codigo === cod && c.estado === "ACTIVO");
    valido ? mostrarPantalla('pantalla-login') : alert('❌ CÓDIGO INVÁLIDO');
}

function verificarLogin() {
    const user = document.getElementById('usuario').value.trim();
    const pass = document.getElementById('clave').value.trim();
    const valido = usuarios.some(u => u.usuario === user && u.password === pass);
    valido ? mostrarPantalla('pantalla-menu') : alert('❌ DATOS INCORRECTOS');
}
</script>

</body>
</html>
