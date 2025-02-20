'''
Joseph DiMartino
CSC330: Caesar Cipher program
'''
import os
#long_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&*(),.?/'
#upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#all_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def encrypt(inp, shift, alphabet): # encryption (either by specified or all shifts)
    length = len(alphabet)
    if shift is None or shift == "000":  # Will try all possible shifts
        cipher_list = []
        for shift in range(1, length):
            cipher_text = ""
            for i in inp:
                if i in alphabet:
                    cipher_text += alphabet[(alphabet.index(i) + shift) % length]
                else:
                    cipher_text += i
            cipher_list.append(cipher_text)
        return cipher_list

    else:
        cipher_text = ""
        for i in inp:
            if i in alphabet:
                cipher_text += alphabet[(alphabet.index(i) + shift) % length]
            else:
                cipher_text += i
        return cipher_text


def decrypt(inp, shift, alphabet):
    length = len(alphabet)

    if shift == "000":  # Try all possible shifts
        plaintext_list = []
        for shift in range(1, length):
            plain_text = f"Shift: {shift}:"
            for i in inp:
                if i in alphabet:
                    plain_text += alphabet[(alphabet.index(i) - shift) % length]
                else:
                    plain_text += i
            plaintext_list.append(plain_text)
        return plaintext_list

    else:  # Decrypt with a specific shift
        plain_text = ""
        for i in inp:
            if i in alphabet:
                plain_text += alphabet[(alphabet.index(i) - shift) % length]
            else:
                plain_text += i
        return plain_text


# main method to run everything
def main(output_file, cryptograph, input_type):
    selected_alphabet = input("Enter the Alphabet: ")  # User chooses the alphabet size

    if input_type == "T":
        inp = input("Enter the text: ")
        shift = input("Enter how much the shift should be (# / 000): ")
        shift = int(shift) if shift != "000" else "000"  # set up to handle unspecified shifts (000)

        result = encrypt(inp, shift, selected_alphabet) if cryptograph == "E" else decrypt(inp, shift,
                                                                                           selected_alphabet)

        with open(output_file, "w") as out_file:
            if isinstance(result, list):  # check if trying to write a list
                out_file.write("\n".join(result))
            else:
                out_file.write(result)

    elif input_type == "R":
        file_path = os.path.expanduser("~/Desktop/CSC330Files/inputs/")
        file_name = os.path.join(file_path, input("Enter file name: "))

        try:
            with open(file_name, "r") as file, open(output_file, "w") as out_file:
                while True:
                    chunk = file.read(1024 * 1024)  # Read 1MB at a time
                    if not chunk:
                        break

                    shift = input("Enter how much the shift should be (# / 000): ") if cryptograph == "E" else "000"
                    shift = int(shift) if shift != "000" else "000"

                    processed_chunk = encrypt(chunk, shift, selected_alphabet) if cryptograph == "E" else decrypt(chunk,
                                                                                                                  shift,
                                                                                                                  selected_alphabet)

                    if isinstance(processed_chunk, list):  # check if trying to write a list
                        out_file.write("\n".join(processed_chunk))
                    else:
                        out_file.write(processed_chunk)

        except FileNotFoundError:
            print("Error: File not found.")

