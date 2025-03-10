'''
Name: joseph DiMartino
Program: main.py
'''
import os
import binaryCipher
import caesarCipher
import vigenereCipher
import XORCipher


output_path = os.path.expanduser("~/Desktop/CSC330Files/outputs/")

while True:
    output_file = os.path.join(output_path, input("Enter output file name (Q): "))
    cipher = input("enter which ciper (binary, caesar, vigenere, XOR, Q): ").lower()

    input_type = input("Type input or Read from file (T / R): ").upper()

    cipher_methods = {
        "binary": lambda: binaryCipher.main(output_file, cryptograph, input_type),
        "caesar": lambda: caesarCipher.main(output_file, cryptograph, input_type),
        "vigenere": lambda: vigenereCipher.main(output_file, cryptograph, input_type),
        "xor": lambda: XORCipher.main(output_file, input_type)
    }

    if cipher != "xor":
        cryptograph = input("Encrypt or Decrypt (E / D): ").upper()

    if cipher in cipher_methods:
        cipher_methods[cipher]()
    else:
        print("Invalid cipher choice.")
    print("\n")
    quitting = input("Quit? (Q)").upper()
    if quitting == "Q":
        break
