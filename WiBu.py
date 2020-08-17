from tkinter import *
from tkinter.messagebox import showinfo

def about():
    showinfo("About","Wisdom Buddy or WiBu is designed to clear your thoughts and make your mind calm.\nYou see a human brain is more complicated than a source code of an advanced AI robot or any complex program!\nHuman brain is full of mysteries, consist of happy moments, has regrets from the past and so on so forth.\nWiBu isn't some kind of pain reliever or anything! It'll just give you right thought's you should think about.\nOnce the arrow is released from the bow there is nothing you can do, Likewise You can't change what has been done or what's happened earlier\nbut there are things you can do even for the things you are done for.")

def first():
    root = Tk()
    root.geometry("520x480")
    root.title("WiBu")
    root.configure(bg='lavender')
    Label(root, text="Wisdom Buddy welcomes you!",bg='lavender', font =("Magneto", 20, "bold")).pack()
    Label(root,text="To Know more Check 'About'",bg='lavender', font =("Mistral", 10, "italic")).pack()
    Button(root, text="About", width=12, command=about).pack()
    Button(root, text="Exit", width=12, command=exit).pack()
    root.mainloop()

user=str(input("Hello There!\nWhat's your name fellow user?\n"))
print("Welcome ",user)
ask=str(input("So are you ready to begin with the Wisdom Buddy?\ny/n?\n"))
if ask=='y':
    first()
elif ask=='n':
    print("Looks like you are not ready!\nThat's fine, no need to be worried.")
    exit()
else:
    print("Inappropriate input!")
    exit()
