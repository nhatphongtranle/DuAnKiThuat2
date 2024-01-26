from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Face_Recognition_Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_Attendance(root)
    root.mainloop()
