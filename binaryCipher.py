'''
Joseph DiMartino
CSC330: Caesar Cipher program
2.11.2025
'''
import os
def encrypt(num_bits, inp):
    pass
def decrypt(num_bits, inp):
    pass

def main():
    cryptograph = input("Encrypt or Decrypt (E / D): ").upper()
    num_bits = input("7 / 8 bit ascii or unknown (7 / 8 / U): ").upper()
    input_type = input("Type input or Read from file (T / R): ").upper()


    if input_type == "T":
        inp = input("Enter the text: ")
    elif input_type == "R":
        file_path = os.path.expanduser("~/Desktop/CSC330Files/inputs/")
        file_name = os.path.join(file_path, input("Enter file name: "))
        try:
            with open(file_name, "r") as file:
                inp = file.read()
                print("File content:\n", inp)
        except FileNotFoundError:
            print("Error: File not found.")

    if cryptograph == "E":
        encrypt(num_bits, inp)
    else:
        decrypt(num_bits, inp)


if __name__ == "__main__":
    main()