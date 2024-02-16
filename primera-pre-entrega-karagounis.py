usuarios = {}

def Registro():
    nuevo_usuario = input(f"Ingrese un nuevo nombre de usuario: \n")
    nueva_contraseña = input(f"Ingrese una nueva contraseña: \n")

    if nuevo_usuario not in usuarios and nueva_contraseña not in usuarios.values():
        usuarios[nuevo_usuario] = nueva_contraseña
        print(f"Usuario registrado exitosamente.")
    
        return
    else:
        print(f"El usuario o la contraseña ya están en uso.")

        return
def Login():
    input1 = input(f"Usuario: ")
    input2 = input(f"Contraseña: ")

    if input1 in usuarios and usuarios[input1] == input2:
        print(f"¡Bienvenido al programa!")

        return
    else:
        print(f"Usuario o contraseña incorrectos.")

        return
def leerData():
    for clave, valor in usuarios.items():
        print(clave, valor)

    return
def guardarEnArchivo():
    with open("C:/Users/Rufo/Desktop/usuarios.txt", "w") as archivo:
        for clave, valor in usuarios.items():
            archivo.write(f"{clave}: {valor}\n")
    return
if __name__ == "__main__":
    while True:
        print(f"\n1. Registrar nuevo usuario")
        print(f"2. Iniciar sesion")
        print(f"3. Imprimir datos de usuarios")
        print(f"4. Guardar datos en archivo")
        print(f"5. Salir")
        opcion = input(f"Seleccione una opcion: \n")

        if opcion == "1":
            Registro()
        elif opcion == "2":
            Login()
        elif opcion == "3":
            leerData()
        elif opcion == "4":
            guardarEnArchivo()
            print(f"Datos guardados en archivo 'usuarios.txt'.")
        elif opcion == "5":
            print(f"¡Hasta luego!")
            break
        else:
            print(f"Opción invalida. Por favor, seleccione una opción valida.")