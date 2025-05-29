from tkinter import *
import Login_Page
from datetime import date
import Database_store
from PIL import Image, ImageTk
from tkinter import Tk, Label
import time
import movie_detial
import update_movie
from tkinter import messagebox



user_details = []
###################################################################################################################################################################
#######################################__MAINFILE_CLASS__###################################################################################
###################################################################################################################################################################
class mainfile:
    def __new__(cls, *args, **kwargs):
        # Create the ect without calling __init__
        instance = super(mainfile, cls).__new__(cls)
        return instance
    

    def __init__(self,val,root,vals = True):
        # os.remove("users.txt")
        self.vals = vals
        self.main = root
        self.is_storeAll = False
        if vals:
            self.main.after(2000,self.userlogin)

        self.main.title("MoviesWave") 
        # self.main.attributes("-topmost",True)
        # self.main.attributes('-alpha',1)
        if val == False:
            self.main.geometry("2x2")
            # print(val)
        else:
            self.main.geometry(f"{self.main.winfo_screenwidth()}x{self.main.winfo_screenheight()}")
            self.main.state("zoomed")
        # print(value[1])
        self.main["bg"] = "#ffffff"
        self.movie_posters = []
        self.movie_posters_up = []
        self.frame_uploaded = []
        self.frame_uploaded_up = []
        self.gen_tu = []
        self.lang_li = []
        self.movie_names = []
        self.movie_names_up = []
        self.sort_tu = []
        self.frame_uploaded_up =[]
        self.change_screen = []
        self.cinema_store = []
        self.store_all_copy = []
        self.store_all = []
         

        dt = ""
        self.AK = ""
        self.name = ""
        self.email = ""
        self.name_len = 0

        self.user_data = []

        self.change_screen_counter = 0 
        self.districts = [
                    "Amritsar", "Barnala", "Bathinda", "Faridkot", "Fatehgarh Sahib", "Fazilka", "Ferozepur",
                    "Gurdaspur", "Hoshiarpur", "Jalandhar", "Kapurthala", "Ludhiana", "Mansa", "Moga", "Pathankot",
                    "Patiala", "Ropar", "Mohali", "Sangrur",
                    "Shahid Bhagat Singh Nagar ", "Sri Muktsar Sahib", "Tarn Taran"
                ] 


        self.after_use_x = []
        self.after_use_y = []
        self.after_use_xy = []

        self.x_axis_movie_frame = []
        self.y_axis_movie_frame = 15

        self.x_axis_movie_up_frame = 60
        self.y_axis_movie_up_frame = 80

        self.x_axis_latest_movie_frame = 60
        self.y_axis_latest_movie_frame = 15

        self.x_axis_bollywood_movie_frame = 60
        self.y_axis_bollywood_movie_frame = 15

        self.x_axis_hollywood_movie_frame = 60
        self.y_axis_hollywood_movie_frame = 15

        self.x_axis_south_movie_frame = 60
        self.y_axis_south_movie_frame = 15

        self.x_axis_punjabi_movie_frame = -240 
        self.y_axis_punjabi_movie_frame = 80

        self.counter = 0
        self.row_count = 0


        self.counter_up = 0
        self.row_count_up = 0
        self.x_axis_upcoming_movie_frame = -240 #50
        self.y_axis_upcoming_movie_frame = 80

        self.counter_slide = 0
        self.counter_slide_visible_left = 1500
        self.counter_slide_invisible_left = -450
        self.slide_center = 325
        self.slide_center_slide = 325
        self.one = 1

        self.user_data_l = Label(self.main)

        # self.width_r = self.right_frame.winfo_width()
        # self.height_r = self.right_frame.winfo_height()
        self.rt_slide = 1200
        self.rdt_slide = 1750

        self.movies_frame = Frame(self.main, height=800, width=1500, bg="white",  relief=FLAT,border=1)
        self.movies_frame.place(x=10, y=160)


        # self.db_retrive=Database_store.movie_show()
        self.current_frame = ""
        self.main_movie()
        self.upload_moive_screen()
        self.upload_moive_screen_upcoming()
        self.category()
        self.create_account_options()
        self.upper_frame()
        self.last_execute()

        if vals == True:
            self.distt_select_frame = Frame(self.inner_frame, height=600, width=800, bg="#570416",  relief=FLAT,border=1)
            self.distt_select_frame.place(x=400, y=120)
            self.distt_selection() 
        

        if vals == False:
            with open("distt.txt", "r") as file:
                content = file.read()
            self.data("",content) 

        if val == False:
            
            self.main.destroy()
        else:
            self.main.mainloop()





    def upper_frame(self):
        self.upper_blue_frame = Frame(self.inner_frame, width=self.main.winfo_screenwidth(), height=150, bg="#e6daba", border=0)
        self.upper_blue_frame.place(x=0, y=0)

        # Store the image as an instance variable
        self._imggg = Image.open("logo_black.png").resize((260, 120))
        self._imgg = ImageTk.PhotoImage(self._imggg) 
        self._logoo = Label(self.upper_blue_frame, image=self._imgg, bg="#e6daba")
        self._logoo.place(x=4, y=5)

        # self.search = Entry(self.upper_blue_frame, width=50, font=("Arial", 15, "normal"), bg="white", relief=SOLID, border=1, fg="#a8a59b")
        # self.search.place(x=340, y=30)
        # self.search.insert(0, "Search for Movies ... ")
        # self.search.bind('<Button-1>', self.search_box)

        self.sign_in = Button(self.upper_blue_frame, text="Sign in", font=("Tw Cen MT", 12, "bold"), bg="#122a6e", fg="white", command=self.login)
        self.sign_in.place(x=1400, y=30)


    def category(self):
        self.counter_submit_click = False
        self.counter_reset_click = False
        self.category_frame = Frame(self.inner_frame, width=400, height=930, bg="#e6daba", border=0, relief=FLAT)
        self.category_frame.place(x=10, y=600)

        self.curve_img_category = ImageTk.PhotoImage(Image.open("rec96.png").resize((390,930 )))
        self.curve_box_cate = Label(self.category_frame, image=self.curve_img_category, bg="#e6daba")
        self.curve_box_cate.place(x=0,y=0)


        self.curve_img = ImageTk.PhotoImage(Image.open("curve_box.png").resize((300,300 )))

        self.hindi_whit = ImageTk.PhotoImage(Image.open("white_circle.png").resize((10, 10)))

        self.genres = Label(self.category_frame, text="Genres ", font=("Arial", 18, "bold"), bg="#fcfafa", fg="#212121")
        self.genres.place(x=48, y=40)

        self.action_cond = self.animation_cond = self.biographiy_cond = self.comdy_cond = self.crime_cond = self.drama_cond = self.family_cond = self.fantsy_cond = self.historical_cond = self.horror_cond = self.musical_cond = self.mystery_cond = self.oth_gen_cond = self.romantic_cond = self.sci_fi_cond = self.thiller_cond = self.war_cond = False

        self.frame_gen = Frame(self.category_frame,height=350,width=320,bg="white")
        self.frame_gen.place(x=40,y=80)
        self.curve_box = Label(self.frame_gen, image=self.curve_img, bg="white")
        self.curve_box.place(x=0,y=0)

        self.gen_frame()

        self.sort = Label(self.category_frame, text="Sort By ", font=("Arial", 18, "bold"), bg="#fcfafa", fg="#212121")
        self.sort.place(x=48, y=400)

        self.revelence_cond = True
        self.new_to_old_cond = False
        self.old_to_new_cond = False

        self.frame_sort = Frame(self.category_frame,height=150,width=300,bg="white")
        self.frame_sort.place(x=40,y=440)

        self.curve_img_sort = ImageTk.PhotoImage(Image.open("rectangle_curve.png").resize((300,120 )))
        self.curve_box_sort = Label(self.frame_sort, image=self.curve_img_sort, bg="white")
        self.curve_box_sort.place(x=0,y=0)


        self.circle_sort(15, 10, "Relevance", self.revelence_cond)
        self.circle_sort(15, 45, "Release date : New to Old", self.new_to_old_cond)
        self.circle_sort(15, 80, "Release date : Old to New", self.old_to_new_cond)


        self.lang = Label(self.category_frame, text="Language ", font=("Arial", 18, "bold"), bg="white", fg="#212121")
        self.lang.place(x=48, y=580)

        self.frame_lang = Frame(self.category_frame,height=170,width=320,bg="white")
        self.frame_lang.place(x=40,y=620)


        self.curve_img_lang = ImageTk.PhotoImage(Image.open("rectangle_curve.png").resize((300,160 )))
        self.curve_box_lang = Label(self.frame_lang, image=self.curve_img_lang, bg="white")
        self.curve_box_lang.place(x=0,y=0)


        self.all_cond = True
        self.eng_cond = self.hin_cond = self.pun_cond = self.mar_cond = self.tel_cond = self.ben_cond = self.guj_cond = self.oth_cond = False

        self.circle_lang(15, 20, "All", self.all_cond)
        self.circle_lang(15, 55, "English", self.eng_cond)
        self.circle_lang(15, 90, "Hindi", self.hin_cond)
        self.circle_lang(15, 125, "Punjabi", self.pun_cond)

        self.circle_lang(160, 20, "Malayalam", self.mar_cond)
        self.circle_lang(160, 55, "Telegu", self.tel_cond)
        self.circle_lang(160, 90, "Tamil", self.ben_cond)
        self.circle_lang(160, 125, "Kannada", self.guj_cond)

        self.submit = Button(self.category_frame, text="Submit", font=("Arial", 12, "normal"), fg="White",bg="green", border=0, relief=SOLID,command=self.submit_click)
        self.submit.place(x=115,y=820)

        self.reset = Button(self.category_frame, text="Reset", font=("Arial", 12, "normal"), fg="White",bg="red", border=0, relief=SOLID,command=self.reset_click)
        self.reset.place(x=118,y=860)



    def reset_click(self):
        
            # self.store_all = temp
            self.is_storeAll = False

            for i in self.inner_frames.winfo_children():
                i.destroy()
            
            self.x_axis_punjabi_movie_frame = -240 
            self.y_axis_punjabi_movie_frame = 80
            self.inner_frames.config(width=920)
            self.inner_frames.config(height=480)
            # self.canvass.config(height=480)
            self.counter = 0
            self.counter_submit_click = True
            self.counter_reset_click = True
            self.upload_moive_screen()
       


    def submit_click(self):
        temp = []
        print("########################################### ")
        print("Selected Language : ",self.lang_li)
        print("Selected Generus : ",self.gen_tu)
        print("Store All : ",self.store_all)
        print("Store All copy : ",self.store_all_copy) 
        print("########################################### ")
        if len(self.lang_li) == 0 and len(self.gen_tu) == 0:
            if self.counter_submit_click == True:
                self.reset_click()
                self.counter_submit_click = False
            else:    
                pass
            

        else:
            for i in range(len(self.store_all_copy)):
                # for  in self.store_all:
                # for j in self.store_all[i]:
                    # if self.gen_tu in j[3]:
                if len(self.lang_li) != 0 and len(self.gen_tu) != 0: 
                    if self.store_all_copy[i][3] in self.gen_tu and self.store_all_copy[i][2] in self.lang_li:
                            # print(self.store_all[i]) 
                            temp.append(self.store_all_copy[i])
                elif len(self.lang_li) != 0 and len(self.gen_tu) == 0: 
                    if self.store_all_copy[i][2] in self.lang_li:
                            # print(self.store_all[i]) 
                            temp.append(self.store_all_copy[i])
                elif len(self.lang_li) == 0 and len(self.gen_tu) != 0:
                    if self.store_all_copy[i][3] in self.gen_tu:
                            # print(self.store_all[i]) 
                            temp.append(self.store_all_copy[i])

            self.store_all = temp
            self.is_storeAll = True

            for i in self.inner_frames.winfo_children():
                i.destroy()
            
            self.x_axis_punjabi_movie_frame = -240 
            self.y_axis_punjabi_movie_frame = 80
            self.inner_frames.config(width=920)
            self.inner_frames.config(height=480)
            # self.canvass.config(height=480)
            self.counter = 0
            self.counter_submit_click = True
            self.counter_reset_click = True
            # self.row_count = 0
            # height=930, width=920
            # width=920,height=480

            self.upload_moive_screen()
                    




    def circle_lang(self, xx, yy, lang_name, cond):
        if cond:
            image = ImageTk.PhotoImage(Image.open("black_circle.png").resize((10, 10)))
        else:
            image = self.hindi_whit

        self.lang_circle = Label(self.frame_lang, image=image, bg="#ebe6e6")
        self.lang_circle.image = image  # Keep a reference to avoid garbage collection
        self.lang_circle.place(x=xx, y=yy)
        self.lang_circle.bind("<Button-1>", lambda x: self.language_circle_change(lang_name))
        
        self.lang_label = Label(self.frame_lang, text=lang_name, font=("Arial", 13, "normal"), fg="#000000", bg="#ebe6e6")
        self.lang_label.place(x=xx + 17, y=yy - 7)

    def language_circle_change(self, lang_name):
        if lang_name == "All":
            self.all_cond = True
            self.eng_cond = self.hin_cond = self.pun_cond = self.mar_cond = self.tel_cond = self.ben_cond = self.guj_cond = self.oth_cond = False
        elif lang_name == "English":
            self.eng_cond = True
            self.all_cond = self.hin_cond = self.pun_cond = self.mar_cond = self.tel_cond = self.ben_cond = self.guj_cond = self.oth_cond = False
        elif lang_name == "Punjabi":
            self.pun_cond = True
            self.all_cond = self.eng_cond = self.hin_cond = self.mar_cond = self.tel_cond = self.ben_cond = self.guj_cond = self.oth_cond = False
        elif lang_name == "Malayalam":
            self.mar_cond= True
            self.all_cond = self.eng_cond = self.hin_cond = self.pun_cond = self.tel_cond = self.ben_cond = self.guj_cond = self.oth_cond = False
        elif lang_name == "Telegu":
            self.tel_cond= True
            self.all_cond = self.eng_cond = self.hin_cond = self.pun_cond = self.mar_cond = self.ben_cond = self.guj_cond = self.oth_cond = False
        elif lang_name == "Tamil":
            self.ben_cond= True
            self.all_cond = self.eng_cond = self.hin_cond = self.pun_cond = self.mar_cond = self.tel_cond = self.guj_cond = self.oth_cond = False
        elif lang_name == "Kannada":
            self.guj_cond= True
            self.all_cond = self.eng_cond = self.hin_cond = self.pun_cond = self.mar_cond = self.tel_cond = self.ben_cond = self.oth_cond = False
        elif lang_name=="Hindi":
            self.hin_cond = True
            self.all_cond = self.eng_cond  = self.pun_cond = self.mar_cond = self.tel_cond = self.ben_cond = self.guj_cond = self.oth_cond = False

        else:
            self.oth_cond = not self.oth_cond
        
        if lang_name in self.lang_li: 
            self.lang_li.remove(lang_name)
        elif lang_name == 'All': 
            self.lang_li.clear()
        else: 
            self.lang_li.clear()
            self.lang_li.append(lang_name)

        print(self.lang_li) 
        self.update_language_selection()

    def update_language_selection(self):
        self.circle_lang(15, 20, "All", self.all_cond)
        self.circle_lang(15, 55, "English", self.eng_cond)
        self.circle_lang(15, 90, "Hindi", self.hin_cond)
        self.circle_lang(15, 125, "Punjabi", self.pun_cond)

        self.circle_lang(160, 20, "Malayalam", self.mar_cond)
        self.circle_lang(160, 55, "Telegu", self.tel_cond)
        self.circle_lang(160, 90, "Tamil", self.ben_cond)
        self.circle_lang(160, 125, "Kannada", self.guj_cond)

       

        # print(self.lang_li)
        


    def gen_frame(self):


        self.circle_gen(20, 10, "Action", self.action_cond)
        self.circle_gen(20, 45, "Animation", self.animation_cond)
        self.circle_gen(20, 80, "Biography", self.biographiy_cond)
        self.circle_gen(20, 115, "Comedy", self.comdy_cond)
        self.circle_gen(20, 150, "Drama", self.drama_cond)
        self.circle_gen(20, 185, "Family", self.family_cond)
        self.circle_gen(20, 220, "Fantsy", self.fantsy_cond)
        self.circle_gen(20, 255, "Historical", self.historical_cond)
        self.circle_gen(160, 10, "Horror", self.horror_cond)
        self.circle_gen(160, 45, "Musical", self.musical_cond)
        self.circle_gen(160, 80, "Mystery", self.mystery_cond)
        self.circle_gen(160, 115, "Romantic", self.romantic_cond)
        self.circle_gen(160, 150, "Sci-Fi", self.sci_fi_cond)
        self.circle_gen(160, 185, "Thiller", self.thiller_cond)
        self.circle_gen(160, 220, "War", self.war_cond)
        self.circle_gen(160, 255, "Other", self.oth_gen_cond)

    def circle_gen(self, xx, yy, lang_name, cond):
        if cond:
            image = ImageTk.PhotoImage(Image.open("check.png").resize((10, 10)))
        else:
            image =  self.hindi_whit


        self.lang_circle = Label(self.frame_gen, image=image)
        self.lang_circle.image = image  # Keep a reference to avoid garbage collection
        self.lang_circle.place(x=xx, y=yy+8)
        self.lang_circle.bind("<Button-1>", lambda x: self.gen_circle_change(lang_name))
        
        self.lang_label = Button(self.frame_gen, text=lang_name, font=("Arial", 13, "normal"), fg="black", bg="#ebe6e6",bd=0, activebackground="#ffffff")
        self.lang_label.place(x=xx+15, y=yy-2)
        
    def circle_sort(self, xx, yy, lang_name, cond):
        if cond:
            image = ImageTk.PhotoImage(Image.open("black_circle.png").resize((10, 10)))
        else:
            image =  self.hindi_whit


        self.lang_circle = Label(self.frame_sort, image=image)
        self.lang_circle.image = image  # Keep a reference to avoid garbage collection
        self.lang_circle.place(x=xx, y=yy+8)
        self.lang_circle.bind("<Button-1>", lambda x: self.sort_circle_change(lang_name))
        
        self.lang_label = Button(self.frame_sort, text=lang_name, font=("Arial", 13, "normal"), fg="black", bg="#ebe6e6",bd=0, activebackground="#ffffff")
        self.lang_label.place(x=xx+15, y=yy-2)
    
    def sort_circle_change(self, gen_name):
        if gen_name == "Relevance":
            self.revelence_cond = True
            self.old_to_new_cond = False
            self.new_to_old_cond = False
        elif gen_name == "Release date : New to Old":
            self.revelence_cond = False
            self.old_to_new_cond = False
            self.new_to_old_cond = True
        else:
            self.revelence_cond = False
            self.old_to_new_cond = True
            self.new_to_old_cond = False



        if gen_name in self.sort_tu:
            self.sort_tu.remove(gen_name)
        else: 
            self.sort_tu.append(gen_name)


        # print(self.sort_tu)
        

        self.update_sort_selection()

    def update_sort_selection(self):
        self.circle_sort(15, 10, "Relevance", self.revelence_cond)
        self.circle_sort(15, 45, "Release date : New to Old", self.new_to_old_cond)
        self.circle_sort(15, 80, "Release date : Old to New", self.old_to_new_cond)

    def gen_circle_change(self, gen_name):
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
        elif gen_name=="War":
            self.war_cond = not self.war_cond
        else:
            self.oth_cond = not self.oth_cond

    # for i in :
        if gen_name in self.gen_tu:
            self.gen_tu.remove(gen_name)
        else: 
            self.gen_tu.append(gen_name)


        # print(self.gen_tu)
        

        self.update_genre_selection()

    def update_genre_selection(self):
        self.circle_gen(20, 10, "Action", self.action_cond)
        self.circle_gen(20, 45, "Animation", self.animation_cond)
        self.circle_gen(20, 80, "Biography", self.biographiy_cond)
        self.circle_gen(20, 115, "Comedy", self.comdy_cond)
        self.circle_gen(20, 150, "Drama", self.drama_cond)
        self.circle_gen(20, 185, "Family", self.family_cond)
        self.circle_gen(20, 220, "Fantsy", self.fantsy_cond)
        self.circle_gen(20, 255, "Historical", self.historical_cond)
        self.circle_gen(160, 10, "Horror", self.horror_cond)
        self.circle_gen(160, 45, "Musical", self.musical_cond)
        self.circle_gen(160, 80, "Mystery", self.mystery_cond)
        self.circle_gen(160, 115, "Romantic", self.romantic_cond)
        self.circle_gen(160, 150, "Sci-Fi", self.sci_fi_cond)
        self.circle_gen(160, 185, "Thiller", self.thiller_cond)
        self.circle_gen(160, 220, "War", self.war_cond)
        self.circle_gen(160, 255, "Other", self.oth_gen_cond)






    def main_movie(self):

        self.canvas = Frame(self.main,bg="#e6daba",bd=5)
        self.canvas.place(x=0,y=0,height=800,width=1540)
        self.scrollbar = Scrollbar(self.canvas,orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.form_frame = Canvas(self.canvas,bg="#e6daba",yscrollcommand=self.scrollbar.set)
        self.form_frame.pack(fill="both" ,side="left",expand=True)
        self.scrollbar.config(command=self.form_frame.yview)
        self.inner_frame = Frame(self.form_frame,bg="#e6daba",width=300)
        self.form_frame.create_window((0,0),window=self.inner_frame,anchor="nw")

   
   
        self.latest_frame = Frame(self.inner_frame, height=430, width=1500, bg="#570416", border=0, relief=SOLID)
        self.latest_frame.name = "latest_frame"
        
        self.curve_img_movie = ImageTk.PhotoImage(Image.open("long_rec.png").resize((980,930 )))
        self.curve_box_movie = Label(self.inner_frame, image=self.curve_img_movie,bg="#e6daba",border=0,relief=FLAT)
        self.curve_box_movie.place(x=440,y=600)
 
        self.punjabi_frame = Frame(self.inner_frame, height=870, width=920, bg="#570416", border=0, relief=SOLID)
        self.punjabi_frame.place(x=480, y=620)
        self.punjabi_frame.name = "punjabi_frame"

        self.canvass = Frame(self.punjabi_frame,bg="#ffffff",bd=5)
        self.canvass.place(x=0,y=0,height=930, width=920) 
        self.scrollbars = Scrollbar(self.canvass,orient=VERTICAL)
        self.scrollbars.pack(side=RIGHT,fill=Y)
        self.form_frames = Canvas(self.canvass,bg="#ffffff",yscrollcommand=self.scrollbars.set)
        self.form_frames.pack(fill="both" ,side="left",expand=True) 
        self.scrollbars.config(command=self.form_frames.yview)
        self.inner_frames = Frame(self.form_frames,bg="#ffffff",width=920,height=480) 
        self.form_frames.create_window((0,0),window=self.inner_frames,anchor="nw")



        self.upcoming_movie_curve = Image.open("rec98.png").resize((1400,520 ))
        self.upcoming_photo = ImageTk.PhotoImage(self.upcoming_movie_curve)
        self.curve_box_upcoming = Label(self.inner_frame, image=self.upcoming_photo,bg="#e6daba",border=0,relief=FLAT)
        self.curve_box_upcoming.place(x=10, y=1700 )

        self.upcoming_frame = Frame(self.inner_frame, height=470, width=1360, bg="#ffffff", border=0, relief=SOLID)
        self.upcoming_frame.place(x=20, y=1720)
        self.upcoming_frame.name = "upcoming_frame"


        # self.curve_box_upcoming.place(x=0,y=0)
        
        
        self.canvasss = Frame(self.upcoming_frame,bg="#ffffff")
        self.canvasss.place(x=0,y=0,height=470, width=1360) 
        self.scrollbarss = Scrollbar(self.canvasss,orient=VERTICAL)
        self.scrollbarss.pack(side=RIGHT,fill=Y)
        self.form_framess = Canvas(self.canvasss,bg="#ffffff",yscrollcommand=self.scrollbarss.set)
        self.form_framess.pack(fill="both" ,side="left",expand=True) 
        self.scrollbarss.config(command=self.form_framess.yview)
        self.inner_framess = Frame(self.form_framess,bg="#ffffff",height=470,width=1360) 
        self.form_framess.create_window((0,0),window=self.inner_framess,anchor="nw")

  




        self.south_frame = Frame(self.inner_frame, height=430, width=1500, bg="#570416", border=0, relief=SOLID)
        self.south_frame.name = "south_frame"

        self.latest_movies = Label(self.inner_frame, text="Latest Movies", font=("Roboto", 20, "bold"), bg="#570416",fg="#cbeff2")




        self.south_movies = Label(self.inner_frame, text="South Movies", font=("Roboto", 20, "bold"), bg="#570416",fg="#cbeff2")

        



        # self.extra_frames = Frame(self.curve_box_movie,bg="#e6daba",bd=5)
        # self.extra_frames.place(x=35,y=20,height=2280, width=900) 
        

    
        self.useless = Label(self.inner_frame,text="",bg="#ffffff")
        self.useless.pack(padx=930,pady=1100)


 

    def allscreenshandler(self,frame_uploaded,movie_loc, movie_name, UA, c, b, rating , img,banner,trailer,date,time,about,lang):

                    frame_name = "latest_frame"
                    # print(f"Processing Frame : {frame_name}")
                    
                    if frame_name == "latest_frame":

                        if self.change_screen_counter == 0:

                            self.central_frame = Frame(self.latest_frame, height=400, width=850, bg="orange", relief=GROOVE, border=1)
                            self.left_frame = Frame(self.latest_frame, height=300, width=750, bg="purple", relief=GROOVE, border=1)
                            self.left_frame.bind("<Button-1>", self.askpython)
                            self.left_frame.place(x=-450, y=b+50)
                            # self.left_frame.place_forget()



                            self.left_upper = ImageTk.PhotoImage(Image.open(self.change_screen[0]).resize((850,400 )))
                        
                    

                            self.left_image = Label(self.left_frame, image=self.left_upper, bg="pink", border=1, relief=SOLID)
                            self.left_image.place(x=0, y=0)
                            self.left_image.bind("<Button-1>", self.askpython) 


                            self.change_screen_counter += 1
                        



                        ################################################################################################
                        ################################################################################################
                        elif self.change_screen_counter == 1:

                            self.latest_frame.place(x=10, y=150)

                            self.central_frame.bind("<Button-1>", self.askpython)
                            self.central_frame.place(x=325, y=b)



                            self.punjabi_upper = ImageTk.PhotoImage(Image.open(self.change_screen[1]).resize((850,400 )))
                        
                    

                            self.kk_image = Label(self.central_frame, image=self.punjabi_upper, bg="green", border=1, relief=SOLID)
                            self.kk_image.place(x=0, y=0)
                            self.kk_image.bind("<Button-1>", self.askpython)

                            self.change_screen_counter += 1

                        ################################################################################################
                        #############################################################################################33
                        elif self.change_screen_counter == 2:

                            self.right_frame = Frame(self.latest_frame, height=300, width=750, bg="yellow", relief=GROOVE, border=0)
                            self.right_frame.bind("<Button-1>", self.askpython)
                            self.right_frame.place(x=1200, y=b+50)



                            self.right_upper = ImageTk.PhotoImage(Image.open(self.change_screen[2]).resize((850,400 )))
                        
                    

                            self.right_image = Label(self.right_frame, image=self.right_upper, bg="#570416", border=1, relief=SOLID)
                            self.right_image.place(x=0, y=0)
                            self.right_image.bind("<Button-1>", self.askpython) 

                            # self.left_frame_dupl = self.left_frame
                            # self.left_frame_dupl.place(x=1200,y=b+50) 

                            self.change_screen_counter += 1

            

                        # self.frame_inside_img = Frame(self.kk_image,bg="#c4062f",height=50,width=250)
                        # self.frame_inside_img.place(x=0,y=280)

                        # self.rating_inside = Label(self.frame_inside_img,text=f"Rating : {rating} / 10",font=("Roboto",12,"bold"),bg="#c4062f",fg="white")
                        # self.rating_inside.place(x=40,y=5)

                        # self.movie_name = Label(self.local_frame, text=movie_name, font=("Arial", 16, "bold"), bg="#6e051c",fg="#cbeff2")
                        # self.movie_name.place(relx=0.5,rely=0.869 ,anchor=CENTER )
                        # self.movie_name.bind("<Button-1>", self.askpython)

                        # self.movie_UA = Label(self.local_frame, text=UA, font=("Arial", 13), bg="#6e051c",fg="#cbeff2")
                        # self.movie_UA.place(x=55, y=360)
                        # self.movie_UA.bind("<Button-1>", self.askpython)

                        self.x_axis_latest_movie_frame += 290
                    
                    try:
                        self.current_frame = self.central_frame
                        # This Line useful for Sliding the Screen
                        # self.current_frame.after(5000, self.automatic_switch)
                    except Exception as e:
                        print(e)
                

            # if frame_name == "latest_frame:":        

                    
                    # if self.counter < 2:
                    #     self.x_axis_punjabi_movie_frame += 290
                    #     self.row_count += 1
                    #     print("x")

                    # else :
                    #     self.inner_frames.config(height= self.inner_frames.winfo_height() + 500)
                    #     self.y_axis_punjabi_movie_frame += 440
                    #     self.x_axis_punjabi_movie_frame = 50
                    #     print("y")

                    # self.temp1 = 500
                    self.temp1 = 870
                    if self.counter <=3 : 
                        if self.counter == 3:
                            self.temp1 += 580
                            # print("I am Three 4")
                            self.y_axis_punjabi_movie_frame += 440 
                            self.x_axis_punjabi_movie_frame = 50 
                            self.counter = 0
                            self.row_count += 1
                            self.inner_frames.config(height= self.temp1)   

                        else:
                            # if self.temp1 != self.row_count:
                                # print(f"This is row Count  -----  {self.row_count}\nAnd this is Temp1 ------- {self.temp1}")
                            self.x_axis_punjabi_movie_frame += 290
                            # print("xx")
                            self.temp1 = self.row_count

                        # print(self.counter)
                        self.counter += 1
                        
                    
                    
                    self.latest_movies = Label(self.inner_frames, text="Latest Movies", font=("Roboto", 14, "bold"),fg="#000000")
                    self.latest_movies.place(x=50, y=25)
                
                    self.local_frame = Frame(self.inner_frames, height=400, width=250, bg="#6e051c", relief=GROOVE, border=1)
                    self.local_frame.bind("<Button-1>",lambda x: self.askpython(x, movie_name, UA, c, b, rating , img,banner,trailer,date,time,about,lang,self.user_data))
                    self.local_frame.place(x=self.x_axis_punjabi_movie_frame, y=self.y_axis_punjabi_movie_frame)


                    self.kk_image = Label(self.local_frame, image=movie_loc, bg="white", border=1, relief=SOLID)
                    self.kk_image.place(x=12, y=10)
                    self.kk_image.bind("<Button-1>", lambda x: self.askpython(x, movie_name, UA, c, b, rating , img,banner,trailer,date,time,about,lang,self.user_data)) 

                    self.frame_inside_img = Frame(self.kk_image,bg="#c4062f",height=50,width=250)
                    self.frame_inside_img.place(x=0,y=280)

                    self.rating_inside = Label(self.frame_inside_img,text=f"Rating : {rating} / 10",font=("Roboto",12,"bold"),bg="#c4062f",fg="white")
                    self.rating_inside.place(x=40,y=5)

                    self.movie_name = Label(self.local_frame, text=movie_name, font=("Arial", 16, "bold"), bg="#6e051c",fg="#cbeff2")
                    self.movie_name.place(relx=0.5,rely=0.869 ,anchor=CENTER )
                    self.movie_name.bind("<Button-1>", lambda x: self.askpython(x,movie_name, UA, c, b, rating , img,banner,trailer,date,time,about,lang,self.user_data))

                    self.movie_UA = Label(self.local_frame, text=UA, font=("Arial", 13), bg="#6e051c",fg="#cbeff2")
                    self.movie_UA.place(x=55, y=360)
                    self.movie_UA.bind("<Button-1>", lambda x: self.askpython(x,movie_name, UA, c, b, rating , img,banner,trailer,date,time,about,lang,self.user_data))

                    # self.main.update()



    def slide_in(self):
        
  
    
 
        for x in range(325, -740, -2):
            
            # if x > 325:

            if self.slide_center > -545:
                self.right_frame.place(x=self.rt_slide, y=self.y_axis_movie_frame)
                self.rt_slide -= 2
                if self.slide_center_slide > -450 :
                    self.central_frame.place(x=self.slide_center_slide, y=self.y_axis_movie_frame+50)
                    # print(self.slide_center)

                if self.counter_slide_invisible_left > -800:
                    self.left_frame.place(x=self.counter_slide_invisible_left,y=self.y_axis_movie_frame+50)
                    self.counter_slide_invisible_left -= 2
                    
                else :
                    if self.rdt_slide > 1200:
                        self.left_frame.place(x=self.rdt_slide , y=self.y_axis_movie_frame+50)
                        self.rdt_slide -= 2
                        # print(self.rdt_slide)
                    elif self.rdt_slide == 1200:
                          
                        self.left_frame.place(x=1200 , y=self.y_axis_movie_frame+50)
                        # This Line useful for Sliding the Screen
                        # self.counter_slide_visible_left -= 2 
                    

                self.slide_center_slide -= 2
                self.slide_center -= 2
                

            if self.counter_slide < 11  :
                self.right_frame.config(height=self.right_frame.winfo_height()+8)
                self.right_frame.config(width=self.right_frame.winfo_width()+9)
                if self.counter_slide < 1:
                    self.central_frame.config(height=300)
                    self.central_frame.config(width=750)
            self.counter_slide += 1

            
            # self.main.update()

        self.counter_slide = 0
        self.counter_slide_visible_left = 1500
        self.counter_slide_invisible_left = -450
        self.slide_center = 325
        self.slide_center_slide = 325
        # self.width_r = self.right_frame.winfo_width()
        # self.height_r = self.right_frame.winfo_height()
        self.rt_slide = 1200
        self.rdt_slide = 1800

        return self.central_frame


    
    def automatic_switch(self):

        # print("I am running")
        # global self.current_frame
        # print(self.current_frame)

        if self.current_frame == self.central_frame:
            try:
                self.slide_in()
                self.current_frame.after(20000, self.automatic_switch)
            except Exception as e:
                print()
            # print("match") 
            time.sleep(3)
        else :
            print("not match")

        
        self.temp_frame = self.central_frame
        self.central_frame = self.right_frame
        self.right_frame = self.left_frame
        self.left_frame = self.temp_frame
        # self.central_frame =  self.left_frame
        self.current_frame = self.central_frame
        

        # elif self.current_frame == self.right_frame:
        #     slide_in(self._frame, frame2, "left")
        #     self.current_frame = frame1

        
    def cinema_frame_fn(self):

            self.cinema_frame = Frame(self.inner_frame, height=130, width=1400, bg="#570416", border=0, relief=SOLID)
            self.cinema_frame.name = "cinema_frame"

            self.cinema_photo = ImageTk.PhotoImage(Image.open("rec99.png").resize((1400,130 )))
            self.curve_box_cinema = Label(self.cinema_frame, image=self.cinema_photo,bg="#e6daba",border=0,relief=FLAT)
            self.curve_box_cinema.place(x=0,y=0)


                
                    
            self.cinema_frame.place(x=10, y=1550)

            self.cinema_label = Label(self.cinema_frame, text="Popular Cinemas", font=("Roboto", 14, "bold"),fg="#000000")
            self.cinema_label.place(x=50, y=25)
            
            xx = 50
            yy = 75
            # print(self.cinema_store,"sada")
            for i in range(len(self.cinema_store)):
                self.cinema_name = Label(self.cinema_frame, text=f"{self.cinema_store[i]}", font=("Roboto", 12, "normal"),fg="#000000")
                self.cinema_name.place(x=xx , y=yy)
                xx += self.cinema_name.winfo_reqwidth() + 20

            #print(f"{self.cinema_name.winfo_width()} data") 
            


        
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
                        


                    self.upcoming_label = Label(self.inner_framess, text="Upcoming Movies ", font=("Roboto", 14, "bold"),fg="#000000")
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

    def search_box(self, event):
        self.search.delete(0, END)

    def askpython(self,event, movie_name, UA, c, b, rating , img, banner,trailer,date,time,about,lang,user_dataa):
        # self.main.destroy()
            # with open("users.txt", "r") as file:
            #     content = file.read()
            #     # print("File content:", content)
            #     self.user_data.append(content)
            #     dt =  ((str(self.user_data[0]).replace('(','')).replace(')','').replace('\'',"").split(","))
            #     print(dt)
            # os.remove("users.txt")
            # print("*************************************************")
            # print(self.) 
            # print("*************************************************")
            movie_detial.details(movie_name, UA, c, b, rating , img, str(banner),trailer,date,time,about,lang,self.distt_name,user_dataa)

    def login(self):
        # self.main.destroy()
        Login_Page.LoginWindow("User") 

    def admin_login(self):
        self.main.destroy()
        Login_Page.LoginWindow("Admin")

    def upload_moive_screen(self):
        
        if self.is_storeAll == False:

            self.store_all_copy = Database_store.movie_show()
            self.store_all = Database_store.movie_show()
            self.store_all = self.store_all_copy 
        
        # print(self.store_all)
        # self.x_axis_movie_frame.append(self.x_axis_latest_movie_frame)
        # self.frame_uploaded.clear()
        # self.movie_names.clear()
        # self.change_screen.clear()
        # self.movie_posters.clear()
        # else:
        for i in range(len(self.store_all)): 
            self.frame_uploaded.clear()
            # print(type(self.store_all[i][2]),self.store_all[i][2],self.store_all[i][1],end="\n")
            self.frame_uploaded.append(self.latest_frame)
            self.movie_names.append(self.store_all[i][1])


            self.movie_posters.append(ImageTk.PhotoImage(Image.open(f"{self.store_all[i][8]}").resize((220, 310))))
            self.change_screen.append(f"{self.store_all[i][10]}")
            self.allscreenshandler(self.frame_uploaded,self.movie_posters[len(self.movie_posters)-1], self.store_all[i][1] , self.store_all[i][3] , self.x_axis_movie_frame , self.y_axis_movie_frame, self.store_all[i][7],self.store_all[i][8],self.store_all[i][10],self.store_all[i][6],self.store_all[i][4],self.store_all[i][9],self.store_all[i][5],self.store_all[i][2])

        # return self.movie_names
            # print(self.store_all[i][4])

    def upload_moive_screen_upcoming(self):
        self.store_all_up = Database_store.upcoming_movie_show()
        for i in range(len(self.store_all_up)):
            self.movie_names_up.append(self.store_all_up[i][1])
            print(self.store_all_up[i])
            self.movie_posters_up.append(ImageTk.PhotoImage(Image.open(f"{self.store_all_up[i][7]}").resize((220, 310))))
            # self.upcoming_frame_fn(self.frame_uploaded_up,self.movie_posters_up[len(self.movie_posters_up)-1], self.store_all_up[i][1] , self.store_all_up[i][3] , self.x_axis_upcoming_movie_frame , self.y_axis_upcoming_movie_frame, self.store_all_up[i][7],self.store_all_up[i][4])
            self.upcoming_frame_fn(self.store_all_up[i][7],self.store_all_up[i][1] ,self.store_all_up[i][2] ,self.store_all_up[i][3] ,self.store_all_up[i][4],self.store_all_up[i][5],self.store_all_up[i][6] ,self.movie_posters_up[len(self.movie_posters_up)-1] ,self.store_all_up[i][8],self.store_all_up[i][9],self.x_axis_upcoming_movie_frame,self.y_axis_upcoming_movie_frame)
                                                                                                                            #    name ,language ,genres ,date ,about ,triler ,poster ,time ,banner 


    def last_execute(self):
        self.form_frame.update_idletasks()
        self.form_frame.config(scrollregion=self.form_frame.bbox("all"))

        self.form_frames.update_idletasks()
        self.form_frames.config(scrollregion=self.form_frames.bbox("all"))

        self.form_framess.update_idletasks()
        self.form_framess.config(scrollregion=self.form_framess.bbox("all"))
    

    def destroy(self):
        # print("naa")
        self.main.destroy()

    def userlogin(self):
        data = Login_Page.LoginWindow("User")
        # print(Login_Page.tu_return,"#################################")
        # li = Login_Page.tu_return
        # li = li[0][1][1:]

        # for i in li:
        #     imp_user.append(i)


        # # self.user_data_l = Entry(self.main)
        # # self.user_data_l.config(text=li)
        print("User Data : ",user_details)
        

        # print(li)
        # print(user_data)


    def distt_selection(self):
        self.scrollbar.pack_forget()
        xx = 80
        yy = 130
        count = 0
        Label(self.distt_select_frame,text=f"Choose Your District",font=("jokerman",21),fg="white",bg="#570416").place(x=250,y=30)
        for i in range(len(self.districts)):
            btn = Button(self.distt_select_frame,text=self.districts[i],font=("Arial", 11,"bold"),width=22,height=1)
            button_name = self.districts[i].replace(" ", "_")
            setattr(self, f"{button_name}_button", btn)  
            btn.place(x=xx,y=yy)
            btn.bind("<Button-1>",lambda x , distt_name = self.districts[i]: self.data(x,distt_name)) 
            xx += 220
            count += 1
            if count == 3: 
                yy += 50
                xx = 80
                count = 0 

    def data(self,event,name):
        
        with open("distt.txt", "w") as file:
            file.write(name)
            # def data(self,event,name):
        if self.vals:
            self.main.after(0,self.wait_for_destroy)
            mainfile(True,Toplevel(),False)
            # nice = Toplevel()


        li = []
        with open("users.txt", "r") as file:
            content = file.read()
        li.append(content)
        dt =  ((str(li[0]).replace('(','')).replace(')','').replace('\'',"").split(","))
        self.AK = (dt[0].split()[0][0]).upper()+(dt[0].split()[1][0]).upper()
        self.name = (dt[0].split()[0])+" "+(dt[0].split()[1])
        self.email = (dt[1])
        self.name_len = len((dt[0].split()[0][0])+(dt[0].split()[1][0]))
        # with open("users.txt", "r") as file:
        #     content = file.read()
        #     li.append(content)
        #     dt =  ((str(li[0]).replace('(','')).replace(')','').replace('\'',"").split(","))
        #     self.AK = (dt[0].split()[0][0])+(dt[0].split()[1][0])
        #     self.name_len = len((dt[0].split()[0][0])+(dt[0].split()[1][0]))
        self.imgg = Image.open("circle_grey.png").resize((60,60))
        self.img = ImageTk.PhotoImage(self.imgg.resize((80,80)))
        self.logo_button = Button(self.upper_blue_frame, image=self.img, bg="#e6daba", bd=0, activebackground="#e6daba")
        self.logo_button.place(x=1400, y=30)
        self.logo_button.bind("<Button-1>",lambda x :self.toggle_account_options(x,self.account_options_frame,1100, 105))
        self.name_label.config(text=self.name)
        self.email_label.config(text=self.email)
        
        if self.name_len == 1:
            self.user_labels = Label(self.upper_blue_frame, text=self.AK, font=("Arial", 24, "bold"), fg="#ffffff", bg="#570416")
            self.user_labels.place(x=1405, y=46)
            self.user_label.config(text=self.AK)
        else:
            self.user_labels = Label(self.upper_blue_frame, text=self.AK, font=("Arial", 18, "bold"), fg="#ffffff", bg="#570416")
            self.user_labels.place(x=1420, y=50)
            self.user_label.config(text=self.AK)

        self.sign_in.place_forget() 
        # print(name)

        self.cinema_stores = Database_store.cinemas_distt_show(name)
        self.distt_name = name
        for i in range(len(self.cinema_stores)):
            # print(self.cinema_stores[i])
            
            self.cinema_store.append((str(self.cinema_stores[i]).replace("('","")).replace("',)",""))
        # print(self.cinema_store)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        if self.vals:
            self.distt_select_frame.place_forget()



        # self.logo_button.bind("<Button-1>", lambda x : self.toggle_account_options(x,self.account_options_frame,1100,105))



        self.cinema_frame_fn()



    def wait_for_destroy(self):
        self.main.withdraw()
        

    def toggle_account_options(self, event,name,xx,yy):
        if name.winfo_viewable():
            name.place_forget()
        else:
            name.place(x=xx, y=yy)
            name.lift()


    
    def create_account_options(self):


        self.account_options_frame = Frame(self.main, bg="#ffffff", width=350, height=400,border=1,relief=SOLID )
        self.account_options_frame.place(x=1100, y=105)
        self.account_options_frame.place_forget()
    
        self.circle_img = Image.open("circle.png").resize((80,80))
        self.imgg_local_real = ImageTk.PhotoImage(self.circle_img)
        self.logo_local = Label(self.account_options_frame, image=self.imgg_local_real, bd=0,bg="#ffffff")
        self.logo_local.place(x=22, y=35)

        if self.name_len == 1:
            self.user_label = Label(self.logo_local, font=("Arial", 20, "bold"), fg="#ffffff", bg="#570416")
            self.user_label.place(x=25, y=20)
        else:
            self.user_label = Label(self.logo_local, font=("Arial", 18, "bold"), fg="#ffffff", bg="#570416")
            self.user_label.place(x=18, y=20)
        
        self.name_label = Label(self.account_options_frame ,font=("Arial", 15,"bold"), bg="#ffffff")
        self.name_label.place(x=100,y=45)

        self.email_label = Label(self.account_options_frame, font=("Arial", 12), bg="#ffffff")
        self.email_label.place(x=100,y=70)

        self.grey_line = Frame(self.account_options_frame, bg="grey", height=1,width=self.account_options_frame.winfo_screenwidth())
        self.grey_line.place(x=0,y=120)

        settings_button = Button(self.account_options_frame, text="Settings", font=("Arial", 14), bg="SystemButtonFace", width=30,height=1,border=1,relief=FLAT,anchor="nw",pady=10)#,command=self.open_settings)
        settings_button.place(x=5,y=140)
        settings_button.bind("<Enter>",self.side_enter)
        settings_button.bind("<Leave>",self.side_leave)
        settings_button.bind("<Button-1>",lambda x:update_movie.settings(self.email))

        purchase_history_button = Button(self.account_options_frame, text="Purchase History", font=("Arial", 14), bg="SystemButtonFace", width=30,height=1,border=1,relief=FLAT,anchor="nw",pady=10)# command=self.open_purchase_history)
        purchase_history_button.place(x=5,y=190)
        purchase_history_button.bind("<Enter>",self.side_enter)
        purchase_history_button.bind("<Leave>",self.side_leave)
        purchase_history_button.bind("<Button-1>",lambda x:update_movie.purchase_his())
        
        logout = Button(self.account_options_frame, text="Log Out", font=("Arial", 14), bg="SystemButtonFace", width=30,height=1,border=1,relief=FLAT,anchor="nw",pady=10)# command=self.open_purchase_history)
        logout.place(x=5,y=240)
        logout.bind("<Enter>",self.side_enter)
        logout.bind("<Leave>",self.side_leave)
        logout.bind("<Button-1>",lambda x:self.logout(x))

    def logout(self,event):
        # self.main.after(100,self.main.destroy())
            self.main.after(100,self.wait_for_destroy)
            mainfile(True,Toplevel(),True)
        # print("ok")
        
    

    def side_enter(self,event):
        event.widget["bg"]="#570416" 
        event.widget['fg']="white"

    def side_leave(self,event):
        event.widget['bg']="#e6cfcf"
        event.widget['fg']="#000000"



     

if __name__ == "__main__":
    imp_user = []
    root = Tk()
    obj = mainfile(True,root,False)
    root.mainloop()
    print(imp_user)

# Just Find this line and uncomment below line then its work 
# This Line useful for Sliding the Screen
