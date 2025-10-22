import mysql.connector
import subprocess
import requests
import socket
from datetime import datetime


conn = mysql.connector.connect(
    host="localhost",
    user="monitor",
    password="senha_forte",
    database="monitoring"
)
cursor = conn.cursor()

def registrar_status(nome, tipo, status, tempo_resposta=0):
    sql = """
    INSERT INTO status_servicos (nome_servico, tipo, status, tempo_resposta_ms)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, (nome, tipo, status, tempo_resposta))
    conn.commit()
    print(f"{datetime.now()} | {nome} ({tipo}) -> {status} [{tempo_resposta}ms]")


def test_tcp(host, port):
    try:
        with socket.create_connection((host, port), timeout=5) as sock:
            registrar_status(f"{host}:{port}", "TCP", "OPEN")
    except Exception:
        registrar_status(f"{host}:{port}", "TCP", "CLOSED")


tcp_hosts = [("8.8.8.8", 53)]

for host, port in tcp_hosts:
    test_tcp(host, port)

cursor.close()
conn.close()
