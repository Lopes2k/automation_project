import socket

host = "google.com"
port = 80

try:
    sock = socket.create_connection((host, port), timeout=5)
    print(f"{host}:{port} está acessível")
    sock.close()
except socket.error:
    print(f"{host}:{port} NÃO está acessível")