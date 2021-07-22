# preprocessing
import os
import pickle
import tkinter as tk
from pathlib import Path
from tkinter import *

class DeleteModel:
    def __init__(self):
        self.paths=None
        
    def getModel(self):
        name=self.entry1.get()
        f=False
        for a in os.listdir(self.paths):
            if a==name:
                f=True
        if f:
            self.deleteModel(name=name)
    def getLable(self):
        str1="Existing Model:\t"
        for a in os.listdir(self.paths):
            str1+=a+',  '
        return str1
            
    def windowBox(self):
        str1=self.getLable()            
        Dwindow =tk.Toplevel()
        listModel=os.listdir(self.paths)
        frm1 = Frame(Dwindow)
        frm1.pack(side=TOP)
        name = Label(Dwindow,text = str1).pack(side=LEFT)
        name1 = Label(frm1,text = "Enter Model Name:  ").pack(side=LEFT)
        self.entry1=Entry(frm1,width = 50)
        self.entry1.pack(side=LEFT)
        self.lb = Label(Dwindow)
        self.lb.pack(side=TOP)
        b1 = Button(Dwindow,text="Submit",command=self.getModel).pack(side=BOTTOM)
        Dwindow.title("Delete Model")
        Dwindow.mainloop()
        
    def deleteModel(self,name):
        p=os.path.join(self.paths,name)
        for a in os.listdir(p):
            os.remove(os.path.join(p,a))
        os.rmdir(os.path.join(self.paths,name))
        self.lb.configure(text=name+' model is Deleted successfully.')
        self.lb.text=name+' model is Deleted successfully.'
        
    def getpath(self):
        self.paths = os.path.join(os.getcwd(),'UserAccounts')
        
        
if __name__=='__main__':
    obj=DeleteModel()
    obj.getPath()
    obj.windowBox()