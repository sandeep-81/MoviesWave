from tkinter import *
from datetime import date 
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk,ImageDraw
from tkinter import filedialog
from tkcalendar import DateEntry 
import Database_store
from subprocess import *
import front_logo
import test
import admin_handle
import update_movie

class details:
    def __init__(self, movie_name, UA, c, b, rating , img, banner,trailer,date,time,about,lang,loc,user_detail):
        self.main = Toplevel()
        self.main.title(f"{movie_name}")
        self.main.geometry(f"{self.main.winfo_screenwidth()}x{self.main.winfo_screenheight()}")
        self.main.state("zoomed")
        self.main["bg"] = "#ffffff"
        self.name = movie_name
        self.user_data = user_detail
        self.loc = loc
        self.lang = lang
        self.upload_t = trailer
        self.banner = banner
        self.poster = img
        self.genue = UA
        self.date = date
        self.time = time
        self.about = about     
        self.rating = float(rating)/2
        self.main.attributes("-topmost",True)

        print("###################################################################",)
        print("This is banner --------------------------",banner)
        print("###################################################################",)

        self.movie_names_up = []
        self.movie_posters_up = []
        self.counter_up = 0
        self.row_count_up = 0
        self.y_axis_upcoming_movie_frame = 80 
        self.x_axis_upcoming_movie_frame = -240

        
        print(self.upload_t)

        print("here access page ")


        self.main_movie(user_detail)
        self.movie_frame(self.big_poster_upload,0)
        self.last_execute()



        self.back = Button(self.main, text="Back", font=("Arial", 15),anchor=CENTER, activebackground="#ffffff",bg="white",border=1,relief=FLAT,command = self.back)
        self.back.place(x=10,y=10)


        self.main.mainloop()

    def back(self):
         self.main.destroy()
        #  test.mainfile(True,self.main,False)


    def upper_frame(self):
        self.upper_blue_frame = Frame(self.inner_frame, width=self.main.winfo_screenwidth(), height=150, bg="#6C1B1F", border=0)
        self.upper_blue_frame.place(x=0, y=0)

        # Store the image as an instance variable
        self.imgg = Image.open("logo_black.png").resize((260, 120))
        self.img = ImageTk.PhotoImage(self.imgg)
        self.logo = Label(self.upper_blue_frame, image=self.img, bg="#6C1B1F")
        self.logo.place(x=4, y=5)

        self.search = Entry(self.upper_blue_frame, width=50, font=("Arial", 15, "normal"), bg="white", relief=SOLID, border=1, fg="#a8a59b")
        self.search.place(x=340, y=30)
        self.search.insert(0, "Search for Movies ... ")
        self.search.bind('<Button-1>', self.search_box)

        self.sign_in = Button(self.upper_blue_frame, text="Sign in", font=("Tw Cen MT", 12, "bold"), bg="#122a6e", fg="white", command=self.login)
        self.sign_in.place(x=1330, y=30)

        self.admin_sign_in = Button(self.upper_blue_frame, text="Admin", font=("Tw Cen MT", 12, "bold"), bg="#122a6e", fg="white", command=self.admin_login)
        self.admin_sign_in.place(x=1400, y=30)



    def main_movie(self,user_data):

        self.canvas = Frame(self.main,bg="#6C1B1F",bd=5)
        self.canvas.place(x=0,y=0,height=800,width=1540)
        self.scrollbar = Scrollbar(self.canvas,orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.form_frame = Canvas(self.canvas,bg="#6C1B1F",yscrollcommand=self.scrollbar.set)
        self.form_frame.pack(fill="both" ,side="left",expand=True)
        self.scrollbar.config(command=self.form_frame.yview)
        self.inner_frame = Frame(self.form_frame,bg="#6C1B1F",width=300)
        self.form_frame.create_window((0,0),window=self.inner_frame,anchor="nw") 

        
        self.poster_frame = Frame(self.inner_frame, height=530, width=1500, bg="#570416", border=0, relief=SOLID)
        self.poster_frame.name = "poster_frame"

        self.big_poster_open = Image.open(self.banner).resize((1500,530 ))
        self.big_poster_upload = ImageTk.PhotoImage(self.big_poster_open)



    #################################################################################################################################
        
        self.details_frame = Frame(self.inner_frame, height=370, width=970, bg="#6C1B1F", border=0, relief=SOLID)
        self.details_frame.name = "details_frame"


        self.details_movie_curve = Image.open("rec98.png").resize((970,370 ))
        self.details_photo = ImageTk.PhotoImage(self.details_movie_curve)
        self.curve_box_details = Label(self.details_frame, image=self.details_photo,bg="#6C1B1F",border=0,relief=FLAT)
        self.details_frame.place(x=20, y=470) 
        self.curve_box_details.place(x=0,y=0) 


        self.add_movie_orignal = ImageTk.PhotoImage(Image.open(self.poster).resize((250,320)))
        self.local_frame = Label(self.details_frame , image=self.add_movie_orignal, height=320, width=250, bg="#ffffff", relief=GROOVE, border=1)
        self.local_frame.place(x=70,y=25)

        self.movie_name_label = Label(self.details_frame, text=f"{self.name}", font=("Roboto", 35, "bold"),fg="#000000",bg="#ffffff")
        self.movie_name_label.place(x=350, y=25) 

##################################################################################################################################
        self.star_frame = Frame(self.details_frame, height=35, width=200, bg="#B0AEAE", border=0, relief=SOLID)
        self.star_frame.name = "star_frame"
        self.star_frame.place(x=350 , y=100 )

        self.yello_star = Image.open("yellow_Star.png").resize((35,35 ))
        self.ye_star = ImageTk.PhotoImage(self.yello_star)

        self.y_star1 = Label(self.star_frame, image=self.ye_star,bg="#B0AEAE",border=0,relief=FLAT)
        self.y_star1.place(x=0, y=0) 

        self.y_star2 = Label(self.star_frame, image=self.ye_star,bg="#B0AEAE",border=0,relief=FLAT)
        self.y_star2.place(x=40, y=0) 

        self.y_star3 = Label(self.star_frame, image=self.ye_star,bg="#B0AEAE",border=0,relief=FLAT)
        self.y_star3.place(x=80, y=0)

        self.y_star4 = Label(self.star_frame, image=self.ye_star,bg="#B0AEAE",border=0,relief=FLAT)
        self.y_star4.place(x=120, y=0)

        self.y_star5 = Label(self.star_frame, image=self.ye_star,bg="#B0AEAE",border=0,relief=FLAT)
        self.y_star5.place(x=160, y=0) 

        
        li = [390,430,470,510,550]
        self.star_frame_up = Frame(self.details_frame, height=35, width=10, bg="#B0AEAE", border=0, relief=SOLID)
        self.star_frame_up.name = "star_frame_up"
        if self.rating <= 1 and self.rating > 0:
            self.star_frame_up.place(x=li[0] , y=100 )
            self.star_frame_up.config(width=160)
        elif self.rating <= 2 and self.rating > 1:
            self.star_frame_up.place(x=li[1] , y=100 )
            self.star_frame_up.config(width=(120))
        elif self.rating <= 3 and self.rating > 2:
            self.star_frame_up.place(x=li[2] , y=100 )
            self.star_frame_up.config(width=(80))
        elif self.rating <= 4 and self.rating > 3:
            self.star_frame_up.place(x=li[3] , y=100 )
            self.star_frame_up.config(width=(40))
        elif self.rating <= 5 and self.rating > 4:
            self.star_frame_up.place(x=li[3] , y=100 )
            self.star_frame_up.config(width=0)
        


##################################################################################################################################
        self.movie_details_label = Label(self.details_frame, text=f"{self.time} min . {self.genue} . {self.date}", font=("Comic Sans MS", 16, "normal"),fg="#575656",bg="#ffffff")
        self.movie_details_label.place(x=350, y=140) 

        # self.dim_frame = Frame(self.details_frame, height=35, width=100, bg="#B0AEAE", border=0, relief=SOLID)
        # self.dim_frame.name = "dim_frame"
        # self.dim_frame.place(x=350 , y=185 )


        self.lang_frame = Frame(self.details_frame, height=35, width=100, bg="#B0AEAE", border=0, relief=SOLID)
        self.lang_frame.name = "lang_frame"
        self.lang_frame.place(x=350 , y=185 )
        self.movie_lang_label = Label(self.lang_frame, text=f"{self.lang}", font=("Comic Sans MS", 16),fg="#000000",bg="#B0AEAE")
        self.movie_lang_label.place(x=5, y=0)
        label_width = self.movie_lang_label.winfo_width() 
        print(len(self.lang)) 
        self.lang_frame.config(width = len(self.lang)*14) 

        if self.rating == 0:
            self.book_btn = ImageTk.PhotoImage(Image.open("comming_soon.png").resize((170,70)))
            self.book_now = Label(self.details_frame, image=self.book_btn, font=("Arial", 15),anchor=CENTER, activebackground="#ffffff",bg="white",border=1,relief=FLAT)
            self.book_now.place(x=350,y=240)
             
        else:
            self.book_btn = ImageTk.PhotoImage(Image.open("book.png").resize((170,80)))
            self.book_now = Button(self.details_frame, image=self.book_btn, font=("Arial", 15),anchor=CENTER, activebackground="#ffffff",bg="white",border=1,relief=FLAT)
            self.book_now.place(x=350,y=230)
            self.book_now.bind("<Button-1>",lambda x:self.data(x,user_data))
    #################################################################################################################################


        self.about_frames = Frame(self.inner_frame, height=370, width=400, bg="#6C1B1F", border=0, relief=SOLID)
        self.about_frames.name = "about_frames"
        self.about_frames.place(x=1000, y=470) 

        self.about_movie_curve = Image.open("rec97.png").resize((400,370 ))
        self.about_photo = ImageTk.PhotoImage(self.about_movie_curve)
        self.about_box_details = Label(self.about_frames, image=self.about_photo,bg="#6C1B1F",border=0,relief=FLAT)
        self.about_box_details.place(x=0,y=0) 


        self.about_label = Label(self.about_frames, text="About the Movie", font=("Roboto", 14, "bold"),fg="#000000",bg="white")
        self.about_label.place(x=20, y=25) 

        self.about_movie_label = Label(self.about_frames, text=self.about, font=("arial", 12, "normal"),fg="#000000",bg="white",justify=LEFT,wraplength=380)
        self.about_movie_label.place(x=20, y=65) 


    #################################################################################################################################
       

        self.x_cast_image = 0
        self.y_cast_image = 60

        self.cast_frame = Frame(self.inner_frame, height=220, width=1400, bg="#570416", border=0, relief=SOLID)
        self.cast_frame.name = "cast_frame"
        self.cast_frame.place(x=10, y=860)

        self.cast_photo = ImageTk.PhotoImage(Image.open("rec99.png").resize((1400,220 )))
        self.curve_box_cast = Label(self.cast_frame, image=self.cast_photo,bg="#6C1B1F",border=0,relief=FLAT)
        self.curve_box_cast.place(x=0,y=0)

        cast_db_store = Database_store.cast_details(self.name)
        # print(cast_db_store)

        for i in cast_db_store:
             self.add_new_circle(i[2],i[5],self.x_cast_image,self.y_cast_image)
                
                    
        

        self.cast_label = Label(self.cast_frame, text="Cast", font=("Roboto", 14, "bold"),fg="#000000",bg="white") 
        self.cast_label.place(x=50, y=25)
              

    #################################################################################################################################
        # Frame(self.inner_frame, height=470, width=1360, bg="#ffffff", border=0, relief=SOLID)
        self.rec_org = Image.open("rec98.png").resize((1400,570 ))
        self.rec_photo = ImageTk.PhotoImage(self.rec_org)
        self.curve_box_rec = Label(self.inner_frame, image=self.rec_photo,bg="#6C1B1F",border=0,relief=FLAT)
        self.curve_box_rec.place(x=10,y=1100)
        
        self.rec_frame = Frame(self.inner_frame, height=530, width=1370, bg="white", border=0, relief=SOLID)
        self.rec_frame.place(x=25, y=1110)

        self.canvasss = Frame(self.rec_frame,bg="#ffffff")
        self.canvasss.place(x=0,y=0,height=550, width=1360) 
        self.scrollbarss = Scrollbar(self.canvasss,orient=VERTICAL)
        self.scrollbarss.pack(side=RIGHT,fill=Y)
        self.form_framess = Canvas(self.canvasss,bg="#ffffff",yscrollcommand=self.scrollbarss.set)
        self.form_framess.pack(fill="both" ,side="left",expand=True) 
        self.scrollbarss.config(command=self.form_framess.yview)
        self.inner_framess = Frame(self.form_framess,bg="#ffffff",height=550,width=1360) 
        self.form_framess.create_window((0,0),window=self.inner_framess,anchor="nw")
                
                    
        self.upload_moive_screen_upcoming() 


    


        self.useless = Label(self.inner_frame,text="",bg="#ffffff")
        self.useless.pack(padx=850,pady=900)

        self.form_framess.update_idletasks()
        self.form_framess.config(scrollregion=self.form_framess.bbox("all"))


    def add_new_circle(self,name,imgs,x_img,y_img):

        label = Label(self.cast_frame,border=0)
        label.place(x=x_img+120,y=y_img)
        img = Image.open(imgs).convert("RGBA")
        mask = Image.new("L",(80,80),0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0,0,80,80),fill=255)
        img = img.resize((80,80))
        sq_mask = Image.new("RGBA",(100,100),(0,0,0,0))
        sq_mask.paste(img,(0,0),mask=mask)
        bg = Image.new("RGBA",(80,80),"#ffffff")
        bg.paste(sq_mask,(0,0),sq_mask)
        orignal_img = ImageTk.PhotoImage(bg)
        label.config(image=orignal_img)
        label.image = orignal_img
        
        cast_name = Label(self.cast_frame,text=str(name).replace(" ","\n"),font=("Arial",13,"bold"),bg="#ffffff",fg="#000000")
        if len(name) > 7:
            cast_name.place(x=self.x_cast_image+120,y=self.y_cast_image+90)
        elif len(name) == 6 :
            cast_name.place(x=self.x_cast_image+130,y=self.y_cast_image+90)
        elif len(name) == 5 :
            cast_name.place(x=self.x_cast_image+135,y=self.y_cast_image+90)
        elif len(name) == 4 :
            cast_name.place(x=self.x_cast_image+138,y=self.y_cast_image+90)
        elif len(name) == 3 :
            cast_name.place(x=self.x_cast_image+140,y=self.y_cast_image+90)
        else:
            cast_name.place(x=self.x_cast_image+140,y=self.y_cast_image+90)


        self.x_cast_image = self.x_cast_image+120


        

    def movie_frame(self,img,b):
                    
                    self.poster_frame.place(x=0,y=0)
                    self.local_frame = Frame(self.poster_frame, height=530, width=1500, bg="green", relief=GROOVE, border=1)
                    self.local_frame.bind("<Button-1>", self.askpython)
                    self.local_frame.place(x=0, y=0)



                    # self.p = ImageTk.PhotoImage(Image.open(img).resize((950,600 )))
                
            

                    self.kk_image = Label(self.local_frame, image=img, bg="white", border=1, relief=SOLID)
                    self.kk_image.place(x=0, y=0)
                    self.kk_image.bind("<Button-1>", self.askpython) 

                    self.play_btns = ImageTk.PhotoImage(Image.open("YT.png").resize((90,60)))
                    self.play_btn = Label(self.local_frame,image=self.play_btns,bg="black")
                    self.play_btn.place(relx=0.5,rely=0.5)
                    self.play_btn.bind("<Button-1>",self.play_pause)

    
    def play_pause(self,event):
        self.vlc = f"vlc \"{self.upload_t}\"".replace("/","\\")
        print(self.vlc)
        run(self.vlc ,shell=True).stdout

    def askpython():
          print("ok")
        
    
    def last_execute(self):
    
        self.form_frame.update_idletasks()
        self.form_frame.config(scrollregion=self.form_frame.bbox("all"))

        
    def data(self,event,user_data):
        print("Data")
        print(user_data)
        update_movie.show_cinemas(self.loc,self.name,self.time,user_data)

    def upcoming_frame_fn(self,movie_loc,name ,language ,genres ,date ,about ,triler ,poster ,time ,banner,xx,yy ):

            self.temp = 500
            if self.counter_up <= 4:
                if self.counter_up == 4:
                    # print("I am Three 4")
                    self.temp += 450 
                    self.y_axis_upcoming_movie_frame += 440 
                    self.x_axis_upcoming_movie_frame = 50
                    self.counter_up = 0
                    self.row_count_up += 1
                    self.inner_framess.config(height= self.temp)  #self.inner_framess.winfo_height() + 500)   
                    # print("yy")
                else:
                    
                    # self.inner_framess.config(height= self.inner_framess.winfo_height() + 500)   
                    self.x_axis_upcoming_movie_frame += 290
                    # print("xx")
                    self.temp = self.row_count_up 
                # print(self.counter_up)
                self.counter_up += 1
                


            self.upcoming_label = Label(self.inner_framess, text="Upcoming Movies", font=("Roboto", 14, "bold"),fg="#000000")
            self.upcoming_label.place(x=50, y=25)

            
        
            self.local_frame = Frame(self.inner_framess, height=400, width=250, bg="#6e051c", relief=GROOVE, border=1)
            self.local_frame.place(x=self.x_axis_upcoming_movie_frame, y=self.y_axis_upcoming_movie_frame)
            self.local_frame.bind("<Button-1>", lambda x: self.askpython(x, name, genres, xx,yy, 0 , movie_loc,banner,triler,date,time,about,language,self.user_data))


            self.kk_image = Label(self.local_frame, image=poster, bg="white", border=1, relief=SOLID)
            self.kk_image.place(x=12, y=10) 
            self.kk_image.bind("<Button-1>", lambda x: self.askpython(x,name, genres, xx,yy, 0 , movie_loc,banner,triler,date,time,about,language,self.user_data))

            self.frame_inside_img = Frame(self.kk_image,bg="#c4062f",height=50,width=250)
            self.frame_inside_img.place(x=0,y=280)
            self.frame_inside_img.bind("<Button-1>", lambda x: self.askpython(x, name, genres, xx,yy, 0 , movie_loc,banner,triler,date,time,about,language,self.user_data))

            self.date_inside = Label(self.frame_inside_img,text=f"Date : {date}",font=("Roboto",12,"bold"),bg="#c4062f",fg="white")
            self.date_inside.place(x=40,y=5)
            self.date_inside.bind("<Button-1>", lambda x: self.askpython(x, name, genres, xx,yy, 0 , poster,banner,triler,date,time,about,language,self.user_data))

            self.movie_name = Label(self.local_frame, text=name, font=("Arial", 16, "bold"), bg="#6e051c",fg="#cbeff2")
            self.movie_name.place(relx=0.5,rely=0.869 ,anchor=CENTER )
            self.movie_name.bind("<Button-1>", lambda x: self.askpython(x, name, genres, xx,yy, 0 , movie_loc,banner,triler,date,time,about,language,self.user_data))

            self.movie_UA = Label(self.local_frame, text=genres, font=("Arial", 13), bg="#6e051c",fg="#cbeff2")
            self.movie_UA.place(x=55, y=360)

            self.movie_UA.bind("<Button-1>", lambda x: self.askpython(x ,name, genres, xx,yy, 0 , movie_loc,banner,triler,date,time,about,language,self.user_data))


    def upload_moive_screen_upcoming(self):
        self.store_all_up = Database_store.upcoming_movie_show()
        for i in range(len(self.store_all_up)):
            self.movie_names_up.append(self.store_all_up[i][1])

            self.movie_posters_up.append(ImageTk.PhotoImage(Image.open(f"{self.store_all_up[i][7]}").resize((220, 310))))
            # self.upcoming_frame_fn(self.frame_uploaded_up,self.movie_posters_up[len(self.movie_posters_up)-1], self.store_all_up[i][1] , self.store_all_up[i][3] , self.x_axis_upcoming_movie_frame , self.y_axis_upcoming_movie_frame, self.store_all_up[i][7],self.store_all_up[i][4])
            self.upcoming_frame_fn(self.store_all_up[i][7],self.store_all_up[i][1] ,self.store_all_up[i][2] ,self.store_all_up[i][3] ,self.store_all_up[i][4],self.store_all_up[i][5],self.store_all_up[i][6] ,self.movie_posters_up[len(self.movie_posters_up)-1] ,self.store_all_up[i][8],self.store_all_up[i][9],self.x_axis_upcoming_movie_frame,self.y_axis_upcoming_movie_frame)
                                                                                                                            #    name ,language ,genres ,date ,about ,triler ,poster ,time ,banner 
    def askpython(self,event, movie_name, UA, c, b, rating , img, banner,trailer,date,time,about,lang,user_dataa):
            self.main.after(2000,self.destroy)
            details(movie_name, UA, c, b, rating , img, str(banner),trailer,date,time,about,lang,self.loc,user_dataa)
            
    def destroy(self):
         self.main.destroy()


        
        

  
if __name__ == "__main__":
         obj = test.mainfile(True)
    # obj = details()