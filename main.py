###################################################   PRESENTATION   ###################################################

# This is a litle project about Password Manager.
# This is the version 0.0.0 where we are going to add the first steps to become a great and useful program.

# On this section I'm going to explain the points where I'm working on. First of all, I'll start with some functions
# and defying some variables to create the body program.

########################################################################################################################

import time
import cryptography
import os
from config import PATH
import stdiomask
import getpass


def new_profile():
    print("Vamosa  crear un nuevo usuario y una contraseña:")
    time.sleep(0.2)

    user = input("Nombre de Usuario: ")
    print("Usuario añadido")
    password_01 = stdiomask.getpass("Contraseña: ", "*")

    print(user, password_01)


def new_profile_02():
    print("Vamosa  crear un nuevo usuario y una contraseña:")
    time.sleep(0.2)

    user = input("Nombre de Usuario: ")
    print("Usuario añadido")
    password_01 = getpass.getpass("Contraseña: ")

    print(user, password_01)


new_profile_02()
