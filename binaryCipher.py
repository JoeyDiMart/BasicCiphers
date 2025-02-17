'''
Joseph DiMartino
CSC330: Caesar Cipher program
2.11.2025
'''
def encrypt():
    numBits = int(input("7 or 8 bit ASCII?"))
    if numBits == 7 or numBits == 8:
        plainText = input("The plaintext: ")
        ascii = [ord(char) for char in plainText]
        binString = ''
        for char in ascii:
            if (char < 0 or char > 127) and numBits == 7: # ignore unknown characters
                
            binary = bin(char)[2:]
            binary = binary.zfill(numBits)
            binString += binary
            binString += " "

        print(binString)


    else:
        return "Re-run: invalid bits"

def decrypt():
    pass

def main():
    inp = input("Encrypt or Decrypt (E / D): ")
    r = True
    while r:
        if  inp.upper() == "E":
            encrypt()
        elif inp.upper() == "D":
            decrypt()
        r = False







if __name__ == "__main__":
    main()