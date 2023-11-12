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
    with open(PATH + "Password Manager/files/user_list.txt", "r") as user_list:
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
    install()
else:
    print("Parece tiene todo lo necesario...")

user_name = input("Por favor, introduzca su nombre: ").upper()

time.sleep(0.5)
print(f"Bienvenido {user_name}")

check_list(user_name)
