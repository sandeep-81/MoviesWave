from tkinter import *
from PIL import Image, ImageTk
from tkinter import Tk, Label
import time
import Login_Page


class logo:
    def __init__(self,root,cond):

        self.main = root
        if cond == True:
            self.main.state("zoomed")
            self.main["bg"]="black"
            self.main.attributes('-alpha',1)
            self.main.attributes("-topmost", True)

            # self.mainfile_thread.join()
            
            img2 = ImageTk.PhotoImage((Image.open("logo.png")).resize((380, 250)))
            self.logo_label = Label(self.main, image=img2, bg="black")
            self.logo_label.place(x=550, y=250)

            self.process = Frame( self.main,height=6, width=500 ,bg="red")
            self.process.place(x=500,y=530)

            self.process_cp = Frame( self.main,height=6, width=0 ,bg="white")
            self.process_cp.place(x=500,y=530)
            
            self.counter = 1
            for i in range(500):
                if self.counter == 500:
                    break
                self.process_cp.config(width=self.counter)
                if i == 150 or i==300 or i==400 :
                    time.sleep(1) 
                    print(i)
                    self.counter += 1
                else:
                    self.counter += 1

                # print()
                self.main.update()
            time.sleep(1)


            a_count = 1
            self.main.after(300, self.run(root,cond)) 
            for i in range(10000):
                if i%10 == 0:
                    a_count -= 0.001

            # self.main.destroy()
                # self.main.attributes('-alpha',a_count)  

                # self.main.update()
            print("yess") 
            
            self.main.mainloop()
        else:
            self.run(root,cond)


    def run(self,root,cond):
        Login_Page.ru(root,cond)
        print("End")
        
        # test.mainfile(True,root)

    

def start(cond): 
    root = Tk()
    # user = test.mainfile(True,root)
    logo(root,cond)
    root.mainloop()


if __name__ == "__main__":
    start(True)

