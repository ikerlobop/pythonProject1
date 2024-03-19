import tkinter as tk
from tkinter import messagebox
import subprocess

def obtener_ip():
    try:
        resultado = subprocess.run(['powershell', '-Command', "(Get-NetAdapter | Where-Object {$_.Status -eq 'Up'}).IPAddress"], capture_output=True, text=True)
        ips = resultado.stdout.strip().split('\n')
        messagebox.showinfo("Direcciones IP", "Direcciones IP de las conexiones activas:\n" + "\n".join(ips))
    except Exception as e:
        messagebox.showerror("Error", "Se produjo un error al obtener las direcciones IP:\n" + str(e))

# Crear la ventana principal
root = tk.Tk()
root.title("Obtener IP de conexiones activas")

# Crear y posicionar los elementos en la ventana
label = tk.Label(root, text="Presiona el botón para obtener las direcciones IP de las conexiones activas.")
label.pack(pady=10)

button = tk.Button(root, text="Obtener IP", command=obtener_ip)
button.pack(pady=5)

# Ejecutar el bucle principal
root.mainloop()
