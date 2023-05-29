from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import time
from plyer import notification
from threading import *


class Student:
    def __init__(self, root):
        # ==> Main Body of Root and Title <==
        self.root = root
        self.flag = False
        self.flag_another = False
        self.Sub = False
        self.Name = ""
        self.Weight = 0
        self.root.title("Water Reminder System")
        self.root.geometry("353x285")
        self.root.resizable(0, 0)
        root.wm_iconbitmap('@water.xbm')

        Management_Frame = Frame(self.root, highlightbackground="#427aa1", highlightthickness=18, relief=SOLID, bg="#ebf2fa" )
        Management_Frame.place(x=0, y=0,) # width=455, height=388,

        m_title = Label(Management_Frame, text='WATER REMINDER\nSet up a reminder', font=("Times New Roman", 22, "bold"),bg="#ebf2fa", fg = "#064789")
        m_title.grid(row=0, column=1, pady=0, padx=20)

        # ====> Button Section <====

        Submit_btn = Button(Management_Frame, command=self.SubmitBTN, text="Enter Details", width=17, bd=4,
                            relief=SOLID, font=("Times New Roman", 20, "bold"), bg="#064789", fg="white")
        Submit_btn.grid(row=1, column=1, pady=25, padx=0)

        Start_Reminder = Button(Management_Frame, command=self.StartBTN, text="Start", width=8, bd=4,
                                relief=SOLID, font=("Times New Roman", 17, "bold"),  bg="#064789", fg="white")
        Start_Reminder.grid(row=2, column=1, pady=13, padx=20, sticky="NW")

        Stop_Reminder = Button(Management_Frame, command=self.StopBTN, text="Stop", width=8, bd=4,relief=SOLID, font=("Times New Roman", 17, "bold"), bg="#064789", fg="white")
        Stop_Reminder.grid(row=2, column=1, pady=13, padx=20, sticky="SE")


        print(self.flag)

    def SubmitBTN(self):
        print(self.flag)
        try:
            self.Name = simpledialog.askstring("Enter Name", "What is your Name?")
        except ValueError:
            messagebox.showerror("Error", "Name Must be Text")
        try:
            self.Weight = int(simpledialog.askstring("Enter Weight", "What is your Weight?"))
        except ValueError:
            messagebox.showerror("Error", "Weight Must be Value")

        Final_Name = "Your Name is " + self.Name + ", And Weight " + str(self.Weight) + ", Right?"
        messagebox.showinfo("Conformation", Final_Name)

    def StopBTN(self):
        print(self.flag)
        self.flag = False

    def StartBTN(self):
        print(self.flag)
        if self.flag == False:
            self.flag = True
            thread = Thread(target=self.StartNotify)
            thread.start()
        elif self.flag_another == False:
            messagebox.showerror("Something went Wrong ","Please Provide Details Click on Name And Weight Button !!!")
        else:
            messagebox.showwarning("Activated", "Notification Already Activated")

    def StartNotify(self):
        if __name__ == "__main__":
            self.flag_another = True
            print(self.flag)
            while self.flag:
                notification.notify(
                    title="Hey " + self.Name + ", Please Drink A Glass of Water Now !!",
                    timeout=3
                )
                time.sleep(5) #2700sec=45min



root = Tk()
ob = Student(root)
root.mainloop()
