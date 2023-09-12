from tkinter import Tk, Button, filedialog, Label, Entry
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from PIL import Image



def encrypt_image(key, input_file, output_file):
    # Open the input image
    input_image = Image.open(input_file)

    # Convert the image to RGB mode
    input_image = input_image.convert('RGB')
    # Get the size of the input image
    width, height = input_image.size

    # Create a new image for the encrypted output
    encrypted_image = Image.new('RGB', (width, height))

    # Initialize the AES cipher
    cipher = AES.new(key, AES.MODE_ECB)

    # Process the image block by block
    for y in range(0, height, AES.block_size):
        for x in range(0, width, AES.block_size):
            # Get the block of pixel data
            block = input_image.crop((x, y, x + AES.block_size, y + AES.block_size))

            # Convert the block to bytes
            block_bytes = block.tobytes()

            # Encrypt the block bytes
            encrypted_block = cipher.encrypt(block_bytes)

            # Create an image from the encrypted block
            encrypted_block_image = Image.frombytes('RGB', (AES.block_size, AES.block_size), encrypted_block)

            # Paste the encrypted block into the output image
            encrypted_image.paste(encrypted_block_image, (x, y))

    # Save the encrypted image
    encrypted_image.save(output_file)
    print("Encryption completed.")

def decrypt_image(key, input_file, output_file):
    # Open the input image
    input_image = Image.open(input_file)

    # Get the size of the input image
    width, height = input_image.size

    # Create a new image for the decrypted output
    decrypted_image = Image.new('RGB', (width, height))

    # Initialize the AES cipher
    cipher = AES.new(key, AES.MODE_ECB)

    # Process the image block by block
    for y in range(0, height, AES.block_size):
        for x in range(0, width, AES.block_size):
            # Get the block of encrypted pixel data
            block = input_image.crop((x, y, x + AES.block_size, y + AES.block_size))

            # Convert the block to bytes
            block_bytes = block.tobytes()

            # Decrypt the block bytes
            decrypted_block = cipher.decrypt(block_bytes)

            # Create an image from the decrypted block
            decrypted_block_image = Image.frombytes('RGB', (AES.block_size, AES.block_size), decrypted_block)

            # Paste the decrypted block into the output image
            decrypted_image.paste(decrypted_block_image, (x, y))

    # Save the decrypted image
    decrypted_image.save(output_file)
    print("Decryption completed.")

def select_input_file():
    file_path = filedialog.askopenfilename(title="Select Input Image")
    input_entry.delete(0, 'end')
    input_entry.insert('end', file_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(title="Save Output Image")
    output_entry.delete(0, 'end')
    output_entry.insert('end', file_path)

def encrypt_button_clicked():
    key = bytes(key_entry.get(), 'utf-8')
    input_file = input_entry.get()
    output_file = output_entry.get()
    encrypt_image(key, input_file, output_file)

def decrypt_button_clicked():
    key = bytes(key_entry.get(), 'utf-8')
    input_file = input_entry.get()
    output_file = output_entry.get()
    decrypt_image(key, input_file, output_file)
root4 = Tk()
root4.geometry("1200x700")
f1 = Frame(root4, width=800, relief=SUNKEN)
f1.pack(side=LEFT)
# Labels
lblMs = Label(f1, font=('arial', 16, 'bold'),
               text="Message", bd=16, anchor="w")

lblMs.grid(row=1, column=0)
txtMsg = Entry(f1, font=('arial', 16, 'bold'),
               textvariable=Msg, bd=10, insertwidth=4,
               bg="#588BAE", justify='right')


txtMsg.grid(row=1, column=1)

lblkey = Label(f1, font=('arial', 16, 'bold'),
               text="Key (Only Integer)", bd=16, anchor="w")

lblkey.grid(row=2, column=0)

txtkey = Entry(f1, font=('arial', 16, 'bold'),
               textvariable=key, bd=10, insertwidth=4,
               bg="#588BAE", justify='right')

txtkey.grid(row=2, column=1)

lblmode = Label(f1, font=('arial', 16, 'bold'),
                text="Mode(e for encrypt, d for decrypt)",
                bd=16, anchor="w")

lblmode.grid(row=3, column=0)

txtmode = Entry(f1, font=('arial', 16, 'bold'),
                textvariable=mode, bd=10, insertwidth=4,
                bg="#588BAE", justify='right')

txtmode.grid(row=3, column=1)

lblResult = Label(f1, font=('arial', 16, 'bold'),
                  text="The Result-", bd=16, anchor="w")

lblResult.grid(row=2, column=2)


txtResult = Entry(f1, font=('arial', 16, 'bold'),
                  textvariable=Result, bd=10, insertwidth=4,
                  bg="#588BAE", justify='right')

txtResult.grid(row=2, column=3)

#logo

      




btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black",
                  font=('arial', 16, 'bold'), width=10,
                  text="Show Message", bg="#588BAE",
                  command=Results).grid(row=10, column=1)

btnReset = Button(f1, padx=16, pady=8, bd=16,
                  fg="black", font=('arial', 16, 'bold'),
                  width=10, text="Reset", bg="#588BAE",
                  command=Reset).grid(row=10, column=2)


btnExit = Button(f1, padx=16, pady=8, bd=16,
                 fg="black", font=('arial', 16, 'bold'),
                 width=10, text="Back", bg="#588BAE",
                 command=mainscreen).grid(row=10, column=3)


root4.mainloop()
