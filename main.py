from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Face_Recognition_Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")
        
        # Background Imange
        image = Image.open(r"E:\Workspace\Project\FaceRecognitionSystem\assets\background.jpg")
        image = image.resize((1430,710),Image.LANCZOS)
        # Convert the image to a PhotoImage object
        self.photoimage = ImageTk.PhotoImage(image)
        # Create the label with the PhotoImage object
        bg_image = Label(self.root, image= self.photoimage)
        bg_image.place(x=0,y=0,width=1430,height=710)
        
        # Title
        title_lbl = Label(text = "FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font = ("times new roman",20, "bold"), bg="white", fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=40)
        
        # Student button
        # Imange
        image_student = Image.open(r"E:\Workspace\Project\FaceRecognitionSystem\assets\student.jpg")
        image_student = image_student.resize((200,200),Image.LANCZOS)
        # Convert the image to a PhotoImage object
        self.photoimage_student = ImageTk.PhotoImage(image_student)
        Studen_button = Button(bg_image,image=self.photoimage_student, cursor="hand2")
        Studen_button.place(x=200,y=100,width=150,height=150)

        Studen_button_text = Button(bg_image,text="Student details", cursor="hand2", font = ("times new roman",15, "bold"), bg="darkblue", fg="white")
        Studen_button_text.place(x=200,y=250,width=150,height=40)
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_Attendance(root)
    root.mainloop()
