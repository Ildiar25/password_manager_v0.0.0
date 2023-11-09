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


def generate_key():
    key = Fernet.generate_key()
    with open(PATH+"key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open(PATH+"key.key", "rb").read()


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

    open(f"{PATH}{user_name}_DATA.txt", "wb").close()

    user = input("Nombre de Usuario: ")
    password_01 = input("Contraseña: ")

    while True:
        password_02 = input("Repita la contraseña: ")

        if password_02 == password_01:
            print("Contraseña confirmada")
            time.sleep(0.2)

            user_encrypt = data_encode(user + "|" + password_01)

            with open(f"{PATH}{user_name}_DATA.txt", "ab") as data:
                data.write(user_encrypt)

            break
        else:
            print("Lo siento, la contraseña no coincide.")
            continue


def install():
    os.mkdir(f"{PATH}data")
    os.mkdir(f"{PATH}users")
    os.mkdir(f"{PATH}sites")
    with open(f"{PATH}build.txt", "w") as version:
        version.write("Password Manager v0.0.0")
