import serial
import socket

def detect_connection():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("192.168.100.20", 5000))  # IP & device port
        print("Connection via TCP/IP")
        return client_socket, "TCP"
    except (socket.error, ConnectionRefusedError):
        ser = serial.Serial(port='/dev/ttyS0', baudrate=9600, timeout=1)
        print("Connection via RS232")
        return ser, "RS232"
