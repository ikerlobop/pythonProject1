def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while retries > 0:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries -= 1
        print(reminder)
    raise ValueError('Invalid user response')

# Ejemplo de uso
try:
    result = ask_ok("¿Quieres continuar? ")
    print("Respuesta válida:", result)
except ValueError as e:
    print(e)

