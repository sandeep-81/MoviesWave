import mysql.connector
from datetime import date
import numpy as np

movie_data = []
cinemas_data = []
booking_data = []


try :
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        db='movieswaves'
    )
    # print("connected")

except Exception as e:
    print("error ---",e)

cursor = db.cursor()
def registerUser(data):
    try: 
        print(data)
        cursor.execute('Insert into registeruser(Name,Email,Phone,Password) values (%s,%s,%s,%s)',data)
        print(data)
        db.commit()
        return True
    except Exception as e:
        print("Error --",e)
        return False
    
def new_movie_upload(data):
    try:
        print(data)
        cursor.execute('Select name from `new_movies`')
        all_movies_names = cursor.fetchall() 
        for i in range(len(all_movies_names)):
            movie_data.append((str(all_movies_names[i]).replace("',)","")).replace("('",""))
        if data[0] not in movie_data:        
            cursor.execute('Insert into new_movies (name,language,genres,date,about,trailer,rating,poster,time,banner) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',data)
            print(data)
            # db.commit()
            return True
        elif data[0] in movie_data:  
            return "exist"
             
    except Exception as e:
        print("Error --",e)
        return False
    
def upcoming_movie_upload(data):
    try:
        print(data)
        cursor.execute('Select name from `upcoming_movies`')
        all_movies_names = cursor.fetchall() 
        for i in range(len(all_movies_names)):
            movie_data.append((str(all_movies_names[i]).replace("',)","")).replace("('",""))
        if data[0] not in movie_data:        
            cursor.execute('Insert into upcoming_movies (name,language,genres,date,about,trailer,poster,time,banner) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)',data)
            print(data)
            db.commit()
            return True
        elif data[0] in movie_data:  
            return "exist"
             
    except Exception as e:
        print("Error --",e)
        return False
    
def cast(data):
    try:
        print(data)
        cursor.execute('INSERT INTO `cast` (movie_name, cast_name, charcter, about, image) VALUES (%s, %s, %s, %s, %s)', data)

        print(data)
        db.commit()
        return True
    except Exception as e:
        print("Error --",e)
        return False
    
def loginUser(data):
    try:

        # print("yes reachable")
        cursor.execute('Select * from registeruser where Email=%s and Password=%s',data)
        check=cursor.fetchone() 
        cursor.execute('Select name,email from registeruser where Email=%s and Password=%s',data)
        check_r=cursor.fetchone() 
        # print(check_r)

        name = str(check_r[0])
        email = str(check_r[1])
        # tu = (True,check,tuple(name),tuple(email)) 
        tu = (True,check) 
        return tu 
        
    except Exception as e:
        print("error -- ",e)
        return False
    
def loginUser_show():
    try:

        cursor.execute('Select Name from registeruser ')
        store = cursor.fetchall()
        return store
        
    except Exception as e:
        print("error -- ",e)
        return False

def movies_store_data(data):
    try:
        cursor.execute("Insert into movies_data(Name,UA,Release_Date,Location) values (%s,%s,%s,%s)",data)
        print("Done")
        db.commit()
        return True
    except Exception as e:
        print("Error---",e)
        return False
    
def movies_update_data(data,upnew):
    try:
        if upnew == "latest":
            print(data)
            cursor.execute("UPDATE `new_movies` SET name=%s,language=%s,genres=%s,date=%s,about=%s,trailer=%s,rating=%s,poster=%s,time=%s,banner=%s where name=%s",data)
            db.commit()
            return True
        elif upnew == "cinema":
            print(data)
            cursor.execute("UPDATE `cinemas` SET cinema_name=%s, address=%s, road=%s ,district=%s ,pincode=%s ,screeens=%s ,seats=%s ,phone=%s ,email=%s ,opening_time=%s ,closing_time=%s ",data)
            db.commit()
            return True
        elif upnew == "users":
            # print(data)
            print(data)
            cursor.execute("UPDATE `registeruser` SET Name=%s,Email=%s,Phone=%s,Password=%s where Email=%s",data)
            db.commit()
            return True
        elif upnew == "password":
            # print(data)
            print(data)
            cursor.execute("UPDATE `registeruser` SET Name=%s,Email=%s,Phone=%s,Password=%s where Email=%s",data)
            db.commit()
            return True
        else:
            print(data)
            cursor.execute("UPDATE `upcoming_movies` SET name=%s,language=%s,genres=%s,date=%s,about=%s,trailer=%s,poster=%s,time=%s,banner=%s where name=%s",data)
            db.commit()
            return True
    except Exception as e:
        print("Error---",e)
        return False

def movie_show():
    try:
        # name = movie_data[0]

        cursor.execute("SELECT * FROM `new_movies` ")
        store_all = cursor.fetchall() 
        return store_all
    except Exception as e:
        print("Error---",e)

def movie_gen_payment(data):
    try:
        # name = movie_data[0]

        cursor.execute("SELECT genres FROM `new_movies` where name=%s",(data,))
        store_all = cursor.fetchall() 
        return store_all
    except Exception as e:
        print("Error---",e)

def bookings_show():
    try:
        cursor.execute("SELECT Booking_id,movie_name FROM `booking` ")
        store_all = cursor.fetchall() 
        return store_all
    except Exception as e:
        print("Error---",e)

def bookings_particular_show(data):
    try:
        cursor.execute("SELECT Booking_id,movie_name FROM `booking` where user_mail=%s ",(data,))
        store_all = cursor.fetchall() 
        return store_all
    except Exception as e:
        print("Error---",e)

def bookings_particular_details_show(data):
    try:
        cursor.execute("SELECT * FROM `booking` where Booking_id=%s ",(data,))
        store_all = cursor.fetchall() 
        return store_all
    except Exception as e:
        print("Error---",e)

def select_passwords_only(data):
    try:
        print(data)
        # name = movie_data[0]

        cursor.execute("SELECT Password FROM `registeruser` where Email=%s",(data,))
        store_all = cursor.fetchall() 
        return store_all
    except Exception as e:
        print("Error---",e)

def dashaord_upper_data(data):
    try:
    
        # name = movie_data[0]
        if data=="movie":
            cursor.execute("SELECT COUNT(*) FROM `new_movies`")
            store = cursor.fetchall()
            print(store) 
            return store
        elif data=="ticket":
            cursor.execute("SELECT COUNT(*) FROM `booking`")
            store = cursor.fetchall()
            print(store) 
            return store
        elif data=="users":
            cursor.execute("SELECT COUNT(*) FROM `registeruser`")
            store = cursor.fetchall()
            print(store) 
            return store
        elif data=="profit":
            cursor.execute("SELECT SUM(total_amount) FROM `booking`")
            store = cursor.fetchall()
            print(store) 
            return store
    except Exception as e:
        print("Error---",e)

def dashboard_line_graph():
    try:
            today = today1= today2 = today3 = today4 = today5 = today6 = 0
            xval = np.array([date.today().day-6,date.today().day-5,date.today().day-4,date.today().day-3,date.today().day-2,date.today().day-1,date.today().day])

            cursor.execute("SELECT booking_id,today FROM `booking`")
            store = cursor.fetchall()
            print(store)
            for i in store:
                
                if (str(i[1]).split("-")[2]) == str(xval[len(xval)-1]):
                    today += 1
                elif (str(i[1]).split("-")[2]) == str(xval[len(xval)-2]):
                    today1 += 1
                elif (str(i[1]).split("-")[2]) == str(xval[len(xval)-3]):
                    today2 += 1
                elif (str(i[1]).split("-")[2]) == str(xval[len(xval)-4]):
                    today3 += 1
                elif (str(i[1]).split("-")[2]) == str(xval[len(xval)-5]):
                    today4 += 1
                elif (str(i[1]).split("-")[2]) == str(xval[len(xval)-6]):
                    today5 += 1
                elif (str(i[1]).split("-")[2]) == str(xval[len(xval)-7]):
                    today6 += 1

            li = [today ,today1 ,today2 ,today3 ,today4 ,today5 ,today6]
            print(li)             
            return li

    except Exception as e:
        print("Error---",e)
dashboard_line_graph()

def particular_movie_show(data,upnew):
    try:
        if upnew == "latest":
            cursor.execute("SELECT * FROM `new_movies` where name=%s",(data,))
            store_all = cursor.fetchall() 
            return store_all
        elif upnew == "cinema":
            cursor.execute("SELECT * FROM `cinemas` where cinema_name=%s",(data,))
            store_all = cursor.fetchall() 
            return store_all
        else:
            cursor.execute("SELECT * FROM `upcoming_movies` where name=%s",(data,))
            store_all = cursor.fetchall() 
            return store_all
        
    except Exception as e:
        print("Error---",e)

def movie_name_show():
    try:
        # name = movie_data[0]

        cursor.execute("SELECT name FROM `new_movies` ")
        store_all = cursor.fetchall() 
        return store_all
    except Exception as e:
        print("Error---",e)

def movie_name_show_up():
    try:
        # name = movie_data[0]

        cursor.execute("SELECT name FROM `upcoming_movies`")
        store_all = cursor.fetchall() 
        return store_all
    except Exception as e:
        print("Error---",e)

def upcoming_movie_show():
    try:
        # name = movie_data[0]

        cursor.execute("SELECT * FROM `upcoming_movies` ")
        store_all = cursor.fetchall() 
        return store_all
    except Exception as e:
        print("Error---",e)

def users_login(name):
    try:
        # name = movie_data[0]

        cursor.execute("SELECT * FROM `registeruser` where name=%s",(name,))
        store_all = cursor.fetchone() 
        return store_all
    except Exception as e:
        print("Error---",e)
    
def admin_login(data):
    try:
        cursor.execute('Select * from admin where Email=%s and Password=%s',data)
        check=cursor.fetchone() 
        cursor.execute('Select name from admin where Email=%s and Password=%s',data)
        name = str(cursor.fetchone()[0])
        print(name)
        tu = (True,check,tuple(name)) 
        return tu
    except Exception as e:
        print("error -- ",e)
        return False
    
def delete_movie(m_name,upnew):
    try:
        if upnew == "latest":
            cursor.execute('DELETE FROM `new_movies` WHERE name = %s',m_name)
            db.commit()
            return True
        elif upnew == "user":
            cursor.execute('DELETE FROM `registeruser` WHERE name = %s',m_name)
            db.commit()
            return True
        
        elif upnew == "cinema":
            print(m_name)
            cursor.execute('DELETE FROM `cinemas` WHERE cinema_name = %s',m_name)
            # db.commit()
            return True
        else:
            cursor.execute('DELETE FROM `upcoming_movies` WHERE name = %s',m_name)
            db.commit()
            return True
    except Exception as e:
        print("Error --- ",e)
        return False

def new_cinema_upload(data):
    try:
        print(data)
        cursor.execute('Select cinema_name from `cinemas`')
        all_cinemas_names = cursor.fetchall() 
        for i in range(len(all_cinemas_names)):
            cinemas_data.append((str(all_cinemas_names[i]).replace("',)","")).replace("('",""))
        if data[0] not in cinemas_data:        
            cursor.execute('Insert into cinemas (cinema_name,address,road,district,pincode,screeens,seats,phone,email,opening_time,closing_time) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',data)
            print(data)
            db.commit()
            return True
        elif data[0] in cinemas_data:  
            return "exist"
    
    except Exception as e:
        print("Error --",e)
        return False
    

def bookings(data):
    try:
        print(data)
        cursor.execute('Select booking_id from `booking`')
        booking_id = cursor.fetchall() 
        for i in range(len(booking_id)):
            booking_data.append((str(booking_id[i]).replace("',)","")).replace("('",""))
        if data[0] not in booking_data:        
            cursor.execute('INSERT INTO `booking`(booking_id,movie_name,movie_date,show_time,cinema_name,ticket_price,total_tickets,total_amount,user_name,user_mail,today) Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',data)
            print(data)
            db.commit()
            return True
        elif data[0] in booking_data:  
            return "exist"
    
    except Exception as e:
        print("Error --",e)
        return False


def cinemas_show():
    try:
        # name = movie_data[0]

        cursor.execute("SELECT cinema_name FROM `cinemas` ")
        store_all = cursor.fetchall() 
        return store_all
    except Exception as e:
        print("Error---",e)

def cinemas_distt_show(data):
    try:
        # name = movie_data[0]
        datas = (data,)
        cursor.execute("SELECT cinema_name FROM `cinemas` where district=%s",datas)
        store_all = cursor.fetchall() 
        print(store_all)
        return store_all 
    except Exception as e:
        print("Error---",e)

def cinemas_details_show(data):
    try:
        # name = movie_data[0]
        datas = (data,)
        cursor.execute("SELECT * FROM `cinemas` where cinema_name=%s",datas)
        store_all = cursor.fetchall() 
        print(store_all)
        return store_all 
    except Exception as e:
        print("Error---",e)

def cast_details(data):
    try:
        # name = movie_data[0]
        datas = (data,)
        cursor.execute("SELECT * FROM `cast` where movie_name=%s",datas)
        store_all = cursor.fetchall() 
        return store_all 
    except Exception as e:
        print("Error---",e)

def cinema_details(data):
    try:
        # name = movie_data[0]
        datas = (data,)
        print(data)
        cursor.execute("SELECT * FROM `cinemas` where district=%s",datas)
        store_all = cursor.fetchall() 
        return store_all 
    except Exception as e:
        print("Error---",e)

def particular_cinema_details(data):
    try:
        # name = movie_data[0]
        datas = (data,)
        print(data)
        cursor.execute("SELECT * FROM `cinemas` where cinema_name=%s",datas)
        store_all = cursor.fetchall() 
        return store_all 
    except Exception as e:
        print("Error---",e)

def upcome_to_latest(data,rating):
    try:
        # name = movie_data[0]
        datas = (data,)
        cursor.execute("SELECT * FROM `upcoming_movies` WHERE name = %s",datas)
        store_all = cursor.fetchall()
        print(store_all)
        counter = 0
        li = []
        for i in range(1,11):
            if i<7:

                li.append(store_all[0][i])
                print(i)
            elif i==7:
                li.append(rating)
                print(i)
            else:
                li.append(store_all[0][i-1])
                print(i)
        
        tuple(li)

        data = new_movie_upload(li)
    
        if data:
            delete_movie(datas,"upcoming")
            db.commit()
            return True
        else:
            return False
    except Exception as e:
        print("Error---",e)
    
