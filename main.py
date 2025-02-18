'''
Name: joseph DiMartino
Program: main.py
'''
import os
import binaryCipher
import caesarCipher


output_path = os.path.expanduser("~/Desktop/CSC330Files/outputs/")

while True:
    output_file = os.path.join(output_path, input("Enter output file name: "))
    cipher = input("enter which ciper (binary, caesar, Q): ").lower()

    if cipher == 'q':
        break

    cryptograph = input("Encrypt or Decrypt (E / D): ").upper()

    if cipher == "binary":
        num_bits = int(input("7 / 8 bit ascii or unknown (7 / 8): "))

    input_type = input("Type input or Read from file (T / R): ").upper()

    cipher_methods = {
        "binary": lambda: binaryCipher.main(output_file, cryptograph, num_bits, input_type),
        "caesar": lambda: caesarCipher.main(output_file, cryptograph, input_type)
    }

    if cipher in cipher_methods:
        cipher_methods[cipher]()
    else:
        print("Invalid cipher choice.")
    print("\n")
