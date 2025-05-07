"""Elaboracion de contraseñas aleatorias con Python"""

import random
import string

def password_generator():
    password = ""
    for i in range(15):
        password += random.choice(string.ascii_letters + string.digits)
    return password

print(password_generator())
