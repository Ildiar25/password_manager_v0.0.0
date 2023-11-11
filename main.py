###################################################   PRESENTATION   ###################################################

# This is a litle project about Password Manager.
# This is the version 0.0.0 where we are going to add the first steps to become a great and useful program.

# On this section I'm going to explain the points where I'm working on. First of all, I'll start with some functions
# and defying some variables to create the body program.

########################################################################################################################

from cryptography.fernet import Fernet
import os
import time
from config import PATH
from config import BUILD

name = "jpast"  # Wait! This name must be the same name used by computer user


def generate_key():
    key = Fernet.generate_key()
    with open(PATH + "Password Manager/key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open(PATH + "Password Manager/key.key", "rb").read()


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


def new_profile(user_name):
    print("Vamos a crear un nuevo usuario: ")
    time.sleep(0.2)

    open(f"{PATH}Password Manager/user/{user_name}_DATA.txt", "wb").close()

    user = input("Nombre de Usuario: ")
    password_01 = input("Contraseña: ")

    while True:
        password_02 = input("Repita la contraseña: ")

        if password_02 == password_01:
            print("Contraseña confirmada")
            time.sleep(0.2)

            with open(f"{PATH}Password Manager/files/user_list.txt", "a") as data:
                data.write(user.upper() + "|")

            user_encrypt = data_encode(user + "|" + password_01)

            with open(f"{PATH}Password Manager/user/{user_name}_DATA.txt", "ab") as data:
                data.write(user_encrypt)

            login(user_name)

            break

        else:
            print("Lo siento, la contraseña no coincide.")
            continue


def login(user_name):
    print(f"Bienvenido {user_name}")
    load_user = f"{PATH}Password Manager/user/{user_name}_DATA.txt"
    u_data = data_decode(load_user)

    count = 2

    u_data = u_data.split("|")

    time.sleep(2)

    while True:
        user = input("Usuario: ")
        password = input("Contraseña: ")

        if user == u_data[0] and password == u_data[1]:
            print("Bienvenido de nuevo!")
            break

        elif count == 0:
            print("Demasiados intentos, se cerrará el programa.")
            time.sleep(2)
            quit()

        else:
            print("Usuario o contraseña no coinciden. Vuelva a intentarlo.")
            count -= 1
            continue


def install():
    print("Instalando...")

    main_folder = PATH
    os.mkdir(main_folder + "Password Manager")

    main_path = main_folder + "Password Manager/"

    time.sleep(2)
    print("Creando subcarpetas...")

    os.mkdir(main_path + "user")
    os.mkdir(main_path + "data")
    os.mkdir(main_path + "files")

    time.sleep(0.2)
    generate_key()

    open(main_path + "/files/user_list.txt", "w").close()

    with open(main_path + "build.txt", "w") as build_version:
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
            main_path = "C:/Users/jpast/Desktop/temp_folder/Password Manager/"

            print("Eliminando los archivos de sistema...")
            time.sleep(0.2)

            data_folder = main_path + "data/"
            files = os.listdir(data_folder)

            for file in files:
                print(file)
                os.remove(data_folder + file)

            time.sleep(0.2)
            files_folder = main_path + "files/"
            files = os.listdir(files_folder)

            for file in files:
                print(file)
                os.remove(files_folder + file)

            time.sleep(0.2)
            user_folder = main_path + "user/"
            files = os.listdir(user_folder)

            for file in files:
                print(file)
                os.remove(user_folder + file)

            time.sleep(0.2)

            print("Eliminando codificación...")

            print("key.key")
            os.remove(main_path + "key.key")
            time.sleep(0.2)

            print("build.txt")
            os.remove(main_path + "build.txt")
            time.sleep(0.2)

            print("Eliminando carpetas...")

            folders = os.listdir(main_path)

            for folder in folders:
                print("Carpeta " + folder + " eliminada")
                os.rmdir(main_path + folder)

            time.sleep(0.2)

            print("Limpiando sistema...")
            time.sleep(0.2)

            os.rmdir("C:/Users/jpast/Desktop/temp_folder/Password Manager")
            print("Finalización Exitosa")
            quit()

        elif answer == "N":
            break

        else:
            print(f"Lo siento, {answer} no es un comando válido.")
            continue


def check_list(user_name):
    with open(PATH + "Password Manager/files/user_list.txt", "r") as user_list:
        u_list = user_list.read()
        u_list = u_list.split("|")

    if user_name.upper() in u_list:
        print("¡Hola!")
        login(user_name)

    else:
        print(f"Bienvenido {user_name}, parece que es su primera vez.")
        new_profile(user_name)


def new_file(name_file):
    pass


def view_file(name_file):
    pass


def modify_file(name_file):
    pass


def delete_file(name_file):
    pass


def generate_password():
    pass


install()
user = input("Su nombre: ").upper()
check_list(user)

