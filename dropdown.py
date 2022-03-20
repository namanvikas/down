from tkinter import *

root=Tk()
root.title("classes")
root.geometry("900x600")

class Createelement:
     
  def __init__(self):
      print("this is create element class")
      
  def getdropdown(self):
      label=Label(root,text="tis label is created by class",fg="red")
      label.pack()
      
      planet=["mercury","Venus","Earth"]
      dropdown=ttk.Combobox(root,values=planet,textvariable=selectedwal)
      btn.pack(padx=20,pady=10)
      
  def message(self):
      messagebox.showinfo("showinfo","this button is created using class")
      
obj1=getdropdown()

btn1=Button(root,text="create GUI elements",command=obj1.createnewelement)
btn1.pack(padx=20,pady=10)
root.mainloop()
     