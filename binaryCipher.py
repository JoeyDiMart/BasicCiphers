'''
Joseph DiMartino
CSC330: Binary Cipher program
2.11.2025
'''
import os


def encrypt(num_bits, inp):
    ascii = [ord(char) for char in inp]
    bin_string = ''.join([bin(b)[2:].zfill(num_bits) for b in ascii])
    return bin_string


def decrypt(num_bits, inp):
    plain_text = []
    for i in range(0, len(inp), num_bits):
        segment = inp[i:i+num_bits]
        plain_text.append(chr(int(segment, 2)))
    return ''.join(plain_text)


def main(output_file, cryptograph, num_bits, input_type):
    if input_type == "T":
        inp = input("Enter the text: ")
        result = encrypt(num_bits, inp) if cryptograph == "E" else decrypt(num_bits, inp)
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
