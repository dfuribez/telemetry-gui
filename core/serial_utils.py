from serial.tools import list_ports

def get_serial_ports():
    return [port.device for port in list_ports.comports()]