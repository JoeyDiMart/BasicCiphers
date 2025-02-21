'''
Joseph DiMartino
CSC330: Vigenere Cipher program
'''
import os


# function to encrypt (but probably not needed)
def encrypt(inp, key, alphabet):
    cipher_text = ""
    length = len(alphabet)
    key_len = len(key)
    j = 0
    for i in inp:
        if i in alphabet:
            cipher_text += alphabet[(alphabet.index(i) + key[j]) % length]
            j = (j + 1) % key_len
        else:
            cipher_text += i
    return cipher_text


# very similar to caesar, just shift by alphabet - key
def decrypt(inp, key, alphabet):
    plain_text = ""
    length = len(alphabet)
    key_len = len(key)
    j = 0
    for i in inp:
        if i in alphabet:
            plain_text += alphabet[(alphabet.index(i) - key[j]) % length]
            j = (j + 1) % key_len
        elif i == "\n":
            plain_text += "\n"
            j = 0  # resets when a new line appears
        else:
            plain_text += i
    return plain_text


def main(output_file, cryptograph, input_type):
    selected_alphabet = input("Enter the Alphabet: ")
    key = input("Enter a key: ")
    key_shifts = []
    #start_alphabet = selected_alphabet[0]
    for i in key: # did upper since the shift from 'i to a' is the same as 'I to A'
        if i in selected_alphabet:
            #key_shifts.append(ord(i) - ord(start_alphabet))
            key_shifts.append(selected_alphabet.index(i))
    if input_type == "T":
        inp = input("Enter the text: ")

        result = encrypt(inp, key_shifts, selected_alphabet) if cryptograph == "E" else decrypt(inp, key_shifts, selected_alphabet)



    elif input_type == "R":
        file_path = os.path.expanduser("~/Desktop/CSC330Files/inputs/")
        file_name = os.path.join(file_path, input("Enter file name: "))

        try:
            with open(file_name, "r") as file:
                while True:
                    chunk = file.read(1024 * 1024)  # Read 1MB at a time, got this from chatGPT
                    if not chunk:
                        break

                    result = encrypt(chunk, key_shifts, selected_alphabet) if cryptograph == "E" else decrypt(chunk,
                                                                                                        key_shifts,
                                                                                                              selected_alphabet)
        except FileNotFoundError:
            print("Error: File not found.")

    with open(output_file, "w") as out_file:
        if isinstance(result, list):  # check if trying to write a list
            out_file.write("\n".join(result))
        else:
            out_file.write(result)