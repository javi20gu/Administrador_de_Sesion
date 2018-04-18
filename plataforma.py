from sys import argv, exit
from obj_cliente import Cliente


def iniciar_sesion(clientes: list):

    email = input("\nIntroduzca su email: ")
    pasword = input("Introduce su contraseña: ")

    for cliente in clientes:
        if cliente.get_email() == email and cliente.get_password() == pasword:
            print("\nHas Iniciado la sesión como: {}\n".format(cliente.get_nombre()))
            break
    else:
        print("Correo o Contraseña incorrecto.\n")


def crear_sesion(clientes: list):

    clientes.append(Cliente())

    for cliente in clientes:
        if not cliente.get_operativo():
            cliente.set_nombre(input("Introduce su Nombre: "))
            cliente.set_apellidos(input("Introduce sus apellidos: "))
            try:
                edad = int(input("Introduce su edad: "))
                cliente.set_edad(edad)
            except ValueError as error:
                print("Numero esperado --> [{}]".format(error))
            cliente.set_email(input("Introduce su email: "))
            cliente.set_password(input("Introduce su contraseña: "))
            cliente.set_operativo(True)
            print("\n{} --> Correcto".format(cliente), end='\n\n')
        else:
            continue

def main():
    clientes: list = []

    print("--------------Bienvenido--------------\n")

    while True:
        opcion_elegida = input("1) Iniciar Sesión\n2) Crear Sesión\n3) Salir\n>>>")
    
        if opcion_elegida == '1':
            iniciar_sesion(clientes)
        elif opcion_elegida == '2':
            crear_sesion(clientes)
        elif opcion_elegida == '3':   
            exit()   


if __name__ == '__main__':
    for arg in argv:
        if arg == "--start":
            main()
    else:
        print("Introduzca el comando --start para iniciar.")
