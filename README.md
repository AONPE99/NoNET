⚠️ Este proyecto es solo con fines académicos.
No realiza actividad real maliciosa ni se conecta a Internet.
Se ejecuta únicamente en entorno controlado y simulado.

--------------------------------------------------------------------------------------------------------------------------------------------


# NoNET


NoNET es una botnet que infecta routers y módems residenciales directamente desde 
"internet"(credenciales por defecto y servicios expuestos), los convierte en nodos
persistentes para DDoS, spam y actividades maliciosas con IPs domésticas legítimas
sin que el usuario note nada… y que más adelante puede expandirse en silencio a
cualquier dispositivo IoT de la red: cámaras, bombillas, termostatos o 
electrodomésticos, transformando casas enteras en un ejército zombi invisible.

---------------------------------------------------------------------------------------------------------------

| Tecnología                 | Uso en el Proyecto                                                    |
| -------------------------- | --------------------------------------------------------------------- |
| **🐍 Python 3**            | Desarrollo del **C2** y los **bots**, manejo de lógica y flujo de red |
| **🔌 Sockets (TCP)**       | Comunicación directa entre C2 ↔ Bot ↔ Router                          |
| **🧾 JSON**                | Formato para configuración, estructura de comandos y respuestas       |
| **💻 Bash / Python (CLI)** | Ejecución en terminal para control y automatización                   |
| **📡 Wireshark / tcpdump** | Análisis del tráfico de red y monitoreo de paquetes                   |
| **🧪 Nmap / arp-scan**     | Escaneo de dispositivos y reconocimiento de la LAN                    |
| **🔧 Raspberry Pi**        | Plataforma física del C2 y Bot dentro de la red                       |



--------------------------------------------------------------------------------------------------------------------------------------------
### ⚙️ Requisitos del Sistema

📌 **Hardware (mínimo):**
- 1 CPU (1 núcleo)
- 512 MB de RAM
- 100 MB de espacio libre

🧠 **Recomendado para mejor rendimiento:**
- 2 núcleos CPU
- 1 GB RAM
- Linux  Python3 instalado

📌 **Sistema Operativo compatible:**
| Sistema | Compatible |
|--------|------------|
| Windows 7 /8.2 /10 / 11 | ✔ |
| Linux (Ubuntu, Debian, Arch...) | ✔ |
| Raspberry Pi OS | ✔ (opcional) |
| Termux Android  | ✔ (opcional) |
| macOS | ✔ |

### 📦 Dependencias
> ⚠️ **Requisito previo:** Python **3.8 o superior**  
> Verifica tu versión antes de ejecutar:

```bash
python --version
```
----------------------------------------------------------------------------------------------------------------


<!-- Título con estilo llamativo -->
<h2 align="center">⚙️ MODO DE EJECUCIÓN</h2>


### 1️⃣ Iniciar el servidor C2.py
```bash
python3 c2_server.py
```

### 2️⃣ Iniciar un bot.py

```bash
python3 bot.py
```

----------------------------------------------------------------------------------------------------------------
