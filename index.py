from tkinter import *
root = Tk()
e = Entry(root,width=50)  # it creates a input display 
e.pack()
e.insert()
def myClick():
    myLabel = Label(root,text='Hello'+e.get())  # here get() takes everything on the input dispaly 
    myLabel.pack()   

myButton = Button(root,text='Enter your name ',command=myClick)
myButton.pack()

root.mainloop()
