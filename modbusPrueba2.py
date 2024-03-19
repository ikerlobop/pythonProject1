from pymodbus.client import ModbusTcpClient


def get_device_info(ip_address, port, unit_id):
    try:
        client = ModbusTcpClient(ip_address, port)
        client.connect()

        # Leer registros específicos que contienen información del dispositivo
        # Ejemplo: leer el modelo del dispositivo
        response = client.read_holding_registers(0, 20, unit=unit_id)  # Dirección y cantidad de registros a leer

        if not response.isError():
            device_info = response.registers  # Procesar los datos según la estructura definida en la documentación

            # Procesar la información del dispositivo
            # Ejemplo: decodificar la información de los registros leídos
            model = ''.join(chr(char) for char in
                            device_info)  # Ejemplo de decodificación, esto puede variar según la estructura de los
            # datos

            print("Modelo del dispositivo:", model)
        else:
            print("Error al leer registros:", response)

        client.close()
    except Exception as e:
        print("Error:", e)


# Ejemplo de uso
if __name__ == "__main__":
    IP_ADDRESS = "192.168.2.149"  # IP del dispositivo Modbus
    PORT = 502  # Puerto del dispositivo Modbus
    UNIT_ID = 2  # Modbus Unit ID del dispositivo

    get_device_info(IP_ADDRESS, PORT, UNIT_ID)
