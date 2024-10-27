from connection import detect_connection
from reading import read_message
from processing import interpret_message
from send_data import send_data

def main():
    device, connection_type = detect_connection()
    data = read_message(device, connection_type)
    datos = interpret_message(data)
    send_data(datos)

if __name__ == "__main__":
    main()
