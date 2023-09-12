
from tkinter import *
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

    if (m == 'e'):
        Result.set(encode(k, msg))
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
    

    root = Tk()
    root.geometry("1200x6000")

    root.title("Message Encryption and Decryption")

    Tops = Frame(root, width=1600, relief=SUNKEN)
    Tops.pack(side=TOP)

    f1 = Frame(root, width=800, relief=SUNKEN)
    f1.pack(side=LEFT)

    lblInfo = Label(Tops, font=('helvetica', 30, 'bold'),
                    text="SECRET MESSAGING ",
                    fg="Black", bd=10, anchor='w')

    lblInfo.grid(row=0, column=0)

    Msg = StringVar()
    key = StringVar()
    mode = StringVar()
    Result = StringVar()

    lblMs = Label(f1, font=('arial', 16, 'bold'),
                   text="MESSAGE", bd=16, anchor="w")

    lblMs.grid(row=1, column=0)
    txtMsg = Entry(f1, font=('arial', 16, 'bold'),
                   textvariable=Msg, bd=10, insertwidth=4,
                   bg="powder blue", justify='right')


    txtMsg.grid(row=1, column=1)

    lblkey = Label(f1, font=('arial', 16, 'bold'),
                   text="KEY (Only Integer)", bd=16, anchor="w")

    lblkey.grid(row=2, column=0)

    txtkey = Entry(f1, font=('arial', 16, 'bold'),
                   textvariable=key, bd=10, insertwidth=4,
                   bg="powder blue", justify='right')

    txtkey.grid(row=2, column=1)

    lblmode = Label(f1, font=('arial', 16, 'bold'),
                    text="MODE(e for encrypt, d for decrypt)",
                    bd=16, anchor="w")

    lblmode.grid(row=3, column=0)

    txtmode = Entry(f1, font=('arial', 16, 'bold'),
                    textvariable=mode, bd=10, insertwidth=4,
                    bg="powder blue", justify='right')

    txtmode.grid(row=3, column=1)

    lblResult = Label(f1, font=('arial', 16, 'bold'),
                      text="The Result-", bd=16, anchor="w")

    lblResult.grid(row=2, column=2)


    txtResult = Entry(f1, font=('arial', 16, 'bold'),
                      textvariable=Result, bd=10, insertwidth=4,
                      bg="powder blue", justify='right')

    txtResult.grid(row=2, column=3)

    #logo

          


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
        root.destroy()


    def Reset():

        Msg.set("")
        key.set("")
        mode.set("")
        Result.set("")

    btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black",
                      font=('arial', 16, 'bold'), width=10,
                      text="Show Message", bg="powder blue",
                      command=Results).grid(row=10, column=1)

    btnReset = Button(f1, padx=16, pady=8, bd=16,
                      fg="black", font=('arial', 16, 'bold'),
                      width=10, text="Reset", bg="green",
                      command=Reset).grid(row=10, column=2)


    btnExit = Button(f1, padx=16, pady=8, bd=16,
                     fg="black", font=('arial', 16, 'bold'),
                     width=10, text="Exit", bg="red",
                     command=qExit).grid(row=10, column=3)

    root.mainloop()

    
    
    
   

# Use CTkButton instead of tkinter Button

button = customtkinter.CTkButton(master=app,width=200,height=200, text="TEXT ENCRYPT/DECRYPT", command=text_code)
button.place(relx=0.6, rely=0.3, anchor=tkinter.W)
button1 = customtkinter.CTkButton(master=app,width=200,height=200, text="IMAGE ENCRYPT/DECRYPT", command=button_function1)
button1.place(relx=0.4, rely=0.3, anchor=tkinter.E)
button1 = customtkinter.CTkButton(master=app,width=200,height=200, text="Steganography ENCRYPT/DECRYPT", command=button_function1)
button1.place(relx=0.9, rely=0.7, anchor=tkinter.E)
button1 = customtkinter.CTkButton(master=app,width=200,height=200, text="VIDEO ENCRYPT/DECRYPT", command=button_function1)
button1.place(relx=0.4, rely=0.7, anchor=tkinter.E)




app.mainloop()
