from tkinter import *
from datetime import date
window=Tk()
window.title("Account setup")
window.geometry("500x600")
window.mainloop()
l1=Label(text="Create your account",bg="blue",fg="#B3C5F8")
n1=Label(text="Enter your username: ")
n2= Entry()
def display():
    name=n2.get()
    message="You have successfully created your account! \nToday's date is :"
    greet=f"Hello {name}! \n"
    tbox.insert(END,greet)
    tbox.insert(END,message)
    tbox.insert(END,date.today())
tbox=Text()
btn=Button(text="Proceed",command=display)
l1.pack()
n1.pack()
n2.pack()
btn.pack()
tbox.pack()
window.mainloop()