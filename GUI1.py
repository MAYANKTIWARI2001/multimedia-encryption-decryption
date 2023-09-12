import tkinter as tk
import customtkinter
from tkinter import filedialog
from PIL import Image
from tkinter import messagebox
import base64



customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("700x600")
app.minsize(700,600)
app.maxsize(700,600)
mydir=''





def Results():

    msg = Msg.get()
    k = key.get()
    m = mode.get()
    print(msg)
    

    if (m == 'e'):
        screen.destroy()
    else:
        Result.set(decode(k, msg))
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

def upload_file():
    file = filedialog.askopenfilename(title="Select Image File")
    
    #print(file.read())
     
    print(file)
    
    img = customtkinter.CTkImage(dark_image=Image.open("file"),size=(30, 30))
    l3.configure(image=img)
    l3.image=img
def encrypt_text():
    pass
def button_function1():
    app.destroy()
    customtkinter.set_default_color_theme("blue")
    app1 = customtkinter.CTk()
    app1.geometry("700x600+600+200")
    app1.minsize(700,600)
    app1.maxsize(700,600)
    my_font1=('times', 18, 'bold')
    l1 = customtkinter.CTkLabel(master=app1,text='mydir',width=30,font=my_font1)  
    l1.grid(row=1,column=1)
    b1 = customtkinter.CTkButton(master=app1, width=20,text="Upload File",command=upload_file)
    b1.grid(row=2,column=1) 
    app1.mainloop()
    l3=customtkinter.CTkLabel(app1)
    l3.pack()
def text_code():
    screen=customtkinter.CTk()
    screen.geometry("700x600")
    screen.minsize(700,600)
    screen.maxsize(700,600)
    global Msg
    global key
    global mode
    global Result
    Msg = tk.StringVar()
    print(Msg)
    key = tk.StringVar()
    mode = tk.StringVar()
    Result = tk.StringVar()
    l2=customtkinter.CTkLabel(master=screen,text='Enter Text for Encryption and Decryption').place(x=30,y=30)
    text1=customtkinter.CTkEntry(master=screen,textvariable=Msg,placeholder_text="Enter Your Text Here",width=600,height=250,border_width=2,corner_radius=10)
    text1.place(relx=0.5,rely=0.31 ,anchor=tk.CENTER)
    
    L22=customtkinter.CTkLabel(master=screen,text='Enter Sequrity Key for Encryption and Decryption').place(x=30,y=330)
    text11=customtkinter.CTkEntry(master=screen,textvariable=key,placeholder_text="ONLY INTEGER VALUE",width=600,height=50,border_width=2,corner_radius=10)
    text11.place(relx=0.5,rely=0.65 ,anchor=tk.CENTER)

    l33=customtkinter.CTkLabel(master=screen,text='Enter e for encryption and d for decryption').place(x=30,y=420)
    text11=customtkinter.CTkEntry(master=screen,textvariable=mode,placeholder_text="",width=600,height=50,border_width=2,corner_radius=10)
    text11.place(relx=0.5,rely=0.8 ,anchor=tk.CENTER)
    
    button = customtkinter.CTkButton(master=screen,width=100,height=50, text="SHOW MESSAGE", command=Results)
    button.place(relx=0.1, rely=0.85)
    text11=customtkinter.CTkEntry(master=screen,textvariable=Result,placeholder_text="",width=400,height=50,border_width=2,corner_radius=10)
    text11.place(relx=0.6,rely=0.9 ,anchor=tk.CENTER)


    
    screen.mainloop()
    
    
   

# Use CTkButton instead of tkinter Button

button = customtkinter.CTkButton(master=app,width=200,height=200, text="TEXT ENCRYPT/DECRYPT", command=text_code)
button.place(relx=0.6, rely=0.3, anchor=tk.W)
button1 = customtkinter.CTkButton(master=app,width=200,height=200, text="IMAGE ENCRYPT/DECRYPT", command=button_function1)
button1.place(relx=0.4, rely=0.3, anchor=tk.E)
button1 = customtkinter.CTkButton(master=app,width=200,height=200, text="Steganography ENCRYPT/DECRYPT", command=button_function1)
button1.place(relx=0.9, rely=0.7, anchor=tk.E)
button1 = customtkinter.CTkButton(master=app,width=200,height=200, text="VIDEO ENCRYPT/DECRYPT", command=button_function1)
button1.place(relx=0.4, rely=0.7, anchor=tk.E)




app.mainloop()
