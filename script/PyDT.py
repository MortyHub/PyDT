from tkinter import *
import os

name = ""

# Grabbing the text from the box
def get_text():
    text1 = text.get("1.0", END)
    return text1

def nameText():
    text2 = Name_text.get("1.0", END)
    return text2

def quit_program_root(event):
    root.destroy()

# Configuration
root = Tk()

root.title("IDE")
root.geometry("1200x720")
root.configure(bg="#121212")

# Save file & Run File
def handle_key(event):

    name = nameText().replace("\n", "")

    # Save
    if event.keysym.lower() == "s" and (event.state & 0x4) != 0:
        if name != "":
            with open(f"{name}", "w") as f:
                f.write(get_text())
            try:
                Current_File.configure(text=f"File: {name}")
            except:
                pass
    
    # Run
    if event.keysym.lower() == "r" and (event.state & 0x4) != 0:
        if name != "":
            with open(f"{name}", "w") as f:
                f.write(get_text())
            os.system(f"python {name}")

    # Insert Script
    if event.keysym.lower() == "y" and (event.state & 0x4) != 0:
        try:
            with open(f"{name}", "r") as f:
                text.delete("1.0", END)
                text.insert(END, f.read())
        except:
            pass        

    # Create Directory
    if event.keysym.lower() == "q" and (event.state & 0x4) != 0:
        os.mkdir(name)

# Text Box

text = Text(root, bg="#101010",height=200, bd=0, wrap=WORD)
text.configure(font=("Courier", 13))
text.configure(font=("Courier", 13, "bold"), fg="white")
text.pack(side="right")

# Name

Name_text = Text(root, bg="black", bd=0, fg="white", font=("Courier", 12, "bold"), height=1)
Name_text.place(relx=0.5, rely=1.0, anchor=S)

# Side Bar

Current_File = Label(root, text = "File:", font=("Courier", 20, "bold"), bg="#101010", fg="white")
Current_File.pack()

root.bind("<Escape>", quit_program_root)
root.bind("<Key>", handle_key)


root.overrideredirect(True)
root.mainloop()