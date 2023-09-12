import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet


def generate_key():
    # Generate a key
    key = Fernet.generate_key()
    key_entry.delete(0, tk.END)  # Clear the key entry field
    key_entry.insert(tk.END, key.decode())  # Insert the generated key in the key entry field


def encrypt_file():
    # Initialize the Fernet object with the key
    fernet = Fernet(key_entry.get())

    # Open the video file
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'rb') as f:
            data = f.read()

        # Encrypt the data
        encrypted_data = fernet.encrypt(data)

        # Write the encrypted data to a new file
        save_path = filedialog.asksaveasfilename(defaultextension='.mp4')
        if save_path:
            with open(save_path, 'wb') as f:
                f.write(encrypted_data)
            print("Successfully encrypted")


def decrypt_file():
    # Initialize the Fernet object with the key
    fernet = Fernet(key_entry.get())

    # Open the encrypted video file
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()

        # Decrypt the data
        decrypted_data = fernet.decrypt(encrypted_data)

        # Write the decrypted data to a new file
        save_path = filedialog.asksaveasfilename(defaultextension='.mp4')
        if save_path:
            with open(save_path, 'wb') as f:
                f.write(decrypted_data)
            print("Successfully decrypted")


# Create the main application window
window = tk.Tk()
window.title("Video Encryption Tool")

# Generate Key button
generate_key_button = tk.Button(window, text="Generate Key", command=generate_key)
generate_key_button.pack(pady=10)

# Key entry
key_entry = tk.Entry(window)
key_entry.pack(pady=5)

# Encrypt button
encrypt_button = tk.Button(window, text="Encrypt File", command=encrypt_file)
encrypt_button.pack(pady=10)

# Decrypt button
decrypt_button = tk.Button(window, text="Decrypt File", command=decrypt_file)
decrypt_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
