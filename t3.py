import tkinter as tk
import customtkinter as ctk

def submit(dialog, entry, var):
    var.set(entry.get())
    dialog.destroy()

def cancel(dialog, var):
    var.set(None)
    dialog.destroy()

def show_input_dialog(parent, title, message):
    result = tk.StringVar()

    dialog = tk.Toplevel(parent)
    dialog.geometry("300x150")
    dialog.title(title)

    label = tk.Label(dialog, text=message)
    label.pack(pady=10)

    entry = ctk.CTkEntry(dialog)
    entry.pack(pady=10, padx=10)

    submit_button = ctk.CTkButton(dialog, text="Submit", command=lambda: submit(dialog, entry, result))
    submit_button.pack(pady=5)

    dialog.protocol("WM_DELETE_WINDOW", lambda: cancel(dialog, result))
    entry.focus_set()
    dialog.grab_set()

    parent.wait_window(dialog)

    return result.get()

def on_click():
    result = show_input_dialog(root, "Custom Input", "Please enter your input:")
    if result is not None:
        output_label.config(text="Output: " + result)

root = tk.Tk()
root.geometry("400x200")

button = ctk.CTkButton(root, text="Open Input Dialog", command=on_click)
button.pack(pady=20)

output_label = tk.Label(root, text="Output:")
output_label.pack(pady=10)

root.mainloop()
