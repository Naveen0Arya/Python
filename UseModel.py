import pickle
import tkinter as tk
import os
import numpy as np
from skimage.io import imread
from skimage.transform import resize
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageOps, ImageTk

class UseModel:
    def __init__(self):
        self.path=None
        
    def getPath(self):
        self.path=self.entry1.get()
        self.name=self.entry2.get()
        f=False
        for a in os.listdir(self.paths):
            if a==self.name:
                f=True
        if f:
            self.testModel()
        else:
            self.lb.configure(text='Model Not Exist.')
            self.lb.text='Model Not Exist.'
        
    def testModel(self):
        paths=self.findPath()
        model=pickle.load(open(paths+'\\model.p','rb'))
        cat=pickle.load(open(paths+'\\cat.txt','rb'))
        flat_data =[]
        img=imread(self.path)
        imgl=Image.open(self.path)
        imgl.thumbnail((200,200))
        im = ImageTk.PhotoImage(imgl)
        self.lbl.configure(image=im)
        self.lbl.image=im
        img_resized= resize(img,(250,250,10))
        flat_data.append(img_resized.flatten())
        flat_data = np.array(flat_data)
        y=model.predict(flat_data)
        self.lb.configure(text=cat[y[0]])
        self.lb.text=cat[y[0]]
        
    def getLable(self):
        self.paths=os.path.join(os.getcwd(),'UserAccounts')
        str1="Existing Model:\t"
        for a in os.listdir(self.paths):
            str1+=a+',  '
        return str1

    def openFile(self):
        filepath=filedialog.askopenfilename(initialdir="C:\\",
                                       title="Open Image",
                                       filetypes=(("Image file",".jpg"),
                                                 ("Image file",".jpeg"),
                                                 ("Image file",".png")))
        file=open(filepath,'r')
        self.entry1.insert(0,filepath)
        file.close
    def windowBox(self):
            
        str1=self.getLable() 
        Uwindow =tk.Toplevel()
        frm1 = Frame(Uwindow)
        frm1.pack(side=TOP)
        name = Label(frm1, text = "Select Image: ").pack(side=LEFT)
        self.entry1=Entry(frm1,width = 50)
        self.entry1.pack(side=LEFT)
        frm2 = Frame(Uwindow)
        frm2.pack(side=TOP)
        name1 = Label(frm2, text = "Enter Model Name: ").pack(side=LEFT)
        self.entry2=Entry(frm2,width = 50)
        self.entry2.pack(side=LEFT)
        button1 = Button(frm1,text="browes",command=self.openFile).pack(side=RIGHT)
        self.lbl = Label(Uwindow)
        self.lbl.pack(side=TOP)
        self.lb = Label(Uwindow)
        self.lb.pack(side=TOP)
        modelsname = Label(Uwindow,text = str1).pack(side=TOP)
        button2 = Button(Uwindow,text="Submit",command=self.getPath).pack(side=BOTTOM)
        Uwindow.title("Create Model")
        Uwindow.geometry("600x600")
        Uwindow.mainloop()
        
    def findPath(self):
        paths=os.path.join(os.getcwd(),'UserAccounts')
        return os.path.join(paths,self.name)
        
        
if __name__=='__main__':
    obj=UseModel()
    obj.windowBox()