from tkinter import *
from datetime import date 
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk,ImageDraw
from tkinter import filedialog
from tkcalendar import DateEntry 
import Database_store
from subprocess import *
import test
import admin_handle
import update_movie
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np
from scipy.interpolate import make_interp_spline





class admin_Edit:
    def __init__(self, name_words,email):

        # self.obj = test.mainfile(False)
        # self.movie_names = self.obj.movie_names
        # print(self.movie_names)

        self.modify = False
        self.notifications = False

        self.districts = [
                    "Amritsar", "Barnala", "Bathinda", "Faridkot", "Fatehgarh Sahib", "Fazilka", "Ferozepur",
                    "Gurdaspur", "Hoshiarpur", "Jalandhar", "Kapurthala", "Ludhiana", "Mansa", "Moga", "Pathankot",
                    "Patiala", "Ropar", "Mohali", "Sangrur",
                    "Shahid Bhagat Singh Nagar ", "Sri Muktsar Sahib", "Tarn Taran"
                ]    

        self.color="#e6cfcf"
        self.email = name_words[2]
        self.name = name_words[1]
        self.lang_li = []
        self.upload_t=""
        self.upload_c=""
        self.upload_b=""
        self.upload=""
        self.db_data = []
        print(self.email ,"\n",self.name)
        # names_write = str(str(str(name_words[1]).split()).replace('[,',"")).replace("],","")
        # print(len())
        # print(len(str(self.name).split()))
        self.name_len = (len(str(self.name).split()))
        if self.name_len == 2:
            self.AK = (str(((str(self.name).split())[0][0])+((str(self.name).split())[1][0])).upper())
        elif self.name_len == 1:
            self.AK = (str(((str(self.name).split())[0][0])).upper())
        
        # self.mai = Toplevel()
        self.main = Toplevel()
        self.main.title("Admin")
        self.main.geometry(f"{self.main.winfo_screenwidth()}x{self.main.winfo_screenheight()}")
        self.main.state('zoomed')
        self.main.attributes("-topmost",True)
        self.cond = True

        

        
        self.upper_frame = Frame(self.main, width=self.main.winfo_screenwidth(), height=120, border=1, relief=SOLID, bg="#ffffff")
        self.upper_frame.pack(side=TOP, fill=X)

        img2 = ImageTk.PhotoImage((Image.open("logo_black.png")).resize((180, 80)))
        self.logo_label = Label(self.upper_frame, image=img2, bg="white")
        self.logo_label.place(x=8, y=22)

        self.notfi_on_img = Image.open("notification_on.png").resize((40,40))
        self.n_on_img = ImageTk.PhotoImage(self.notfi_on_img.resize((40,40)))

        self.notfi_img = Image.open("notification_off.png").resize((40,40))
        self.n_img = ImageTk.PhotoImage(self.notfi_img.resize((40,40)))
        self.notification_button = Button(self.upper_frame, image=self.n_img, bg="#ffffff", bd=0, activebackground="#ffffff")
        self.notification_button.place(x=1360, y=50)
        self.notification_button.bind("<Button-1>", lambda x: self.notification_toogle(x))

        self.imgg = Image.open("circle.png").resize((60,60))
        self.img = ImageTk.PhotoImage(self.imgg.resize((65,65)))
        self.logo_button = Button(self.upper_frame, image=self.img, bg="#ffffff", bd=0, activebackground="#ffffff")
        self.logo_button.place(x=1424, y=42)
        self.logo_button.bind("<Button-1>", lambda x : self.toggle_account_options(x,self.account_options_frame,1100,105))

        if self.name_len == 1:
            self.user_label = Label(self.upper_frame, text=self.AK, font=("Arial", 18, "bold"), fg="#ffffff", bg="#570416")
            self.user_label.place(x=1445, y=60)
        else:
            self.user_label = Label(self.upper_frame, text=self.AK, font=("Arial", 14, "bold"), fg="#ffffff", bg="#570416")
            self.user_label.place(x=1440, y=60)

        self.side_frame = Frame(self.main, bg="#ffffff", width=300, height=800,border=1,relief=SOLID)
        self.side_frame.place(x=0, y=120)

        self.side_side_frame = Frame(self.side_frame, bg=self.color, width=300, height=800,border=1,relief=SOLID)
        self.side_side_frame.place(x=0, y=90)

        self.main_frame = Frame(self.main, bg="#ffffff", width=1250, height=800,border=1,relief=SOLID)
        self.main_frame.place(x=300, y=120)

        self.gen_tu = []

        self.mark = ImageTk.PhotoImage(Image.open("white.jpg").resize((10, 10)))


        # self.new_movie()
        self.create_account_options()
        self.side_frame_fn()
        self.notification_center()
        self.nofication_enable()
        # self.dashboard
        # self.dashboard
        # self.dashboard()
        # self.homepage_setting()
        # self.cast_type()

        self.main.mainloop()

    def notification_toogle(self,event):
        if self.notifications == False:
            self.notification_button.config(image=self.n_img)
            self.notification_frame.place(x=1050,y=95)
            self.notifications = True

        else:
            self.notification_button.config(image=self.n_on_img)
            self.notification_frame.place_forget()
            self.notifications = False

    def notification_center(self):
        self.notification_frame = Frame(self.main, bg="#ffffff", width=350, height=600,border=1,relief=SOLID )
        self.notification_frame.place(x=1050 ,y=95)
        self.notification_frame.place_forget()

        message = self.nofication_enable()
        if len(message) == 0 :
            self.sad_img = Image.open("sad.png").resize((200,200))
            self.no_noti_img = ImageTk.PhotoImage(self.sad_img.resize((300,200)))
            self.no_notification_button = Label(self.notification_frame, image=self.no_noti_img, bg="#ffffff", bd=0)
            self.no_notification_button.place(x=35, y=100)
            title_label = Label(self.notification_frame, text=f"No Notifications", font=("Tw Cen MT", 16, "bold"), fg="#4d4c4c", bg="#ffffff")
            title_label.place(x=105, y=340)
            
        else:
            self.notification_message(message)
        

        


    def notification_message(self,message):
        y_ = 1
        for i in range(len(message)): 

            self.noti_message = Frame(self.notification_frame, bg=self.color, width=348, height=90,border=1,relief=SOLID )
            self.noti_message.place(x=1 ,y=y_)


            title_label = Label(self.noti_message, text=f"•  Update {message[i]} Movie", font=("Tw Cen MT", 14, "bold"), fg="#000000", bg=self.color)
            title_label.place(x=25, y=18)
            description_label1 = Label(self.noti_message, text=f"You need to Update Rating of the {message[i]} Movie.", font=("Tw Cen MT", 12, "normal"), fg="#000000", bg=self.color,wraplength=300)
            description_label1.place(x=25, y=40)
            description_label2 = Label(self.noti_message, text="This Movie Releasing date is Today.", font=("Tw Cen MT", 12, "normal"), fg="#000000", bg=self.color,wraplength=300)
            description_label2.place(x=25, y=60)

            y_ += 91
            setattr(self, message[i].strip().split(':')[0].replace(" ", "_"), self.noti_message)

            self.noti_message.bind("<Button-1>",lambda x , msg = message[i]: self.movie_update(x,msg))
            title_label.bind("<Button-1>", lambda event, msg=message[i]: self.movie_update(event, msg))
            description_label1.bind("<Button-1>", lambda event, msg=message[i]: self.movie_update(event, msg))
            description_label2.bind("<Button-1>", lambda event, msg=message[i]: self.movie_update(event, msg))

    def movie_update(self,event,message):
        update_movie.upload_rating(message)







    def create_account_options(self):
        self.account_options_frame = Frame(self.main, bg="#ffffff", width=350, height=250,border=1,relief=SOLID )
        self.account_options_frame.place(x=1100, y=105)
        self.account_options_frame.place_forget()
    
        self.circle_img = Image.open("circle.png").resize((80,80))
        self.imgg_local_real = ImageTk.PhotoImage(self.circle_img)
        self.logo_local = Label(self.account_options_frame, image=self.imgg_local_real, bd=0,bg="#ffffff")
        self.logo_local.place(x=22, y=35)

        if self.name_len == 1:
            self.user_label = Label(self.logo_local, text=self.AK, font=("Arial", 20, "bold"), fg="#ffffff", bg="#570416")
            self.user_label.place(x=25, y=20)
        else:
            self.user_label = Label(self.logo_local, text=self.AK, font=("Arial", 20, "bold"), fg="#ffffff", bg="#570416")
            self.user_label.place(x=16, y=20)
        
        name_label = Label(self.account_options_frame, text=self.name, font=("Arial", 15,"bold"), bg="#ffffff")
        name_label.place(x=120,y=45)

        email_label = Label(self.account_options_frame, text=self.email, font=("Arial", 12), bg="#ffffff")
        email_label.place(x=120,y=70)

        self.grey_line = Frame(self.account_options_frame, bg="grey", height=1,width=self.account_options_frame.winfo_screenwidth())
        self.grey_line.place(x=0,y=120)

        settings_button = Button(self.account_options_frame, text="Settings", font=("Arial", 14), bg="SystemButtonFace", width=30,height=1,border=1,relief=FLAT,anchor="nw",pady=10)
        settings_button.place(x=5,y=140)
        settings_button.bind("<Enter>",self.side_enter)
        settings_button.bind("<Leave>",self.side_leave)
        settings_button.bind("<Button-1>",lambda x:update_movie.settings(self.email))


        # purchase_history_button = Button(self.account_options_frame, text="Purchase History", font=("Arial", 14), bg="SystemButtonFace", width=30,height=1,border=1,relief=FLAT,anchor="nw",pady=10, command=self.open_purchase_history)
        # purchase_history_button.place(x=5,y=190)
        # purchase_history_button.bind("<Enter>",self.side_enter)
        # purchase_history_button.bind("<Leave>",self.side_leave)

        # get_help_button = Button(self.account_options_frame, text="Get Help", font=("Arial", 14), bg="SystemButtonFace", width=30,height=1,border=1,relief=FLAT,anchor="nw",pady=10, command=self.open_get_help)
        # get_help_button.place(x=5,y=240)
        # get_help_button.bind("<Enter>",self.side_enter)
        # get_help_button.bind("<Leave>",self.side_leave)

        # suggest_improvement_button = Button(self.account_options_frame, text="Suggest Improvement", font=("Arial", 14), bg="SystemButtonFace", width=30,height=1,border=1,relief=FLAT,anchor="nw",pady=10, command=self.open_suggest_improvement)
        # suggest_improvement_button.place(x=5,y=290)
        # suggest_improvement_button.bind("<Enter>",self.side_enter)
        # suggest_improvement_button.bind("<Leave>",self.side_leave)

        # refer_friends_button = Button(self.account_options_frame, text="Refer Friends", font=("Arial", 14), bg="SystemButtonFace", width=30,height=1,border=1,relief=FLAT,anchor="nw",pady=10,command=self.open_refer_friends)
        # refer_friends_button.place(x=5,y=340)
        # refer_friends_button.bind("<Enter>",self.side_enter)
        # refer_friends_button.bind("<Leave>",self.side_leave)

        # create_team_button = Button(self.account_options_frame, text="Create Team", font=("Arial", 14), bg="SystemButtonFace",width=30,height=1,border=1,relief=FLAT,anchor="nw",pady=10, command=self.open_create_team)
        # create_team_button.place(x=5,y=390)
        # create_team_button.bind("<Enter>",self.side_enter)
        # create_team_button.bind("<Leave>",self.side_leave)

        # report_content_button = Button(self.account_options_frame, text="Report Content", font=("Arial", 14), bg="SystemButtonFace",width=30,height=1,border=1,relief=FLAT,anchor="nw",pady=10, command=self.open_report_content)
        # report_content_button.place(x=5,y=440)
        # report_content_button.bind("<Enter>",self.side_enter)
        # report_content_button.bind("<Leave>",self.side_leave)

        # privacy_policy_button = Button(self.account_options_frame, text="Privacy Policy", font=("Arial", 14), bg="SystemButtonFace",width=30,height=1,border=1,relief=FLAT,anchor="nw",pady=10, command=self.open_privacy_policy)
        # privacy_policy_button.place(x=5,y=490)
        # privacy_policy_button.bind("<Enter>",self.side_enter)
        # privacy_policy_button.bind("<Leave>",self.side_leave)

        sign_out_button = Button(self.account_options_frame, text="Sign Out", font=("Arial", 14), bg="SystemButtonFace",width=30,height=1,border=1,relief=FLAT,anchor="nw",pady=10)
        sign_out_button.place(x=5,y=190)
        sign_out_button.bind("<Enter>",self.side_enter)
        sign_out_button.bind("<Leave>",self.side_leave)
        sign_out_button.bind("<Button-1>",lambda x:self.logout(x))

    def logout(self,event):
        # self.main.after(100,self.main.destroy())
            self.main.after(100,self.wait_for_destroy)
            test.mainfile(True,Toplevel(),True)
        # print("ok")
    def wait_for_destroy(self):
        self.main.withdraw()
        

    def side_frame_fn(self):

        self.circle_img_ = Image.open("circle.png").resize((80,80))
        self.imgg_local_side = ImageTk.PhotoImage(self.circle_img_)
        self.logo_local_Side = Label(self.side_frame, image=self.imgg_local_side, bg="red",bd=0)
        self.logo_local_Side.place(x=22, y=10)
        if self.name_len == 1:
            self.user_labe = Label(self.logo_local_Side, text=self.AK, font=("Arial", 22, "bold"), fg="#ffffff", bg="#570416")
            self.user_labe.place(x=24, y=20)
        else:
            self.user_labe = Label(self.logo_local_Side, text=self.AK, font=("Arial", 20, "bold"), fg="#ffffff", bg="#570416")
            self.user_labe.place(x=16, y=20)

        self.name_label = Label(self.side_frame, text=self.name, font=("Arial", 15,"bold"), bg="#ffffff")
        self.name_label.place(x=100,y=25)

        self.email_label = Label(self.side_frame, text=self.email, font=("Arial", 12), bg="#ffffff")
        self.email_label.place(x=100,y=50)

        self.grey_line = Frame(self.side_frame, bg="grey", height=1,width=self.account_options_frame.winfo_screenwidth())
        self.grey_line.place(x=0,y=90)

        self.get_admin_panel= Button(self.side_frame, text="Dashboard", font=("Arial", 14), bg=self.color,fg="black", width=25,height=1,border=1,relief=FLAT,anchor="nw",pady=10, command=self.dashboard)
        self.get_admin_panel.place(x=5,y=100)
        self.get_admin_panel.bind("<Enter>",self.side_enter)
        self.get_admin_panel.bind("<Leave>",self.side_leave)

        self.get_show_users= Button(self.side_frame, text="All Users", font=("Arial", 14), bg=self.color, width=25,height=1,border=1,relief=FLAT,anchor="nw",pady=10, command=self.all_user)
        self.get_show_users.place(x=5,y=150)
        self.get_show_users.bind("<Enter>",self.side_enter)
        self.get_show_users.bind("<Leave>",self.side_leave)

        self.type_options_frame = Frame(self.main, bg="#ffffff", width=286, height=99,border=1,relief=SOLID )
        self.type_options_frame.place(x=900, y=400)
        self.type_options_frame.place_forget()
        self.get_add_new_movie= Button(self.side_frame, text="Add New Movie\t\t⮞", font=("Arial", 14), bg=self.color, width=25,height=1,border=1,relief=FLAT,anchor="nw",pady=10,command=self.choose_frame)
        self.get_add_new_movie.place(x=5,y=200)
        self.get_add_new_movie.bind("<Enter>",self.side_enter_show)
        if self.type_options_frame.winfo_viewable():  
            self.get_add_new_movie.bind("<Button-1>",self.side_enter_show)
        else:
            self.get_add_new_movie.bind("<Button-1>",self.side_leave_hide)

        self.get_add_new_movie.bind("<Leave>",self.side_leave)

        self.get_homepage= Button(self.side_frame, text="Homepage Settings", font=("Arial", 14), bg=self.color, width=25,height=1,border=1,relief=FLAT,anchor="nw",pady=10, command=self.homepage_setting)
        self.get_homepage.place(x=5,y=250)
        self.get_homepage.bind("<Enter>",self.side_enter)
        self.get_homepage.bind("<Leave>",self.side_leave)

        self.get_cinemas= Button(self.side_frame, text="Cinemas", font=("Arial", 14), bg=self.color, width=25,height=1,border=1,relief=FLAT,anchor="nw",pady=10, command=self.cinemas)
        self.get_cinemas.place(x=5,y=300)
        self.get_cinemas.bind("<Enter>",self.side_enter)
        self.get_cinemas.bind("<Leave>",self.side_leave)

        # self.get_timing= Button(self.side_frame, text="Show Timing", font=("Arial", 14), bg=self.color, width=25,height=1,border=1,relief=FLAT,anchor="nw",pady=10, command=self.open_get_help)
        # self.get_timing.place(x=5,y=350)
        # self.get_timing.bind("<Enter>",self.side_enter)
        # self.get_timing.bind("<Leave>",self.side_leave)
        
        self.get_booking= Button(self.side_frame, text="Booking", font=("Arial", 14), bg=self.color, width=25,height=1,border=1,relief=FLAT,anchor="nw",pady=10)
        self.get_booking.place(x=5,y=350)
        self.get_booking.bind("<Enter>",self.side_enter)
        self.get_booking.bind("<Leave>",self.side_leave)
        self.get_booking.bind("<Button-1>",lambda x:self.bookings(x))
    
    def bookings(self,event):

        self.sample_screen()

        self.tickets = []
        store = Database_store.bookings_show() 
        for i in store:
            self.tickets.append(i)

        print(self.tickets)


        self.cinema_label = Label(self.inner_frame, text=f"Bookings", font=("Comic Sans MS", 30, "bold"), bg="#570416", fg="#cbeff2")
        self.cinema_label.place(x=450, y=20)

        self.view_all_label = Label(self.inner_frame, text="View All Bookings", font=("Arial", 18, "bold"), bg="#570416", fg="#ffffff")
        self.view_all_label.place(x=100, y=150)

        # Create a Treeview-like area with Frames
        self.tree_frame = Frame(self.inner_frame, width=901, height=(((len(self.tickets) + 1) * 40) + 2), bg="#ffffff")
        self.tree_frame.place(x=100, y=215)

        self.headings_frame = Frame(self.tree_frame, width=900, height=40, bg="#f5e6e9")
        self.headings_frame.place(x=1, y=1)

        Label(self.headings_frame, text="Ticket No.", font=("Tw Cen MT", 16, "bold")).place(x=150, y=5) 
        Label(self.headings_frame, text="Movie Name", font=("Tw Cen MT", 16, "bold")).place(x=450, y=5) 
        Label(self.headings_frame, text="Details", font=("Tw Cen MT", 16, "bold")).place(x=750, y=5) 

        
        self.row_frames = []  
        y = 40
        for row_counter, cinema_name in enumerate(self.tickets):
            bg_color = "#570416" if row_counter % 2 == 0 else "#6C1B1F"

            row_frame = Frame(self.tree_frame, width=899-2, height=40, bg=bg_color)
            row_frame.place(x=2, y=y)
            y += 40

            Label(row_frame, text=cinema_name[0], font=("Tw Cen MT", 14), fg="white", bg=bg_color).place(x=150, y=5)

            update_button = Button(row_frame, text=cinema_name[1], font=("Tw Cen MT", 14), fg="white", bg=bg_color, border=0, relief=FLAT)
            update_button.place(x=450,y=5)

            delete_button = Button(row_frame, text="Details", font=("Tw Cen MT", 14), fg="white", bg=bg_color, border=0, relief=FLAT)
            delete_button.place(x=750, y=5)

            # Correct lambda to capture current movie name
            delete_button.bind("<Button-1>", lambda event, ticket = cinema_name[0]: update_movie.show_ticket_detials(ticket))
            update_button.bind("<Button-1>", lambda event, name=cinema_name: self.press_delete(event, name,"update","cinema"))
            # update_button.bind("<Button-1>", lambda event, name=cinema_name: self.press_show_details(event, name))

            self.row_frames.append(row_frame)



        self.useless = Label(self.inner_frame,text="",font=("arial",1),bg="#570416")
        self.useless.pack(padx=500,pady=(((len(self.tickets) + 1) * 40) + 2))

        self.form_frame.update_idletasks()
        self.form_frame.config(scrollregion=self.form_frame.bbox("all"))

    def dashboard(self):
        self.sample_screen()

        self.dashbrd = Label(self.inner_frame, text="Dashboard", font=("Comic Sans MS", 30, "bold"), bg="#570416", fg="#cbeff2")
        self.dashbrd.place(x=340, y=30)

        self.total_movies_run = Frame(self.inner_frame,bg="#6C1B1F",height=80,width=200)
        self.total_movies_run.place(x=100,y=200)
        self.total_movies_run_text= Label(self.total_movies_run,text="Latest Movies",font=("Comic Sans MS",15),bg="#6C1B1F",fg="white")
        self.total_movies_run_text.place(x=30,y=5)
        self.total_movies_run_text_count= Label(self.total_movies_run,text=Database_store.dashaord_upper_data("movie"),font=("Comic Sans MS",15),bg="#6C1B1F",fg="white")
        self.total_movies_run_text_count.place(x=70,y=40)

        self.total_tickets_today = Frame(self.inner_frame,bg="#6C1B1F",height=80,width=200)
        self.total_tickets_today.place(x=350,y=200)
        Label(self.total_tickets_today,text="Tickets Sale",font=("Comic Sans MS",15),bg="#6C1B1F",fg="white").place(x=30,y=5)
        self.total_movies_run_text_count= Label(self.total_tickets_today,text=Database_store.dashaord_upper_data("ticket"),font=("Comic Sans MS",15),bg="#6C1B1F",fg="white")
        self.total_movies_run_text_count.place(x=70,y=40)


        self.total_users = Frame(self.inner_frame,bg="#6C1B1F",height=80,width=200)
        self.total_users.place(x=600,y=200)
        Label(self.total_users,text="Total Users",font=("Comic Sans MS",15),bg="#6C1B1F",fg="white").place(x=30,y=5)
        self.total_movies_run_text_count= Label(self.total_users,text=Database_store.dashaord_upper_data("users"),font=("Comic Sans MS",15),bg="#6C1B1F",fg="white")
        self.total_movies_run_text_count.place(x=70,y=40)

        self.total_tickets_profit = Frame(self.inner_frame,bg="#6C1B1F",height=80,width=200)
        self.total_tickets_profit.place(x=850,y=200)
        Label(self.total_tickets_profit,text="Total Profit",font=("Comic Sans MS",15),bg="#6C1B1F",fg="white").place(x=30,y=5)
        self.total_movies_run_text_count= Label(self.total_tickets_profit,text=Database_store.dashaord_upper_data("profit"),font=("Comic Sans MS",15),bg="#6C1B1F",fg="white")
        self.total_movies_run_text_count.place(x=70,y=40)
        
        self.weekly_sale = Label(self.inner_frame, text="Weekly Sale", font=("Comic Sans MS", 20, "bold"), bg="#570416", fg="#cbeff2")
        self.weekly_sale.place(x=340, y=350)
        self.bar_graph = Frame(self.inner_frame,bg="green",height=1000,width=1000)
        self.bar_graph.place(x=100,y=400)


        store = Database_store.dashboard_line_graph()
        x_labels = np.array([date.today().day-6,date.today().day-5,date.today().day-4,date.today().day-3,date.today().day-2,date.today().day-1,date.today().day])
        x_numeric = np.array([1, 2, 3, 4, 5, 6, 7])  # Numeric values for interpolation
        y_numeric = np.array([store[6],store[5],store[4],store[3],store[2],store[1],store[0]])  # Corresponding y values for interpolation

        # Create spline representation
        X_Y_Spline = make_interp_spline(x_numeric, y_numeric)

        # Returns evenly spaced numbers over the range of x
        X_ = np.linspace(x_numeric.min(), x_numeric.max(), 500)
        Y_ = X_Y_Spline(X_)

        # Create a figure for plotting
        fig, ax = plt.subplots()

        # Plotting the graph
        ax.plot(X_, Y_)

        # Replace numeric x-axis values with string labels (days of the week)
        ax.set_xticks([1, 2, 3, 4, 5, 6, 7])
        ax.set_xticklabels([date.today().day-6,date.today().day-5,date.today().day-4,date.today().day-3,date.today().day-2,date.today().day-1,date.today().day])

        ax.set_title("Values of Total Sale per Day ")
        ax.set_xlabel("Dates")
        ax.set_ylabel("Sale")

        # Integrating the Matplotlib figure with Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=self.bar_graph)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        # canvas.get_tk_widget().place(x=10,y=10)



        self.useless = Label(self.inner_frame,text="",font=("arial",1),bg="#570416")
        self.useless.pack(padx=600,pady=500)

        self.form_frame.update_idletasks()
        self.form_frame.config(scrollregion=self.form_frame.bbox("all"))

    def choose_frame(self):
        # print("yes")

        self.Latest = Button(self.type_options_frame, text="Latest Movie", font=("Arial", 14), bg=self.color, width=25,height=1,border=1,relief=FLAT,anchor="nw",pady=10,command=self.latest_movie)
        self.Latest.place(x=0,y=2)
        self.Latest.bind("<Enter>",self.side_enter)
        self.Latest.bind("<Leave>",self.side_leave)
        self.Upcoming = Button(self.type_options_frame, text="Upcoming Movie", font=("Arial", 14), bg=self.color, width=25,height=1,border=1,relief=FLAT,anchor="nw",pady=10,command=self.upcoming_movie)
        self.Upcoming.place(x=0,y=40)
        self.Upcoming.bind("<Enter>",self.side_enter)
        self.Upcoming.bind("<Leave>",self.side_leave)

    def latest_movie(self):
        self.type_options_frame.place_forget()
        self.new_movie("Latest")
        self.submit_last.place(x=400,y=1690)



    def upcoming_movie(self):
        self.type_options_frame.place_forget()
        self.new_movie("Upcoming")    
        self.submit_last.place(x=430,y=1580)
   

        
        

    def toggle_account_options(self, event,name,xx,yy):
        if name.winfo_viewable():
            name.place_forget()
        else:
            name.place(x=xx, y=yy)
            name.lift()


    def side_enter(self,event):
        event.widget["bg"]="#570416" 
        event.widget['fg']="white"

    def side_leave(self,event):
        event.widget['bg']=self.color
        event.widget['fg']="#000000"

    def side_enter_show(self,event):
        self.type_options_frame.place(x=310,y=327)
        self.choose_frame()
        event.widget["bg"]="#570416" 
        event.widget['fg']="white"
    def side_leave_hide(self,event):
        self.type_options_frame.place_forget()
        event.widget['bg']=self.color
        event.widget['fg']="#000000"


 
    def sample_screen(self):
            
            self.bg_image = (ImageTk.PhotoImage(Image.open("Curton.jpg").resize((self.main_frame.winfo_screenwidth(), self.main_frame.winfo_screenheight()))))
            self.bg_label = Label(self.main_frame, image=self.bg_image)
            self.bg_label.place(x=0, y=0) 


            self.canvas = Frame(self.main_frame, bg='#570416', bd=5)
            self.canvas.place(relx=0.5, rely=0.43, anchor=CENTER, width=1150, height=650)

            self.scrollbar = Scrollbar(self.canvas, orient="vertical")
            self.scrollbar.pack(side=RIGHT, fill=Y)

            self.form_frame = Canvas(self.canvas,bg='#570416', yscrollcommand=self.scrollbar.set)
            self.form_frame.pack(side="left", fill="both", expand=True)


            self.scrollbar.config(command=self.form_frame.yview)

            # Create an inner frame inside the Canvas
            self.inner_frame = Frame(self.form_frame, bg='#570416')


            # Add the inner frame to the Canvas
            self.form_frame.create_window((0, 0), window=self.inner_frame, anchor="nw")
        
        


    def cinemas(self):
        self.get_cinemas.config(bg="#570416")
        self.get_cinemas.config(fg="#ffffff")
        self.sample_screen()

        self.cinemas_label = Label(self.inner_frame, text="Cinemas", font=("Comic Sans MS", 30, "bold"), bg="#570416", fg="#cbeff2")
        self.cinemas_label.place(x=340, y=30)

        # self.add_new_frame = Frame(self.inner_frame, width=200, height=200, bg="#6C1B1F")
        # self.add_new_frame.place(x=150, y=215)
        # self.add_new_label = Label(self.add_new_frame, text="Add New\nCinema", font=("Tw Cen MT", 20, "normal"), bg="#6C1B1F", fg="#ffffff")
        # self.add_new_label.place(x=35, y=60)
        self.add_new_btn = Button(self.inner_frame, text="Add New\nCinema", font=("Tw Cen MT", 20, "normal"), bg="#6C1B1F", fg="#ffffff",border=0,relief=FLAT,width=14,height=6,command=self.new_cinema)
        self.add_new_btn.place(x=150, y=190)

        # self.view_all_frame = Frame(self.inner_frame, width=200, height=200, bg="#6C1B1F")
        # self.view_all_frame.place(x=450, y=190)
        # self.view_all_label = Label(self.view_all_frame, text="View All\nCinema", font=("Tw Cen MT", 20, "normal"), bg="#6C1B1F", fg="#ffffff")
        # self.view_all_label.place(x=35, y=60)
        self.view_all_btn = Button(self.inner_frame, text="View All\nCinema", font=("Tw Cen MT", 20, "normal"), bg="#6C1B1F", fg="#ffffff",border=0,relief=FLAT,width=14,height=6,command = self.show_all_cinemas)
        self.view_all_btn.place(x=450, y=190)
        print(self.modify)

        # self.modify_frame = Frame(self.inner_frame, width=200, height=200, bg="#6C1B1F")
        # self.modify_frame.place(x=750, y=215)
        # self.modify_label = Label(self.modify_frame, text="Modify\nCinema", font=("Tw Cen MT", 20, "normal"), bg="#6C1B1F", fg="#ffffff")
        # self.modify_label.place(x=35, y=60)

        self.modify_btn = Button(self.inner_frame, text="Modify\nCinema", font=("Tw Cen MT", 20, "normal"), bg="#6C1B1F", fg="#ffffff",border=0,relief=FLAT,width=14,height=6,command = self.modify_cinemas)
        self.modify_btn.place(x=750, y=190)
        

            




        self.useless = Label(self.inner_frame,text="",font=("arial",1),bg="#570416")
        self.useless.pack(padx=500,pady=180)

        self.form_frame.update_idletasks()
        self.form_frame.config(scrollregion=self.form_frame.bbox("all"))

    def modify_cinemas(self):
        self.modify = True
        self.show_all_cinemas()
        self.modify = False

    def show_all_cinemas(self):
        self.cinema_names = []
        store = Database_store.cinemas_show()
        for i in store:
            self.cinema_names.append((str(i).replace("',)","")).replace("('",""))

        print(self.cinema_names)
        self.inner_frame.destroy()
        self.sample_screen()

        self.cinema_label = Label(self.inner_frame, text="Cinemas", font=("Comic Sans MS", 30, "bold"), bg="#570416", fg="#cbeff2")
        self.cinema_label.place(x=300, y=20)

        self.view_all_label = Label(self.inner_frame, text="View All", font=("Arial", 18, "bold"), bg="#570416", fg="#ffffff")
        self.view_all_label.place(x=100, y=150)

        # Create a Treeview-like area with Frames
        self.tree_frame = Frame(self.inner_frame, width=901, height=(((len(self.districts) + 1) * 40) + 2), bg="#ffffff")
        self.tree_frame.place(x=100, y=215)

        self.headings_frame = Frame(self.tree_frame, width=900, height=40, bg="#f5e6e9")
        self.headings_frame.place(x=1, y=1)

        Label(self.headings_frame, text="District", font=("Tw Cen MT", 16, "bold")).place(x=150, y=5)
        Label(self.headings_frame, text="View", font=("Tw Cen MT", 16, "bold")).place(x=450, y=5)

        # Loop to create rows
        self.row_frames = []  # List to store row frames
        y = 40
        for row_counter, distt_name in enumerate(self.districts):
            bg_color = "#570416" if row_counter % 2 == 0 else "#6C1B1F"

            row_frame = Frame(self.tree_frame, width=899-2, height=40, bg=bg_color)
            row_frame.place(x=2, y=y)
            y += 40

            Label(row_frame, text=distt_name, font=("Tw Cen MT", 14), fg="white", bg=bg_color).place(x=150, y=5)

            view_all_button = Button(row_frame, text="View All", font=("Tw Cen MT", 14), fg="white", bg=bg_color, border=0, relief=FLAT)
            view_all_button.place(x=450,y=5)

            # delete_button = Button(row_frame, text="Delete", font=("Tw Cen MT", 12), fg="white", bg=bg_color, border=0, relief=FLAT)
            # delete_button.place(x=750, y=5)

            # Correct lambda to capture current movie name
            # delete_button.bind("<Button-1>", lambda event, name=cinema_name: self.press_delete(event, name,"delete","latest"))
            if self.modify == True:
                view_all_button.bind("<Button-1>", lambda event, name=distt_name: self.press_update_view(event, name))
            else:
                view_all_button.bind("<Button-1>", lambda event, name=distt_name: self.press_view(event, name))

            self.row_frames.append(row_frame)



        self.useless = Label(self.inner_frame,text="",font=("arial",1),bg="#570416")
        self.useless.pack(padx=500,pady=640)

        self.form_frame.update_idletasks()
        self.form_frame.config(scrollregion=self.form_frame.bbox("all"))

    def press_update_view(self,event,name):
        self.selected_disctt = name
        self.inner_frame.destroy()
        self.sample_screen()
        print(name)
        
        self.cinema_names = []
        store = Database_store.cinemas_distt_show(name)
        for i in store:
            self.cinema_names.append((str(i).replace("',)","")).replace("('",""))


        self.cinema_label = Label(self.inner_frame, text=f"{name} Cinemas", font=("Comic Sans MS", 30, "bold"), bg="#570416", fg="#cbeff2")
        self.cinema_label.place(x=300, y=20)

        self.view_all_label = Label(self.inner_frame, text="View All Cinemas", font=("Arial", 18, "bold"), bg="#570416", fg="#ffffff")
        self.view_all_label.place(x=100, y=150)

        # Create a Treeview-like area with Frames
        self.tree_frame = Frame(self.inner_frame, width=901, height=(((len(self.cinema_names) + 1) * 40) + 2), bg="#ffffff")
        self.tree_frame.place(x=100, y=215)

        self.headings_frame = Frame(self.tree_frame, width=900, height=40, bg="#f5e6e9")
        self.headings_frame.place(x=1, y=1)

        Label(self.headings_frame, text="Cinema Name", font=("Tw Cen MT", 16, "bold")).place(x=150, y=5)
        Label(self.headings_frame, text="Update", font=("Tw Cen MT", 16, "bold")).place(x=450, y=5)
        Label(self.headings_frame, text="Delete", font=("Tw Cen MT", 16, "bold")).place(x=750, y=5)

        # Loop to create rows
        self.row_frames = []  # List to store row frames
        y = 40
        for row_counter, cinema_name in enumerate(self.cinema_names):
            bg_color = "#570416" if row_counter % 2 == 0 else "#6C1B1F"

            row_frame = Frame(self.tree_frame, width=899-2, height=40, bg=bg_color)
            row_frame.place(x=2, y=y)
            y += 40

            Label(row_frame, text=cinema_name, font=("Tw Cen MT", 14), fg="white", bg=bg_color).place(x=150, y=5)

            update_button = Button(row_frame, text="Update", font=("Tw Cen MT", 14), fg="white", bg=bg_color, border=0, relief=FLAT)
            update_button.place(x=450,y=5)

            delete_button = Button(row_frame, text="Delete", font=("Tw Cen MT", 14), fg="white", bg=bg_color, border=0, relief=FLAT)
            delete_button.place(x=750, y=5)

            # Correct lambda to capture current movie name
            delete_button.bind("<Button-1>", lambda event, name=cinema_name: self.press_delete(event, name,"delete","cinema"))
            update_button.bind("<Button-1>", lambda event, name=cinema_name: self.press_delete(event, name,"update","cinema"))
            # update_button.bind("<Button-1>", lambda event, name=cinema_name: self.press_show_details(event, name))

            self.row_frames.append(row_frame)



        self.useless = Label(self.inner_frame,text="",font=("arial",1),bg="#570416")
        self.useless.pack(padx=500,pady=640)

        self.form_frame.update_idletasks()
        self.form_frame.config(scrollregion=self.form_frame.bbox("all"))

 ###########################################################################################################################################       
 ###########################################################################################################################################       
 ###########################################################################################################################################       
        
    def press_view(self,event,name):
        self.inner_frame.destroy()
        self.sample_screen()
        print(name)
        
        self.cinema_names = []
        store = Database_store.cinemas_distt_show(name)
        for i in store:
            self.cinema_names.append((str(i).replace("',)","")).replace("('",""))


        self.cinema_label = Label(self.inner_frame, text=f"{name} Cinemas", font=("Comic Sans MS", 30, "bold"), bg="#570416", fg="#cbeff2")
        self.cinema_label.place(x=300, y=20)

        self.view_all_label = Label(self.inner_frame, text="View All Cinemas", font=("Arial", 18, "bold"), bg="#570416", fg="#ffffff")
        self.view_all_label.place(x=100, y=150)

        # Create a Treeview-like area with Frames
        self.tree_frame = Frame(self.inner_frame, width=901, height=(((len(self.cinema_names) + 1) * 40) + 2), bg="#ffffff")
        self.tree_frame.place(x=100, y=215)

        self.headings_frame = Frame(self.tree_frame, width=900, height=40, bg="#f5e6e9")
        self.headings_frame.place(x=1, y=1)

        Label(self.headings_frame, text="Cinema Name", font=("Tw Cen MT", 16, "bold")).place(x=150, y=5)
        Label(self.headings_frame, text="View", font=("Tw Cen MT", 16, "bold")).place(x=450, y=5)

        # Loop to create rows
        self.row_frames = []  # List to store row frames
        y = 40
        for row_counter, cinema_name in enumerate(self.cinema_names):
            bg_color = "#570416" if row_counter % 2 == 0 else "#6C1B1F"

            row_frame = Frame(self.tree_frame, width=899-2, height=40, bg=bg_color)
            row_frame.place(x=2, y=y)
            y += 40

            Label(row_frame, text=cinema_name, font=("Tw Cen MT", 14), fg="white", bg=bg_color).place(x=150, y=5)

            show_details_button = Button(row_frame, text="Show Details", font=("Tw Cen MT", 14), fg="white", bg=bg_color, border=0, relief=FLAT)
            show_details_button.place(x=450,y=5)

            # delete_button = Button(row_frame, text="Delete", font=("Tw Cen MT", 12), fg="white", bg=bg_color, border=0, relief=FLAT)
            # delete_button.place(x=750, y=5)

            # Correct lambda to capture current movie name
            # delete_button.bind("<Button-1>", lambda event, name=cinema_name: self.press_delete(event, name,"delete","latest"))
            show_details_button.bind("<Button-1>", lambda event, name=cinema_name: self.press_show_details(event, name))

            self.row_frames.append(row_frame)



        self.useless = Label(self.inner_frame,text="",font=("arial",1),bg="#570416")
        self.useless.pack(padx=500,pady=640)

        self.form_frame.update_idletasks()
        self.form_frame.config(scrollregion=self.form_frame.bbox("all"))

    def press_show_details(self,event,name):
        update_movie.show_c_detials(name)


    def new_cinema(self):
        print("Disha")
        self.inner_frame.destroy()
        self.sample_screen()
        self.hindi_whit = ImageTk.PhotoImage(Image.open("white_circle.png").resize((10, 10)))

        self.cinemas_label = Label(self.inner_frame, text="Add New Cinema", font=("Comic Sans MS", 30, "bold"), bg="#570416", fg="#cbeff2")
        self.cinemas_label.place(x=340, y=30)


        self.entry_create("Cinema Name : ",50 ,140 ,50 , 180 , "Enter the Cinema Name",850)
        self.entry_create("Address : ",50 ,240 ,50 , 280 , "Address",400)
        self.entry_create("Street : ",500 ,240 ,500 , 280 , "ABC Road",400)
        # self.entry_create("District  : ",50 ,340 ,50 , 380 , "Choose District ",400)
        self.entry_create("PinCode  : ",500 ,340 ,500 , 380 , "Enter the PinCode ",400)
        self.entry_create("Total Screens  : ",50 ,440 ,50 , 480 , "Number of Screens ",400)
        self.entry_create("Total Seats Capacity  : ",500 ,440 ,500 , 480 , "Enter Total Seats Capacity ",400)
        self.entry_create("Contact Number : ",50 ,540 ,50 , 580 , "Enter Phone Number ",400)
        self.entry_create("Contact Email : ",500 ,540 ,500 , 580 , "Enter Email Address ",400)
        self.entry_create("Opening Time : ",50 ,640 ,50 , 680 , "Enter Opening Timing ",400)
        self.entry_create("Closing Time : ",500 ,640 ,500 , 680 , "Enter Closing Timing ",400)

        self.screens_spinbox = Spinbox(self.inner_frame,font=("Arial",14,"normal"), from_=1, to=20)
        self.screens_spinbox.place(x=50,y=480,width=400)

        
        self.frame_gen = Frame(self.inner_frame,height=430,width=400,bg="white")
        self.frame_gen.place(x=60,y=410)
        self.frame_gen.place_forget()
        self.choose_distt() 

        Label(self.inner_frame, text="District", font=("Arial", 14, "bold"), bg="#570416", fg="#cbeff2").place(x=50, y=340)
        self.select_btn = Button(self.inner_frame,text=" District \t\t\t\t\t ▼ ", font=("Arial", 13, "normal"), relief=GROOVE,bg="#ffffff",fg="#bd8080",border=0,anchor=NW)
        self.select_btn.place(x=50, y=380, width=400)
        self.select_btn.bind('<Button-1>',lambda x : self.toggle_account_options(x,self.frame_gen,50,410))
                
        self.submit_btn = ImageTk.PhotoImage(Image.open("submit.png").resize((150,50)))
        self.submit_last = Button(self.inner_frame, image=self.submit_btn, font=("Arial", 15),anchor=CENTER, activebackground="#570416",bg="#570416",border=1,relief=FLAT,command=self.cinemas_upload)
        self.submit_last.place(x=400,y=750)

        

        self.useless = Label(self.inner_frame,text="",font=("arial",1),bg="#570416")
        self.useless.pack(padx=500,pady=430)

        self.form_frame.update_idletasks()
        self.form_frame.config(scrollregion=self.form_frame.bbox("all"))
    
    def choose_distt(self):
        self.Amritsar= self.Barnala= self.Bathinda= self.Faridkot= self.Fatehgarh_Sahib= self.Fazilka= self.Ferozepur=self.Gurdaspur= self.Hoshiarpur= self.Jalandhar= self.Kapurthala= self.Ludhiana= self.Mansa= self.Moga= self.Pathankot=self.Patiala=self.Ropar=self.Mohali= self.Sangrur=self.Shahid_Bhagat_Singh_Nagar= self.Sri_Muktsar_Sahib= self.Tarn_Taran = False
        self.dist_list = [self.Amritsar, self.Barnala, self.Bathinda, self.Faridkot, self.Fatehgarh_Sahib, self.Fazilka, self.Ferozepur,self.Gurdaspur, self.Hoshiarpur, self.Jalandhar, self.Kapurthala, self.Ludhiana, self.Mansa, self.Moga, self.Pathankot,self.Patiala,self.Ropar,self.Mohali, self.Sangrur,self.Shahid_Bhagat_Singh_Nagar, self.Sri_Muktsar_Sahib, self.Tarn_Taran ]

        left_counter = 1
        right_counter = 1
        count = 10
        index = 0 

        while index < len(self.districts):
            i = self.districts[index]
            j = range(count, 386, 35)[index % len(range(count, 386, 35))]  # Adjust j using count and wrap around with modulus
            k = self.dist_list[index]
            
            if left_counter < 12:
                self.circle_gen(5, j, i, k,"cin")
                left_counter += 1
            else:
                self.circle_gen(160, j, i, k,"cin")
                right_counter += 1
            
            if j == 385:
                count = 10  

            index += 1


        


    def entry_create(self, label_name, label_x, label_y, entry_x , entry_y, placeholder , wid =280 ):
        address = Label(self.inner_frame,text=label_name,font=("Arial",14,"bold"),bg="#570416",fg="#cbeff2")
        address.place(x=label_x,y=label_y)
        address_entry = Entry(self.inner_frame, font=("Arial", 14, "normal"), relief=GROOVE,bg="#ffffff",fg="#bd8080",border=0)
        address_entry.place(x=entry_x, y=entry_y, width=wid) 
        address_entry.insert(0,placeholder)
        address_entry.bind('<FocusIn>',lambda x:self.focusin(x,address_entry,placeholder))
        address_entry.bind('<FocusOut>',lambda x :self.focusout(x,placeholder))
        setattr(self, label_name.strip().split(':')[0].replace(" ", "_"), address_entry)


    def cinemas_upload(self):

        li = (self.Cinema_Name_.get(), self.Address_.get(),self.Street_.get(),self.select_btn.cget("text ") ,self.PinCode__.get(),self.screens_spinbox.get(),self.Total_Seats_Capacity__.get(),self.Contact_Number_.get(),self.Contact_Email_.get(),self.Opening_Time_.get(),self.Closing_Time_.get())
        if li[0] =="Enter the Cinema Name":
            messagebox.showerror("Error","Cinema Name Missing")
        elif li[1] =="Address":
            messagebox.showerror("Error","Address Missing")
        elif li[2] =="ABC Road":
            messagebox.showerror("Error","Road Missing")
        elif li[3] ==" District \t\t\t\t\t ▼ ":
            messagebox.showerror("Error","District Missing")
        elif li[4] =="Enter the PinCode ":
            messagebox.showerror("Error","PinCode Missing")
        elif li[5] =="Number of Screens ":
            messagebox.showerror("Error","Screens Missing")
        elif li[6] =="Enter Total Seats Capacity " :
            messagebox.showerror("Error","Seat Capacity Missing")
        elif li[7] =="Enter Phone Number ":
            messagebox.showerror("Error","Phone Number Missing")
        elif li[8] =="Enter Email Address ":
            messagebox.showerror("Error","Email Address Missing")
        elif li[9] =="Enter Opening Timing ":
            messagebox.showerror("Error","Opening Time Missing")
        elif li[10] =="Enter Closing Timing ":
            messagebox.showerror("Error","Closing Time Missing")
        else:
            store = Database_store.new_cinema_upload(li)
            if store == True:
                print(store)
                messagebox.showinfo("Sucess","Uploaded ")
            elif store == "exist":
                messagebox.showerror("Error","Already Uploaded ")
            else:
                messagebox.showerror("Error","Unexpected Value ")

        


    def all_user(self):

        self.users = []
        self.user = Database_store.loginUser_show()
        for i in self.user: 
            self.users.append((str(i).replace("',)","")).replace("('",""))
        

        self.sample_screen()

        self.all_user_label = Label(self.inner_frame, text="All Users", font=("Comic Sans MS", 30, "bold"), bg="#570416", fg="#cbeff2")
        self.all_user_label.place(x=300, y=20)

        self.users_label = Label(self.inner_frame, text="Users", font=("Arial", 18, "bold"), bg="#570416", fg="#ffffff")
        self.users_label.place(x=100, y=150)

        # Create a Treeview-like area with Frames
        self.tree_frame = Frame(self.inner_frame, width=901, height=(((len(self.users) + 1) * 40) + 2), bg="#ffffff")
        self.tree_frame.place(x=100, y=215)

        self.headings_frame = Frame(self.tree_frame, width=900, height=40, bg="#f5e6e9")
        self.headings_frame.place(x=1, y=1)

        Label(self.headings_frame, text="User", font=("Tw Cen MT", 16, "bold")).place(x=150, y=5)
        Label(self.headings_frame, text="Details", font=("Tw Cen MT", 16, "bold")).place(x=450, y=5)
        Label(self.headings_frame, text="Delete", font=("Tw Cen MT", 16, "bold")).place(x=750, y=5)

        # Loop to create rows
        self.row_frames = []  # List to store row frames
        y = 40
        for row_counter, user in enumerate(self.users):
            bg_color = "#570416" if row_counter % 2 == 0 else "#6C1B1F"

            row_frame = Frame(self.tree_frame, width=899-2, height=40, bg=bg_color)
            row_frame.place(x=2, y=y)
            y += 40

            Label(row_frame, text=user, font=("Tw Cen MT", 14), fg="white", bg=bg_color).place(x=150, y=5)

            update_button = Button(row_frame, text="Show Details", font=("Tw Cen MT", 14), fg="white", bg=bg_color, border=0, relief=FLAT)
            update_button.place(x=450,y=5)

            delete_button = Button(row_frame, text="Delete", font=("Tw Cen MT", 14), fg="white", bg=bg_color, border=0, relief=FLAT)
            delete_button.place(x=750, y=5)

            # Correct lambda to capture current movie name
            delete_button.bind("<Button-1>", lambda event, name=user: self.press_delete(event, name,"delete","user"))
            update_button.bind("<Button-1>", lambda event, name=user: self.press_delete(event, name,"details","user"))

            self.row_frames.append(row_frame)

            
        self.useless = Label(self.inner_frame,text="",bg="#570416")
        self.useless.pack(padx=560,pady=850)

        self.form_frame.update_idletasks()
        self.form_frame.config(scrollregion=self.form_frame.bbox("all"))

#############################################################################################################################################################3

    def homepage_setting(self):

        self.movie_names = []
        self.movie_names_up = []

        self.movie_name = Database_store.movie_name_show()
        for i in self.movie_name:
            self.movie_names.append((str(i).replace("',)","")).replace("('",""))
            
        self.movie_name_up = Database_store.movie_name_show_up()
        for i in self.movie_name_up:
            self.movie_names_up.append((str(i).replace("',)","")).replace("('",""))
        
        self.sample_screen()

        self.movie_label = Label(self.inner_frame, text="Homepage Settings", font=("Comic Sans MS", 30, "bold"), bg="#570416", fg="#cbeff2")
        self.movie_label.place(x=300, y=20)

        self.latest_label = Label(self.inner_frame, text="Latest Movies", font=("Arial", 18, "bold"), bg="#570416", fg="#ffffff")
        self.latest_label.place(x=100, y=150)

        # Create a Treeview-like area with Frames
        self.tree_frame = Frame(self.inner_frame, width=901, height=(((len(self.movie_names) + 1) * 40) + 2), bg="#ffffff")
        self.tree_frame.place(x=100, y=215)

        self.headings_frame = Frame(self.tree_frame, width=900, height=40, bg="#f5e6e9")
        self.headings_frame.place(x=1, y=1)

        Label(self.headings_frame, text="Movie Name", font=("Tw Cen MT", 16, "bold")).place(x=150, y=5)
        Label(self.headings_frame, text="Update", font=("Tw Cen MT", 16, "bold")).place(x=450, y=5)
        Label(self.headings_frame, text="Delete", font=("Tw Cen MT", 16, "bold")).place(x=750, y=5)

        # Loop to create rows
        self.row_frames = []  # List to store row frames
        y = 40
        for row_counter, movie_name in enumerate(self.movie_names):
            bg_color = "#570416" if row_counter % 2 == 0 else "#6C1B1F"

            row_frame = Frame(self.tree_frame, width=899-2, height=40, bg=bg_color)
            row_frame.place(x=2, y=y)
            y += 40

            Label(row_frame, text=movie_name, font=("Tw Cen MT", 14), fg="white", bg=bg_color).place(x=150, y=5)

            update_button = Button(row_frame, text="Update", font=("Tw Cen MT", 14), fg="white", bg=bg_color, border=0, relief=FLAT)
            update_button.place(x=450,y=5)

            delete_button = Button(row_frame, text="Delete", font=("Tw Cen MT", 14), fg="white", bg=bg_color, border=0, relief=FLAT)
            delete_button.place(x=750, y=5)

            # Correct lambda to capture current movie name
            delete_button.bind("<Button-1>", lambda event, name=movie_name: self.press_delete(event, name,"delete","latest"))
            update_button.bind("<Button-1>", lambda event, name=movie_name: self.press_delete(event, name,"update","latest"))

            self.row_frames.append(row_frame)

#############################################################################################################################################################3
#############################################################################################################################################################3

        self.upcoming_label = Label(self.inner_frame, text="Upcoming Movies", font=("Arial", 18, "bold"), bg="#570416", fg="#ffffff")
        self.upcoming_label.place(x=100, y=150 + (((len(self.movie_names) + 1) * 40) + 2)+130)

        self.tree_frame_up = Frame(self.inner_frame, width=901, height=(((len(self.movie_names_up) + 1) * 40) + 2), bg="#ffffff")
        self.tree_frame_up.place(x=100, y=150 + (((len(self.movie_names) + 1) * 40) + 2)+195)
       
        self.headings_frame_up = Frame(self.tree_frame_up, width=900, height=40, bg="#f5e6e9")
        self.headings_frame_up.place(x=1, y=1)

        Label(self.headings_frame_up, text="Movie Name", font=("Tw Cen MT", 16, "bold")).place(x=150, y=5)
        Label(self.headings_frame_up, text="Update", font=("Tw Cen MT", 16, "bold")).place(x=450, y=5)
        Label(self.headings_frame_up, text="Delete", font=("Tw Cen MT", 16, "bold")).place(x=750, y=5)


        self.row_frames_up = []  # List to store row frames
        y = 40
        for row_counter, movie_name in enumerate(self.movie_names_up):
            bg_color = "#570416" if row_counter % 2 == 0 else "#6C1B1F"

            row_frame = Frame(self.tree_frame_up, width=899-2, height=40, bg=bg_color)
            row_frame.place(x=2, y=y)
            y += 40

            Label(row_frame, text=movie_name, font=("Tw Cen MT", 14), fg="white", bg=bg_color).place(x=150, y=5)

            update_button = Button(row_frame, text="Update", font=("Tw Cen MT", 14), fg="white", bg=bg_color, border=0, relief=FLAT)
            update_button.place(x=450,y=5)

            delete_button = Button(row_frame, text="Delete", font=("Tw Cen MT", 14), fg="white", bg=bg_color, border=0, relief=FLAT)
            delete_button.place(x=750, y=5)

            # Correct lambda to capture current movie name
            delete_button.bind("<Button-1>", lambda event, name=movie_name: self.press_delete(event, name,"delete","upcoming"))
            update_button.bind("<Button-1>", lambda event, name=movie_name: self.press_delete(event, name,"update","upcoming"))

            self.row_frames_up.append(row_frame)
            
#############################################################################################################################################################3
#############################################################################################################################################################3
        
        self.useless = Label(self.inner_frame,text="",bg="#570416")
        self.useless.pack(padx=560,pady=850)

        self.form_frame.update_idletasks()
        self.form_frame.config(scrollregion=self.form_frame.bbox("all"))

    def press_delete(self, event, name,btn,upnew):
        if btn == "delete":
            reply = messagebox.askokcancel("Warning",f"Do You want to Delete {name}")
            print(reply)
            if reply==True:
                check=Database_store.delete_movie((name,),upnew)
                if check == True:
                    # admin_handle.admin_Edit.homepage_setting(self)
                    messagebox.showinfo("Sucess","Done")
                    if upnew == "latest" or upnew == "update":
                        self.homepage_setting()
                    elif upnew == "cinema":
                        self.press_update_view(0,self.selected_disctt)
                else:
                    messagebox.showerror("Error","Error")
            else:
                print("Not Deleted")


        else:
            if btn == "update":
                if upnew == "cinema":
                    update_movie.update_cin_scr+(name,upnew)
                else:
                    update_movie.update_scr(name,upnew) 
        
            else:
                update_movie.show_detials(name,upnew) 
            





    def new_movie(self,name):

        # self.bg_image = (ImageTk.PhotoImage(Image.open("Curton.jpg").resize((self.main_frame.winfo_screenwidth(), self.main_frame.winfo_screenheight()))))
        # self.bg_label = Label(self.main_frame, image=self.bg_image)
        # self.bg_label.place(x=0, y=0) 


        # self.canvas = Frame(self.main_frame, bg='#570416', bd=5)
        # self.canvas.place(relx=0.5, rely=0.43, anchor=CENTER, width=1150, height=650)

        # self.scrollbar = Scrollbar(self.canvas, orient="vertical")
        # self.scrollbar.pack(side=RIGHT, fill=Y)

        # self.form_frame = Canvas(self.canvas,bg='#570416', yscrollcommand=self.scrollbar.set)
        # self.form_frame.pack(side="left", fill="both", expand=True)


        # self.scrollbar.config(command=self.form_frame.yview)

        # # Create an inner frame inside the Canvas
        # self.inner_frame = Frame(self.form_frame, bg='#570416')


        # # Add the inner frame to the Canvas
        # self.form_frame.create_window((0, 0), window=self.inner_frame, anchor="nw")

        self.sample_screen()



        self.movie_label = Label(self.inner_frame,text=f"Add {name} Movie",font=("Comic Sans MS",30,"bold"),bg="#570416",fg="#cbeff2")
        self.movie_label.place(x=300,y=20)

        self.add_movie_orignal = ImageTk.PhotoImage(Image.open("add_movie.png").resize((150,120)))
        self.local_frame = Label(self.inner_frame , image=self.add_movie_orignal, height=300, width=250, bg="#6e051c", relief=GROOVE, border=1)
        self.local_frame.place(x=100,y=130)
        self.local_frame.bind("<Button-1>", self.upload_file)
        self.local_frame_text = Label(self.local_frame,text="Add New Movie",font=("Arial",15,"bold"),bg="#6e051c",fg="#bd8080")
        self.local_frame_text.place(x=45,y=220)      
          

        self.movie_name = Label(self.inner_frame,text="Movie name : ",font=("Arial",13,"bold"),bg="#570416",fg="#cbeff2")
        self.movie_name.place(x=450,y=140)
        self.movie_name_entry = Entry(self.inner_frame, font=("Arial", 13, "normal"), relief=GROOVE,bg="#ffffff",fg="#bd8080",border=0)
        self.movie_name_entry.place(x=570, y=140, width=280)
        self.movie_name_entry.insert(0,"Enter the Movie Name ")
        self.movie_name_entry.bind('<FocusIn>',lambda x:self.focusin(x,self.movie_name_entry,"Enter the Movie Name "))
        self.movie_name_entry.bind('<FocusOut>',lambda x :self.focusout(x,"Enter the Movie Name "))
        # self.movie_name_frame = Frame(self.inner_frame, height=1,width=280,bg="black")
        # self.movie_name_frame.place(x=560, y=135)  

       
        self.lang = Label(self.inner_frame, text="Language : ", font=("Arial", 13, "bold"), bg="#570416", fg="#cbeff2")
        self.lang.place(x=465, y=200)

        self.hindi_whit = ImageTk.PhotoImage(Image.open("white_circle.png").resize((10, 10)))
       
        self.eng_cond = self.hin_cond = self.pun_cond = self.mar_cond = self.tel_cond = self.ben_cond = self.guj_cond = self.oth_cond = False

        self.circle_lang(568, 207, "English", self.eng_cond)
        self.circle_lang(568, 235, "Hindi", self.hin_cond)
        self.circle_lang(568, 261, "Punjabi", self.pun_cond)
        self.circle_lang(568, 286, "Malayalam", self.mar_cond)

        self.circle_lang(700, 207, "Telegu", self.tel_cond)
        self.circle_lang(700, 235, "Tamil", self.ben_cond)
        self.circle_lang(700, 261, "Kannada", self.guj_cond)
        self.circle_lang(700, 286, "Other", self.oth_cond)

    
        self.genres = Label(self.inner_frame, text="Genres : ", font=("Arial", 13, "bold"), bg="#570416", fg="#cbeff2")
        self.genres.place(x=485, y=320)


        # self.whit = ImageTk.PhotoImage(Image.open("white_circle.png").resize((10, 10)))

        self.action_cond = self.animation_cond = self.biographiy_cond = self.comdy_cond = self.crime_cond = self.drama_cond = self.family_cond = self.fantsy_cond = self.historical_cond = self.horror_cond = self.musical_cond = self.mystery_cond = self.oth_gen_cond = self.romantic_cond = self.sci_fi_cond = self.thiller_cond = self.war_cond = False


        
        self.frame_gen = Frame(self.inner_frame,height=350,width=300,bg="white")
        self.frame_gen.place(x=570,y=360)
        self.frame_gen.place_forget()
        self.gen_frame() 

        self.select_btn = Button(self.inner_frame,text=" Movie Type                         ▼ ", font=("Arial", 13, "normal"), relief=GROOVE,bg="#ffffff",fg="#bd8080",border=0,anchor=NW)
        self.select_btn.place(x=570, y=325, width=280)
        self.select_btn.bind('<Button-1>',lambda x : self.toggle_account_options(x,self.frame_gen,570,360))
        
        self.rel_date = Label(self.inner_frame, text="Release Date : ", font=("Arial", 13, "bold"), bg="#570416", fg="#cbeff2")
        self.rel_date.place(x=438, y=380)

        self.date = DateEntry(self.inner_frame,date_pattern="yyyy/mm/dd",default="yyyy/mm/dd", font=("Arial", 12))
        self.date.place(x=570,y=380)
        self.date.insert(0, "yyyy/mm/dd")

        self.movie_time = Label(self.inner_frame, text="Movie Time : ", font=("Arial", 13, "bold"), bg="#570416", fg="#cbeff2")
        self.movie_time.place(x=438, y=430)
                
        self.movie_time_entry = Entry(self.inner_frame, font=("Arial", 13, "normal"), relief=GROOVE,bg="#ffffff",fg="#bd8080",border=0)
        self.movie_time_entry.place(x=570, y=430, width=280)
        self.movie_time_entry.insert(0,"In Mintues ")
        self.movie_time_entry.bind('<FocusIn>',lambda x:self.focusin(x,self.movie_time_entry,"In Mintues "))
        self.movie_time_entry.bind('<FocusOut>',lambda x :self.focusout(x,"In Mintues "))

        self.movie_banner = Label(self.inner_frame, text="Banner : ", font=("Arial", 13, "bold"), bg="#570416", fg="#cbeff2")
        self.movie_banner.place(x=470, y=480)
        self.movie_banner_btn = Button(self.inner_frame,text="Upload Banner ... ", font=("Arial", 12),width=25,height=1)
        self.movie_banner_btn.place(x=570,y=480)
        self.movie_banner_btn.bind("<Button-1>",self.upload_Banner)

        self.about = Label(self.inner_frame, text="About : ", font=("Arial", 13, "bold"), bg="#570416", fg="#cbeff2")
        self.about.place(x=490, y=530)

        self.about_Entry = Text(self.inner_frame, font=("Arial", 12),width=50,height=6)
        self.about_Entry.place(x=570,y=530)



        self.Trailer = Label(self.inner_frame, text="Trailer : ", font=("Arial", 13, "bold"), bg="#570416", fg="#cbeff2")
        self.Trailer.place(x=490, y=660)
        self.Trailer_Entry = Button(self.inner_frame,text="Upload Trailer ... ", font=("Arial", 12),width=25,height=1)
        self.Trailer_Entry.place(x=570,y=660)
        self.Trailer_Entry.bind("<Button-1>",self.upload_Triler)

    
        self.Trailer_Frame = Frame(self.inner_frame, height=250,bg="#6e051c",width=400, relief=GROOVE, border=1)
        self.Trailer_Frame.place(x=570,y=700) 
        self.Trailer_imgs = ImageTk.PhotoImage(Image.open("YT.png").resize((110,80)))
        self.Trailer_img = Label(self.Trailer_Frame , image=self.Trailer_imgs, height=250, width=400, bg="#6e051c")
        self.Trailer_img.place(x=0,y=0)
      
       




        ##########################################################################################################
        ############################################ |_____CAST_FRAME_____| ##########################################
        ##########################################################################################################
       
    
        self.here_data = 0
        
        self.movie_label = Label(self.inner_frame,text="Cast",font=("Comic Sans MS",30,"bold"),bg="#570416",fg="#cbeff2")
        self.movie_label.place(x=500,y=950)

        self.last_line = Frame(self.inner_frame, height=1, width=820, bg="#969590")
        self.last_line.place(x=150, y=960)
             
        self.x_cast_image = 160
        self.y_cast_image = 1020

        self.cast_imgg = Image.open("cast_add.png").resize((80,80))
        self.cast_img = ImageTk.PhotoImage(self.cast_imgg.resize((85,85)))
        self.cast_logo_button = Button(self.inner_frame, image=self.cast_img, bg="#570416", bd=0, activebackground="#570416")
        self.cast_logo_button.place(x=160, y=1020)
        self.cast_logo_button.bind("<Button-1>",lambda x: self.toggle_account_options(x,self.cast_options_frame,203,1095))



        self.add_new_label = Label(self.inner_frame,text="Add New \n Cast",font=("Arial",12,"bold"),bg="#570416",fg="#cbeff2")
        self.add_new_label.place(x=170,y=1110)

        self.cast_Frame = Frame(self.inner_frame, height=350,bg="#6e051c",width=600, relief=GROOVE, border=1)
        self.cast_Frame.place(x=280,y=1180) 

        self.cast_type()
        
        self.submit_btn = ImageTk.PhotoImage(Image.open("submit.png").resize((150,50)))
        self.useless = Label(self.inner_frame,text="",bg="#570416")

        if name == "Latest":

            
            self.last_line_cast = Frame(self.inner_frame, height=1, width=820, bg="#969590")
            self.last_line_cast.place(x=150, y=1580)

            self.rating = Label(self.inner_frame,text="Rating : ",font=("Arial",16,"bold"),bg="#570416",fg="#cbeff2")
            self.rating.place(x=350,y=1610)
            self.rating_entry = Entry(self.inner_frame, font=("Arial", 16, "normal"), relief=GROOVE,bg="#ffffff",border=0)
            self.rating_entry.place(x=450,y=1617 ,width=50)
            self.rating_10 = Label(self.inner_frame,text="/10 ",font=("Arial",16,"bold"),bg="#570416",fg="#cbeff2")
            self.rating_10.place(x=500,y=1615)

            self.submit_last = Button(self.inner_frame, image=self.submit_btn, font=("Arial", 15),anchor=CENTER, activebackground="#570416",bg="#570416",border=1,relief=FLAT,command=self.db_send_new_movie)
            self.useless.pack(padx=560,pady=880)
        
        else:
            self.useless.pack(padx=560,pady=850)
            self.submit_last = Button(self.inner_frame, image=self.submit_btn, font=("Arial", 15),anchor=CENTER, activebackground="#570416",bg="#570416",border=1,relief=FLAT,command=self.db_send_upcoming_movie)



        self.form_frame.update_idletasks()
        self.form_frame.config(scrollregion=self.form_frame.bbox("all"))



    def cast_type(self):
        
        self.cast_options_frame = Frame(self.inner_frame, bg="#ffffff", width=150, height=85,border=1,relief=SOLID )
        self.cast_options_frame.place(x=230, y=1095)
        self.cast_options_frame.place_forget()
        self.actor = Button(self.cast_options_frame, text="Cast", font=("Arial", 15),anchor=CENTER, bg="SystemButtonFace", width=13,height=1,border=1,relief=FLAT)
        self.actor.place(x=0,y=2)
        self.actor.bind("<Enter>",self.side_enter)
        self.actor.bind("<Leave>",self.side_leave)
        self.actor.bind("<Button-1>",lambda x: self.cast_frame_fn("Cast","Charcter : "))
        self.actress = Button(self.cast_options_frame, text="Crew", font=("Arial", 15),anchor=CENTER, bg="SystemButtonFace", width=13,height=1,border=1,relief=FLAT)
        self.actress.place(x=0,y=40)
        self.actress.bind("<Enter>",self.side_enter)
        self.actress.bind("<Leave>",self.side_leave)
        self.actress.bind("<Button-1>",lambda x: self.cast_frame_fn("Crew","Role : "))

        self.default = Label(self.cast_Frame,text="Add New\n Cast",font=("Arial",25,"bold"),bg="#6e051c",fg="#ab0a2d")
        self.default.place(x=180,y=120)
        
    def cast_frame_fn(self,name,role):
        
        self.cast_label = Label(self.cast_Frame,text=name,font=("Arial",16,"bold"),bg="#6e051c",fg="#cbeff2")

        self.cast_name = Label(self.cast_Frame,text=f"{name} Name : ",font=("Arial",14,"normal"),bg="#6e051c",fg="#cbeff2")
        self.cast_name_entry = Entry(self.cast_Frame, font=("Arial", 13, "normal"), relief=GROOVE,bg="#ffffff",border=0)

        self.char_name = Label(self.cast_Frame,text=f"{role}",font=("Arial",14,"normal"),bg="#6e051c",fg="#cbeff2")
        self.char_name_entry = Entry(self.cast_Frame, font=("Arial", 13, "normal"), relief=GROOVE,bg="#ffffff",border=0)

        self.about_cast = Label(self.cast_Frame,text="About : ",font=("Arial",14,"normal"),bg="#6e051c",fg="#cbeff2")
        self.about_cast_entry = Text(self.cast_Frame, font=("Arial", 13, "normal"), relief=GROOVE,bg="#ffffff",border=0)

        self.next_img = ImageTk.PhotoImage(Image.open("actor.png").resize((150,150)))
        self.next = Button(self.cast_Frame,image=self.next_img,font=("Arial",16,"bold"),bg="#570416",border=0,relief=FLAT,activebackground="#570416")
        self.next.bind("<Button-1>",self.upload_actor)
        # self.next.bind("<Button-1>",self.cast)

        self.submit = Button(self.cast_Frame, text="Submit", font=("Arial", 11, "normal"), fg="White",bg="#570416", border=0, relief=SOLID)
        # self.submit.bind("<Button-1>",lambda x: self.add_new_circle(x,self.cast_name_entry.get(),self.upload_c,self.x_cast_image,self.y_cast_image))
        self.submit.bind("<Button-1>",self.db_upload)
        if name == "Cast":
            if self.here_data != 0 :
                self.crew_cast()
            self.cast_label.place(x=250,y=10)
            self.cast_name.place(x=230,y=70)
            self.cast_name_entry.place(x=350, y=75, width=180)
            self.char_name.place(x=250,y=115)
            self.char_name_entry.place(x=350, y=120, width=180)
            self.about_cast.place(x=270,y=160)
            self.about_cast_entry.place(x=350, y=165, width=180,height=110)
            self.next.place(x=30,y=90)
            self.submit.place(x=400, y=300)
            self.cast_options_frame.place_forget()
            self.default.place_forget()
            self.here_data += 1
        elif name == "Crew":
            if self.here_data != 0 : 
                self.crew_cast()
            self.cast_label.place(x=250,y=10)
            self.cast_name.place(x=230,y=70)
            self.cast_name_entry.place(x=350, y=75, width=180)
            self.char_name.place(x=280,y=115)
            self.char_name_entry.place(x=350, y=120, width=180)
            self.about_cast.place(x=270,y=160)
            self.about_cast_entry.place(x=350, y=165, width=180,height=110)
            self.next.place(x=30,y=90)
            self.submit.place(x=400, y=300)
            self.cast_options_frame.place_forget()
            self.default.place_forget()
            self.here_data += 1
    def crew_cast(self):
        print("I am here")
        for widget in self.cast_Frame.winfo_children():
            if widget.winfo_exists():
                widget.place_forget()
        self.default.place(x=180,y=120)

        print(self.here_data)


    def db_upload(self,event):
        print("yes i am running i am cast added ")
        self.cast_db_li = [self.movie_name_entry.get(),self.cast_name_entry.get(),self.char_name_entry.get(),self.about_cast_entry.get("1.0",END),self.upload_c]
        if self.cast_db_li[1] == "":
            messagebox.showerror("Value Missing","Required Cast Name")
        elif self.cast_db_li[2] == "":
            messagebox.showerror("Value Missing","Charcter Column Empty")
        elif self.cast_db_li[3] == "":
            messagebox.showerror("Value Missing","Required About")
        elif self.cast_db_li[4] == "":
            messagebox.showerror("Value Missing","Required Image")
        else :
            self.add_new_circle(self.cast_name_entry.get(),self.upload_c,self.x_cast_image,self.y_cast_image)
            cast_db_store = Database_store.cast(tuple(self.cast_db_li))
            print(cast_db_store)
            messagebox.showinfo("Sucess","Done")
 

    def add_new_circle(self,name,imgs,x_img,y_img,movie="x"):

        label = Label(self.inner_frame,border=0)
        label.place(x=x_img+120,y=y_img)
        img = Image.open(imgs).convert("RGBA")
        mask = Image.new("L",(80,80),0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0,0,80,80),fill=255)
        img = img.resize((80,80))
        sq_mask = Image.new("RGBA",(100,100),(0,0,0,0))
        sq_mask.paste(img,(0,0),mask=mask)
        bg = Image.new("RGBA",(80,80),"#570416")
        bg.paste(sq_mask,(0,0),sq_mask)
        orignal_img = ImageTk.PhotoImage(bg)
        label.config(image=orignal_img)
        label.image = orignal_img
        self.crew_cast()

        cast_name = Label(self.inner_frame,text=name.replace(" ","\n"),font=("Arial",13,"bold"),bg="#570416",fg="white")
        if len(name) > 7:
            cast_name.place(x=self.x_cast_image+120,y=1110)
        elif len(name) == 6 :
            cast_name.place(x=self.x_cast_image+130,y=1110)
        elif len(name) == 5 :
            cast_name.place(x=self.x_cast_image+135,y=1110)
        elif len(name) == 4 :
            cast_name.place(x=self.x_cast_image+138,y=1110)
        elif len(name) == 3 :
            cast_name.place(x=self.x_cast_image+140,y=1110)
        else:
            cast_name.place(x=self.x_cast_image+140,y=1110)


        self.x_cast_image = self.x_cast_image+120


         


    def upload_actor(self,event):
        self.upload_c = filedialog.askopenfilename()
        if self.upload_c:
            self.orignal_actor = ImageTk.PhotoImage(Image.open(self.upload_c).resize((150,150)))
            self.next.config(image=self.orignal_actor)
            print(self.upload_c)
            return self.upload_c
            # self.next(x=0,y=0)
        else:
            messagebox.showwarning("Error","File Upload Error")

    def gen_frame(self):


        self.circle_gen(5, 10, "Action", self.action_cond,"gen")
        self.circle_gen(5, 45, "Animation", self.animation_cond,"gen")
        self.circle_gen(5, 80, "Biography", self.biographiy_cond,"gen")
        self.circle_gen(5, 115, "Comedy", self.comdy_cond,"gen")
        self.circle_gen(5, 150, "Drama", self.drama_cond,"gen")
        self.circle_gen(5, 185, "Family", self.family_cond,"gen")
        self.circle_gen(5, 220, "Fantsy", self.fantsy_cond,"gen")
        self.circle_gen(5, 255, "Historical", self.historical_cond,"gen")
        self.circle_gen(160, 10, "Horror", self.horror_cond,"gen")
        self.circle_gen(160, 45, "Musical", self.musical_cond,"gen")
        self.circle_gen(160, 80, "Mystery", self.mystery_cond,"gen")
        self.circle_gen(160, 115, "Romantic", self.romantic_cond,"gen")
        self.circle_gen(160, 150, "Sci-Fi", self.sci_fi_cond,"gen")
        self.circle_gen(160, 185, "Thiller", self.thiller_cond,"gen")
        self.circle_gen(160, 220, "War", self.war_cond,"gen")
        self.circle_gen(160, 255, "Other", self.oth_gen_cond,"gen")


    def circle_lang(self, xx, yy, lang_name, cond):
        if cond:
            image = ImageTk.PhotoImage(Image.open("black_circle.png").resize((10, 10)))
        else:
            image = self.hindi_whit

        self.lang_circle = Label(self.inner_frame, image=image, bg="#570416")
        self.lang_circle.image = image  # Keep a reference to avoid garbage collection
        self.lang_circle.place(x=xx, y=yy)
        self.lang_circle.bind("<Button-1>", lambda x: self.language_circle_change(lang_name))
        
        self.lang_label = Label(self.inner_frame, text=lang_name, font=("Arial", 13, "bold"), fg="white", bg="#570416")
        self.lang_label.place(x=xx + 17, y=yy - 7)

    def language_circle_change(self, lang_name):
        if lang_name == "English":
            self.eng_cond = not self.eng_cond
        elif lang_name == "Punjabi":
            self.pun_cond = not self.pun_cond
        elif lang_name == "Malayalam":
            self.mar_cond=not self.mar_cond
        elif lang_name == "Telegu":
            self.tel_cond=not self.tel_cond
        elif lang_name == "Tamil":
            self.ben_cond=not self.ben_cond
        elif lang_name == "Kannada":
            self.guj_cond=not self.guj_cond
        elif lang_name=="Hindi":
            self.hin_cond = not self.hin_cond
        else:
            self.oth_cond = not self.oth_cond
        
        if lang_name in self.lang_li:
            self.lang_li.remove(lang_name)
        else: 
            self.lang_li.append(lang_name)
        self.update_language_selection()

    def update_language_selection(self):
        self.circle_lang(568, 207, "English", self.eng_cond)
        self.circle_lang(568, 235, "Hindi", self.hin_cond)
        self.circle_lang(568, 261, "Punjabi", self.pun_cond)
        self.circle_lang(568, 286, "Malayalam", self.mar_cond)

        self.circle_lang(700, 207, "Telegu", self.tel_cond)
        self.circle_lang(700, 235, "Tamil", self.ben_cond)
        self.circle_lang(700, 261, "Kannada", self.guj_cond)
        self.circle_lang(700, 286, "Other", self.oth_cond)

       

        print(self.lang_li)
        
    def circle_gen(self, xx, yy, lang_name, cond,ty):
        if cond:
            image = ImageTk.PhotoImage(Image.open("check.png").resize((10, 10)))
        else:
            image =  self.hindi_whit

        self.lang_circle = Label(self.frame_gen, image=image)
        self.lang_circle.image = image  # Keep a reference to avoid garbage collection
        self.lang_circle.place(x=xx, y=yy+8)
        self.lang_circle.bind("<Button-1>", lambda x: self.gen_circle_change(lang_name,ty))
        
        self.lang_label = Button(self.frame_gen, text=lang_name, font=("Arial", 13, "normal"), fg="black", bg="#ffffff",bd=0, activebackground="#ffffff")
        self.lang_label.place(x=xx+15, y=yy-2)  

    def gen_circle_change(self, gen_name,ty):
        if gen_name == "Action":
            self.action_cond = not self.action_cond
        elif gen_name == "Animation":
            self.animation_cond = not self.animation_cond
        elif gen_name == "Biography":
            self.biographiy_cond=not self.biographiy_cond
        elif gen_name == "Comedy":
            self.comdy_cond=not self.comdy_cond
        elif gen_name == "Drama":
            self.drama_cond=not self.drama_cond
        elif gen_name == "Family":
            self.family_cond=not self.family_cond
        elif gen_name=="Fantsy":
            self.fantsy_cond = not self.fantsy_cond
        elif gen_name=="Historical":
            self.historical_cond = not self.historical_cond
        elif gen_name=="Horror":
            self.horror_cond = not self.horror_cond
        elif gen_name=="Musical":
            self.musical_cond = not self.musical_cond
        elif gen_name=="Mystery":
            self.mystery_cond = not self.mystery_cond
        elif gen_name=="Romantic":
            self.romantic_cond = not self.romantic_cond
        elif gen_name=="Sci-Fi":
            self.sci_fi_cond = not self.sci_fi_cond
        elif gen_name=="Thiller":
            self.thiller_cond = not self.thiller_cond

        elif gen_name=="Amritsar":
            self.Amritsar= self.Barnala= self.Bathinda= self.Faridkot= self.Fatehgarh_Sahib= self.Fazilka= self.Ferozepur=self.Gurdaspur= self.Hoshiarpur= self.Jalandhar= self.Kapurthala= self.Ludhiana= self.Mansa= self.Moga= self.Pathankot=self.Patiala=self.Ropar=self.Mohali= self.Sangrur=self.Shahid_Bhagat_Singh_Nagar= self.Sri_Muktsar_Sahib= self.Tarn_Taran = False
            self.Amrisar = not self.Amritsar 
        elif gen_name=="Barnala":
            self.Amritsar= self.Barnala= self.Bathinda= self.Faridkot= self.Fatehgarh_Sahib= self.Fazilka= self.Ferozepur=self.Gurdaspur= self.Hoshiarpur= self.Jalandhar= self.Kapurthala= self.Ludhiana= self.Mansa= self.Moga= self.Pathankot=self.Patiala=self.Ropar=self.Mohali= self.Sangrur=self.Shahid_Bhagat_Singh_Nagar= self.Sri_Muktsar_Sahib= self.Tarn_Taran = False
            self.Barnala = not self.Barnala 
        elif gen_name=="Bathinda":
            self.Amritsar= self.Barnala= self.Bathinda= self.Faridkot= self.Fatehgarh_Sahib= self.Fazilka= self.Ferozepur=self.Gurdaspur= self.Hoshiarpur= self.Jalandhar= self.Kapurthala= self.Ludhiana= self.Mansa= self.Moga= self.Pathankot=self.Patiala=self.Ropar=self.Mohali= self.Sangrur=self.Shahid_Bhagat_Singh_Nagar= self.Sri_Muktsar_Sahib= self.Tarn_Taran = False
            self.Bathinda = not self.Bathinda 
        elif gen_name=="Faridkot":
            self.Amritsar= self.Barnala= self.Bathinda= self.Faridkot= self.Fatehgarh_Sahib= self.Fazilka= self.Ferozepur=self.Gurdaspur= self.Hoshiarpur= self.Jalandhar= self.Kapurthala= self.Ludhiana= self.Mansa= self.Moga= self.Pathankot=self.Patiala=self.Ropar=self.Mohali= self.Sangrur=self.Shahid_Bhagat_Singh_Nagar= self.Sri_Muktsar_Sahib= self.Tarn_Taran = False
            self.Faridkot = not self.Faridkot 
        elif gen_name=="Fatehgarh Sahib":
            self.Amritsar= self.Barnala= self.Bathinda= self.Faridkot= self.Fatehgarh_Sahib= self.Fazilka= self.Ferozepur=self.Gurdaspur= self.Hoshiarpur= self.Jalandhar= self.Kapurthala= self.Ludhiana= self.Mansa= self.Moga= self.Pathankot=self.Patiala=self.Ropar=self.Mohali= self.Sangrur=self.Shahid_Bhagat_Singh_Nagar= self.Sri_Muktsar_Sahib= self.Tarn_Taran = False
            self.Fatehgarh_Sahib = not self.Fatehgarh_Sahib 
        elif gen_name=="Fazilka":
            self.Amritsar= self.Barnala= self.Bathinda= self.Faridkot= self.Fatehgarh_Sahib= self.Fazilka= self.Ferozepur=self.Gurdaspur= self.Hoshiarpur= self.Jalandhar= self.Kapurthala= self.Ludhiana= self.Mansa= self.Moga= self.Pathankot=self.Patiala=self.Ropar=self.Mohali= self.Sangrur=self.Shahid_Bhagat_Singh_Nagar= self.Sri_Muktsar_Sahib= self.Tarn_Taran = False
            self.Fazilka = not self.Fazilka
        elif gen_name=="Ferozepur":
            self.Amritsar= self.Barnala= self.Bathinda= self.Faridkot= self.Fatehgarh_Sahib= self.Fazilka= self.Ferozepur=self.Gurdaspur= self.Hoshiarpur= self.Jalandhar= self.Kapurthala= self.Ludhiana= self.Mansa= self.Moga= self.Pathankot=self.Patiala=self.Ropar=self.Mohali= self.Sangrur=self.Shahid_Bhagat_Singh_Nagar= self.Sri_Muktsar_Sahib= self.Tarn_Taran = False
            self.Ferozepur = not self.Ferozepur 
        elif gen_name=="Gurdaspur":
            self.Amritsar= self.Barnala= self.Bathinda= self.Faridkot= self.Fatehgarh_Sahib= self.Fazilka= self.Ferozepur=self.Gurdaspur= self.Hoshiarpur= self.Jalandhar= self.Kapurthala= self.Ludhiana= self.Mansa= self.Moga= self.Pathankot=self.Patiala=self.Ropar=self.Mohali= self.Sangrur=self.Shahid_Bhagat_Singh_Nagar= self.Sri_Muktsar_Sahib= self.Tarn_Taran = False
            self.Gurdaspur = not self.Gurdaspur 
        elif gen_name=="Hoshiarpur":
            self.Amritsar= self.Barnala= self.Bathinda= self.Faridkot= self.Fatehgarh_Sahib= self.Fazilka= self.Ferozepur=self.Gurdaspur= self.Hoshiarpur= self.Jalandhar= self.Kapurthala= self.Ludhiana= self.Mansa= self.Moga= self.Pathankot=self.Patiala=self.Ropar=self.Mohali= self.Sangrur=self.Shahid_Bhagat_Singh_Nagar= self.Sri_Muktsar_Sahib= self.Tarn_Taran = False
            self.Hoshiarpur = not self.Hoshiarpur
        elif gen_name=="Jalandhar":
            self.Amritsar= self.Barnala= self.Bathinda= self.Faridkot= self.Fatehgarh_Sahib= self.Fazilka= self.Ferozepur=self.Gurdaspur= self.Hoshiarpur= self.Jalandhar= self.Kapurthala= self.Ludhiana= self.Mansa= self.Moga= self.Pathankot=self.Patiala=self.Ropar=self.Mohali= self.Sangrur=self.Shahid_Bhagat_Singh_Nagar= self.Sri_Muktsar_Sahib= self.Tarn_Taran = False
            self.Jalandhar = not self.Jalandhar
        elif gen_name=="Kapurthala":
            self.Amritsar= self.Barnala= self.Bathinda= self.Faridkot= self.Fatehgarh_Sahib= self.Fazilka= self.Ferozepur=self.Gurdaspur= self.Hoshiarpur= self.Jalandhar= self.Kapurthala= self.Ludhiana= self.Mansa= self.Moga= self.Pathankot=self.Patiala=self.Ropar=self.Mohali= self.Sangrur=self.Shahid_Bhagat_Singh_Nagar= self.Sri_Muktsar_Sahib= self.Tarn_Taran = False
            self.Kapurthala = not self.Kapurthala
        elif gen_name=="Ludhiana":
            self.Amritsar= self.Barnala= self.Bathinda= self.Faridkot= self.Fatehgarh_Sahib= self.Fazilka= self.Ferozepur=self.Gurdaspur= self.Hoshiarpur= self.Jalandhar= self.Kapurthala= self.Ludhiana= self.Mansa= self.Moga= self.Pathankot=self.Patiala=self.Ropar=self.Mohali= self.Sangrur=self.Shahid_Bhagat_Singh_Nagar= self.Sri_Muktsar_Sahib= self.Tarn_Taran = False
            self.Ludhiana = not self.Ludhiana
        elif gen_name=="Mansa":
            self.Amritsar= self.Barnala= self.Bathinda= self.Faridkot= self.Fatehgarh_Sahib= self.Fazilka= self.Ferozepur=self.Gurdaspur= self.Hoshiarpur= self.Jalandhar= self.Kapurthala= self.Ludhiana= self.Mansa= self.Moga= self.Pathankot=self.Patiala=self.Ropar=self.Mohali= self.Sangrur=self.Shahid_Bhagat_Singh_Nagar= self.Sri_Muktsar_Sahib= self.Tarn_Taran = False
            self.Mansa = not self.Mansa
        elif gen_name=="Moga":
            self.Amritsar= self.Barnala= self.Bathinda= self.Faridkot= self.Fatehgarh_Sahib= self.Fazilka= self.Ferozepur=self.Gurdaspur= self.Hoshiarpur= self.Jalandhar= self.Kapurthala= self.Ludhiana= self.Mansa= self.Moga= self.Pathankot=self.Patiala=self.Ropar=self.Mohali= self.Sangrur=self.Shahid_Bhagat_Singh_Nagar= self.Sri_Muktsar_Sahib= self.Tarn_Taran = False
            self.Moga = not self.Moga
        elif gen_name=="Pathankot":
            self.Amritsar= self.Barnala= self.Bathinda= self.Faridkot= self.Fatehgarh_Sahib= self.Fazilka= self.Ferozepur=self.Gurdaspur= self.Hoshiarpur= self.Jalandhar= self.Kapurthala= self.Ludhiana= self.Mansa= self.Moga= self.Pathankot=self.Patiala=self.Ropar=self.Mohali= self.Sangrur=self.Shahid_Bhagat_Singh_Nagar= self.Sri_Muktsar_Sahib= self.Tarn_Taran = False
            self.Pathankot = not self.Pathankot 
        elif gen_name=="Patiala":
            self.Amritsar= self.Barnala= self.Bathinda= self.Faridkot= self.Fatehgarh_Sahib= self.Fazilka= self.Ferozepur=self.Gurdaspur= self.Hoshiarpur= self.Jalandhar= self.Kapurthala= self.Ludhiana= self.Mansa= self.Moga= self.Pathankot=self.Patiala=self.Ropar=self.Mohali= self.Sangrur=self.Shahid_Bhagat_Singh_Nagar= self.Sri_Muktsar_Sahib= self.Tarn_Taran = False
            self.Patiala = not self.Patiala
        elif gen_name=="Ropar":
            self.Amritsar= self.Barnala= self.Bathinda= self.Faridkot= self.Fatehgarh_Sahib= self.Fazilka= self.Ferozepur=self.Gurdaspur= self.Hoshiarpur= self.Jalandhar= self.Kapurthala= self.Ludhiana= self.Mansa= self.Moga= self.Pathankot=self.Patiala=self.Ropar=self.Mohali= self.Sangrur=self.Shahid_Bhagat_Singh_Nagar= self.Sri_Muktsar_Sahib= self.Tarn_Taran = False
            self.Ropar = not self.Ropar
        elif gen_name=="Mohali":
            self.Amritsar= self.Barnala= self.Bathinda= self.Faridkot= self.Fatehgarh_Sahib= self.Fazilka= self.Ferozepur=self.Gurdaspur= self.Hoshiarpur= self.Jalandhar= self.Kapurthala= self.Ludhiana= self.Mansa= self.Moga= self.Pathankot=self.Patiala=self.Ropar=self.Mohali= self.Sangrur=self.Shahid_Bhagat_Singh_Nagar= self.Sri_Muktsar_Sahib= self.Tarn_Taran = False
            self.Mohali = not self.Mohali
        elif gen_name=="Sangrur":
            self.Amritsar= self.Barnala= self.Bathinda= self.Faridkot= self.Fatehgarh_Sahib= self.Fazilka= self.Ferozepur=self.Gurdaspur= self.Hoshiarpur= self.Jalandhar= self.Kapurthala= self.Ludhiana= self.Mansa= self.Moga= self.Pathankot=self.Patiala=self.Ropar=self.Mohali= self.Sangrur=self.Shahid_Bhagat_Singh_Nagar= self.Sri_Muktsar_Sahib= self.Tarn_Taran = False
            self.Sangrur = not self.Sangrur
        elif gen_name=="Shahid Bhagat Singh Nagar":
            self.Amritsar= self.Barnala= self.Bathinda= self.Faridkot= self.Fatehgarh_Sahib= self.Fazilka= self.Ferozepur=self.Gurdaspur= self.Hoshiarpur= self.Jalandhar= self.Kapurthala= self.Ludhiana= self.Mansa= self.Moga= self.Pathankot=self.Patiala=self.Ropar=self.Mohali= self.Sangrur=self.Shahid_Bhagat_Singh_Nagar= self.Sri_Muktsar_Sahib= self.Tarn_Taran = False
            self.Shahid_Bhagat_Singh_Nagar = not self.Shahid_Bhagat_Singh_Nagar 
        elif gen_name=="Sri Muktsar Sahib":
            self.Amritsar= self.Barnala= self.Bathinda= self.Faridkot= self.Fatehgarh_Sahib= self.Fazilka= self.Ferozepur=self.Gurdaspur= self.Hoshiarpur= self.Jalandhar= self.Kapurthala= self.Ludhiana= self.Mansa= self.Moga= self.Pathankot=self.Patiala=self.Ropar=self.Mohali= self.Sangrur=self.Shahid_Bhagat_Singh_Nagar= self.Sri_Muktsar_Sahib= self.Tarn_Taran = False
            self.Sri_Muktsar_Sahib = not self.Sri_Muktsar_Sahib 
        elif gen_name=="Tarn Taran":
            self.Amritsar= self.Barnala= self.Bathinda= self.Faridkot= self.Fatehgarh_Sahib= self.Fazilka= self.Ferozepur=self.Gurdaspur= self.Hoshiarpur= self.Jalandhar= self.Kapurthala= self.Ludhiana= self.Mansa= self.Moga= self.Pathankot=self.Patiala=self.Ropar=self.Mohali= self.Sangrur=self.Shahid_Bhagat_Singh_Nagar= self.Sri_Muktsar_Sahib= self.Tarn_Taran = False
            self.Tarn_Taran = not self.Tarn_Taran 
        else:
            self.oth_cond = not self.oth_cond
            

    # for i in :


        self.select_btn.config(text=self.gen_tu)
        self.select_btn.config(fg="black")
        
        if ty == "gen":
            if gen_name in self.gen_tu:
                self.gen_tu.remove(gen_name)
            else:
                self.gen_tu.append(gen_name)
            self.select_btn.config(text=self.gen_tu)
            self.select_btn.config(fg="black")
            self.update_genre_selection()
        else:
            # if gen_name in self.gen_tu:
            self.gen_tu.clear()
            self.gen_tu.append(gen_name)

            self.select_btn.config(text=self.gen_tu)
            self.select_btn.config(fg="black")
            self.update_choose_distt()
    
    def update_choose_distt(self):
        # print(self.Amrisar)
        self.dist_list = [self.Amritsar, self.Barnala, self.Bathinda, self.Faridkot, self.Fatehgarh_Sahib, self.Fazilka, self.Ferozepur,self.Gurdaspur, self.Hoshiarpur, self.Jalandhar, self.Kapurthala, self.Ludhiana, self.Mansa, self.Moga, self.Pathankot,self.Patiala,self.Ropar,self.Mohali, self.Sangrur,self.Shahid_Bhagat_Singh_Nagar, self.Sri_Muktsar_Sahib, self.Tarn_Taran ]
        print(self.dist_list)

        left_counter = 1
        right_counter = 1
        count = 10
        index = 0 

        while index < len(self.districts):
            i = self.districts[index]
            j = range(count, 386, 35)[index % len(range(count, 386, 35))]  # Adjust j using count and wrap around with modulus
            k = self.dist_list[index]
            
            if left_counter < 12:
                self.circle_gen(5, j, i, k,"cin")
                left_counter += 1
                # print(i,k) 
            else:
                self.circle_gen(160, j, i, k,"cin")
                right_counter += 1
            
            if j == 385:
                count = 10  

            index += 1  

    def update_genre_selection(self):
        self.circle_gen(5, 10, "Action", self.action_cond,"gen")
        self.circle_gen(5, 45, "Animation", self.animation_cond,"gen")
        self.circle_gen(5, 80, "Biography", self.biographiy_cond,"gen")
        self.circle_gen(5, 115, "Comedy", self.comdy_cond,"gen")
        self.circle_gen(5, 150, "Drama", self.drama_cond,"gen")
        self.circle_gen(5, 185, "Family", self.family_cond,"gen")
        self.circle_gen(5, 220, "Fantsy", self.fantsy_cond,"gen")
        self.circle_gen(5, 255, "Historical", self.historical_cond,"gen")
        self.circle_gen(160, 10, "Horror", self.horror_cond,"gen")
        self.circle_gen(160, 45, "Musical", self.musical_cond,"gen")
        self.circle_gen(160, 80, "Mystery", self.mystery_cond,"gen")
        self.circle_gen(160, 115, "Romantic", self.romantic_cond,"gen")
        self.circle_gen(160, 150, "Sci-Fi", self.sci_fi_cond,"gen")
        self.circle_gen(160, 185, "Thiller", self.thiller_cond,"gen")
        self.circle_gen(160, 220, "War", self.war_cond,"gen")
        self.circle_gen(160, 255, "Other", self.oth_gen_cond,"gen")
    

    def addmovie(self,event):
        print("Yes Access")
    
    def focusin(self,event,name,placeholder):
        if name.get() == placeholder:
            username = event.widget
            username.delete(0, END)  # Clear the text field
            username.config(fg="#000000") 

        

    def focusout(self, event,placeholder):
        username = event.widget
        if not username.get():  # Check if the field is empty
            username.insert(0, placeholder)  # Insert placeholder text
            username.config(fg="#bd8080") 



    def upload_file(self,event):
        self.upload = filedialog.askopenfilename()
        if self.upload:
            # print(self.upload)
            self.orignal_poster = ImageTk.PhotoImage(Image.open(self.upload).resize((250,300)))
            self.local_frame.config(image=self.orignal_poster)
            # self.local_frame(x=0,y=0)
        else:
            messagebox.showwarning("Error","File Upload Error")

    def upload_Banner(self,event):
        self.upload_b = filedialog.askopenfilename()
        if self.upload_b:
            self.movie_banner_btn.config(text=self.upload_b)
            self.movie_banner_btn.config(width=45)
            self.movie_banner_btn.config(anchor=NW)          
            self.upload_bnr = self.upload_t.replace("/","//")  
            print(self.upload_t) 

    def upload_Triler(self,event):
        self.upload_t = filedialog.askopenfilename()
        if self.upload_t:
            self.Trailer_img.destroy()
            self.Trailer_Frame.config(bg="black")
            self.Trailer_Entry.config(text=self.upload_t)
            self.Trailer_Entry.config(width=45)
            self.Trailer_Entry.config(anchor=NW)          
            self.upload_tr = self.upload_t.replace("/","//")  
            print(self.upload_t) 
            print(self.date.get())


            self.play_btns = ImageTk.PhotoImage(Image.open("YT.png").resize((90,60)))
            self.play_btn = Label(self.Trailer_Frame,image=self.play_btns,bg="black")
            self.play_btn.place(x=150,y=85)
            self.play_btn.bind("<Button-1>",self.play_pause)

            
        else:
            messagebox.showwarning("Error","File Upload Error")

    def play_pause(self,event):
        self.vlc = f"vlc \"{self.upload_t}\"".replace("/","\\")
        print(self.vlc)
        run(self.vlc ,shell=True).stdout


    def db_send_new_movie(self):

        self.db_data=[self.movie_name_entry.get(),(((((str(self.lang_li)).replace("[","")).replace(","," / ")).replace("]","")).replace("'","")),(((((str(self.gen_tu)).replace("[","")).replace(","," / ")).replace("]","")).replace("'","")),self.date.get(),self.about_Entry.get("1.0",END),self.upload_t,self.rating_entry.get(),self.upload,self.movie_time_entry.get(),self.upload_b]

        # print(self.db_data[4])
        if self.db_data[0] == "Enter the Movie Name " :
            messagebox.showerror("Value Error","Movie Name Missing")
        elif not self.db_data[1]  :
            messagebox.showerror("Value Error","Language not selected")
        elif not self.db_data[2]  :
            messagebox.showerror("Value Error","Genres not selected")
        elif self.db_data[3] == "yyyy/mm/dd"+(str(date.today())).replace("-","/") :
            messagebox.showerror("Value Error","Date invalid")     
        elif self.db_data[4] == "\n" :
            messagebox.showerror("Value Error","About Empty ")
        elif self.db_data[5] == "" :
            messagebox.showerror("Value Error","Trailer not Uploaded ")
        elif self.db_data[6] == "":
            messagebox.showerror("Value Error","Rating not Given ")
        elif self.db_data[6] < "11":
            messagebox.showerror("Value Error","Rating not valid ")
        elif self.db_data[7] == "" :
            messagebox.showerror("Value Error"," Poster not Uploaded ")
        elif self.db_data[8] == "In Mintues"  :
            messagebox.showerror("Value Error"," Movie Time Missing ")
        elif self.db_data[9] == "" :
            messagebox.showerror("Value Error","Banner not Uploaded ")
        else: 
            store = Database_store.new_movie_upload(tuple(self.db_data))
            if store == True:
                print(store)
                messagebox.showinfo("Sucess","Uploaded ")
                # admin_handle.admin_Edit.homepage_setting(self)
            elif store == "exist":
                messagebox.showerror("Error","Already Uploaded ")
            else:
                messagebox.showerror("Error","Unexpected Value ")

    def db_send_upcoming_movie(self):
        # self.db_data=[self.movie_name_entry,self.lang_li,self.gen_tu,self.date,self.about_Entry,self.upload_t,self.rating_entry,self.upload]
        self.db_upcoming_data=[self.movie_name_entry.get(),  (((((str(self.lang_li)).replace("[","")).replace(","," / ")).replace("]","")).replace("'","")),   (((((str(self.gen_tu)).replace("[","")).replace(","," / ")).replace("]","")).replace("'","")),   self.date.get()   ,self.about_Entry.get("1.0",END)   ,self.upload_t   ,self.upload   ,self.movie_time_entry.get(),   self.upload_b]

        # print(self.db_data[4])
        if self.db_upcoming_data[0] == "Enter the Movie Name " :
            messagebox.showerror("Value Error","Movie Name Missing")
        elif not self.db_upcoming_data[1]  :
            messagebox.showerror("Value Error","Language not selected")
        elif not self.db_upcoming_data[2]  :
            messagebox.showerror("Value Error","Genres not selected")
        elif self.db_upcoming_data[3] == "yyyy/mm/dd"+(str(date.today())).replace("-","/") :
            messagebox.showerror("Value Error","Date invalid")     
        elif self.db_upcoming_data[4] == "\n" :
            messagebox.showerror("Value Error","About Empty ")
        elif self.db_upcoming_data[5] == "" :
            messagebox.showerror("Value Error","Trailer not Uploaded ")
        elif self.db_upcoming_data[6] == "" :
            messagebox.showerror("Value Error"," Poster not Uploaded ")
        elif self.db_upcoming_data[7] == "In Mintues "  :
            messagebox.showerror("Value Error"," Movie Time Missing ")
        elif self.db_upcoming_data[8] == "" :
            messagebox.showerror("Value Error","Banner not Uploaded ")

        else: 
            store = Database_store.upcoming_movie_upload(tuple(self.db_upcoming_data))
            if store == True:
                print(store)
                messagebox.showinfo("Sucess","Uploaded ")
            elif store == "exist":
                messagebox.showerror("Error","Already Uploaded ")
            else:
                messagebox.showerror("Error","Unexpected Value ")
    
    
    def nofication_enable(self):
        self.store_all_up = Database_store.upcoming_movie_show()
        self.noti_li = []
        for i in range(len(self.store_all_up)):

            if self.store_all_up[i][4] == date.today():
                self.noti_li.append(self.store_all_up[i][1])
                
            else:
                print("Not found any date")
        return self.noti_li
                


        
 

if __name__ == "__main__":
    admin = admin_Edit((True,"Amandeep Kaur","Amandeep02@gmail.com"),"A")
    # print("yyyy/mm/dd"+(str(date.today())).replace("-","/"))
