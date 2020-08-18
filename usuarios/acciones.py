import usuarios.usuario as modelo
import notas.acciones as notas


class Acciones:

    def registro(self):
        print("\nOK!! Vamos a registrarte en el sistema...")
        nombre = input("¿Cuál es tu nombre?: ")
        apellidos = input("¿Cuáles son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce una contraseña: ")
        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()
        if registro[0] >= 1:
            print(
                f"Perfecto {registro[1].nombre}, te has registrado con el email {registro[1].email}")
        else:
            print("No te has registrado correctamente!!")

    def login(self):
        print("OK!! Identificate en el sistema")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")
        usuario = modelo.Usuario('', '', email, password)
        login = usuario.identificar()
        if email == login[3]:
            print(
                f"Bienvenido {login[1]}, te has registrado con en el sistema el {login[5]}")
            self.proximasAcciones(login)
        elif login == None:
            print("Login incorrecto, intentalo mas tarde!!")

    def proximasAcciones(self, usuario):
        print("""
            Acciones disponibles:
                - Crear nota (crear)
                - Mostrar tus notas (mostrar)
                - Eliminar nota (eliminar)
                - Salir (salir)
        """)
        accion = input("¿Qué quieres hacer?: ")
        hazEl = notas.Acciones()
        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "salir":
            print(f"Ok {usuario[1]}, hasta pronto!!")
            exit()
