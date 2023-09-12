import tkinter as tk
from tkinter import filedialog
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

def browse_input_file():
    input_file_path = filedialog.askopenfilename(defaultextension='.png')
    input_file_path_entry.delete(0, tk.END)
    input_file_path_entry.insert(0, input_file_path)

def browse_output_file():
    output_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    output_file_path_entry.delete(0, tk.END)
    output_file_path_entry.insert(0, output_file_path)

def encrypt_input_file():
    key = bytes(key_entry.get(), 'utf-8')
    input_file_path = input_file_path_entry.get()
    output_file_path = output_file_path_entry.get()
    encrypt_image(key, input_file_path, output_file_path)

def decrypt_input_file():
    key = bytes(key_entry.get(), 'utf-8')
    input_file_path = input_file_path_entry.get()
    output_file_path = output_file_path_entry.get()
    decrypt_image(key, input_file_path, output_file_path)

root = tk.Tk()
root.title("Image Encryption and Decryption")

key_label = tk.Label(root, text="Enter Key:")
key_label.pack()
key_entry = tk.Entry(root, show="*")
key_entry.pack()

input_file_path_label = tk.Label(root, text="Input Image:")
input_file_path_label.pack()
input_file_path_entry = tk.Entry(root)
input_file_path_entry.pack(side=tk.LEFT)
input_file_path_button = tk.Button(root, text="Browse", command=browse_input_file)
input_file_path_button.pack(side=tk.LEFT)

output_file_path_label = tk.Label(root, text="Output Image:")
output_file_path_label.pack()
output_file_path_entry = tk.Entry(root)
output_file_path_entry.pack(side=tk.LEFT)
output_file_path_button = tk.Button(root, text="Browse", command=browse_output_file)
output_file_path_button.pack(side=tk.LEFT)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_input_file)
encrypt_button.pack(side=tk.LEFT)
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_input_file)
decrypt_button.pack(side=tk.LEFT)

root.mainloop()
