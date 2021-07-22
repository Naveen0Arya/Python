import tkinter as tk
from tkinter import ttk
from CreateModel import CreateModel
from UseModel import UseModel
from DeleteModel import DeleteModel


class ImageRecognition:
    def __init__(self):
        self.modelname="MyModelUsed"
        
    def windowBox(self):
        root = tk.Tk()
        root.title("Image Recognition")
        tabControl = ttk.Notebook(root)
        
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)
        tab4 = ttk.Frame(tabControl)
        
        tabControl.add(tab1, text ='Home')
        tabControl.add(tab2, text ='Create Model')
        tabControl.add(tab3, text ='Use Model')
        tabControl.add(tab4, text ='Delete Model')
        tabControl.pack(expand = 1, fill ="both")
        
        ttk.Label(tab1, text ="\t\t\t\tIMAGE RECOGNITION PROJECT\nModel Process:\n\t\tCreate ModelUse ModelDelete Model\nCreate Model:\n\t\tModel of Data Set is need to create for Prediction.\nUse Model:\n\t\tModel Used for Prediction of Image.\nDelete Model:\n\t\tModel can be deleted is not needed or Not satisfactory.\nCreated by:\t\t\t\t\t\t\t\tTo:\n NAVEEN ARYA\t\t\t\t\t\t\t\tDR. REMESH KUMAR KAIT\nMCA VI\t\t\t\t\t\t\t\t\tDCSA\nD.ROLL NO.: 130\n U.ROLL NO.: 8100457").grid(column = 0, row = 0, padx = 30, pady = 30)
        ttk.Label(tab2,	text ="Create User Modele:\n\t\tTo make a model for Prediction there are some requirements. It will take time when model is building.\nRequirements:\n\t\t1. Data set folder is required to hold the classification folders of data.\n\t\t2. Classification folders are required to hold data Images related to the class.\n\t\t3. Each class should contain sufficient number of Images of that class.\nHow to Create:\n\t\t1. Click on Button Create User Model. New Window is shown.\n\t\t2. Click on Button Browse to browse image.\n\t\t3. Select any image from the dataset.\n\t\t4. Enter Model Name and submit.\n\t\t5. When Model Bullied Accuracy of model is shown.").grid(column = 0, row = 0, padx = 30, pady = 30)
        ttk.Label(tab3,	text ="Use User Model:\n\t\tIt can use all user model which are Created.\nHow to use:\n\t\t1. Click on Button Use User Model. New window is Shown\n\t\t2. Click on Button Browse to browse image for prediction.\n\t\t3. Enter Model name which is exist and submit.\n\t\t4. Image and Prediction is shown on window.").grid(column = 0, row = 0, padx = 30, pady = 30)
        ttk.Label(tab4,	text ="Delete User model:\n\t\tIt can delete the model which is created.\nHow to Delete:\n\t\t1. Click on Button delete User Model. New window is Shown\n\t\t2. Enter name of the model to delete.\n\t\t3. Model is Deleted show on window after deletion of model.").grid(column = 0, row = 0, padx = 30,	pady = 30)
        
        ttk.Button(tab2, text = "Create User Model", command=self.CreateUserModel).grid(column = 0, row = 1, padx = 30, pady = 30)
        ttk.Button(tab3, text = "Use User Model", command=self.UseUserModel).grid(column = 0, row = 1, padx = 30, pady = 30)
        ttk.Button(tab4, text = "Delete User Model", command=self.DeleteUserModel).grid(column = 0, row = 1, padx = 30, pady = 30)
        
        root.mainloop()
        
    def CreateUserModel(self):
        self.modelname = "MyModel"
        cmod=CreateModel()
        cmod.windowBox()
        
    def UseUserModel(self):
        self.modelname = "MyModel"
        umod=UseModel()
        umod.windowBox()
        
        
    def DeleteUserModel(self):
        self.modelname = "MyModel"
        dmod=DeleteModel()
        dmod.getpath()
        dmod.windowBox()
         
if __name__=='__main__':
    obj=ImageRecognition()
    obj.windowBox()