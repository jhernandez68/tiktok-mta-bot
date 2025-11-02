# tik_tok_listener.py

import os
import socket
from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, CommentEvent, GiftEvent, FollowEvent

QUEUE = r"C:\Program Files (x86)\MTA San Andreas 1.6\server\mods\deathmatch\resources\spawncar\spawnqueue.txt"
ID = "@zeninericson"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client = TikTokLiveClient(unique_id=ID)

def enqueue(entry: str):
    with open(QUEUE, "a", encoding="utf-8") as f:
        f.write(entry + "\n")

open(QUEUE, "w", encoding="utf-8").close()

@client.on(ConnectEvent)
async def on_connect(event: ConnectEvent):
    print(f"✅ Conectado al stream {ID!r}, room_id={client.room_id}")

@client.on(CommentEvent)
async def on_comment(event: CommentEvent):
    who = event.user.unique_id or event.user.nickname
    enqueue(f"Pony|{who}")
    print(f"💬 Comentario de {who} → spawn Pony")

@client.on(FollowEvent)
async def on_follow(event: FollowEvent):
    who = event.user.unique_id or event.user.nickname
    enqueue(f"Pony|{who}")
    print(f"👥 Nuevo follow de {who} → spawn Pony")

gift_map = {
    "rose":          ("Moonbeam",    4),
    "finger heart":  ("Rancher",    12),
    "hat":           ("Securecar",  15),
    "donut":         ("Stretch",    16),
    "boxing gloves": ("Rhino",      21),
    "party cone":    ("SWAT Van",   18),
    "money gun":     ("Roadtrain",  24),
    "galaxy":        ("Bus",        38),
    "whale":         ("Dumper",     60),
    "jellyfish":     ("RESET",       1),
    "heart":         ("AYUDA IA",    1),
}

@client.on(GiftEvent)
async def on_gift(event: GiftEvent):
    raw_name = getattr(event.gift, "name", "") or ""
    key      = raw_name.lower()
    print(f"💎 Gift recibido: '{raw_name}' → key='{key}'")
    mapping = gift_map.get(key)
    if not mapping:
        print("⚠️ Gift no mapeado:", raw_name)
        return
    typ, count = mapping
    who = event.user.unique_id or event.user.nickname
    for _ in range(count):
        enqueue(f"{typ}|{who}")
    print(f"✅ Encolados {count}×{typ} por regalo '{raw_name}'")

if __name__ == "__main__":
    client.run()
