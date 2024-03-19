from pymodbus.client import ModbusTcpClient

def scan_modbus_addresses(ip_address, port, unit_id, start_address, end_address):
    occupied_addresses = {}
    try:
        # Crear un cliente Modbus TCP
        client = ModbusTcpClient(ip_address, port)

        # Conectar al dispositivo
        client.connect()

        # Escanear direcciones Modbus
        for address in range(start_address, end_address + 1):
            response = client.read_holding_registers(address, 1, unit=unit_id)
            if not response.isError():
                occupied_addresses[address] = response.registers[0]

        # Desconectar
        client.close()
    except Exception as e:
     print("Error:", type(e), "-", str(e))

    return occupied_addresses


# Ejemplo de uso
if __name__ == "__main__":
    # Configuración del dispositivo Modbus
    IP_ADDRESS = "192.168.2.177"
    PORT = 502
    UNIT_ID = 254
    START_ADDRESS = 40002
    END_ADDRESS = 40003


    # Escanear direcciones Modbus
    occupied_addresses = scan_modbus_addresses(IP_ADDRESS, PORT, UNIT_ID, START_ADDRESS, END_ADDRESS)
    print("Direcciones Modbus ocupadas y sus valores:")
    for address, value in occupied_addresses.items():
        print(f"Dirección: {address}, Valor: {value}")
