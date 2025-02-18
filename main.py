'''
Name: joseph DiMartino
Program: main.py
'''
import os
import binaryCipher
import caesarCipher


output_path = os.path.expanduser("~/Desktop/CSC330Files/outputs/")
output_file = os.path.join(output_path, input("Enter output file name: "))
cryptograph = input("Encrypt or Decrypt (E / D): ").upper()
num_bits = int(input("7 / 8 bit ascii or unknown (7 / 8): "))
input_type = input("Type input or Read from file (T / R): ").upper()
binaryCipher.main(output_file, cryptograph, num_bits, input_type)


