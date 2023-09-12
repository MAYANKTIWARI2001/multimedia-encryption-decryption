from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from PIL import Image
import tkinter as tk
from tkinter import filedialog

class ImageEncryptorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Image Encryptor")

        self.key_label = tk.Label(master, text="Enter encryption key:")
        self.key_label.pack()

        self.key_entry = tk.Entry(master, show="*")
        self.key_entry.pack()

        self.input_button = tk.Button(master, text="Select input image", command=self.get_input_filename)
        self.input_button.pack()

        self.input_label = tk.Label(master, text="")
        self.input_label.pack()

        self.output_button = tk.Button(master, text="Select output file", command=self.get_output_filename)
        self.output_button.pack()

        self.output_label = tk.Label(master, text="")
        self.output_label.pack()

        self.encrypt_button = tk.Button(master, text="Encrypt Image", command=self.encrypt_image)
        self.encrypt_button.pack()

        self.decrypt_button = tk.Button(master, text="Decrypt Image", command=self.decrypt_image)
        self.decrypt_button.pack()

    def get_input_filename(self):
        input_filename = filedialog.askopenfilename()
        self.input_label.config(text="Input file: " + input_filename)
        self.input_filename = input_filename

    def get_output_filename(self):
        output_filename = filedialog.asksaveasfilename(defaultextension=".png")
        self.output_label.config(text="Output file: " + output_filename)
        self.output_filename = output_filename

    def encrypt_image(self):
        key = self.key_entry.get().encode('utf-8')
        try:
            encrypt_image(key, self.input_filename, self.output_filename)
            tk.messagebox.showinfo("Success", "Image encrypted successfully!")
        except Exception as e:
            tk.messagebox.showerror("Error", "Error encrypting image: " + str(e))

    def decrypt_image(self):
        key = self.key_entry.get().encode('utf-8')
        try:
            decrypt_image(key, self.input_filename, self.output_filename)
            tk.messagebox.showinfo("Success", "Image decrypted successfully!")
        except Exception as e:
            tk.messagebox.showerror("Error", "Error decrypting image: " + str(e))

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
    output_image.save(output_file)
    
