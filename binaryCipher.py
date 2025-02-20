'''
Joseph DiMartino
CSC330: Binary Cipher program
2.11.2025
'''
import os


def encrypt(inp):
    bin_list = []
    ascii = [ord(char) for char in inp]
    bin_list.append(f"7 bit ascii: {''.join([bin(b)[2:].zfill(7) for b in ascii])}")
    bin_list.append(f"8 bit ascii: {''.join([bin(b)[2:].zfill(8) for b in ascii])}")
    return bin_list


def decrypt(inp):
    plain_list = []
    plain_text = ''
    for i in range(0, len(inp), 7):
        segment = inp[i:i + 7]
        if len(segment) == 7:
            try:
                plain_text += chr(int(segment, 2))
            except ValueError:
                print("oops")
                break
    plain_list.append(f"7 bit ascii: {plain_text}\n\n")

    plain_text = ''
    for i in range(0, len(inp), 8):
        segment = inp[i:i + 8]
        print(segment)
        if segment == '00001010':
            plain_text += '\n'
        elif len(segment) == 8:
            try:
                plain_text += chr(int(segment, 2))
            except ValueError:
                print("oops")
                break
    plain_list.append(f"8 bit ascii: {plain_text}")

    return plain_list


def main(output_file, cryptograph, input_type):
    if input_type == "T":
        inp = input("Enter the text: ")
        result = encrypt(inp) if cryptograph == "E" else decrypt(inp)
        with open(output_file, "w") as out_file:
            out_file.write("\n".join(result))

    elif input_type == "R":
        file_path = os.path.expanduser("~/Desktop/CSC330Files/inputs/")
        file_name = os.path.join(file_path, input("Enter file name: "))
        try:
            with open(file_name, "r") as file, open(output_file, "w") as out_file:
                while True:
                    chunk = file.read(1024 * 1024)  # read 1MB at a time just in case of large files
                    if not chunk:
                        break
                    chunk = chunk.replace('\n', '00001010')
                    processed_chunk = encrypt(chunk) if cryptograph == "E" else decrypt(chunk)
                    out_file.write('\n'.join(processed_chunk))
        except FileNotFoundError:
            print("Error: File not found.")
