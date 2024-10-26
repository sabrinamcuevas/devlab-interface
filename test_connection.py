import socket
import serial
from unittest.mock import patch
from connection import detect_connection

@patch('socket.socket.connect')
def test_detect_conexion_tcp(mock_connect):
    mock_connect.return_value = True
    device, connection_type = detect_connection()
    assert connection_type == "TCP"
    assert isinstance(device, socket.socket)

@patch('serial.Serial')
@patch('socket.socket.connect', side_effect=socket.error)
def test_detect_conexion_rs232(mock_connect, mock_serial):
    mock_serial_instance = mock_serial.return_value
    device, connection_type = detect_connection()
    assert connection_type == "RS232"
    assert device == mock_serial_instance
