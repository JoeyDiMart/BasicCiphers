'''
Joseph DiMartino
CSC330: XOR Cipher
'''
import os


def XOR(inp, key):
    key_length = len(key)

    # https: // stackoverflow.com / questions / 4019837 / what - do - we - mean - by - byte - array
    cipher_array = bytearray()  # got a byte array idea from chatGPT, this is apparently mroe efficient

    for index, byte in enumerate(inp):
        cipher_array.append(byte ^ key[index % key_length])

    return bytes(cipher_array)


def main(output_file, input_type):
    file_path = os.path.expanduser("~/Desktop/CSC330Files/inputs/")
    type_key = input("Type key or key read from file: (T/R): ").upper()

    if type_key == "T":
        key = input("Enter the key").encode()   # encode to make sure string is in bytes
    else:
        key_file = os.path.join(file_path, input("Enter file name for the key: "))
        with open(key_file, "rb") as kf:
            key = kf.read()


    if input_type == "T":
        inp = input("Enter the text:").encode()
        result = XOR(inp, key)

    else:
        file_name = os.path.join(file_path, input("Enter file name: "))

        try:
            with open(file_name, "rb") as file:
                result = b""  # create a byte string
                while True:
                    chunk = file.read(1024 * 1024)  # Read 1MB at a time, got this from chatGPT
                    if not chunk:
                        break
                    result += XOR(chunk, key)

        except FileNotFoundError:
            print("Error: File not found.")
            return

    with open(output_file, "wb") as out_file:
        out_file.write(result)
# https://filehelper.com/view tested if it worked here