from usuarios import acciones

print("""
  Acciones disponibles: 
    - Registro
    - Login
""")

hazEl = acciones.Acciones()

accion = input("¿Qué quieres hacer?: ")

if accion == "registro":
    hazEl.registro()
elif accion == "login":
    hazEl.login()
