from tkinter import *
from tkinter import Tk
from PIL import Image,ImageTk
from tkinter import messagebox

class student_details:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1360x780+0+0")
        self.root.title("student management")
        
        image = Image.open(r"E:\Workspace\Project\FaceRecognitionSystem\assets\Background.png")
        image = image.resize((1530,750),Image.LANCZOS)
        # Convert the image to a PhotoImage object
        self.photoimage = ImageTk.PhotoImage(image)
        # Create the label with the PhotoImage object
        bg_image = Label(self.root, image= self.photoimage)
        bg_image.place(x=0,y=0,width=1380,height=770)
    
        # Title
        title_lbl = Label(text = "STUDENT MANAGEMENT SYSTEM", font = ("times new roman",20, "bold"), bg="brown", fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=55)
       
        # Creating Frame 
        main_frame = Frame(bg_image,bd="0", bg="white") #bd mean border 
        main_frame.place(x=-1,y=0,width=1370,height=510)
if __name__ == "__main__":
    root=Tk()
    obj=student_details(root)
    root.mainloop()