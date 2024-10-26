from unittest.mock import MagicMock
from reading import read_message

def test_read_message_tcp():
    mock_device = MagicMock()
    mock_device.recv.return_value = b'MSH|^~\\&|LAB|L||202401012359||ORU^R01|12345|P|2.4'
    data = read_message(mock_device, "TCP")
    assert "MSH" in data

def test_read_message_rs232():
    mock_device = MagicMock()
    mock_device.read.return_value = b'MSH|^~\\&|LAB|L||202401012359||ORU^R01|12345|P|2.4'
    data = read_message(mock_device, "RS232")
    assert "MSH" in data
