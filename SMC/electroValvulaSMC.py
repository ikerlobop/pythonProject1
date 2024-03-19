import tkinter as tk
from pymodbus.client import ModbusTcpClient
import threading
import time


# Direcciones IP y puerto del dispositivo Modbus TCP
SERVER_HOST = '192.168.2.149'
SERVER_PORT = 502

class ModbusControlApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Control de Electrovalvula")

        # Direcciones de registro de electroválvulas para monitorear
        # Ejemplos de direcciones
        self.valve_register_addresses = [0x0009, 0x0010, 0x000C, 0x000F]

        # Crear cliente Modbus
        self.client = ModbusTcpClient(SERVER_HOST, port=SERVER_PORT)

        # Crear etiquetas, casillas de verificación y estados para cada dirección de registro
        self.labels = []
        self.checkboxes = []
        self.states = []
        self.labels_states = []  # Lista para almacenar los widgets de estado (True/False con fondo rojo/verde)
        for i, address in enumerate(self.valve_register_addresses):
            label = tk.Label(master, text=f"Registro {hex(address)}:")
            label.grid(sticky="w")
            self.labels.append(label)

            var = tk.IntVar()
            checkbox = tk.Checkbutton(master, variable=var)
            checkbox.grid(sticky="w")
            self.checkboxes.append(checkbox)

            state_label = tk.Label(master, text="False", width=5, bg="red")
            state_label.grid(sticky="w")
            self.labels_states.append(state_label)

            self.states.append(var)

        # Iniciar hilo de escaneo continuo
        self.scan_thread = threading.Thread(target=self.continuous_scan, daemon=True)
        self.scan_thread.start()

        # Botón para cambiar el estado de las electroválvulas
        self.button = tk.Button(master, text="Cambiar estado de la electroválvula", command=self.change_valve_state)
        self.button.grid(sticky="ew")

    def continuous_scan(self):
        while True:
            try:
                # Conectarse al dispositivo Modbus
                self.client.connect()

                # Escanear el estado actual de las electroválvulas
                for i, address in enumerate(self.valve_register_addresses):
                    state = self.client.read_coils(address, 1).bits[0]
                    self.states[i].set(int(state))

                    # Actualizar el texto y color del estado
                    if state:  # Si el estado es True
                        self.labels_states[i].config(text="True", bg="green")
                    else:  # Si el estado es False
                        self.labels_states[i].config(text="False", bg="red")

            finally:
                # Cerrar la conexión
                self.client.close()

            # Esperar un momento antes de volver a escanear (por ejemplo, 1 segundo)
            time.sleep(10)

    def change_valve_state(self):
        try:
            self.client.connect()

            # Cambiar el estado
            for i, address in enumerate(self.valve_register_addresses):
                state = self.states[i].get()
                self.client.write_coil(address, state)

            print("Se han cambiado los estados de las electroválvulas.")

        finally:

            self.client.close()

def main():
    root = tk.Tk()
    app = ModbusControlApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

