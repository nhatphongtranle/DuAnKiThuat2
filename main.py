from tkinter import*
import tkinter as tk
from PIL import Image,ImageTk
import os
from Student import Student


class Face_Recognition_Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1360x780+0+0")
        self.root.title("Face Recognition Attendance System")
    # This part is image labels setting start    
        # Background Imange
        image = Image.open(r"E:\Workspace\Project\FaceRecognitionSystem\assets\Background.png")
        image = image.resize((1530,750),Image.LANCZOS)
        # Convert the image to a PhotoImage object
        self.photoimage = ImageTk.PhotoImage(image)
        # Create the label with the PhotoImage object
        bg_image = Label(self.root, image= self.photoimage)
        bg_image.place(x=0,y=0,width=1380,height=770)
    
        # Title
        title_lbl = Label(text = "FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font = ("times new roman",20, "bold"), bg="white", fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=40)

    # Create buttons below the section 
        # Student button
        # Image
        image_student = Image.open(r"E:\Workspace\Project\FaceRecognitionSystem\assets\student.jpg")
        image_student = image_student.resize((170,170),Image.LANCZOS)
        # Convert the image to a PhotoImage object
        self.photoimage_student = ImageTk.PhotoImage(image_student)
        Studen_button = Button(bg_image,command=self.student_pannels,image=self.photoimage_student, cursor="hand2")
        Studen_button.place(x=270,y=100,width=150,height=150)

        Studen_button_text = Button(bg_image,command=self.student_pannels,text="Student details", cursor="hand2", font = ("times new roman",15, "bold"), bg="darkblue", fg="white")
        Studen_button_text.place(x=270,y=250,width=150,height=40)
        
        # Detect face button
        image_detect = Image.open(r"E:\Workspace\Project\FaceRecognitionSystem\assets\detect.jpg")
        image_detect = image_detect.resize((200,200),Image.LANCZOS)
        # Convert the image to a PhotoImage object
        self.photoimage_detect = ImageTk.PhotoImage(image_detect)
        Detect_button = Button(bg_image,image=self.photoimage_detect, cursor="hand2")
        Detect_button.place(x=480,y=100,width=150,height=150)

        Detect_button_text = Button(bg_image,text="Face detector", cursor="hand2", font = ("times new roman",15, "bold"), bg="darkblue", fg="white")
        Detect_button_text.place(x=480,y=250,width=150,height=40)
        
        # Attendance button
        image_attendance = Image.open(r"E:\Workspace\Project\FaceRecognitionSystem\assets\attendance.jpg")
        image_attendance = image_attendance.resize((200,200),Image.LANCZOS)
        # Convert the image to a PhotoImage object
        self.photoimage_attendance = ImageTk.PhotoImage(image_attendance)
        Attendance_button = Button(bg_image,image=self.photoimage_attendance, cursor="hand2")
        Attendance_button.place(x=690,y=100,width=150,height=150)

        Attendance_button_text = Button(bg_image,text="Attendance", cursor="hand2", font = ("times new roman",15, "bold"), bg="darkblue", fg="white")
        Attendance_button_text.place(x=690,y=250,width=150,height=40)
        
        # Support button
        image_support = Image.open(r"E:\Workspace\Project\FaceRecognitionSystem\assets\support.jpg")
        image_support = image_support.resize((200,200),Image.LANCZOS)
        # Convert the image to a PhotoImage object
        self.photoimage_support = ImageTk.PhotoImage(image_support)
        Support_button = Button(bg_image,image=self.photoimage_support, cursor="hand2")
        Support_button.place(x=900,y=100,width=150,height=150)

        Support_button_text = Button(bg_image,text="Support", cursor="hand2", font = ("times new roman",15, "bold"), bg="darkblue", fg="white")
        Support_button_text.place(x=900,y=250,width=150,height=40)
    #Line 2
        # Data training button
        image_data = Image.open(r"E:\Workspace\Project\FaceRecognitionSystem\assets\Data_train.jpg")
        image_data = image_data.resize((200,200),Image.LANCZOS)
        # Convert the image to a PhotoImage object
        self.photoimage_data = ImageTk.PhotoImage(image_data)
        Data_button = Button(bg_image,image=self.photoimage_data, cursor="hand2")
        Data_button.place(x=270,y=370,width=150,height=150)

        Data_button_text = Button(bg_image,text="Data training", cursor="hand2", font = ("times new roman",15, "bold"), bg="darkblue", fg="white")
        Data_button_text.place(x=270,y=520,width=150,height=40)
        
        # Photo button
        image_photo = Image.open(r"E:\Workspace\Project\FaceRecognitionSystem\assets\photo.png")
        image_photo = image_photo.resize((200,200),Image.LANCZOS)
        # Convert the image to a PhotoImage object
        self.photoimage_photo = ImageTk.PhotoImage(image_photo)
        Photo_button = Button(bg_image,image=self.photoimage_photo, cursor="hand2")
        Photo_button.place(x=480,y=370,width=150,height=150)

        Photo_button_text = Button(bg_image,text="Photo", cursor="hand2", font = ("times new roman",15, "bold"), bg="darkblue", fg="white")
        Photo_button_text.place(x=480,y=520,width=150,height=40)
        
        # Developer button
        image_developer = Image.open(r"E:\Workspace\Project\FaceRecognitionSystem\assets\developer.jpg")
        image_developer  = image_developer.resize((200,200),Image.LANCZOS)
        # Convert the image to a PhotoImage object
        self.photoimage_developer  = ImageTk.PhotoImage(image_developer)
        Developer_button = Button(bg_image,image=self.photoimage_developer, cursor="hand2")
        Developer_button.place(x=690,y=370,width=150,height=150)

        Developer_button_text = Button(bg_image,text="Developer", cursor="hand2", font = ("times new roman",15, "bold"), bg="darkblue", fg="white")
        Developer_button_text.place(x=690,y=520,width=150,height=40)
        
        # Exit button
        image_exit = Image.open(r"E:\Workspace\Project\FaceRecognitionSystem\assets\exit.jpg")
        image_exit = image_exit.resize((200,200),Image.LANCZOS)
        # Convert the image to a PhotoImage object
        self.photoimage_exit = ImageTk.PhotoImage(image_exit)
        Exit_button = Button(bg_image,image=self.photoimage_exit, cursor="hand2")
        Exit_button.place(x=900,y=370,width=150,height=150)

        Exit_button_text = Button(bg_image,text="Exit", cursor="hand2", font = ("times new roman",15, "bold"), bg="darkblue", fg="white")
        Exit_button_text.place(x=900,y=520,width=150,height=40)
        
    # ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("dataset")
        
    # ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    def Close(self):
        root.destroy()

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_Attendance(root)
    root.mainloop()
