import socket
import errno
import time

ip_address = '192.168.2.240'
port = 41300

# Datos para controlar la electroválvula (debes ajustar estos valores según la especificación de tu dispositivo)
command_template = b'\x01\x01\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x01\x00'

valve_states = {'A': False, 'B': False, 'C': False}


def generate_command(valve_states_):
    command = bytearray(command_template)
    for valvula, state in valve_states_.items():
        if state:
            command[11] |= 1 << (ord(valve) - ord('A'))
        else:
            command[11] &= ~(1 << (ord(valve) - ord('A')))
    return bytes(command)


print("Estableciendo conexión..", end='', flush=True)

try:
    for i in range(12):  # Ciclo para hacer que los puntos suspensivos parpadeen 12 veces
        print(".", end='', flush=True)
        time.sleep(0.5)
        print("\b", end='', flush=True)  # Borrar el último punto
        time.sleep(0.5)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(10)

        s.connect((ip_address, port))
        print("Conexión establecida con éxito.")
        s.sendall(generate_command(valve_states))
        response = s.recv(1024)
        print("Respuesta del dispositivo:", response)

        while True:
            print("\nMenú de control de válvulas:")
            print("1. Comprobar estado de una válvula")
            print("2. Cambiar estado de una válvula")
            print("3. Salir")
            choice = input("Seleccione una opción (1/2/3): ")

            if choice == '1':
                valve = input("Ingrese la letra de la válvula (A/B/C): ")
                if valve.upper() in valve_states:
                    print(f"Estado de la válvula {valve.upper()}: {valve_states[valve.upper()]}")
                else:
                    print("Válvula no válida. Por favor, ingrese A, B o C.")

            elif choice == '2':
                valve = input("Ingrese la letra de la válvula (A/B/C): ")
                if valve.upper() in valve_states:
                    new_state = input("Ingrese el nuevo estado (True/False): ")
                    if new_state.lower() == 'true':
                        valve_states[valve.upper()] = True
                    elif new_state.lower() == 'false':
                        valve_states[valve.upper()] = False
                    else:
                        print("Entrada no válida. Por favor, ingrese True o False.")
                else:
                    print("Válvula no válida. Por favor, ingrese A, B o C.")

            elif choice == '3':
                print("Saliendo del programa.")
                break

            else:
                print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

except socket.timeout:
    print("Error: Tiempo de espera agotado. Verifique la conexión e inténtelo nuevamente.")

except socket.error as e:
    if e.errno == errno.WSAECONNREFUSED:
        print("Error: La conexión fue rechazada por el servidor. Verifique la configuración del servidor.")
    else:
        print("Error:", e)

