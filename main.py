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

# SISTEM FUNCTIONS ----


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
        answer = input("Y/N: ").upper()

        if answer == "Y":

            print("Eliminando los archivos de sistema...")
            time.sleep(0.2)

            data_folder = PATH + "data/"
            files = os.listdir(data_folder)

            for file in files:
                print(file)
                os.remove(data_folder + file)

            time.sleep(0.2)
            files_folder = PATH + "files/"
            files = os.listdir(files_folder)

            for file in files:
                print(file)
                os.remove(files_folder + file)

            time.sleep(0.2)
            user_folder = PATH + "user/"
            files = os.listdir(user_folder)

            for file in files:
                print(file)
                os.remove(user_folder + file)

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
            quit()

        elif answer == "N":
            break

        else:
            print(f"Lo siento, {answer} no es un comando válido.")
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


def data_decode(file):
    key = load_key()
    f = Fernet(key)

    with open(file, "rb") as encrypt_data:
        data = encrypt_data.read()

    decrypted_data = f.decrypt(data)

    return decrypted_data.decode()


# START FUNCTIONS ----


def check_list(name):
    with open(PATH + "files/user_list.txt", "r") as user_list:
        u_list = user_list.read()
        u_list = u_list.split("|")

    if name in u_list:
        pass  # call login function

    else:
        print(f"Parece que es su primera vez. No hay problema")
        # call new_profile function

######################## ------------------------------ PROGRAM ------------------------------ ########################


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
