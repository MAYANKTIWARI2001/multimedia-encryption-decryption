from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from cryptography.fernet import Fernet

from tkinter import messagebox
from PIL import Image 
from PIL import ImageTk


import os
import random
import base64
from stegano import lsb
#pip install stegano

# Themes: blue (default), dark-blue, green
def text_code2():
    global root5
    global screen
    if screen==1:
        screenname=app
    elif screen==2:
        screenname=root2
    elif screen==3:
        screenname=root3
    elif screen==4:
        screenname=root4
    screenname.destroy()
    screen=5
    def generate_key():
    # Generate a key
        key = Fernet.generate_key()
        key_entry.delete(0, tk.END)  # Clear the key entry field
        key_entry.insert(tk.END, key.decode())  # Insert the generated key in the key entry field


    def encrypt_file():
        try:
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
        except:
            messagebox.showinfo("Invalid Key","Please enter valid 32 bit key or generate it.")


    def decrypt_file():
        # Initialize the Fernet object with the key
        try:
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
        except:
            messagebox.showinfo("Invalid Key","Please enter valid key or file to proceed")


    # Create the main application window
    root5 = tk.Tk()
    root5.geometry("1200x700")
    root5.configure(bg="blue")
    root5.title("Video Encryption Tool")

    # Generate Key button
    generate_key_button = tk.Button(root5, text="Generate Key",font=('Times', 30), command=generate_key)
    generate_key_button.pack(pady=10)

    # Key entry
    key_entry = tk.Entry(root5,font=('Times', 50))
    key_entry.pack(pady=5)

    # Encrypt button
    
    encrypt_button = tk.Button(root5, text="Encrypt File", font=('Times', 30),command=encrypt_file)
    encrypt_button.pack(pady=10)

    # Decrypt button
    decrypt_button = tk.Button(root5, text="Decrypt File",font=('Times', 30), command=decrypt_file)
    decrypt_button.pack(pady=10)
    decrypt_button = tk.Button(root5, text="Back", font=('Times', 30),command=mainscreen)
    decrypt_button.pack(pady=30)

    # Start the Tkinter event loop
    root5.mainloop()


def text_code1():
    global root4
    global screen
    if screen==1:
        screenname=app
    elif screen==2:
        screenname=root2
    elif screen==3:
        screenname=root3
    
    elif screen==5:
        screenname=root5
    screenname.destroy()
    screen=4
    
    root4 = Tk()
    root4.geometry("1200x600")
    root4.config(bg="blue")
    root4.resizable(False,False)

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
        try:
            key = bytes(key_entry.get(), 'utf-8')
            input_file = input_entry.get()
            output_file = output_entry.get()
            encrypt_image(key, input_file, output_file)
        
        except:
            messagebox.showinfo("Invalid key 0r Value","please enter 16 bit key or select the file to proceed")

    def decrypt_button_clicked():
        try:
            key = bytes(key_entry.get(), 'utf-8')
            input_file = input_entry.get()
            output_file = output_entry.get()
            decrypt_image(key, input_file, output_file)
        except:
            messagebox.showinfo("Invalid key 0r Value","please enter correct key or correct file to proceed")

    # Labels
    key_label = Label(root4, text="Enter 16 Digit Key:", bg="blue",font=('Times', 20), pady=20)
    key_label.grid(row=10, column=3, sticky="n")

    input_label = Label(root4, text="Input Image:",bg="blue", font=('Times', 20), pady=20)
    input_label.grid(row=15, column=3, sticky="n")

    output_label = Label(root4, text="Output Image:",bg="blue", font=('Times', 20), pady=20)
    output_label.grid(row=20, column=3, sticky="n")


    # Key Entry
    key_entry = Entry(root4, width=30, font=('Times', 20), justify="center")
    key_entry.grid(row=10, column=5)

    # Input File Entry and Select Button
    input_entry = Entry(root4, width=30, font=('Times', 20), justify="center")
    input_entry.grid(row=15, column=5)
    Button(root4, text="Select", font=('Times', 15), command=select_input_file).grid(row=15, column=7)

    # Output File Entry and Select Button
    output_entry = Entry(root4, width=30, font=('Times', 20), justify="center")
    output_entry.grid(row=20, column=5)
    Button(root4, text="Select", font=('Times', 15), command=select_output_file).grid(row=20, column=7)

    # Encrypt and Decrypt Buttons
    Button(root4, text="Encrypt", font=('Times', 20), command=encrypt_button_clicked).grid(row=30, column=3)
    Button(root4, text="Decrypt", font=('Times', 20), command=decrypt_button_clicked).grid(row=30, column=4)
    Button(root4, text="Back", font=('Times', 20),command=mainscreen).grid(row=30 ,column=5)


    root4.mainloop()


def text_code():
    global root3
    global screen
    if screen==1:
        screenname=app
    elif screen==2:
        screenname=root2
   
    elif screen==4:
        screenname=root4
    elif screen==5:
        screenname=root5
    screenname.destroy()
    
    
    def encode(key, msg):
        enc = []
        for i in range(len(msg)):
            key_c = key[i % len(key)]
            enc_c = chr((ord(msg[i]) +
                         ord(key_c)) % 256)
            enc.append(enc_c)
            print("enc:", enc)
        return base64.urlsafe_b64encode("".join(enc).encode()).decode()


    def decode(key, enc):
        dec = []

        enc = base64.urlsafe_b64decode(enc).decode()
        for i in range(len(enc)):
            key_c = key[i % len(key)]
            dec_c = chr((256 + ord(enc[i]) -
                         ord(key_c)) % 256)

            dec.append(dec_c)
            print("dec:", dec)
        return "".join(dec)


    def Results():

        msg = Msg.get()
        k = key.get()
        m = mode.get()

        if (m == 'e'):
            Result.set(encode(k, msg))
        else:
            Result.set(decode(k, msg))



    def qExit():
        root3.destroy()


    def Reset():

        Msg.set("")
        key.set("")
        mode.set("")
        Result.set("")

    
    root3 = Tk()
    root3.geometry("1200x600")
    root3.resizable(False,False)
    

    root3.title("Text Encryption and Decryption")
   

    

    Tops = Frame(root3, width=1600, relief=SUNKEN)
    Tops.pack(side=TOP)

    f1 = Frame(root3, width=800, relief=SUNKEN)
    f1.pack(side=LEFT)

    lblInfo = Label(Tops, font=('Trebuchet', 30, 'bold'),text="Text Encryption ",fg="Black", bd=10, anchor='w')

    lblInfo.grid(row=0, column=0)
    global Msg
    global key
    global mode
    global Result

    Msg = StringVar()
    key = StringVar()
    mode = StringVar()
    Result = StringVar()

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
   
    screen=3

    root3.mainloop()


def button_function1():
    
    global root2
    global screen
    if screen==1:
        screenname=app
   
    elif screen==3:
        screenname=root3
    elif screen==4:
        screenname=root4
    elif screen==5:
        screenname=root5
    screenname.destroy()    
    screen=2
    
    root2 = Tk()
    root2.title("Steganography - Hide a secret text message in an image.")
    root2.geometry("800x700+483+284")
    root2.resizable(False,False)
    root2.configure(bg="#2f4155")

    def showimage():
        global filename
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                            title="Select Image File",
                                            filetype=(("png file","*.png"),
                                                      ("jpg file","*.jpg"),("all file","*.txt")))
        img = Image.open(filename)
        img = ImageTk.PhotoImage(img)
        my_label = Label(root1, image=img)
        my_label.pack()
        my_label.configure(image=img,bd=3,width=340, height=280)
        my_label.image=img
        my_label.place(x=15,y=80)
        #my_label.configure(image=img,width=250,height=250)
        #my_label.image=img
       
        
    def Hide():
        global secret
        message=text1.get(1.0,END)
        secret = lsb.hide(str(filename), message)
        messagebox.showinfo("information","data hidden")
        text1.delete(1.0, END)
        

    def show():
        clear_message = lsb.reveal(filename)
        text1.delete(1.0, END)
         
        text1.insert(END, clear_message)
        
        

    def save():
       
        
        file = filedialog.asksaveasfilename(
            filetypes=[('PDF file','.pdf'),('JPEG file',".jpeg"),("PNG file",".png")],
            defaultextension='.png')
        path2=file
        secret.save(path2)
        
        
            
                                          
        
       
        

          
        



    Label(root2,text="Cyber Security",bg='#2d4155',fg="white",font="arial 25 bold").place(x=100,y=20)

    f=Frame(root2,bd=3,bg="black",width=340,height=280,relief=GROOVE).place(x=10,y=80)

    #lbl=Label(f,bg="black")
    #lbl.place(x=10,y=0)

    frame2=Frame(root2,bd=3,bg="white",width=340,height=280,relief=GROOVE)
    frame2.place(x=360,y=80)

    text1=Text(frame2,font="Robote 20",bg="white",fg="black",relief=GROOVE)
    text1.place(x=0,y=0,width=320,height=295)



    frame3=Frame(root2,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
    frame3.place(x=10,y=370)

    Button(frame3,text="Open Image",width=10,height=2,font="arial 14 bold",command=showimage).place(x=20,y=30)
    Button(frame3,text="Save Image",width=10,height=2,font="arial 14 bold",command=save).place(x=180,y=30)
    


    frame4=Frame(root2,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
    frame4.place(x=360,y=370)

    Button(frame4,text="Hide data",width=10,height=2,font="arial 14 bold",command=Hide).place(x=20,y=30)
    Button(frame4,text="Show data",width=10,height=2,font="arial 14 bold",command=show).place(x=180,y=30)
    Button(frame4, text="Back", font=('Times', 20),command=mainscreen).grid(row=12, column=3, pady=20)
    










    root2.mainloop()

def mainscreen():
    global screen
    global app
    if screen !=1:
            
        if screen==2:
            screenname=root2
        elif screen==3:
            screenname=root3
        elif screen==4:
            screenname=root4
        elif screen==5:
            screenname=root5
        screenname.destroy()
    app = Tk()  # create CTk window like you do with the Tk window
    app.geometry("700x600")
    app.resizable(False,False)
    bgimg=Image.open("bg1.PNG")
    image=ImageTk.PhotoImage(bgimg)

    limg=Label(app,image=image)
    logo = PhotoImage(file = "1234.png")
    Label(app,image=logo,bg="#2f4155").place(x=10,y=0)
    l2=Label(app,text="EnigmaVault",bg='black',fg="white",font="arial 25 bold").place(x=130,y=20)
    l1=Label(app,text="Securing your secrets \n with cutting-edge \n encryption technology.",bg='#2d4155',fg="white",font="arial 20 bold").place(x=20,y=200)





    button = Button(master=app,width=7,height=1, text="Text " ,bg ='#588BAE',font= ('Helvetica 20 bold italic'), command=text_code)
    button.place(relx=0.2, rely=0.7, anchor=tk.E)

    button1 = Button(master=app,width=7,height=1, text="Image " ,bg ='#588BAE',font= ('Helvetica 20 bold italic'), command=text_code1)
    button1.place(relx=0.4, rely=0.7, anchor=tk.E)
    button2 = Button(master=app,width=7,height=1, text="Video " ,bg ='#588BAE',font= ('Helvetica 20 bold italic'), command=text_code2)
    button2.place(relx=0.6, rely=0.7, anchor=tk.E)
    button3 = Button(master=app,width=15,height=1, text="Steganography " ,bg ='#588BAE',font= ('Helvetica 18 bold italic'), command=button_function1)
    button3.place(relx=0.5, rely=0.8, anchor=tk.E)
    limg.place(x=0,y=0,relwidth=1,relheight=1)
    screen=1



    app.mainloop()
screen=1
mainscreen()

