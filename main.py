###################################################   PRESENTATION   ###################################################

# This is a litle project about Password Manager.
# This is the version 0.0.0 where we are going to add the first steps to become a great and useful program.

# On this section I'm going to explain the points where I'm working on. First of all, I'll start with some functions
# and defying some variables to create the body program.

########################################################################################################################

from cryptography.fernet import Fernet
import os
from config import PATH

def generate_key():
    key = Fernet.generate_key()
    with open(PATH+"key.key", "wb") as key_file:
        key_file.write(key)