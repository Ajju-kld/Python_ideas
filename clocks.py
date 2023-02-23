from tkinter import *

from tkinter.ttk import *
from time import strftime

root= Tk()
root.title('clock')
def time():
    string=strftime("%H:%M:%S:%p")
   
    label.config(text=string)
    label.after(1000,time)
 
label=Label(root,underline=22,font=('ds-digital', 200),background="black",foreground="blue")
label.pack(anchor='center')
time()
mainloop()