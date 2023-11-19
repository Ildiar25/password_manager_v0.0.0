###################################################   PRESENTATION   ###################################################

# This is a litle project about Password Manager.
# This is the version 0.0.0 where we are going to add the first steps to become a great and useful program.

# On this section I'm going to explain the points where I'm working on. First of all, I'll start with some functions
# and defying some variables to create the body program.

########################################################################################################################

import os
import time
from cryptography.fernet import Fernet
from config import PATH
from config import NAME
from config import BUILD

####################### ------------------------------ VARIABLES ------------------------------ #######################

content = os.listdir(f"C:/Users/{NAME}/")

####################### ------------------------------ FUNCTIONS ------------------------------ #######################


# SYSTEM FUNCTIONS ----


def install():
    main_folder = f"C:/Users/{NAME}/"
    print("Instalando...")

    os.mkdir(main_folder + "Password Manager")

    main_path = main_folder + "Password Manager/"

    time.sleep(2)
    print("Creando subcarpetas...")

    os.mkdir(main_path + "user")
    os.mkdir(main_path + "data")
    os.mkdir(main_path + "files")

    time.sleep(0.2)
    generate_key()

    open(main_path + "files/user_list.txt", "w").close()

    with open(main_path + "/build.txt", "w") as build_version:
        build_version.write(f"Password Manager {BUILD}")

    time.sleep(2)
    print("Instalación completada.")


def uninstall():
    print("Ha seleccionado desinstalar.")
    time.sleep(0.2)

    print("¿Seguro que desea desinstalar el programa?")
    print("Perderá cualquier información almacenada y no se podrá recuperar...")

    while True:
        u_answer = input("Y/N: ").upper()

        if u_answer == "Y":

            print("Eliminando los archivos de sistema...")
            time.sleep(0.2)

            data_folder = PATH + "data/"
            files = os.listdir(data_folder)

            for ufile in files:
                print(ufile)
                os.remove(data_folder + ufile)

            time.sleep(0.2)
            files_folder = PATH + "files/"
            files = os.listdir(files_folder)

            for ufile in files:
                print(ufile)
                os.remove(files_folder + ufile)

            time.sleep(0.2)
            user_folder = PATH + "user/"
            files = os.listdir(user_folder)

            for ufile in files:
                print(ufile)
                os.remove(user_folder + ufile)

            time.sleep(0.2)

            print("Eliminando codificación...")

            print("key.key")
            os.remove(PATH + "key.key")
            time.sleep(0.2)

            print("build.txt")
            os.remove(PATH + "build.txt")
            time.sleep(0.2)

            print("Eliminando carpetas...")

            folders = os.listdir(PATH)

            for folder in folders:
                print("Carpeta " + folder + " eliminada")
                os.rmdir(PATH + folder)

            time.sleep(0.2)

            print("Limpiando sistema...")
            time.sleep(0.2)

            os.rmdir(f"C:/Users/{NAME}/Password Manager")
            print("Finalización Exitosa")
            time.sleep(0.2)

            print(f"Gracias por utilizar Password Manager" + BUILD)
            quit()

        elif u_answer == "N":
            break

        else:
            print(f"Lo siento, {u_answer} no es un comando válido.")
            continue


def new_file(name_file):
    print(f"Creación del elemento {name_file} en la biblioteca.")
    time.sleep(0.2)
    open(PATH + f"data/{name_file}.txt", "wb").close()

    user = input("Nombre de Usuario: ")
    password_01 = input("Contraseña: ")

    while True:
        password_02 = input("Repita la contraseña: ")

        if password_02 == password_01:
            print("Contraseña confirmada")
            time.sleep(0.2)

            user_encrypt = data_encode(user + "|" + password_01)

            with open(PATH + f"data/{name_file}.txt", "ab") as data:
                data.write(user_encrypt)

            print(f"{name_file} añadido a la biblioteca con éxito.")

            break

        else:
            print("Lo siento, la contraseña no coincide.")
            continue


def modify_file():
    content_list = os.listdir(PATH + "data")
    temp = []

    for element in content_list:
        name = element.split(".")
        temp.append(name[0])

    while True:
        print("Qué archivo desea modificar?")
        print(temp)
        element = input().upper()

        if element in temp:
            load_data = PATH + f"data/{element}.txt"
            l_data = data_decode(load_data)
            l_data = l_data.split("|")
            print("Usuario:", l_data[0])
            print("Contraseña:", l_data[1])

            while True:
                print("¿Qué desea modificar?")
                m_answer = input().upper()

                if m_answer == "USUARIO":
                    print("Introduzca el nuevo nombre de usuario:")
                    l_data[0] = input()

                    final_data = "|".join(l_data)

                    new_user = data_encode(final_data)

                    with open(PATH + f"data/{element}.txt", "wb") as nfile:
                        nfile.write(new_user)

                    print(f"Nombre de usuario de {element} actualizado.")
                    time.sleep(1)
                    break

                elif m_answer == "CONTRASEÑA":
                    print("Introduzca la nueva contraseña:")
                    l_data[1] = input()

                    final_data = "|".join(l_data)

                    new_password = data_encode(final_data)

                    with open(PATH + f"data/{element}.txt", "wb") as nfile:
                        nfile.write(new_password)

                    print(f"Contraseña de {element} actualizada.")
                    time.sleep(1)
                    break

                elif m_answer == "ATRÁS" or m_answer == "ATRAS":
                    break

                else:
                    print(f"Lo siento, {m_answer} no es un comando válido.")
                    continue

        elif element == "ATRÁS" or element == "ATRAS":
            break

        else:
            print(f"Lo siento, {file} no se encuentra en la lista de archivos almacenados.")
            continue


def view_file():
    content_list = os.listdir(PATH + "data")
    temp = []

    for element in content_list:
        name = element.split(".")
        temp.append(name[0])

    while True:
        print("¿Qué datos desea ver?")
        print(temp)
        v_answer = input().upper()

        if v_answer in temp:
            load_data = PATH + f"data/{v_answer}.txt"
            l_data = data_decode(load_data)
            l_data = l_data.split("|")

            print("Usuario:", l_data[0])
            print("Contraseña:", l_data[1])

            time.sleep(10)

        elif v_answer == "ATRÁS" or v_answer == "ATRAS":
            break

        else:
            print(f"Lo siento, {v_answer} no se encuentra en la lista de archivos almacenados.")
            continue


def delete_file():

    while True:
        content_list = os.listdir(PATH + "data")
        temp = []

        for element in content_list:
            name = element.split(".")
            temp.append(name[0])

        print("Ha seleccionado eliminar. ¿Que archivo desea eliminar de la lista siguiente?")
        print(temp)
        dfile = input().upper()

        if dfile in temp:
            print(f"Ha seleccionado eliminar {dfile}. ¿Desea proceder? Esta acción no se puede deshacer.")

            while True:
                d_answer = input("Y/N: ").upper()

                if d_answer == "Y":
                    print(f"{dfile} eliminado.")
                    time.sleep(0.2)

                    os.remove(PATH + f"data/{dfile}.txt")
                    break

                elif d_answer == "N":
                    print("De acuerdo.")
                    break

                elif d_answer == "ATRÁS" or d_answer == "ATRAS":
                    break

                else:
                    print(f"Lo siento, {d_answer} no es un comando válido.")
                    continue

        elif dfile == "ATRÁS" or dfile == "ATRAS":
            break

        else:
            print(f"Lo siento, {dfile} no tiene un archivo asociado.")
            continue


# CODING FUNCTIONS ----


def generate_key():
    key = Fernet.generate_key()

    with open(PATH + "key.key", "wb") as key_file:
        key_file.write(key)


def load_key():

    return open(PATH + "key.key", "rb").read()


def data_encode(data):
    data = data.encode()
    key = load_key()
    f = Fernet(key)

    return f.encrypt(data)


def data_decode(dfile):
    key = load_key()
    f = Fernet(key)

    with open(dfile, "rb") as encrypt_data:
        data = encrypt_data.read()

    decrypted_data = f.decrypt(data)

    return decrypted_data.decode()


# MAIN FUNCTIONS ----


def check_list(name):
    with open(PATH + "files/user_list.txt", "r") as user_list:
        u_list = user_list.read()
        u_list = u_list.split("|")

    if name in u_list:
        login(name)

    else:
        print(f"Parece que es su primera vez. No hay problema")
        new_profile(name)


def new_profile(name):
    print("Vamos a crear un nuevo usuario: ")
    time.sleep(0.2)

    open(PATH + f"user/{name}_DATA.txt", "wb").close()

    n_user = input("Nombre de Usuario: ")
    password_01 = input("Contraseña: ")

    while True:
        password_02 = input("Repita la contraseña: ")

        if password_02 == password_01:
            print("Contraseña confirmada")
            time.sleep(0.2)

            with open(PATH + "files/user_list.txt", "a") as data:
                data.write(name + "|")

            user_encrypt = data_encode(n_user + "|" + password_01)

            with open(PATH + f"user/{name}_DATA.txt", "ab") as data:
                data.write(user_encrypt)

            login(name)

            break

        else:
            print("Lo siento, la contraseña no coincide.")
            continue


def login(name):
    print("Inicie sesión rellenando los campos")
    load_user = PATH + f"user/{name}_DATA.txt"

    u_data = data_decode(load_user)
    u_data = u_data.split("|")

    time.sleep(2)

    for attempt in range(3):
        user = input("Nombre de usuario: ")
        password = input("Contraseña: ")

        if user == u_data[0] and password == u_data[1]:
            print("Bienvenido de nuevo!")
            break

        elif attempt == 2:
            print("Demasiados intentos, se cerrará el programa.")
            time.sleep(2)
            quit()

        else:
            print("Usuario o contraseña no coinciden. Vuelva a intentarlo.")
            continue


def profile_update():
    load_data = PATH + f"user/{user_name}_DATA.txt"
    l_data = data_decode(load_data)
    l_data = l_data.split("|")
    print("Nombre de usuario:", l_data[0])
    print("Contraseña:", l_data[1])

    while True:
        print("¿Qué desea modificar?")
        m_answer = input().upper()

        if m_answer == "NOMBRE" or m_answer == "USUARIO":
            print("Introduzca el nuevo nombre de usuario:")
            l_data[0] = input()

            final_data = "|".join(l_data)

            new_user = data_encode(final_data)

            with open(PATH + f"user/{user_name}_DATA.txt", "wb") as nfile:
                nfile.write(new_user)

            print(f"Nombre de usuario de {user_name} actualizado.")
            time.sleep(1)
            login(user_name)
            break

        elif m_answer == "CONTRASEÑA":
            print("Introduzca la nueva contraseña:")
            l_data[1] = input()

            final_data = "|".join(l_data)

            new_password = data_encode(final_data)

            with open(PATH + f"user/{user_name}_DATA.txt", "wb") as nfile:
                nfile.write(new_password)

            print(f"Contraseña de {user_name} actualizada.")
            time.sleep(1)
            login(user_name)
            break

        elif m_answer == "ATRÁS" or m_answer == "ATRAS":
            break

        else:
            print(f"Lo siento, {m_answer} no es un comando válido.")
            continue


######################## ------------------------------ PROGRAM ------------------------------ ########################

# SARTING SYSTEM


print("BIENVENIDO A PASSWORD MANAGER v0.0.0")
print("Realizando las comprobaciones necesarias...")

time.sleep(2)

if "Password Manager" not in content:
    while True:
        print("El programa no se encuentra instalado, ¿desea hacerlo?")
        answer = input("Y/N: ").upper()

        if answer == "Y":
            install()
            break

        elif answer == "N":
            quit()

        else:
            print(f"Parece que {answer} no es un comando válido. Pruebe otra vez.")
            continue

else:
    print("Parece tiene todo lo necesario...")

user_name = input("Por favor, introduzca su nombre: ").upper()

time.sleep(0.5)
print(f"Bienvenido {user_name}")

check_list(user_name)


# MENU

while True:
    answer = input(f"MENÚ PRINCIPAL: {user_name}, qué desea hacer? ").upper()

    if answer == "AÑADIR":
        print("Ha seleccionado AÑADIR elemento a la base de datos")
        time.sleep(0.2)

        file = input("Nombre del proveedor a almacenar: ").upper()
        new_file(file)

    elif answer == "MODIFICAR":
        print("Ha seleccionado MODIFICAR datos de archivo")
        time.sleep(0.2)

        modify_file()

    elif answer == "VER":
        print("Ha seleccionado VER datos de un archivo")
        time.sleep(0.2)

        view_file()

    elif answer == "ELIMINAR":
        print("Ha seleccionado ELIMINAR datos")
        time.sleep(0.2)

        delete_file()

    elif answer == "AYUDA":
        print("Los comandos disponibles son:")
        time.sleep(0.2)

        print("AÑADIR: Añade nuevos datos a la base de datos")
        print("MODIFICAR: Modifica los datos disponibles")
        print("VER: Ver los datos almacenados")
        print("ELIMINAR: Eliminar un dato en específico")
        print("AYUDA: Muestra los comandos disponibles")
        print("OPCIONES: Abre el menú de opciones")
        print("SALIR: Sale del programa")

    elif answer == "OPCIONES":
        while True:
            answer = input(f"MENÚ OPCIONES: Qué desea hacer? ").upper()

            if answer == "USUARIO":
                print("Ha elegido actualizar los datos de usuario")
                time.sleep(0.2)

                profile_update()
                break

            elif answer == "DESINSTALAR":
                uninstall()

            elif answer == "LOGOUT":
                print(f"Hasta luego {user_name}")
                time.sleep(2)

                print("Bienvenido!")
                user_name = input("Por favor, introduzca su nombre: ").upper()

                time.sleep(0.5)

                check_list(user_name)
                break

            elif answer == "ATRÁS" or answer == "ATRAS":
                break

            elif answer == "AYUDA":
                print("Los comandos disponibles son:")
                time.sleep(0.2)

                print("USUARIO: Modifica los datos del usuario actual")
                print("DESINSTALAR: Elimina el programa y los datos almacenados")
                print("LOGOUT: Cambiar de usuario")
                print("ATRÁS: Volver al menú principal")
                print("AYUDA: Muestra los comandos disponibles")

            else:
                print(f"Lo siento, {answer} no es un comando válido. Prueba otra vez")
                continue

    elif answer == "SALIR":
        print(f"Hasta luego {user_name}")
        time.sleep(2)
        quit()

    else:
        print(f"Lo siento, {answer} no es un comando válido. Prueba otra vez")
        continue
