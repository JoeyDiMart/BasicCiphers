'''
Joseph DiMartino
CSC330: Caesar Cipher program
'''
import os
long_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&*(),.?/'
upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
all_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def encrypt(num_bits, inp, shift, alphabet):
    cipher_text = ''
    if num_bits == 7:
        max_val = 127
    else:
        max_val = 255
    for char in inp:
        if char in alphabet:
            ord_value = ord(char)
            shifted_value = (ord_value + shift) % (max_val + 1)
            cipher_text += chr(shifted_value)
        else:
            cipher_text += char

    return cipher_text


def decrypt(num_bits, inp):
    pass


def main(output_file, cryptograph, num_bits, input_type):

    if input_type == "T":
        shift = int(input("Enter how much the shift should be: "))
        alphabet_type = input("All printable chars, upper only, or Aa-Zz (A, U, O): ")
        alph = {
            "A": long_alphabet,
            "U": upper_alphabet,
            "O": all_alphabet
        }
        selected_alphabet = alph[alphabet_type]

        result = encrypt(num_bits, inp, shift, selected_alphabet) if cryptograph == "E" else decrypt(num_bits, inp)
        with open(output_file, "w") as out_file:
            out_file.write(result)

    elif input_type == "R":
        file_path = os.path.expanduser("~/Desktop/CSC330Files/inputs/")
        file_name = os.path.join(file_path, input("Enter file name: "))
        try:
            with open(file_name, "r") as file, open(output_file, "w") as out_file:
                while True:
                    chunk = file.read(1024 * 1024) # read 1MB at a time just in case of large files
                    if not chunk:
                        break
                    processed_chunk = encrypt(num_bits, chunk) if cryptograph == "E" else decrypt(num_bits, chunk)
                    out_file.write(processed_chunk)
        except FileNotFoundError:
            print("Error: File not found.")
