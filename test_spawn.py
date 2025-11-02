# test_spawn.py
import socket, time

UDP_IP, UDP_PORT = "127.0.0.1", 8888
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(5):
    msg = f"spawn_car|TEST_DONOR_{i}"
    sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))
    print("Enviado:", msg)
    time.sleep(1)
