'''
Name: joseph DiMartino
Program: main.py
'''
import os
import binaryCipher
import caesarCipher


output_path = os.path.expanduser("~/Desktop/CSC330Files/outputs/")
output_file = os.path.join(output_path, input("Enter output file name: "))

while True:
    cipher = input("enter which ciper (binary, caesar, Q): ").lower()

    if cipher == 'q':
        break

    cryptograph = input("Encrypt or Decrypt (E / D): ").upper()
    num_bits = int(input("7 / 8 bit ascii or unknown (7 / 8): "))
    input_type = input("Type input or Read from file (T / R): ").upper()

    cipher_methods = {
        "binary": binaryCipher.main(output_file, cryptograph, num_bits, input_type),
        "caesar": caesarCipher.main(output_file, cryptograph, num_bits, input_type)
    }

    print("\n")
