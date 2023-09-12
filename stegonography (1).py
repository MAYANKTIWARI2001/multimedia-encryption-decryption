from tkinter import*
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox



from PIL import Image 
from PIL import ImageTk 
import os
from stegano import lsb #pip install stegano


root = Tk()
root.title("steganograohy - hide a secret text message in an image ")
root.geometry("800x700+483+284")
root.resizable(False,False)
root.configure(bg="#2f4155")

def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title="Select Image File",
                                        filetype=(("png file","*.png"),
                                                  ("jpg file","*.jpg"),("all file","*.txt")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    my_label = Label(root, image=img)
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
    
    
        
                                      
    
   
    
#icon
p1 = PhotoImage(file = 'flower.png')
root.iconphoto(False, p1)

#logo
logo = PhotoImage(file = "logo1.png")
Label(root,image=logo,bg="#2f4155").place(x=10,y=0)
      
    



Label(root,text="Cyber Security",bg='#2d4155',fg="white",font="arial 25 bold").place(x=100,y=20)

f=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE).place(x=10,y=80)

#lbl=Label(f,bg="black")
#lbl.place(x=10,y=0)

frame2=Frame(root,bd=3,bg="white",width=340,height=280,relief=GROOVE)
frame2.place(x=360,y=80)

text1=Text(frame2,font="Robote 20",bg="white",fg="black",relief=GROOVE)
text1.place(x=0,y=0,width=320,height=295)



frame3=Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
frame3.place(x=10,y=370)

Button(frame3,text="open image",width=10,height=2,font="arial 14 bold",command=showimage).place(x=20,y=30)
Button(frame3,text="save image",width=10,height=2,font="arial 14 bold",command=save).place(x=180,y=30)
Label(frame3,text="picture,Image,photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)


frame4=Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
frame4.place(x=360,y=370)

Button(frame4,text="Hide data",width=10,height=2,font="arial 14 bold",command=Hide).place(x=20,y=30)
Button(frame4,text="Show data",width=10,height=2,font="arial 14 bold",command=show).place(x=180,y=30)
Label(frame4,text="picture,Image,photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)










root.mainloop()


