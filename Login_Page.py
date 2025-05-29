from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import Register_page
import Database_store
import admin_handle
import test
import os


# os.remove("users.txt")
tu_return = []
class LoginWindow:
    def __init__(self,usr):

        self.screen = Toplevel()
        # self.screen.geometry(f"{self.screen.winfo_screenwidth()}x{self.screen.winfo_screenheight()}")
        self.screen.title("Login")
        self.screen.attributes("-topmost",True)
 
        self.screen.protocol("WM_DELETE_WINDOW", lambda x: print())

        # self.screen.state('zoomed')
        window_width = 1100
        window_height = 560

            # Get the screen width and height
        screen_width = self.screen.winfo_screenwidth()
        screen_height = self.screen.winfo_screenheight()

          # Calculate the position to center the window
        position_x = int((screen_width / 2) - (window_width / 2)) 
        position_y = int((screen_height / 2) - (window_height / 2)) 

        self.screen.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

        # self.bg_image = (ImageTk.PhotoImage(Image.open("background.jpg").resize((self.screen.winfo_screenwidth(), self.screen.winfo_screenheight()))))
        # self.bg_image = (ImageTk.PhotoImage(Image.open("background.jpg").resize((1150, 650))))
        # self.bg_label = Label(self.screen, image=self.bg_image)
        # self.bg_label.place(x=0, y=0)
        self.cond = False

        # self.main = Frame(self.screen, height=50, width=1100 ,bg="#570416")
        # self.main.place(x=0, y=0)
        self.main = Frame(self.screen, height=600, width=1100 ,bg="#570416")
        self.main.place(x=0, y=0)

        
        self.up_head = Frame(self.main, height=42, width=550 ,bg="#ffffff")
        self.up_head.place(x=0, y=0)

        self.up_user = Frame(self.main, height=40, width=550 ,bg="#6C1B1F")
        self.up_user.place(x=0, y=0)
        self.user_label = Label(self.up_user,text="User",font=("Tw Cen MT", 14),fg="#ffffff",bg="#6C1B1F")
        self.user_label.place(x=280,y=10)
        self.up_user.bind("<Button-1>",lambda x: self.cond_checker(x,"User"))
        self.user_label.bind("<Button-1>",lambda x: self.cond_checker(x,"User"))

        
        self.up_admin = Frame(self.main, height=40, width=550 ,bg="#570416")
        self.up_admin.place(x=550, y=0) 
        self.admin_label = Label(self.up_admin,text="Admin",font=("Tw Cen MT", 14),fg="#ffffff",bg="#570416")
        self.admin_label.place(x=280,y=10)
        self.up_admin.bind("<Button-1>",lambda x: self.cond_checker(x,"Admin",))
        self.admin_label.bind("<Button-1>",lambda x: self.cond_checker(x,"Admin",))

        self.up_head_x = 0
        self.up_head_admin = 550
        self.up_head_ad_lab = 280
        self.up_head_user = 0
        self.up_head_ur_lab = 280

                

        self.create_widgets(usr,)
        self.screen.mainloop()

    def cond_checker(self,event,mode,):
        self.cond = True
        # print(mode)
        self.create_widgets(mode,self.cond,)


    def create_widgets(self,usr,cond=False):

        # self.main.place(x=0, y=0)
        # self.up_head.place(x=self.up_head_x, y=0)
        
        # self.up_user.place(x=0, y=0)
        # self.user_label.place(x=280,y=10)

        # self.up_admin.place(x=550, y=0) 
        # self.admin_label.place(x=280,y=10)



        self.logo_image = ImageTk.PhotoImage(Image.open("logo.png").resize((190, 120)))
        self.logo_label = Label(self.main, image=self.logo_image, bg="#570416")
        self.logo_label.place(x=100, y=50)

        
        
        self.bgsideframe_image = Image.open("side_panel.png")  # Replace with the path to your background image
        self.bgsideframe_image = ImageTk.PhotoImage(self.bgsideframe_image.resize((600,400)))
        self.bgsideframe_label = Label(self.main, image=self.bgsideframe_image,bg="#570416")
        self.bgsideframe_label.place(x=440, y=90)
        
        # self.username_label = Label(self.main,text="Email Address",font=("Arial",12,"bold"),bg="#570416",fg="#ffffff",border=0)
        # self.username_label.place(x=80,y=190)
        self.username_entry = Entry(self.main, font=("Arial", 15, "normal"), relief=GROOVE,bg="#570416",fg="#bd8080",border=0)
        self.username_entry.place(x=80, y=230, width=230)
        self.username_entry.insert(0,"Email Address")
        self.username_entry.bind('<FocusIn>',lambda x:self.focusin(x,self.username_entry,"Email Address"))
        self.username_entry.bind('<FocusOut>',lambda x :self.focusout(x,self.username_entry,"Email Address"))

        self.username_frame = Frame(self.main, height=1,width=280,bg="white")
        self.username_frame.place(x=80, y=255)

        self.mail_image = Image.open("mail.png")  # Replace with the path to your logo
        self.mail_image = ImageTk.PhotoImage(self.mail_image.resize((29, 19)))
        self.mail_label = Label(self.main, image=self.mail_image, bg="#570416")
        self.mail_label.place(x=320, y=228)

        # self.password_label = Label(self.main, text="Password", font=("Arial", 12, "bold"), relief=GROOVE,bg="#570416",fg="#ffffff" ,bg="#570416")
        # self.password_label.place(x=80, y=280)
        self.password_entry = Entry(self.main, font=("Arial", 15, "normal"), relief=GROOVE,bg="#570416",fg="#bd8080",border=0)
        # self.password_entry = Entry(self.main, font=("Arial", 15, "normal"), border=0)
        self.password_entry.place(x=80, y=310, width=230)
        self.password_entry.insert(0,"Password")
        self.password_entry.bind('<FocusIn>',lambda x:self.focusin(x,self.password_entry,"Password"))
        self.password_entry.bind('<FocusOut>',lambda x :self.focusout(x,self.password_entry,"Password"))

        self.password_frame = Frame(self.main, height=1,width=280,bg="white")
        self.password_frame.place(x=80, y=340)

        self.pass_image = Image.open("password.png")  # Replace with the path to your logo
        self.pass_image = ImageTk.PhotoImage(self.pass_image.resize((29, 29)))
        self.pass_label = Label(self.main, image=self.pass_image, bg="#570416")
        self.pass_label.place(x=320, y=300)


        self.login_btn = Button(self.main, text="Login", font=("Arial", 14, "normal"), bg="#212d9c", fg="white", border=0, relief=SOLID)
        self.login_btn.place(x=160, y=390) 
        self.login_btn.bind("<Button-1>",lambda x: self.click_login())

        if usr == "User":

            self.sign_up_btn = Button(self.main, text="Create new account", font=("Arial", 12, "bold"), fg="white", bg="#20a30b", border=0, relief=SOLID, command=self.register)
            self.sign_up_btn.place(x=120, y=510)

            self.last_line = Frame(self.main, height=1, width=320, bg="#969590")
            self.last_line.place(x=60, y=470)

            self.login_btn.bind("<Button-1>",self.click_user_login)
            print("User")
            self.up_head.place(x=0,y=0)
            self.up_user.config(bg="#6C1B1F"    )
            self.user_label.config(bg="#6C1B1F")
            self.up_admin.config(bg="#570416")
            self.admin_label.config(bg="#570416")
            self.sign_up_btn.place(x=120,y=510)
            self.last_line.place(x=60,y=470)
            self.main.update()


        else: 
            print("Admin")
            self.up_head.place(x=550,y=0)
            self.up_admin.config(bg="#6C1B1F")
            self.admin_label.config(bg="#6C1B1F")
            self.up_user.config(bg="#570416")
            self.user_label.config(bg="#570416")

            self.sign_up_btn.place_forget()
            self.last_line.place_forget()
            self.main.update()

  

        # self.cond=False




    def click_login(self):
    
        self.login_details = (self.username_entry.get(), self.password_entry.get())
        return_store = Database_store.admin_login(self.login_details)
        if return_store[0]:
            self.show=messagebox.showinfo("Login", "Login Successfully")
            print(self.show) 
      
            if self.show=="ok":
                file_name = "temp.txt"
                with open(file_name, "w") as file:
                    file.write("ok")
            
            file_name = "users.txt"
            with open(file_name, "w") as file:
                file.write(f"{return_store[1][1:]}")
            self.main.destroy() 
            self.screen.destroy()
            admin = admin_handle.admin_Edit(return_store[1],return_store[2])
        else: 
            messagebox.showerror("Login", "User not registered")

    def focusin(self, event, entry_widget, placeholder_text):
        if entry_widget.get() == placeholder_text:
            entry_widget.delete(0, END)
            entry_widget.config(fg='white')

    def focusout(self, event, entry_widget, placeholder_text):
        if entry_widget.get() == '':
            entry_widget.insert(0, placeholder_text)
            entry_widget.config(fg='#bd8080')  # Optional: revert color



    def register(self):
        # self.main.destroy()
        self.screen.destroy()
        Register_page.reg()

    def delete_pass(self,event):
        self.length_arg = len(self.password_entry.get())
        for i in range(self.length_arg):
            self.password_entry.delete(0) 
        self.password_entry["fg"]="#ffffff"
    def delete_name(self,event):
        self.length_arg = len(self.username_entry.get())
        for i in range(self.length_arg):
            self.username_entry.delete(0) 
        self.username_entry["fg"]="#ffffff"



    def click_user_login(self,event):

        login_details = (self.username_entry.get(), self.password_entry.get())
        return_store = Database_store.loginUser(login_details)
        if return_store:
            tu_return.append(return_store)
            # print(return_store)
            self.screen.destroy()
            
            st = messagebox.showinfo("Login", "Login Successfully")
            if st == "ok": 
                file_name = "temp.txt"
                with open(file_name, "w") as file:
                    file.write("ok")
            
            file_name = "users.txt"
            with open(file_name, "w") as file:
                file.write(f"{return_store[1][1:]}")
            self.main.destroy()
        else: 
            messagebox.showerror("Login", "User not registered")

    def return_val(self):
        return tu_return

    
    def forgot_password(self):
        messagebox.showinfo("Forgotten Password", "Password recovery process is not implemented yet.")
        
def ru(root,cond):
    if cond == True:
        user = test.mainfile(True,root)
    else:
        user = test.mainfile(True,root,False)
         
         


if __name__ == "__main__":
    # root = Tk()
    # ru(root)
    # root.mainloop()

    LoginWindow("User")
    # return tu_return
