# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iAM-JU_EIIIIcZQSgtUwa30niCj6YQSV
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from PIL import Image

def encrypt_image(key, input_file, output_file):
    # Open the input image
    input_image = Image.open(input_file)
    
    # Convert the image to RGB mode
    input_image = input_image.convert('RGB')
    
    # Convert the image to bytes
    input_bytes = input_image.tobytes()
    
    # Initialize the AES cipher
    cipher = AES.new(key, AES.MODE_ECB)
    
    # Encrypt the image bytes
    encrypted_bytes = cipher.encrypt(pad(input_bytes, AES.block_size))
    
    # Create a new image from the encrypted bytes
    output_image = Image.frombytes('RGB', input_image.size, encrypted_bytes)
    
    # Save the output image
    output_image.save(output_file)

def decrypt_image(key, input_file, output_file):
    # Open the input image
    input_image = Image.open(input_file)
    
    # Convert the image to bytes
    input_bytes = input_image.tobytes()
    
    # Initialize the AES cipher
    cipher = AES.new(key, AES.MODE_ECB)
    
    # Decrypt the image bytes
    decrypted_bytes = unpad(cipher.decrypt(input_bytes), AES.block_size)
    
    # Create a new image from the decrypted bytes
    output_image = Image.frombytes('RGB', input_image.size, decrypted_bytes)
    
    # Save the output image
    output_image.save(output_file)

# Example usage
key = b'juhfgydhstgai3ij'
input_file = '/content/red team recon.png'
encrypted_file = 'encrypted_image.png'



encrypt_image(key, input_file, encrypted_file)

