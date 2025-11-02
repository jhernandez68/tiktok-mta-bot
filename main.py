import time
import numpy as np
import cv2
import pydirectinput
from mss import mss
from ultralytics import YOLO

MODEL_PATH     = 'yolov8n.pt'
TARGET_CLASSES = {'car', 'truck', 'bus', 'motorbike', 'bicycle'}
MONITOR        = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
FPS            = 60
FRAME_TIME     = 1.0 / FPS
START_REACT_Y  = 600  # px: nivel de la “línea roja”

# Intervalo y dirección de movimiento lateral
SIDE_INTERVAL  = 3.0   # segundos entre movimientos
side_direction = 'd'
last_side_time = time.time()

model = YOLO(MODEL_PATH)
sct   = mss()

def capture_frame():
    img = np.array(sct.grab(MONITOR))
    return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

def detect_vehicles(frame):
    res = model(frame)[0]
    vehicles = []
    for box in res.boxes:
        cls = int(box.cls)
        name = res.names[cls]
        if name in TARGET_CLASSES:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cx = (x1 + x2) // 2
            bottom = y2
            vehicles.append((cx, bottom))
    return vehicles

# Mantener W
pydirectinput.keyDown('w')
time.sleep(1)

while True:
    start = time.time()
    frame = capture_frame()
    vehicles = detect_vehicles(frame)

    # Reacción a amenazas
    threats = [(cx, b) for cx, b in vehicles if b <= START_REACT_Y]
    if threats:
        center_x = MONITOR['width'] // 2
        cx, _ = min(threats, key=lambda t: abs(t[0] - center_x))
        dodge_key = 'a' if cx > center_x else 'd'
        pydirectinput.keyUp('w')
        pydirectinput.press(dodge_key)
        pydirectinput.keyDown('w')

    # Movimiento lateral periódico
    now = time.time()
    if now - last_side_time >= SIDE_INTERVAL:
        pydirectinput.keyUp('w')
        pydirectinput.press(side_direction)
        pydirectinput.keyDown('w')
        # alternar dirección
        side_direction = 'a' if side_direction == 'd' else 'd'
        last_side_time = now

    # Dibuja línea roja guía
    cv2.line(frame,
             (0, START_REACT_Y),
             (MONITOR['width'], START_REACT_Y),
             (0,0,255), 2)
    cv2.imshow('MTA SA', frame)

    # Salir con Esc
    if cv2.waitKey(1) & 0xFF == 27:
        break

    # Control de FPS
    elapsed = time.time() - start
    if elapsed < FRAME_TIME:
        time.sleep(FRAME_TIME - elapsed)

pydirectinput.keyUp('w')
cv2.destroyAllWindows()
