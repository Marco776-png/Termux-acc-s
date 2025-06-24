import socket

HOST = '0.0.0.0'  # Écoute sur toutes les interfaces
PORT = 9999       # Choisis un port libre

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"[*] En attente de connexion sur {HOST}:{PORT}")

conn, addr = server.accept()
print(f"[+] Connexion de {addr}")

while True:
    command = input("Commande à envoyer > ")
    if command.lower() == "exit":
        conn.send(b"exit")
        break
    if len(command.strip()) == 0:
        continue
    conn.send(command.encode())
    data = conn.recv(4096).decode()
    print(data)

conn.close()
server.close()
