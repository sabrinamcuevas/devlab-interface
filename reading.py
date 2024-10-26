def read_message(connected_device, connection_type):
    if connection_type == "TCP":
        data = connected_device.recv(1024).decode("utf-8")
    else:
        data = connected_device.read(1024).decode("utf-8")
    print(f"Message received: {data}")
    return data
