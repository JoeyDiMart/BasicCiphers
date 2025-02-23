import base64
import os

# Prompt user for the input file (Base64-encoded)
input_file = input("Enter the name of the file to decode: ")

# Prompt user for the output file (.bin)
output_file = input("Enter the name of the output .bin file: ")

# Read the encoded content from the file
with open(input_file, "r") as f:
    encoded_data = f.read().strip()  # Read and remove extra spaces/newlines

# Decode the Base64 content into raw bytes
decoded_data = base64.b64decode(encoded_data)

# Write the raw bytes to the output file
with open(output_file, "wb") as f:
    f.write(decoded_data)

print(f"Decoded data saved as '{output_file}'.")

