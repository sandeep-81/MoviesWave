from tkinter import *
from datetime import date 
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk,ImageDraw
from tkinter import filedialog
from tkcalendar import DateEntry 
import Database_store
from subprocess import *
import calendar
import smtplib  
from email.message import EmailMessage
import random 


class update_scr:
    def __init__(self,movie_name,upnew):
            
            self.main = Tk()
            self.main.title(f"{movie_name}")
            self.main.attributes("-topmost",True)


            
            window_width = 600
            window_height = 600

            # Get the screen width and height
            screen_width = self.main.winfo_screenwidth()
            screen_height = self.main.winfo_screenheight()

            # Calculate the position to center the window
            position_x = int((screen_width / 2) - (window_width / 2)) + 70
            position_y = int((screen_height / 2) - (window_height / 2)) + 30

            self.main.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

            self.upnew = upnew

            
############################################################################################################################
############################################################################################################################
            self.upload_p = ""
            self.upload_b = ""
            self.upload_t = ""

            self.movie_name_para = movie_name

            self.store = Database_store.particular_movie_show(movie_name,upnew)

            self.movie_name = self.store[0][1]
            self.movie_lang = self.store[0][2]
            self.movie_gen = self.store[0][3]
            self.movie_date = [str(self.store[0][4])[i] for i in range(10)]
            print("".join(self.movie_date))
            self.movie_about = self.store[0][5]
            self.movie_tr = self.store[0][6]
            if upnew == "latest":
                self.movie_rate = self.store[0][7]
                self.movie_pos = self.store[0][8]
                self.movie_time = self.store[0][9]
                self.movie_ban = self.store[0][10]
            else:
                # self.movie_rate = self.store[0][7]
                self.movie_pos = self.store[0][7]
                self.movie_time = self.store[0][8]
                self.movie_ban = self.store[0][9]



            self.upload_t = self.store[0][6]
            self.upload_p = self.store[0][8]
            self.upload_b = self.store[0][9]






############################################################################################################################
############################################################################################################################

            self.canvas = Frame(self.main, bg='#570416', bd=5)
            self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER, width=600, height=600)

            self.scrollbar = Scrollbar(self.canvas, orient="vertical")
            self.scrollbar.pack(side=RIGHT, fill=Y)

            self.form_frame = Canvas(self.canvas,bg='#570416', yscrollcommand=self.scrollbar.set)
            self.form_frame.pack(side="left", fill="both", expand=True)


            self.scrollbar.config(command=self.form_frame.yview)

            # Create an inner frame inside the Canvas
            self.inner_frame = Frame(self.form_frame, bg='#570416')


            # Add the inner frame to the Canvas
            self.form_frame.create_window((0, 0), window=self.inner_frame, anchor="nw")




            self.update_frame = Frame(self.inner_frame,height=700,width=600,bg="#570416")
            self.update_frame.place(x=0,y=0)

            Label(self.update_frame,text=f"Update {movie_name}",font=("jokerman",18),fg="white",bg="#570416").place(x=180,y=10)

            Label(self.update_frame,text="Movie Poster : ",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=30,y=70)
            self.movie_poster = Button(self.update_frame,text=self.movie_pos,font=("Arial", 9),width=32,height=1)
            self.movie_poster.place(x=165,y=73)
            self.movie_poster.bind("<Button-1>",lambda x:self.upload_Banner(x,self.movie_poster))

            Label(self.update_frame,text="Movie Name : ",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=30,y=120)
            self.movie_name_ori = Entry(self.update_frame,width=25,font=("Arial",12))
            self.movie_name_ori.place(x=165,y=123)
            self.movie_name_ori.insert(0,self.movie_name)

            
            Label(self.update_frame,text="Language : ",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=30,y=170)
            movie_lang = Entry(self.update_frame,width=25,font=("Arial",12))
            movie_lang.place(x=165,y=173)
            movie_lang.insert(0,self.movie_lang)


            Label(self.update_frame,text="Genres : ",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=30,y=220)
            movie_gen = Entry(self.update_frame,width=25,font=("Arial",12))
            movie_gen.place(x=165,y=223)
            movie_gen.insert(0,self.movie_gen)

            Label(self.update_frame,text="Release Date : ",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=30,y=270)
            self.date_var = StringVar(self.main)
            self.date = DateEntry(self.update_frame,date_pattern="yyyy/mm/dd", font=("Arial", 12),textvariable=self.date_var)
            self.date.place(x=165,y=273)
            self.date_var.set('') 
            self.date.insert(0, ("".join(self.movie_date)))

            Label(self.update_frame,text="Movie Time : ",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=30,y=320)
            self.movie_time_ori = Entry(self.update_frame,width=25,font=("Arial",12))
            self.movie_time_ori.place(x=165,y=323)
            self.movie_time_ori.insert(0,self.movie_time)

            Label(self.update_frame,text="Banner : ",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=30,y=370)
            self.movie_banner = Button(self.update_frame,text=self.movie_ban,font=("Arial", 9),width=32,height=1)
            self.movie_banner.place(x=165,y=373)
            self.movie_banner.bind("<Button-1>",lambda x:self.upload_Banner(x,self.movie_banner))
            


            Label(self.update_frame,text="About : ",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=30,y=420)
            self.movie_about_ori = Text(self.update_frame,width=25,height=6,font=("Arial",12))
            self.movie_about_ori.place(x=165,y=423)
            self.movie_about_ori.insert(1.0,self.movie_about)

            Label(self.update_frame,text="Trailer : ",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=30,y=560)
            self.movie_trailer = Button(self.update_frame,text=self.movie_tr,font=("Arial", 9),width=32,height=1)
            self.movie_trailer.place(x=165,y=563)
            self.movie_trailer.bind("<Button-1>",lambda x:self.upload_Banner(x,self.movie_trailer))

            self.submit= Button(self.update_frame,text="Submit",font=("Arial", 11),width=20,height=1,command=self.upload_data)
            # self.submit.bind("<button-1>",lambda x:self.upload_data(x,upnew))
            self.useless = Label(self.inner_frame,text="",bg="#570416")

            if upnew == "latest":
                Label(self.update_frame,text="Rating : ",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=30,y=610)
                self.movie_rating_ori = Entry(self.update_frame,width=25,font=("Arial",12))
                self.movie_rating_ori.place(x=165,y=613)
                self.movie_rating_ori.insert(0,self.movie_rate)
                self.submit.place(x=175,y=670)
                self.useless.pack(padx=560,pady=370)
            else:
                self.submit.place(x=165,y=620)
                self.useless.pack(padx=560,pady=340)




            self.form_frame.update_idletasks()
            self.form_frame.config(scrollregion=self.form_frame.bbox("all"))


            self.main.mainloop()

    def upload_Banner(self,event,btn):
            self.main.attributes("-topmost", True)

            container = filedialog.askopenfilename()
            if container:
                btn.config(text=container)
                btn.config(width=45)
                btn.config(anchor=NW)        
                  
            if btn == self.movie_poster:
                self.upload_p = container
            elif btn == self.movie_banner:
                self.upload_b = container
            elif btn == self.movie_trailer:
                 self.upload_t = container
            print(f"File uploaded: {container}")
            print("poster - ",self.upload_p)
            print("banner - ",self.upload_b)
            print("Trailer - ",self.upload_t)
             
    def upload_data(self):
            
            if self.upnew == "latest":
                self.db_data=[self.movie_name_ori.get(),self.movie_lang,self.movie_gen,self.date.get(),self.movie_about_ori.get("1.0",END),self.upload_t,self.movie_rating_ori.get(),self.upload_p,self.movie_time_ori.get(),self.upload_b,self.movie_name_para]
            else:
                self.db_data=[self.movie_name_ori.get(),self.movie_lang,self.movie_gen,self.date.get(),self.movie_about_ori.get("1.0",END),self.upload_t,self.upload_p,self.movie_time_ori.get(),self.upload_b,self.movie_name_ori.get()]
            reply = messagebox.askokcancel("Warning",f"Do You want to Update {self.movie_name_ori.get()}")
            print(reply)
            if reply==True:
                
                check=Database_store.movies_update_data(tuple(self.db_data),self.upnew)
                if check == True:
                    # admin_handle.admin_Edit.homepage_setting(self)
                    messagebox.showinfo("Sucess","Done")
                    
                    self.main.destroy()
                else:
                    messagebox.showerror("Error","Error")
            else:
                print("Not Updated")

class show_detials:
    def __init__(self,user_name,upnew):
            self.main = Tk()
            self.main.title(f"{user_name}")
            self.main.attributes("-topmost",True)


            container = Database_store.users_login(user_name)
            data_con = []
            print(container)
            for i in container:
                 data_con.append(i)
                 

            
            window_width = 350
            window_height = 350

            # Get the screen width and height
            screen_width = self.main.winfo_screenwidth()
            screen_height = self.main.winfo_screenheight()

            # Calculate the position to center the window
            position_x = int((screen_width / 2) - (window_width / 2)) +100
            position_y = int((screen_height / 2) - (window_height / 2)) +30

            self.main.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

            self.upnew = upnew


            self.update_frame = Frame(self.main,height=350,width=350,bg="#570416")
            self.update_frame.place(x=0,y=0)

            #######################################################################################################3

            
            Label(self.update_frame,text=f"Details",font=("jokerman",21),fg="white",bg="#570416").place(x=120,y=10)
            Label(self.update_frame,text=f"Name : {data_con[1]}",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=70)
            Label(self.update_frame,text=f"Email : {data_con[2]}",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=110)
            Label(self.update_frame,text=f"Contact : {data_con[3]}",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=150)
            Label(self.update_frame,text=f"Password : {data_con[4]}",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=190)
            # Label(self.update_frame,text=f"Details",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=270)


            self.submit= Button(self.update_frame,text="Ok",font=("Arial", 11),width=10,height=1,command=self.close)
            self.submit.place(x=120,y=250)


            self.main.mainloop()
    def close(self):
         self.main.destroy()

#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################


class update_cin_scr:
    def __init__(self,cinema_name,upnew):
            
            self.main = Tk()
            self.main.title(f"{cinema_name}")
            self.main.attributes("-topmost",True)

            
            window_width = 600
            window_height = 600

            # Get the screen width and height
            screen_width = self.main.winfo_screenwidth()
            screen_height = self.main.winfo_screenheight()

            # Calculate the position to center the window
            position_x = int((screen_width / 2) - (window_width / 2)) + 70
            position_y = int((screen_height / 2) - (window_height / 2)) + 30

            self.main.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

            self.upnew = upnew

            
############################################################################################################################
############################################################################################################################


            self.movie_name_para = cinema_name

            self.store = Database_store.particular_movie_show(cinema_name,upnew)

            self.cinema_name = self.store[0][1]
            self.cinema_address = self.store[0][2]
            self.cinema_road = self.store[0][3]
            self.cinema_distt = self.store[0][4]
            self.cinema_pincode = self.store[0][5]
            self.cinema_screen = self.store[0][6]

            self.cinema_seat = self.store[0][7]
            self.cinema_phone = self.store[0][8]
            self.cinema_email = self.store[0][9]
            self.cinema_open_t = self.store[0][10]
            self.cinema_close_t = self.store[0][11]



############################################################################################################################
############################################################################################################################

            self.canvas = Frame(self.main, bg='#570416', bd=5)
            self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER, width=600, height=600)

            self.scrollbar = Scrollbar(self.canvas, orient="vertical")
            self.scrollbar.pack(side=RIGHT, fill=Y)

            self.form_frame = Canvas(self.canvas,bg='#570416', yscrollcommand=self.scrollbar.set)
            self.form_frame.pack(side="left", fill="both", expand=True)


            self.scrollbar.config(command=self.form_frame.yview)

            # Create an inner frame inside the Canvas
            self.inner_frame = Frame(self.form_frame, bg='#570416')


            # Add the inner frame to the Canvas
            self.form_frame.create_window((0, 0), window=self.inner_frame, anchor="nw")




            self.update_frame = Frame(self.inner_frame,height=700,width=600,bg="#570416")
            self.update_frame.place(x=0,y=0)

            Label(self.update_frame,text=f"Update {cinema_name}",font=("jokerman",18),fg="white",bg="#570416").place(x=180,y=10)

            Label(self.update_frame,text="Cinema Name : ",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=30,y=70)
            self.cin_name = Entry(self.update_frame,font=("Arial", 12),width=25)
            self.cin_name.place(x=165,y=73)
            self.cin_name.insert(0,self.cinema_name)

            Label(self.update_frame,text="Address : ",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=30,y=120)
            self.cin_addr = Entry(self.update_frame,width=25,font=("Arial",12))
            self.cin_addr.place(x=165,y=123)
            self.cin_addr.insert(0,self.cinema_address)

            
            Label(self.update_frame,text="Road/Street : ",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=30,y=170)
            self.cin_road = Entry(self.update_frame,width=25,font=("Arial",12))
            self.cin_road.place(x=165,y=173)
            self.cin_road.insert(0,self.cinema_road)


            Label(self.update_frame,text="District : ",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=30,y=220)
            self.distt = Entry(self.update_frame,width=25,font=("Arial",12))
            self.distt.place(x=165,y=223)
            self.distt.insert(0,self.cinema_distt)

            Label(self.update_frame,text="PinCode : ",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=30,y=270)
            self.cin_pin = Entry(self.update_frame,width=25,font=("Arial",12))
            self.cin_pin.place(x=165,y=273)
            self.cin_pin.insert(0,self.cinema_pincode)
            

            Label(self.update_frame,text="Screens : ",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=30,y=320)
            self.cin_screens = Entry(self.update_frame,width=25,font=("Arial",12))
            self.cin_screens.place(x=165,y=323)
            self.cin_screens.insert(0,self.cinema_screen)
            
            Label(self.update_frame,text="Screens : ",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=30,y=370)
            self.cin_seats = Entry(self.update_frame,width=25,font=("Arial",12))
            self.cin_seats.place(x=165,y=373)
            self.cin_seats.insert(0,self.cinema_seat)


            Label(self.update_frame,text="Phone : ",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=30,y=420)
            self.cin_phone = Entry(self.update_frame,width=25,font=("Arial",12))
            self.cin_phone.place(x=165,y=423)
            self.cin_phone.insert(0,self.cinema_phone)


            Label(self.update_frame,text="Email : ",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=30,y=470)
            self.cin_email = Entry(self.update_frame,width=25,font=("Arial",12))
            self.cin_email.place(x=165,y=473)
            self.cin_email.insert(0,self.cinema_email)


            Label(self.update_frame,text="Opening Time : ",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=30,y=520)
            self.cin_open = Entry(self.update_frame,width=25,font=("Arial",12))
            self.cin_open.place(x=165,y=523)
            self.cin_open.insert(0,self.cinema_open_t)


            Label(self.update_frame,text="Closing Time : ",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=30,y=570)
            self.cin_close = Entry(self.update_frame,width=25,font=("Arial",12))
            self.cin_close.place(x=165,y=573)
            self.cin_close.insert(0,self.cinema_close_t)



            self.submit= Button(self.update_frame,text="Submit",font=("Arial", 11),width=20,height=1,command=self.upload_data)
            self.submit.place(x=165,y=630)


            self.useless = Label(self.inner_frame,text="",bg="#570416")
            self.useless.pack(padx=560,pady=340)




            self.form_frame.update_idletasks()
            self.form_frame.config(scrollregion=self.form_frame.bbox("all"))


            self.main.mainloop()


             
    def upload_data(self):
            

            self.db_data=[self.cin_name.get(),self.cin_addr.get(),self.cin_road.get(),self.distt.get(),self.cin_pin.get(),self.cin_screens.get(),self.cin_seats.get(),self.cin_phone.get(),self.cin_email.get(),self.cin_open.get(),self.cin_close.get()]
            reply = messagebox.askokcancel("Warning",f"Do You want to Update {self.cin_addr.get()}")
            print(reply)
            if reply==True:
                
                check=Database_store.movies_update_data(tuple(self.db_data),self.upnew)
                if check == True:
                    # admin_handle.admin_Edit.homepage_setting(self)
                    messagebox.showinfo("Sucess","Done")
                    
                    self.main.destroy()
                else:
                    messagebox.showerror("Error","Error")
            else:
                print("Not Updated")

class show_detials:
    def __init__(self,user_name,upnew):
            self.main = Tk()
            self.main.title(f"{user_name}")
            self.main.attributes("-topmost",True)

            container = Database_store.users_login(user_name)
            data_con = []
            print(container)
            for i in container:
                 data_con.append(i)
                 

            self.cond = False
            window_width = 350
            window_height = 350

            # Get the screen width and height
            screen_width = self.main.winfo_screenwidth()
            screen_height = self.main.winfo_screenheight()

            # Calculate the position to center the window
            position_x = int((screen_width / 2) - (window_width / 2)) +100
            position_y = int((screen_height / 2) - (window_height / 2)) +30

            self.main.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

            self.upnew = upnew


            self.update_frame = Frame(self.main,height=350,width=350,bg="#570416")
            self.update_frame.place(x=0,y=0)

            #######################################################################################################3

            
            Label(self.update_frame,text=f"Details",font=("jokerman",21),fg="white",bg="#570416").place(x=120,y=10)
            Label(self.update_frame,text=f"Name : {data_con[1]}",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=70)
            Label(self.update_frame,text=f"Email : {data_con[2]}",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=110)
            Label(self.update_frame,text=f"Contact : {data_con[3]}",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=150)
            Label(self.update_frame,text=f"Password : {data_con[4]}",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=190)
            # Label(self.update_frame,text=f"Details",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=270)


            self.submit= Button(self.update_frame,text="Ok",font=("Arial", 11),width=10,height=1,command=self.close)
            self.submit.place(x=120,y=250)


            self.main.mainloop()
    def close(self):
         self.main.destroy()

class show_cinemas:
    def __init__(self,data,movie_name,timing,user_data):
            self.main = Tk()
            self.main.title(f"{data}") 
            self.data = data
            self.timing = timing
            self.movie_name = movie_name
            self.main.attributes("-topmost",True)


            container = Database_store.cinema_details(self.data)
            self.data_con = []
            for i in container: 
                 self.data_con.append(i)
            print(self.data_con)
            self.date_str = ""
            self.cond = False
            self.times = str(self.timing)
            self.timing_list = []
            for i in range(len(self.times)):
                for j in range(len(self.times)):
                    for k in range(len(self.times)):
                        if i != j and j != k and k != i:

                            last_two = int(self.times[j]+self.times[k])
                            if last_two > 60:
                                 last_two = last_two - 60
                                 if len(str(last_two)) == 1:
                                      last_two = "0"+str(last_two)
                            self.timing_list.append(self.times[i]+':'+str(last_two))
            print(self.timing_list)
            self.price_li = []
            for i in range(len(self.times)):
                for j in range(len(self.times)):
                    for k in range(len(self.times)):
                        if i != j and j != k and k != i:
                            t1,t2,t3 = int(self.times[i]),int(self.times[j]),int(self.times[k])
                            if t1 > 5:
                                t1 = t1-5
                            if t2 > 5:
                                t2 = t2-5
                            if t3 > 5:
                                t3 = t3-5
                            if t1 == 0:
                                t1=1
                            total = int(str(t1)+str(t2)+str(t3)) 
                            if total >500:
                                total -= 400
                            elif total >400:
                                total -= 300
                            elif total >300:
                                total -= 200
                            elif total >200:
                                total -= 100
                            # 
                            self.price_li.append(total*2)
            self.sample_screen()
            
            window_width = 1150
            window_height = 550

            # Get the screen width and height
            screen_width = self.main.winfo_screenwidth()
            screen_height = self.main.winfo_screenheight()

            # Calculate the position to center the window
            position_x = int((screen_width / 2) - (window_width / 2)) +100
            position_y = int((screen_height / 2) - (window_height / 2)) +30

            self.main.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
            # self.show_frame()
        


            self.inner_frame = Frame(self.main,height=550,width=550,bg="#570416")
            self.inner_frame.place(x=0,y=0)
            self.show_frame(self.timing_list,self.price_li,self.timing,user_data)

            self.dates_frame = Frame(self.inner_frame, width=901, height= 80, bg="#6C1B1F")
            self.dates_frame.place(x=100, y=115)
            self.upload_dates(timing)

            self.main.mainloop()
            
    def show_frame(self,timing_list,price_li,movie_len,user_data):

                 

            
            self.cinema_label = Label(self.inner_frame, text=f"{self.movie_name} -  {self.data}", font=("Comic Sans MS", 25, "bold"), bg="#570416", fg="#cbeff2")
            self.cinema_label.place(x=300, y=20)

            
            self.tree_frame = Frame(self.inner_frame, width=901, height=((len(self.data_con)+1)*40)+2, bg="#ffffff")
            self.tree_frame.place(x=100, y=215)

            # Heading labels
            self.headings_frame = Frame(self.tree_frame, width=900, height=40, bg="#f5e6e9")
            self.headings_frame.place(x=1, y=1)

            Label(self.headings_frame, text="Cinemas", font=("Tw Cen MT", 16, "bold")).place(x=100, y=5)
            Label(self.headings_frame, text="Timing", font=("Tw Cen MT", 16, "bold")).place(x=300, y=5)
            Label(self.headings_frame, text="Price", font=("Tw Cen MT", 16, "bold")).place(x=500, y=5)
            Label(self.headings_frame, text="Booking", font=("Tw Cen MT", 16, "bold")).place(x=700, y=5)

            self.row_frames = []
            row_counter = 0
            y = 40  

            for distt_name,timing_li,price_li in zip(self.data_con,timing_list,price_li):
                distt = distt_name[1]  
                bg_color = "#570416" if row_counter % 2 == 0 else "#6C1B1F"  

                # Row Frame
                row_frame = Frame(self.tree_frame, height=40, width=897, bg=bg_color)
                row_frame.place(x=2, y=y)
                y += 40  

                
                self.cin_name = Label(row_frame, text=distt, font=("Tw Cen MT", 14), fg="white", bg=bg_color)
                self.cin_name.place(x=100, y=5)
                self.timing = Label(row_frame, text=timing_li, font=("Tw Cen MT", 14), fg="white", bg=bg_color)
                self.timing.place(x=300, y=5)
                self.price = Label(row_frame, text=price_li, font=("Tw Cen MT", 14), fg="white", bg=bg_color)
                self.price.place(x=500, y=5)

                # Button in the row
                view_all_button = Button(row_frame, text="Book Now", font=("Tw Cen MT", 14), fg="white", bg=bg_color, border=0, relief=FLAT)
                view_all_button.place(x=700, y=5)
                view_all_button.bind("<Button-1>",lambda x ,cin_name = self.cin_name.cget("text"),user_data= user_data ,movie_name = self.movie_name, time = self.timing.cget("text") ,price = self.price.cget("text") , timing = movie_len:self.booking(x,cin_name,movie_name,time,price,timing,user_data))

                # Save the row frame to the list
                self.row_frames.append(row_frame)

                row_counter += 1

            self.useless = Label(self.inner_frame,text="",font=("arial",1),bg="#570416")
            self.useless.pack(padx=500,pady=640)

            self.form_frame.update_idletasks()
            self.form_frame.config(scrollregion=self.form_frame.bbox("all"))



    def booking(self,event,cin_name,movie_name,time,price,timing,user_data):
         print("booked")
        #  print(f"Cinema Name : {cin_name}\nMovie Name : {movie_name}\nTiming : {time}\nPrice : {price}\nMovie Lenght : {timing}")
         no_of_tickets(cin_name,movie_name,time,price,timing,self.book_date,user_data)





    def upload_dates(self,timing):
        self.frames = []
        xx, yy = 20, 4
        date_count = 0
        current_week = int(date.weekday(date.today()))  # Get the current day of the week
        current_day = int(date.today().day)  # Get the current day of the month
        current_month = int(date.today().month)  # Get the current month
        temp_month = current_month
        current_year = int(date.today().year)  # Get the current year

        # Loop to display 9 consecutive dates
        for i in range(9): 
            # Calculate the current date with date_count
            current_date = current_day + date_count
            # Get the number of days in the current month
            days_in_month = calendar.monthrange(current_year, current_month)[1]

            

            if current_date == days_in_month:
                print(current_date)
                # current_month += 1  
                month_change = True
            
                  
            # Handle transition to next month
            if current_date > days_in_month:
                print(current_date,'-',days_in_month,current_date-days_in_month)
                if current_month != temp_month:
                    current_date = current_date - days_in_month+1
                else:
                    current_date = current_date - days_in_month
                
                
                # Handle year transition if current_month exceeds 12 (December)
                if current_month > 12:
                    current_month = 1
                    current_year += 1  # Move to next year
            if current_date == 1:
                    current_month += 1
                    # current_date =1

            # Get the actual week day name
            week_days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
            acutal_week = week_days[current_week]

            # Get the actual month name
            months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
            acutal_mon = months[current_month - 1]

            # Create the Frame and Labels for the date display
            frame = Frame(self.dates_frame, height=70, width=70, bg="#570416")
            frame.place(x=xx, y=yy)
            
            l1= Label(frame, text=acutal_week, font=("arial", 9), fg="white", bg="#570416")
            l1.place(x=18, y=4)
            l2= Label(frame, text=current_date, font=("arial", 19), fg="white", bg="#570416")
            l2.place(x=16, y=20)
            l3 = Label(frame, text=acutal_mon, font=("arial", 9), fg="white", bg="#570416")
            l3.place(x=18, y=48)
            setattr(self,str(current_date) ,frame )
            self.frames.append((frame,l1,l2,l3))
            for widget in [frame, l1, l2, l3]:
                widget.bind("<Button-1>", lambda e, f=frame, l1=l1, l2=l2, l3=l3, date=current_date ,time = timing: self.clicks(f, l1, l2, l3,date,self.cond,time))
            self.cond = False
                # widget.bind("<Button-1>",self.show_frame())  

            # Update counters
            date_count += 1
            xx += 80
            

            # Update current_week, reset to 0 if it's the end of the week
            current_week = (current_week + 1) % 7

            if self.frames:
                first_frame, first_l1, first_l2, first_l3 = self.frames[0]
                self.click(first_frame, first_l1, first_l2, first_l3,current_date,self.cond,timing) 
            

    def clicks(self,clicked_frame,clicked_l1,clicked_l2,clicked_l3,dates,cond,timing):
         self.cond = True
         self.click(clicked_frame,clicked_l1,clicked_l2,clicked_l3,dates,cond,timing)
         
    def click(self,clicked_frame,clicked_l1,clicked_l2,clicked_l3,dates,cond,timing):

        self.date_str = dates
        
        if self.cond:
            print("if")
            # self.timing_list.reverse()
            
            # for i in range(len(self.timing_list)-1):
            self.first_element = self.timing_list.pop(0)  
            self.timing_list.append(self.first_element)
            print(self.timing_list)   
            self.first_price_element = self.price_li.pop(0)  
            self.price_li.append(self.first_price_element)
            print(self.price_li)   
            # self.main.update()
            for frame, l1, l2, l3 in self.frames:
                frame.config(background="#570416")
                l1.config(background="#570416", font=("arial", 9))
                l2.config(background="#570416", font=("arial", 19))
                l3.config(background="#570416", font=("arial", 9))

            # Set the clicked frame and labels to the selected state
            clicked_frame.config(background="green")
            clicked_l1.config(background="green", font=("arial", 9, "bold"))
            clicked_l2.config(background="green", font=("arial", 19, "bold"))
            clicked_l3.config(background="green", font=("arial", 9, "bold"))

            self.book_date = str(clicked_l2.cget("text")) +" "+ str(clicked_l3.cget("text")) 

            print(clicked_l1.cget("text"),clicked_l2.cget("text"),clicked_l3.cget("text"))

            self.show_frame(self.timing_list,self.price_li,timing,"")
        else:
        # show_cinemas("Jalandhar","Bibi Rajni",186)
            print("Else")
        
            
            for frame, l1, l2, l3 in self.frames:
                frame.config(background="#570416")
                l1.config(background="#570416", font=("arial", 9))
                l2.config(background="#570416", font=("arial", 19))
                l3.config(background="#570416", font=("arial", 9))

            # Set the clicked frame and labels to the selected state
            clicked_frame.config(background="green")
            clicked_l1.config(background="green", font=("arial", 9, "bold"))
            clicked_l2.config(background="green", font=("arial", 19, "bold"))
            clicked_l3.config(background="green", font=("arial", 9, "bold"))

            self.book_date = str(clicked_l2.cget("text")) +" "+str(clicked_l3.cget("text")) 

        

        



         
    def close(self):
         
         self.main.destroy()
    
    def sample_screen(self):
            


            self.canvas = Frame(self.main, bg='#570416', bd=5)
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


#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################



class show_c_detials:
    def __init__(self,cinema_name):
            self.main = Tk()
            self.main.title(f"{cinema_name}")
            self.main.attributes("-topmost",True)

            container = Database_store.cinemas_details_show(cinema_name)
            print(container)
            data_con = []
            print(container)
            for i in range(12):
                 data_con.append(container[0][i])
                 

            
            window_width = 350
            window_height = 550

            # Get the screen width and height
            screen_width = self.main.winfo_screenwidth()
            screen_height = self.main.winfo_screenheight()

            # Calculate the position to center the window
            position_x = int((screen_width / 2) - (window_width / 2)) +100
            position_y = int((screen_height / 2) - (window_height / 2)) +30

            self.main.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

            # self.upnew = upnew


            self.update_frame = Frame(self.main,height=550,width=350,bg="#570416")
            self.update_frame.place(x=0,y=0)

            #######################################################################################################3

            
            Label(self.update_frame,text=f"Details",font=("jokerman",21),fg="white",bg="#570416").place(x=120,y=10)
            Label(self.update_frame,text=f"Cinema Name : {data_con[1]}",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=70)
            Label(self.update_frame,text=f"Address : {data_con[2]}",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=110)
            Label(self.update_frame,text=f"Street : {data_con[3]}",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=150)
            Label(self.update_frame,text=f"District : {data_con[4]}",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=190)
            Label(self.update_frame,text=f"Pincode : {data_con[5]}",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=230)
            Label(self.update_frame,text=f"Screens : {data_con[6]}",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=270)
            Label(self.update_frame,text=f"Seats : {data_con[7]}",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=310)
            Label(self.update_frame,text=f"Phone : {data_con[8]}",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=350)
            Label(self.update_frame,text=f"Email : {data_con[9]}",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=390)
            Label(self.update_frame,text=f"Open Time : {data_con[10]}",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=430)
            Label(self.update_frame,text=f"Close Time : {data_con[11]}",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=470)
            # Label(self.update_frame,text=f"Details",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=270)


            self.submit= Button(self.update_frame,text="Ok",font=("Arial", 11),width=10,height=1,command=self.close)
            self.submit.place(x=120,y=510)


            self.main.mainloop()
    def close(self):
         self.main.destroy()

class upload_rating:
    def __init__(self,msg):
            self.main = Tk()
            self.main.title("data")
            self.main.attributes("-topmost",True)

 
                 
            window_width = 350
            window_height = 350

            # Get the screen width and height
            screen_width = self.main.winfo_screenwidth()
            screen_height = self.main.winfo_screenheight()

            # Calculate the position to center the window
            position_x = int((screen_width / 2) - (window_width / 2)) -20
            position_y = int((screen_height / 2) - (window_height / 2)) -40

            self.main.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")



            self.update_frame = Frame(self.main,height=350,width=350,bg="#570416")
            self.update_frame.place(x=0,y=0)

            Label(self.update_frame,text=f"Rating {msg}",font=("jokerman",21),fg="white",bg="#570416").place(x=100,y=10)
            Label(self.update_frame,text=f"Rating",font=("Tw Cen MT",16),fg="white",bg="#570416").place(x=130,y=80)
            self.rating_entry = Entry(self.update_frame, font=("Arial", 14, "normal"), relief=GROOVE,bg="#ffffff",fg="black",border=0)
            self.rating_entry.place(x=50, y=120) 

            self.submit= Button(self.update_frame,text="Submit",font=("Arial", 11),width=10,height=1)
            self.submit.place(x=120,y=180)
            self.submit.bind("<Button-1>",lambda x : self.upcome_to_latest(x,msg))
    

            self.main.mainloop()

    def upcome_to_latest(self,event,message):
        # print(message)
        store = Database_store.upcome_to_latest(message,self.rating_entry.get())
        if store:
            messagebox.showinfo("Success", "Work Successful")

        else:
            messagebox.showerror("Error", "Work Not Successful")

class no_of_tickets:
     def __init__(self,cin_name,movie_name,time,price,timing,book_date,user_data):
            self.main = Tk()
            self.main.title("data")
            self.main["bg"]="#6C1B1F"
            self.main.attributes("-topmost",True)

 
            print(user_data," ------------------- >>> Details")
            window_width = 350
            window_height = 350

            # Get the screen width and height
            screen_width = self.main.winfo_screenwidth()
            screen_height = self.main.winfo_screenheight()


            # Calculate the position to center the window
            position_x = int((screen_width / 2) - (window_width / 2)) 
            position_y = int((screen_height / 2) - (window_height / 2)) 

            self.main.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

            Label(self.main,text=f"Book Now",font=("Comic Sans MS",24),fg="white",bg="#6C1B1F").place(x=100,y=10)
            Label(self.main,text=f"No. of Tickets : ",font=("Tw Cen MT",19),fg="white",bg="#6C1B1F").place(x=80,y=100)
            
            self.total = Spinbox(self.main,font=("Arial",14,"normal"), from_=1, to=20)
            self.total.place(x=80,y=150,width=150)

            
            self.submit= Button(self.main,text="Submit",font=("Arial", 11),width=10,height=1)
            self.submit.place(x=100,y=220)
            self.submit.bind("<Button-1>",lambda x: self.close(x,cin_name,movie_name,time,price,timing,book_date,user_data,self.total.get()))

            self.main.mainloop()
     def close(self,event,cin_name,movie_name,time,price,timing,book_date,user_data,total):
           payment(cin_name,movie_name,time,price,timing,book_date,user_data,total)
          
 
          
class payment:
    def __init__(self,cin_name,movie_name,time,price,timing,book_date,user_data,total):
            self.main = Toplevel()
            self.main.title(f"Payment") 

            self.main.attributes("-topmost",True)

            window_width = 950
            window_height = 550

            screen_width = self.main.winfo_screenwidth()
            screen_height = self.main.winfo_screenheight()

            position_x = int((screen_width / 2) - (window_width / 2)) +100
            position_y = int((screen_height / 2) - (window_height / 2)) +30

            self.main.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")        
            self.main.resizable(False,False)
            self.main.attributes("-topmost",True)

            self.sample_screen()

            self.inner_frame = Frame(self.main,height=550,width=1150,bg="#570416")
            self.inner_frame.place(x=0,y=0)

   
            
            

            Frame(self.inner_frame,height=550,width=301,bg="white").place(x=0,y=0)
            self.sides_frame = Frame(self.inner_frame,height=550,width=300,bg="#6C1B1F")
            self.sides_frame.place(x=0,y=0)

            self.sidein_frame = Frame(self.sides_frame,height=120,width=301,bg="#85262b")
            self.sidein_frame.place(x=0,y=0)

            Label(self.sides_frame, text=f"{movie_name}" ,font=("Comic Sans MS", 17,"bold"), bg="#85262b",fg="white").place(x=60,y=25)
            Label(self.sides_frame, text=str(str(Database_store.movie_gen_payment(movie_name)).replace('{','')).replace('}','') ,font=("Comic Sans MS", 15,"normal"), bg="#85262b",fg="white").place(x=60,y=65)

            Label(self.sides_frame, text="Price :" ,font=("Comic Sans MS", 14,"bold"), bg="#6C1B1F",fg="white").place(x=50,y=145)
            Label(self.sides_frame, text=f"Tickets Price : {price}" ,font=("Comic Sans MS", 13), bg="#6C1B1F",fg="white").place(x=60,y=185)
            Label(self.sides_frame, text=f"Total Tiekcts : {total}" ,font=("Comic Sans MS", 13), bg="#6C1B1F",fg="white").place(x=60,y=225)
            Label(self.sides_frame, text=f"Sub Total : {price*int(total)} " ,font=("Comic Sans MS", 13), bg="#6C1B1F",fg="white").place(x=60,y=265)
            Label(self.sides_frame, text="Amount Payable : " ,font=("Comic Sans MS", 13), bg="#6C1B1F",fg="white").place(x=20,y=325)
            Label(self.sides_frame, text=f"Rs. {price*int(total)}" ,font=("Comic Sans MS", 20), bg="#6C1B1F",fg="white").place(x=165,y=315)


            self.heading = Label(self.inner_frame,text=f"Payment Method",font=("Comic Sans MS",24),fg="white",bg="#570416")
            self.heading.place(x=400,y=10)
            self.credit_card = Label(self.inner_frame,text=f"Credit Card :",font=("Tw Cen MT",19),fg="white",bg="#570416")
            self.credit_card.place(x=320,y=100)
            self.name = Label(self.inner_frame,text=f"Card on the Name : ",font=("Tw Cen MT",19),fg="white",bg="#570416")
            self.name.place(x=320,y=200)
            self.expireMM = Label(self.inner_frame,text=f"Expire : ",font=("Tw Cen MT",19),fg="white",bg="#570416")
            self.expireMM.place(x=320,y=300)
            self.expireYY = Label(self.inner_frame,text=f"CVV : ",font=("Tw Cen MT",19),fg="white",bg="#570416")
            self.expireYY.place(x=620,y=300)
            
            
            self.username = Entry(self.inner_frame,font=("Arial",14,"normal"),fg="#b7bdb9")
            self.username.place(x=340 ,y=150,width=350)
            self.username.bind('<FocusIn>',lambda x:self.focusin(x,self.username,"Holder Name"))
            self.username.insert(0,"Holder Name")
            self.username.bind('<FocusOut>',lambda x :self.focusout(x,"Holder Name"))

            self.card_no = Entry(self.inner_frame,font=("Arial",14,"normal"),fg="#b7bdb9")
            self.card_no.place(x=340 ,y=250,width=350)
            self.card_no.insert(0,"XXXX-XXXX-XXXX-XXXX")   
            self.card_no.bind('<FocusIn>',lambda x:self.focusin(x,self.card_no,"XXXX-XXXX-XXXX-XXXX"))
            self.card_no.bind('<FocusOut>',lambda x :self.focusout(x,"XXXX-XXXX-XXXX-XXXX"))
            
            self.expireMM_e = Entry(self.inner_frame,font=("Arial",14,"normal"),fg="#b7bdb9")
            self.expireMM_e.place(x=340 ,y=350,width=60)
            self.expireMM_e.insert(0,"MM")
            self.expireMM_e.bind('<FocusIn>',lambda x:self.focusin(x,self.expireMM_e,"MM"))
            self.expireMM_e.bind('<FocusOut>',lambda x :self.focusout(x,"MM"))

            self.expireYY_e = Entry(self.inner_frame,font=("Arial",14,"normal"),fg="#b7bdb9")
            self.expireYY_e.place(x=420 ,y=350,width=60)
            self.expireYY_e.insert(0,"YY")
            self.expireYY_e.bind('<FocusIn>',lambda x:self.focusin(x,self.expireYY_e,"YY"))
            self.expireYY_e.bind('<FocusOut>',lambda x :self.focusout(x,"YY"))

            self.cvv = Entry(self.inner_frame,font=("Arial",14,"normal"),fg="#b7bdb9")
            self.cvv.place(x=630 ,y=350,width=120)
            self.cvv.insert(0,"CVV")
            self.cvv.bind('<FocusIn>',lambda x:self.focusin(x,self.cvv,"CVV"))
            self.cvv.bind('<FocusOut>',lambda x :self.focusout(x,"CVV"))

            self.submits= Button(self.inner_frame,text="Pay",font=("Arial", 11),width=10,height=1)
            self.submits.place(x=450,y=420)
            self.submits.bind("<Button-1>",lambda x: self.check(x,cin_name,movie_name,time,price,timing,book_date,user_data,total))

            self.main.mainloop()

    def check(self,event,cin_name,movie_name,time,price,timing,book_date,user_data,total):

        # self.main.attributes("-topmost",False)
        # if self.username.get() == "" or self.card_no.get() == "" or self.expireMM_e.get() == "" or self.expireYY_e.get() == "" or self.cvv.get() == "":
        #     messagebox.showerror("Missing Value Error", "Value Missing")
        # elif len(self.card_no.get()) != 16:
        #     messagebox.showerror("Card Number", "Invalid Card Number!")
        # elif len(self.username.get()) > 2:
        #     messagebox.showerror("User Name", "Invalid Name!")
        # elif len(self.expireMM_e.get()) != 2 or self.expireMM_e.get() < 0 or self.expireMM_e.get() > 13  :
        #     messagebox.showerror("Month", "Invalid MM!")
        # elif self.expireYY_e.get() < 2024 or len(self.expireYY_e.get()) != 4:
        #     messagebox.showerror("Year Error", "Invalid YY!")
        # else:
            # messagebox.showinfo("Success", "Registration Successful")
            self.close(cin_name,movie_name,time,price,timing,book_date,user_data,total)

    def close(self,cin_name,movie_name,time,price,timing,book_date,user_data,total_t):
        print(f"Total Tickets : {total_t}")
        book_id = random.randint(1000,9999)
        li = []
        container = Database_store.particular_cinema_details(cin_name)
        with open("users.txt", "r") as file:
            content = file.read()
            li.append(content)
            dt =  ((str(li[0]).replace('(','')).replace(')','').replace('\'',"").split(","))

        print(container)
        print(user_data)
        subject = f"🎉 Your Ticket Has Been Successfully Booked - MoviesWave Confirmation"
        below = f"""Dear {dt[0].split()[0]},
Thank you for choosing MoviesWave! We are excited to inform you that your ticket has been successfully booked.

Movie Details:
Movie Title: {movie_name}
Show Date: {str(book_date)} {str(date.today().year)}
Show Time: {time} 
Cinema Name: {cin_name} 
Movie Lenght: {timing} min 
Booking ID: {book_id}

Ticket Summary:
Total Tickets: {total_t}
Price per Ticket: {price} 
Total Amount Paid: {int(total_t)*int(price)}

Venue Address:
{container[0][2]},{container[0][3]}
{container[0][4]},{container[0][5]}

Please arrive 15 minutes early to avoid any last-minute rush. Remember to bring this confirmation email or your booking ID for seamless entry.
If you need to make any changes to your booking or have any questions, feel free to contact our support team at [support email/phone number].
We look forward to seeing you at the movies! 🍿

Best regards,
MoviesWave Team"""
                
        self.send_email(subject, below,dt[1])
        print(below)
        all_data = (book_id,movie_name,f"{str(book_date)} {str(date.today().year)}",time,cin_name,price,total_t,int(total_t)*int(price),dt[0],dt[1],date.today())
        store = Database_store.bookings(all_data)
        # store = True
        if store:
            messagebox.showinfo("Success", "Booking Successful")
        else:
            messagebox.showerror("Error", "Booking Error")
             
        self.main.destroy()

    def send_email(self,subject, body, to_email):
    # Create an EmailMessage object
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = 'movieswave8@gmail.com'  # Replace with your sender email
        msg['To'] = to_email
        msg.set_content(body)

        # Connect to the Gmail SMTP server using smtplib
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                # Use your actual Gmail credentials here
                smtp.login('movieswave8@gmail.com', 'rvev dqgq cbgb cpkt')  # Replace with your Gmail password
                smtp.send_message(msg)
            print('Email sent successfully!')
        except Exception as e:
            print(f"Error: {e}")

    def sample_screen(self):
            


            self.canvas = Frame(self.main, bg='#570416', bd=5)
            self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER, width=1150, height=550) 

            self.scrollbar = Scrollbar(self.canvas, orient="vertical")
            self.scrollbar.pack(side=RIGHT, fill=Y)

            self.form_frame = Canvas(self.canvas,bg='#570416', yscrollcommand=self.scrollbar.set)
            self.form_frame.pack(side="left", fill="both", expand=True)


            self.scrollbar.config(command=self.form_frame.yview)

            # Create an inner frame inside the Canvas
            self.inner_frame = Frame(self.form_frame, bg='#570416')


            # Add the inner frame to the Canvas
            self.form_frame.create_window((0, 0), window=self.inner_frame, anchor="nw")


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



class settings:
    def __init__(self,email):
            self.main = Toplevel()
            self.main.title(f"Settings") 
            # self.data = ""
            # self.timing = ""
            # self.movie_name = "" 
            self.only_values()
            self.main.attributes("-topmost",True)

            window_width = 950
            window_height = 550

            screen_width = self.main.winfo_screenwidth()
            screen_height = self.main.winfo_screenheight()

            position_x = int((screen_width / 2) - (window_width / 2)) +100
            position_y = int((screen_height / 2) - (window_height / 2)) +30

            self.main.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")        
            self.main.resizable(False,False)
            self.main.attributes("-topmost",True)

            self.sample_screen()

            self.inner_frame = Frame(self.main,height=550,width=1150,bg="#570416")
            self.inner_frame.place(x=0,y=0)

  

            Frame(self.inner_frame,height=550,width=301,bg="white").place(x=0,y=0)
            self.sides_frame = Frame(self.inner_frame,height=550,width=300,bg="#6C1B1F")
            self.sides_frame.place(x=0,y=0)

            self.sidein_frame = Frame(self.sides_frame,height=120,width=301,bg="#85262b")
            self.sidein_frame.place(x=0,y=0)

            self.circle_img = Image.open("circle_6C1B1F.png").resize((80,80))
            self.imgg_local_real = ImageTk.PhotoImage(self.circle_img)
            self.logo_local = Label(self.sides_frame, image=self.imgg_local_real, bd=0,bg="#85262b")
            self.logo_local.place(x=22, y=35)

            if self.name_len == 1:
                self.user_label = Label(self.logo_local, text=self.AK,font=("Arial", 20, "bold"), fg="white", bg="#570416")
                self.user_label.place(x=25, y=20)
            else:
                self.user_label = Label(self.logo_local, text=self.AK, font=("Arial", 18, "bold"), fg="white", bg="#570416")
                self.user_label.place(x=18, y=20)
            
            self.name_label = Label(self.sides_frame, text=self.name ,font=("Arial", 15,"bold"), bg="#85262b",fg="white")
            self.name_label.place(x=100,y=45)

            self.email_label = Label(self.sides_frame, text=self.email ,font=("Arial", 12), bg="#85262b",fg="white")
            self.email_label.place(x=100,y=70)
            
            # self.cond = True

            self.get_account= Button(self.sides_frame, text="Account Settings", font=("Arial", 14), fg="white",bg="#6C1B1F", width=25,height=1,border=1,relief=FLAT,anchor="nw",pady=10)
            self.get_account.place(x=5,y=150)
            self.get_account.bind("<Enter>",self.side_enter)
            self.get_account.bind("<Leave>",self.side_leave)
            self.get_account.bind("<Button-1>",lambda x: self.security(False))
            
            self.get_security= Button(self.sides_frame, text="Security", font=("Arial", 14), fg="white",bg="#6C1B1F", width=25,height=1,border=1,relief=FLAT,anchor="nw",pady=10)
            self.get_security.place(x=5,y=210)
            self.get_security.bind("<Enter>",self.side_enter)
            self.get_security.bind("<Leave>",self.side_leave)
            self.get_security.bind("<Button-1>",lambda x: self.security(True))
            ##############################################################################################################################
            ##############################################################################################################################


            self.headd = Label(self.inner_frame,text=f"Account Settings",font=("Comic Sans MS",24),fg="white",bg="#570416")
            self.user = Label(self.inner_frame,text=f"Username : ",font=("Tw Cen MT",19),fg="white",bg="#570416")
            self.em = Label(self.inner_frame,text=f"Email : ",font=("Tw Cen MT",19),fg="white",bg="#570416")
            self.con = Label(self.inner_frame,text=f"Contact : ",font=("Tw Cen MT",19),fg="white",bg="#570416")
            
            
            self.username = Entry(self.inner_frame,font=("Arial",14,"normal"))

            self.mail = Entry(self.inner_frame,font=("Arial",14,"normal"))
            self.contact = Entry(self.inner_frame,font=("Arial",14,"normal"))
            

            self.submits= Button(self.inner_frame,text="Submit",font=("Arial", 11),width=10,height=1,command=self.update_users)




            self.username.insert(0,self.names)

            self.contact.insert(0,self.contacts)

            self.mail.insert(0,self.email)

            # self.submit.bind("<Button-1>",lambda x: self.close(x,cin_name,movie_name,time,price,timing,book_date,user_data,self.total.get()))
            
            # self.main_frames = Frame(self.inner_frame,height=550,width=850,bg="#570416")
            # self.main_frame.place(x=301,y=0)
            

         
            self.head = Label(self.inner_frame,text=f"Security",font=("Comic Sans MS",24),fg="white",bg="#570416")
            self.pas = Label(self.inner_frame,text=f"Change Password ",font=("Tw Cen MT",19),fg="white",bg="#570416")
            self.olf = Label(self.inner_frame,text=f"Old Password : ",font=("Tw Cen MT",19),fg="white",bg="#570416")
            self.new_l = Label(self.inner_frame,text=f"New Password : ",font=("Tw Cen MT",19),fg="white",bg="#570416")
            
            
 
            self.old = Entry(self.inner_frame,font=("Arial",14,"normal"))

            self.new = Entry(self.inner_frame,font=("Arial",14,"normal"))

            
            self.submit= Button(self.inner_frame,text="Submit",font=("Arial", 11),width=10,height=1,command=self.update_user_password)

            self.security(False)
            self.main.mainloop()
   
    def only_values(self):
        li = []
        with open("users.txt", "r") as file:
            content = file.read()
        li.append(content)
        dt =  ((str(li[0]).replace('(','')).replace(')','').replace('\'',"").split(","))
        self.AK = (dt[0].split()[0][0]).upper()+(dt[0].split()[1][0]).upper()
        self.name = (dt[0].split()[0])+" "+(dt[0].split()[1])
        self.names = (dt[0])
        self.email = (dt[1]).replace(" ","")
        self.name_len = len((dt[0].split()[0][0])+(dt[0].split()[1][0]))
        self.contacts = dt[2].replace(" ","")
        self.passwords = dt[3].replace(" ","")

    def security(self,val):
        if val == True:
            self.con.place_forget()
            self.user.place_forget()
            self.em.place_forget()
            self.headd.place_forget()
            self.username.place_forget()#,width=350)
            self.contact.place_forget()#,width=350)
            self.mail.place_forget()#,width=350)
            self.submit.place_forget()#
            
            self.submit.place(x=440,y=420)
            self.new.place(x=340 ,y=350,width=350)
            self.old.place(x=340 ,y=250,width=350)
            self.new_l.place(x=320,y=300)
            self.pas.place(x=420,y=100)
            self.head.place(x=400,y=10)
            self.olf.place(x=320,y=200)
        else:
            self.submit.place_forget()
            self.new.place_forget()
            self.old.place_forget()
            self.new_l.place_forget()
            self.pas.place_forget()
            self.head.place_forget()            
            self.olf.place_forget()

            self.headd.place(x=400,y=10)
            self.user.place(x=320,y=100)
            self.em.place(x=320,y=200)
            self.con.place(x=320,y=300)
            self.username.place(x=340 ,y=150,width=350)
            self.contact.place(x=340 ,y=350,width=350)
            self.mail.place(x=340 ,y=250,width=350)
            self.submits.place(x=440,y=420)

         
    def close(self):
         
         self.main.destroy()

    def update_users(self):
        
        li = (self.username.get(),self.mail.get(),self.contact.get(),self.passwords,self.email)
        store  = Database_store.movies_update_data(li,"users")
        if store:
             messagebox.showinfo("Updated","Details Updates")
        else:
             messagebox.showerror("Error","Details not Updated")

    def update_user_password(self):
        data = (self.email)
        datas = Database_store.select_passwords_only(data) 
        # print(datas[0][0]) 

        if self.old.get() == datas[0][0]:
            li = (self.name,self.email,self.contacts,self.new.get(),self.email)

            store  = Database_store.movies_update_data(li,"password")
            if store:
                messagebox.showinfo("Updated","Password Updates")
            else:
                messagebox.showerror("Error","Password not Updated")
        else:
            messagebox.showerror("Error","Old Password Wrong")
             
    
    def sample_screen(self):
            


            self.canvas = Frame(self.main, bg='#570416', bd=5)
            self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER, width=1150, height=550) 

            self.scrollbar = Scrollbar(self.canvas, orient="vertical")
            self.scrollbar.pack(side=RIGHT, fill=Y)

            self.form_frame = Canvas(self.canvas,bg='#570416', yscrollcommand=self.scrollbar.set)
            self.form_frame.pack(side="left", fill="both", expand=True)


            self.scrollbar.config(command=self.form_frame.yview)

            # Create an inner frame inside the Canvas
            self.inner_frame = Frame(self.form_frame, bg='#570416')


            # Add the inner frame to the Canvas
            self.form_frame.create_window((0, 0), window=self.inner_frame, anchor="nw")


    
    def side_enter(self,event):
        event.widget["bg"]="green" 
        event.widget["fg"]="white"

    def side_leave(self,event):
        event.widget["bg"]="#6C1B1F"
        event.widget["fg"]="white"



class purchase_his(settings):
    # def __init__(self):
            # super().__init__("Email")


    def __init__(self):
            self.main = Tk()
            self.main.title(f"Purchase History") 
            self.main.attributes("-topmost",True)

            window_width = 1150
            window_height = 550

            screen_width = self.main.winfo_screenwidth()
            screen_height = self.main.winfo_screenheight()

            position_x = int((screen_width / 2) - (window_width / 2)) +100
            position_y = int((screen_height / 2) - (window_height / 2)) +30

            self.main.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")        
            self.main.resizable(False,False)
            li = []
            super().sample_screen()
            super().only_values()
     
            print(self.passwords)


            self.inner_frame = Frame(self.main,height=550,width=1150,bg="#570416")
            self.inner_frame.place(x=0,y=0)

            
            self.press_update_view()

            self.main.mainloop()

    def press_update_view(self,name="ravi"):
        self.selected_disctt = name
        self.inner_frame.destroy()
        self.sample_screen()
        print(name)
        
        self.tickets = []
        print(self.email)
        store = Database_store.bookings_particular_show(self.email) 
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
 
            delete_button.bind("<Button-1>", lambda event, ticket = cinema_name[0]: show_ticket_detials(ticket))

            # delete_button.bind("<Button-1>", lambda event, : self.press)
            update_button.bind("<Button-1>", lambda event, name=cinema_name: self.press_delete(event, name,"update","cinema"))
            # update_button.bind("<Button-1>", lambda event, name=cinema_name: self.press_show_details(event, name))

            self.row_frames.append(row_frame)



        self.useless = Label(self.inner_frame,text="",font=("arial",1),bg="#570416")
        self.useless.pack(padx=500,pady=(((len(self.tickets) + 1) * 40) + 2)) 

        self.form_frame.update_idletasks()
        self.form_frame.config(scrollregion=self.form_frame.bbox("all"))
            # sample_screen()


class show_ticket_detials:
    def __init__(self,ticket_no):
            store = Database_store.bookings_particular_details_show(ticket_no)
            print(store)

            user_name = "ok"
            self.main = Tk()
            self.main.title(f"{store[0][1]}")
            self.main.attributes("-topmost",True)


            
            window_width = 350
            window_height = 350

            # Get the screen width and height
            screen_width = self.main.winfo_screenwidth()
            screen_height = self.main.winfo_screenheight()

            # Calculate the position to center the window
            position_x = int((screen_width / 2) - (window_width / 2)) +100
            position_y = int((screen_height / 2) - (window_height / 2)) +30

            self.main.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

        


            self.update_frame = Frame(self.main,height=350,width=350,bg="#570416")
            self.update_frame.place(x=0,y=0)

            #######################################################################################################3

            
            Label(self.update_frame,text=f"Details",font=("jokerman",21),fg="white",bg="#570416").place(x=120,y=10)
            Label(self.update_frame,text=f"Ticket No : {store[0][0]}",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=70)
            Label(self.update_frame,text=f"Movie Name : {store[0][1]}",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=110)
            Label(self.update_frame,text=f"Ticket Date : {store[0][2]}",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=150)
            Label(self.update_frame,text=f"Show Time : {store[0][3]}",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=190)
            # Label(self.update_frame,text=f"Details",font=("Tw Cen MT",14),fg="white",bg="#570416").place(x=70,y=270)


            self.submit= Button(self.update_frame,text="Ok",font=("Arial", 11),width=10,height=1,command=self.close)
            self.submit.place(x=120,y=250)


            self.main.mainloop()
    def close(self):
         self.main.destroy()
            




if __name__ == "__main__":

      
    #   update_scr("Gandhi 3","upcoming")
    # show_c_detials("Aman","user")
    # upload_rating()
    # data = ('sandeep singh', 'sandeep81@gmail.com', '7719427838', '@_Sandeep81')
    # show_cinemas("Jalandhar","Bibi Rajni",186,data)
    # settings("s@gmail.com")
    # no_of_tickets()
    show_ticket_detials("1277")
