# MTA IA Project

Sistema de automatización inteligente para **MTA San Andreas** que integra visión por computadora y control interactivo desde TikTok Live.

## 📋 Descripción

Este proyecto combina tres componentes principales:

### 1. **main.py** - Bot de Conducción Autónoma
- Utiliza **YOLOv8** para detectar vehículos en pantalla
- Detecta amenazas (vehículos que se acercan por encima de una línea roja)
- Esquiva automáticamente presionando las teclas A/D
- Realiza movimientos laterales periódicos para mayor realismo
- Captura pantalla a 60 FPS con `mss` y OpenCV

**Clases detectadas**: car, truck, bus, motorbike, bicycle

### 2. **tik_tok_listener.py** - Integración TikTok Live
- Conecta con TikTok Live del streamer (@zeninericson)
- Escucha eventos de interacción:
  - 💬 **Comentarios** → Spawn de Pony
  - 👥 **Seguir** → Spawn de Pony
  - ❤️ **Likes** → Spawn de Pony
  - 💎 **Regalos** → Diferentes vehículos según el regalo

**Mapeo de Regalos**:
- 🌹 Rose → Moonbeam (4×)
- 💕 Finger Heart → Rancher (12×)
- 🎩 Hat → Securecar (15×)
- 🍩 Donut → Stretch (16×)
- 🥊 Boxing Gloves → Rhino (21×)
- 🎉 Party Cone → SWAT Van (18×)
- 💰 Money Gun → Roadtrain (24×)
- 🌌 Galaxy → Bus (38×)
- 🐋 Whale → Dumper (60×)
- 🪼 Jellyfish → RESET
- 💗 Heart → AYUDA IA (Asistencia IA)

### 3. **test_spawn.py** - Pruebas
Script de prueba para verificar el sistema de spawn mediante UDP.

## 🔧 Dependencias

```
ultralytics (YOLOv8)
opencv-python (cv2)
mss (captura de pantalla)
pydirectinput (control de teclado)
TikTokLive
```

## 📥 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/mta-ai-streamer.git
cd mta-ai-streamer
```

### 2. Crear entorno virtual
```bash
python -m venv .venv
.venv\Scripts\activate  # En Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Descargar modelo YOLOv8
```bash
python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"
```

## 🚀 Uso

1. **Iniciar el listener de TikTok**:
   ```bash
   python tik_tok_listener.py
   ```

2. **Ejecutar el bot de conducción**:
   ```bash
   python main.py
   ```

## ⚙️ Configuración

En `main.py`:
- `FPS`: 60 (fotogramas por segundo)
- `START_REACT_Y`: 600px (altura donde el bot reacciona a amenazas)
- `SIDE_INTERVAL`: 3 segundos (intervalo de movimientos laterales)
- `MODEL_PATH`: 'yolov8n.pt' (modelo YOLOv8 nano)

En `tik_tok_listener.py`:
- `ID`: Username del streamer en TikTok
- `QUEUE`: Ruta del archivo spawnqueue.txt del servidor MTA

---

**Generado por Jhoan Hernandez**
