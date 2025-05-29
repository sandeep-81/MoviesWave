from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import Login_Page
import Database_store
import re
import test

class reg:
    def __init__(self):
        self.main = Toplevel()
        self.main.title("Register")
        self.main.protocol("WM_DELETE_WINDOW", lambda x: print())
        self.main.attributes("-topmost",True)



        # self.main.state("zoomed")
        window_width = 1150
        window_height = 600

            # Get the screen width and height
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()

          # Calculate the position to center the window
        position_x = int((screen_width / 2) - (window_width / 2)) 
        position_y = int((screen_height / 2) - (window_height / 2)) 

        self.main.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
        # Load background image
        # self.bg_image = Image.open("background.jpg")  # Replace with your background image path
        # self.bg_photo = ImageTk.PhotoImage(self.bg_image.resize((self.main.winfo_screenwidth(), self.main.winfo_screenheight())))
        # self.bg_label = Label(self.main, image=self.bg_photo)
        # self.bg_label.place(x=0, y=0)

        # Create a semi-transparent frame for the registration form
        self.form_frame = Frame(self.main, bg='#570416', bd=5, width=1150, height=600)
        self.form_frame.place(x=0,y=0)

        self.create_widgets()
        self.main.mainloop()

    def create_widgets(self):
       
        

        self.logo = Label(self.form_frame, text="Register", font=("Arial Rounded MT Bold", 20, "normal"), bg='#570416',fg="#ffffff")
        self.logo.place(x=170, y=40)
        self.subtitle = Label(self.form_frame, text="Kindly fill in this form to register", font=("Arial", 10, "normal"), bg='#570416',fg="#ffffff")
        self.subtitle.place(x=130, y=90)

        self.logoside_image = Image.open("side_panel_reg.png")  # Replace with the path to your logo
        self.logoside_image = ImageTk.PhotoImage(self.logoside_image.resize((600, 500)))
        self.logoside_label = Label(self.main, image=self.logoside_image, bg="#570416")
        self.logoside_label.place(x=470, y=40)
        
        # self.first_name = Label(self.form_frame, text="UserName", font=("Arial", 12, "normal"), bg='#570416')
        # self.first_name.place(x=90, y=120)
        self.first_name_entry = Entry(self.form_frame,width=34, font=("Arial", 14, "normal"), relief=GROOVE,bg="#570416",fg="#bd8080",border=0)
        self.first_name_entry.place(x=90, y=150)
        self.username_frame = Frame(self.form_frame, height=1,width=280,bg="white")
        self.username_frame.place(x=90, y=175)
        self.first_name_entry.insert(0,"Username")
        self.first_name_entry.bind('<FocusIn>',lambda x : self.focusin(x,self.first_name_entry,"Username"))
        self.first_name_entry.bind('<FocusOut>',lambda x : self.focusout(x,self.first_name_entry,"Username"))


        # self.email = Label(self.form_frame, text="Email", font=("Arial", 12, "normal"), bg='white')
        # self.email.place(x=90, y=180)
        self.email_entry = Entry(self.form_frame,width=34, font=("Arial", 14, "normal"), relief=GROOVE,bg="#570416",fg="#bd8080",border=0)
        self.email_entry.place(x=90, y=210)
        self.email_frame = Frame(self.form_frame, height=1,width=280,bg="white")
        self.email_frame.place(x=90, y=235)
        self.email_entry.insert(0,"Email Address")
        self.email_entry.bind('<FocusIn>',lambda x : self.focusin(x,self.email_entry,"Email Address"))
        self.email_entry.bind('<FocusOut>',lambda x : self.focusout(x,self.email_entry,"Email Address"))

        # self.phone = Label(self.form_frame, text="Phone", font=("Arial", 12, "normal"), bg='white')
        # self.phone.place(x=90, y=240)

        self.phone_entry = Entry(self.form_frame,width=34, font=("Arial", 14, "normal"), relief=GROOVE,bg="#570416",fg="#bd8080",border=0)
        self.phone_entry.place(x=90, y=270)
        self.phone_frame = Frame(self.form_frame, height=1,width=280,bg="white")
        self.phone_frame.place(x=90, y=295)
        self.phone_entry.insert(0,"Phone")
        self.phone_entry.bind('<FocusIn>',lambda x : self.focusin(x,self.phone_entry,"Phone"))
        self.phone_entry.bind('<FocusOut>',lambda x : self.focusout(x,self.phone_entry,"Phone"))

        # self.Password = Label(self.form_frame, text="Password", font=("Arial", 12, "normal"), bg='white')
        # self.Password.place(x=90, y=300)
        self.Password_entry = Entry(self.form_frame,width=34, font=("Arial", 14, "normal"), relief=GROOVE,bg="#570416",fg="#bd8080",border=0)
        self.Password_entry.place(x=90, y=330)
        self.password_frame = Frame(self.form_frame, height=1,width=280,bg="white")
        self.password_frame.place(x=90, y=355)
        self.Password_entry.insert(0,"Password")
        self.Password_entry.bind('<FocusIn>',lambda x : self.focusin(x,self.Password_entry,"Password"))
        self.Password_entry.bind('<FocusOut>',lambda x : self.focusout(x,self.Password_entry,"Password"))


        # self.Password_c = Label(self.form_frame, text="Confirm Password", font=("Arial", 12, "normal"), bg='white')
        # self.Password_c.place(x=90, y=360)
        self.Password_entry_c = Entry(self.form_frame,width=34, font=("Arial", 14, "normal"), relief=GROOVE,bg="#570416",fg="#bd8080",border=0)
        self.Password_entry_c.place(x=90, y=390)
        self.password_frame_c = Frame(self.form_frame, height=1,width=280,bg="white")
        self.password_frame_c.place(x=90, y=415)
        self.Password_entry_c.insert(0,"Confirm Password")
        self.Password_entry_c.bind('<FocusIn>',lambda x : self.focusin(x,self.Password_entry_c,"Confirm Password"))
        self.Password_entry_c.bind('<FocusOut>',lambda x : self.focusout(x,self.Password_entry_c,"Confirm Password"))

        self.Signup = Button(self.form_frame, text="Register", font=("Arial", 11, "normal"), fg="white", bg="#0f0691", border=0, relief=SOLID, width=40, command=self.register)
        self.Signup.place(x=90, y=435)

        self.already_exist = Label(self.form_frame, text="Already have an account?", font=("Arial", 12, "normal"), bg='#570416',fg="#ffffff")
        self.already_exist.place(x=120, y=500)

        self.login_end_of_already_exist = Button(self.form_frame, text="Log in", font=("Arial", 12, "underline"), fg="#ffffff", bg='#570416', border=0, relief=SOLID, command=self.login_button)
        self.login_end_of_already_exist.place(x=300, y=497)

    def login_button(self):
        self.main.destroy()
        aman = Login_Page.LoginWindow("User")

    def focusin(self, event, entry_widget, placeholder_text):
        if entry_widget.get() == placeholder_text:
            entry_widget.delete(0, END)
            entry_widget.config(fg='black')

    def focusout(self, event, entry_widget, placeholder_text):
        if entry_widget.get() == '':
            entry_widget.insert(0, placeholder_text)
            entry_widget.config(fg='#bd8080')  # Optional: revert color


    def register(self):
        contact_reg = '[6-9]{1}[0-9]{9}'
        mail_reg = "[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-z]{2,6}"
        pass_reg = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$"
        a = re.match(contact_reg, self.phone_entry.get())
        b = re.match(mail_reg, self.email_entry.get())
        c = re.match(pass_reg, self.Password_entry.get())
        if self.first_name_entry.get() == "" or self.phone_entry.get() == "" or self.email_entry.get() == "" or self.Password_entry.get() == "":
            messagebox.showerror("Missing Value Error", "Value Missing")
        elif not a:
            messagebox.showerror("Contact Error", "Invalid Contact!")
        elif not b:
            messagebox.showerror("Mail Error", "Invalid Email!")
        elif not c:
            messagebox.showerror("Password Error", "Weak Password!")
        elif self.Password_entry.get() != self.Password_entry_c.get():
            messagebox.showerror("Password Error", "Password not match!")
        else:
            messagebox.showinfo("Success", "Registration Successful")
            self.all_data = (self.first_name_entry.get(), self.email_entry.get(), self.phone_entry.get(), self.Password_entry.get())
            print(self.all_data)

            check_true_false = Database_store.registerUser(self.all_data)
            print(check_true_false)

if __name__ == "__main__":
    # root = Tk()
    # user = test.mainfile(True,root)
    # root.mainloop()
    reg()