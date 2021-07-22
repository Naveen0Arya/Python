# preprocessing
import os
import pickle
import numpy as np
from pathlib import Path
from sklearn.metrics import accuracy_score,confusion_matrix
from skimage.io import imread
from skimage.transform import resize
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn import svm
from tkinter import *
from tkinter import filedialog

class CreateModel:
    def __init__(self):
        self.target = []
        self.images = []
        self.flat_data = []
        
    def getPath(self):
        self.path=self.entry1.get()
        self.name=self.entry2.get()
        f=True
        for a in os.listdir(self.paths):
            if a==self.name:
                f=False
        if f:
            self.trainSet()
        
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
        Cwindow =Tk()
        frm1 = Frame(Cwindow)
        frm1.pack(side=TOP)
        name = Label(frm1, text = "Select Image: ").pack(side=LEFT)
        self.entry1=Entry(frm1,width = 50)
        self.entry1.pack(side=LEFT)
        frm2 = Frame(Cwindow)
        frm2.pack(side=TOP)
        name1 = Label(frm2, text = "Enter Model Name: ").pack(side=LEFT)
        self.entry2=Entry(frm2,width = 50)
        self.entry2.pack(side=LEFT)
        b1 = Button(frm1,text="Browse",command=self.openFile).pack(side=RIGHT)
        self.lb = Label(Cwindow)
        self.lb.pack(side=TOP)
        modelsname = Label(Cwindow,text = str1).pack(side=TOP)
        b2 = Button(Cwindow,text="Submit",command=self.getPath).pack(side=BOTTOM)
        Cwindow.title("Create Model")
        Cwindow.geometry("800x200")
        Cwindow.mainloop()
    def trainSet(self):
        paths=Path(r""+self.path)
        paths=paths.parent.parent
        print(paths)
        DATADIR=paths
        CATEGORIES=os.listdir(DATADIR)
        self.cat=CATEGORIES
        for category in CATEGORIES:
            class_num = CATEGORIES.index(category)# label Encoding the values
            path = os.path.join(DATADIR,category)#Create path to use all the images
            for img in os.listdir(path):
                img_array=imread(os.path.join(path,img))
                img_resized=resize(img_array,(250,250,10))
                self.flat_data.append(img_resized.flatten())
                self.images.append(img_resized)
                self.target.append(class_num)
        flat_data = np.array(self.flat_data)
        images = np.array(self.images)
        target = np.array(self.target)
        #Split Data into Traning and Testing
        x_train,x_test,y_train,y_test = train_test_split(flat_data,target,test_size=0.1,random_state=109)
        self.trainModel(x_train,x_test,y_train,y_test)
        
    def trainModel(self,x_train,x_test,y_train,y_test):
        param_grid = [
                {'C':[1,10,100,1000],'kernel':['linear']},
                {'C':[1,10,100,1000],'gamma':[0.001,0.0001],'kernel':['rbf']}
                ]
        svc=svm.SVC(probability=True)
        clf=GridSearchCV(svc,param_grid)
        clf.fit(x_train,y_train)
        y_pred = clf.predict(x_test)
        accu=round(accuracy_score(y_pred,y_test)*100)
        self.lb.configure(text=self.name+' model is Created successfully accuracy is '+str(accu)+' %')
        self.lb.text=self.name+' model is Created successfully accuracy is '+str(accu)+' %'
        paths=self.findPath()
        pickle.dump(self.cat,open(os.path.join(paths,'cat.txt'),'wb'))
        pickle.dump(clf,open(os.path.join(paths,'Model.p'),'wb'))
        
    def findPath(self):
        paths=os.path.join(os.getcwd(),'UserAccounts')
        os.mkdir(paths+'\\'+self.name)
        return os.path.join(paths,self.name)
        
        
if __name__=='__main__':
    obj=CreateModel()
    obj.windowBox()