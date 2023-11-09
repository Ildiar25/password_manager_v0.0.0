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

# START FUNCTIONS ----


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

######################## ------------------------------ PROGRAM ------------------------------ ########################


if "Password Manager" not in content:
    install()
else:
    pass  # call to check function
