from cgi import test
import tkinter

window = tkinter.Tk() 
window.title('My First GUI Program')
window.minsize(width=500, height=300)

my_label = tkinter.Label(text= 'I Am a Label')
my_label.pack()






window.mainloop()