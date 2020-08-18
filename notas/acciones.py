import notas.nota as modelo


class Acciones:

    def crear(self, usuario):
        print(f"\nOk {usuario[1]}!! Vamos a crear una nueva nota...")
        titulo = input("Introduce el título de tu nota: ")
        descripcion = input("Introduce el contenido de tu nota: ")
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()
        if guardar[0] >= 1:
            print(f"\nPerfecto, has guardado la nota: {nota.titulo}")
        else:
            print(f"\nNo se ha guardado la nota, lo siento {usuario[1]}")
        return guardar

    def mostrar(self, usuario):
        print(f"OK {usuario[1]}!! Aquí estan tus notas: ")
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        for nota in notas:
            print("*******************************************************")
            print(f"Título: {nota[2]}")
            print(f"\nContenido : \n - {nota[3]}")
            print("\n*******************************************************")

    def borrar(self, usuario):
        print(f"\nOK {usuario[1]}!! Vamos a borrar notas...")
        titulo = input("Introduce el título de la nota a borrar: ")
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()
        if eliminar[0] >= 1:
            print(f"Se borró la nota: {nota.titulo}")
        else:
            print("No se borró la nota, intentalo nuevamente...")
