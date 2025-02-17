import random
from cryptography.fernet import Fernet
import os

def main_prog():
    print("Password Generator\n")
    print("Welcome to the password generator!")
    print("Do you want to access to your passwords? (y/n)")
    choice = input()
    if choice == "y":
        print("Enter the filename to access the passwords")
        filename = input()
        if (not os.path.exists(filename)):
            print("File does not exist.")
            return
        with open(filename, "rb") as file:
            while True:
                key = file.readline().strip()
                if not key:
                    break
                encrypted_password = file.readline().strip()
                cipher_suite = Fernet(key)
                password = cipher_suite.decrypt(encrypted_password).decode()
                print("Password: " + password)

    while (True):
        print("Do you want to generate a password? (y/n)")
        choice = input()
        if choice == "y":
            print("How many characters do you want?")
            length = int(input())
            print("Do you want specials characters? (y/n)")
            specials = input()
            password = generate_password(length, specials == "y")
            print("Do you want to save this password? (y/n)")
            choice = input()
            if choice == "y":
                save_password(password)
        print("Do you want to generate another password? (y/n)")
        choice = input()
        if choice == "n":
            break
    print("Goodbye!")

def generate_password(length, specials):
    password = ""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    special_chars = "!@#$%^&*()_+"
    if specials:
        chars += special_chars
    for i in range(length):
        password += random.choice(chars)
    print("Generated password: " + password)
    return password

def save_password(password):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    encrypted_password = cipher_suite.encrypt(password.encode())
    print("Enter the filename to save the password")
    filename = input()
    name = filename
    print("What name do you want to give to this password?")
    name = input()
    with open(filename, "ab") as file:
        file.write(key + b"\n" + encrypted_password + b"\n" + name.encode() + b"\n")
    if os.path.exists(filename):
        print("Do you want to save your password in " + filename + "? (y/n)")
        choice = input()
        if (choice == "y"):
            with open(filename, "ab") as file:
                file.write(key + b"\n" + encrypted_password + b"\n" + name.encode() + b"\n")
            print("Password saved to " + filename)
            return
    else:
        print("File does not exist. Do you want to create it? (y/n)")
        choice = input()
        if choice == "n":
            return
    print("Password saved to " + filename)

if __name__ == "__main__":
    main_prog()