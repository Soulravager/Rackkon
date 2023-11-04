from tkinter import*
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import filedialog
import webbrowser
import requests
import cv2
import os
import DetectChars
import DetectPlates
import datetime
import time
import csv
import random
import psycopg2
import socket
import sys

###############page 1
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="alpha123"
)
tele_ID='754112013'#Alwin tele_ID='766494078' mdss
urllink="192.168.0.100"
#urllink = "192.168.0.100"  # <<<ip_cam_add#####

class userlogin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #          img
        img = Image.open("loginpmss1.jpg")
        img = img.resize((1000, 600), Image.Resampling.LANCZOS)
        loginimg = ImageTk.PhotoImage(img)
        #img label
        imglil= tk.Label(self, image = loginimg,borderwidth=0)
        imglil.image=loginimg
        imglil.place(x=0,y=0)

#            User Login

        border = tk.LabelFrame(self, text="                                   Login Page                                     ", font=("Arial",16), fg="white", bg="#051425",borderwidth=2,highlightbackground='#051412',highlightthickness=3,)
        border.pack(fill="both", expand="yes",padx=230,pady=160)

        l1 = Label(border, text="Username", font=("Arial Bold", 15),fg="white", bg="#051425")
        l1.place(x=100, y=30)
        d1 = Entry(border, width=30, bd=5)
        d1.place(x=250, y=30)

        l2 = Label(border, text="Password", font=("Arial Bold", 15),fg="white", bg="#051425")
        l2.place(x=100, y=100)
        d2 = Entry(border, width=30, bd=5, show='*')
        d2.place(x=250, y=100)
        cur = conn.cursor()
        # login condition
        cur.execute("SELECT username, password FROM tesetpass;")
        results = cur.fetchone()
        username = results[0]
        password = results[1]
        def verify1():                                                          #using data base
            if d1.get() ==username and d2.get() == password:
                controller.show_frame(pmsshome)
            else:
                messagebox.showinfo("ERROR", "Please Enter Correct Username or Password!!!")
            d1.delete(first=0, last=100)  # for clear from field after submit
            d2.delete(first=0, last=100)
        def verify2():                                                          #using logical
            if d1.get() == '123' and d2.get() == '123':
                controller.show_frame(pmsshome)
            else:
                messagebox.showinfo("ERROR", "Please Enter Correct Username or Password!!!")
            d1.delete(first=0, last=100)  # for clear from field after submit
            d2.delete(first=0, last=100)

        # DBMS LOG OUT
        ##########

        button = tk.Button(border, text='Login', font=("Arial", 14), command=verify1, padx=7, pady=8, fg="white", bg="#121b40", borderwidth=0,relief=RAISED)
        button.place(x=420, y=175)




#Page2          PMSS home main page

class pmsshome(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #images ________________
        img1 = Image.open("parkingtheme.jpg")  # theme for frame left and right

        img1 = img1.resize((170, 600), Image.Resampling.LANCZOS)  # resize image
        themeside = ImageTk.PhotoImage(img1)

        # image frametop
        img2 = Image.open("guitoptheme.jpg")
        img2 = img2.resize((657, 60), Image.Resampling.LANCZOS)
        themetop = ImageTk.PhotoImage(img2)

        # image frambot
        img3 = Image.open("guibottheme.jpg")
        img3 = img3.resize((660, 60), Image.Resampling.LANCZOS)
        themebot = ImageTk.PhotoImage(img3)

        # image frame1
        img4 = Image.open("guiframe1.jpg")
        img4 = img4.resize((350, 490), Image.Resampling.LANCZOS)
        thememain1 = ImageTk.PhotoImage(img4)

        # image frame2
        img5 = Image.open("guiframe2.jpg")
        img5 = img5.resize((310, 490), Image.Resampling.LANCZOS)
        thememain2 = ImageTk.PhotoImage(img5)


#       left frame
        leftbord = tk.LabelFrame(self, width=170,height=600,bg="#051425", borderwidth=0,relief=RAISED)
        leftbord.pack(side=LEFT,fill="both")
        #imglabel
        imglil = tk.Label(leftbord, image=themeside, borderwidth=0)
        imglil.image = themeside
        imglil.place(x=0, y=0)


#       right frame
        rightbord = tk.LabelFrame(self, width=170, height=600, bg="#051425", borderwidth=0,relief=RAISED)
        rightbord.pack(side=RIGHT, fill="both")
        #imglabel1
        imglil1 = tk.Label(rightbord, image=themeside, borderwidth=0)
        imglil1.image = themeside
        imglil1.place(x=0, y=0)


#       top frame
        bordertop = tk.LabelFrame(self, width=660,height=50, bg="#051425",relief=SUNKEN, borderwidth=0)
        bordertop.pack(side=TOP, fill="both")
        #imglabel2
        imglil2 = tk.Label(bordertop, image=themetop, borderwidth=0)
        imglil2.image = themetop
        imglil2.place(x=0, y=0)


#       bottom frame
        borderbot = tk.LabelFrame(self, width=660,height=60, bg="#051425",relief=SUNKEN, borderwidth=0)
        borderbot.pack(side=BOTTOM, fill="both")
        #imglabel3
        imglil3 = tk.Label(borderbot, image=themebot, borderwidth=0)
        imglil3.image = themebot
        imglil3.place(x=0, y=0)

        #content frame
        main1 = tk.LabelFrame(self, width=350,height=490,bg='white',relief=SUNKEN, borderwidth=0)
        main1.pack(side=LEFT, fill="both")
        # imglabel4
        imglil4 = tk.Label(main1, image=thememain1, borderwidth=0)
        imglil4.image = thememain1
        imglil4.place(x=0, y=0)

        #image preview frame
        main2 = tk.LabelFrame(self, width=310, height=490, bg='white', relief=SUNKEN, borderwidth=0)
        main2.pack(side=RIGHT, fill="both")
        #imagelabel5
        imglil4 = tk.Label(main2, image=thememain2, borderwidth=0)
        imglil4.image = thememain2
        imglil4.place(x=0, y=0)



        # cam setting url
        #new = 1
        #url = "http://" + urllink + ":8080/settings_window.html"



        # to clear field
        def myclick():  ####Out put value

            ##################
            # ipcamid=str(e.get())
            # print("ipiddd:::" + ipcamid)
            # ipcamport=str(e1.get())
            u.delete(first=0, last=100)  # for clear from field after submit
            e.delete(first=0, last=100)  # for clear from field after submit
            e1.delete(first=0, last=100)  # for clear from field after submit

        # print("ipport:::"+ipcamport)

        # def for exit/close window

        #url1 = "http://" + urllink + ":8080/video"

#--------------------------rror
        #def destroy():
            #app.destroy()
#----------------------------
        def myclickst():

            print("PMS SYSTEM IS STARTING...")
            time.sleep(1)
            print("Connecting...")
            print("PMS SYSTEM IS CONNECTED TO CAMERA:" + e.get())#url1)
            PMSSYS()
#-------------------------
        def mylickst111():  # for loop ver of PMSSS
            while True:
                PMSSYS()
                k = cv2.waitKey(1) & 0xFF
                # press 'q' to exit
                if k == ord('q'):
                    break
#------------------------
        def myclickstop():

            cv2.destroyAllWindows()

        # -------------------destroy button, to exit window
        def destroy():
            print("PMS SYSTEM IS SHUTDOWNING..")
            time.sleep(1)
            sys.exit("PMS system is shutdowning.....")

        #       Label for informations

        lil1 = Label(bordertop, text='Parking Management & Security System', font=("Arial", 16), fg="white",bg="#051425", borderwidth=0, )
        lil1.place(x=145, y=17)


        # label2  user info
        label2 = Label(main1, text='User Information', font=("Arial", 12, 'bold'), fg="white", bg="#0b1829",borderwidth=0, )
        label2.place(x=110, y=10)

        # ipcamid

        label2 = Label(main1, text='IPCAM ID', font=('Arial', 10, 'bold'), fg="white", bg="#002036", borderwidth=0,pady=3, relief=GROOVE)
        label2.place(x=15, y=60)

        # input ipcam id
        u = Entry(main1, width=35, justify=CENTER, fg="white", bg="#080914", borderwidth=8)  # input
        u.place(x=110, y=50)

        # ipaddress

        label2 = Label(main1, text='IP ADDRESS', font=('Arial', 10, 'bold'), fg="white", bg="#002036", borderwidth=0,pady=3, relief=GROOVE)
        label2.place(x=15, y=115)

        # input ip address

        e = Entry(main1, width=35, justify=CENTER, fg="white", bg="#080914", borderwidth=8)  # input value
        e.place(x=110, y=110)

        # ipport

        label3 = Label(main1, text='IP PORT', font=('Arial', 10, 'bold'), fg="white", bg="#002036", borderwidth=0,pady=3, relief=GROOVE)
        label3.place(x=15, y=180)

        # input ip port

        e1 = Entry(main1, width=35, justify=CENTER, fg="white", bg="#080914", borderwidth=8)  # input value
        e1.place(x=110, y=175)

        #####################################################################################
        # def setting url
        new = 1
        cameraset="http://"+urllink+":8080/settings_window.html"
        def web():
            webbrowser.open(cameraset, new=new)
        #buttons

        # clear button, clear entry field

        clear = Button(main1, text="Clear", padx=15, pady=10, command=myclick, fg="white", bg="#121b40", borderwidth=0,relief=RAISED)
        clear.place(x=280, y=250)

        # start button,start ipcam option

        start = Button(main1, text="Start", padx=20, pady=10, command=myclickst, fg="white", bg="#121b40",borderwidth=0, relief=RAISED)
        start.place(x=275, y=390)

        # stop button,stop ipcam process

        stop = Button(main1, text="Stop", padx=20, pady=8, command=myclickstop, fg="white", bg="#121b40",borderwidth=0, relief=RAISED)
        stop.place(x=275, y=440)

        # cam setting to customise camera feature
        setting = Button(main1, text="Settings", padx=20, pady=8, command=web, fg="white", bg="#121b40", borderwidth=0,relief=RAISED)
        setting.place(x=10, y=440)


#           dbms register button page
        reg = Button(main1, text='Register',padx=20, pady=8, fg="white", bg="#121b40",borderwidth=0,relief=RAISED,  command=lambda: controller.show_frame(regdbms))
        reg.place(x=10, y=395)
        #-----------------------------------------------

        # cam setting url


        url = "http://" + e1.get() + ":8080/video"



        ##>>PMMS_MAIN------------------------------------
        def PMSSYS():


            cur = conn.cursor()
            now = datetime.datetime.now()

            blnKNNTrainingSuccessful = DetectChars.loadKNNDataAndTrainKNN()  # attempt KNN training

            if blnKNNTrainingSuccessful == False:  # if KNN training was not successful
                print("\nerror: KNN traning was not successful\n")  # show error message
                return  # and exit program
            # end if



            #url = url1
            # url=IPcamadd
            #url = "http://192.168.0.100:8080/shot.jpg"

            cap = cv2.VideoCapture("http://" + e.get() + ":8080/video")#url)
            while (1):
                time.sleep(6)
                ret, frame = cap.read()
                # cv2.imshow('Camera', frame)
                key = cv2.waitKey(1)
                if key:
                    break
            cap.release()
            cv2.destroyAllWindows()
            imgOriginalScene = frame  # cv2.imread(imgout)               # open image

            if imgOriginalScene is None:  # if image was not read successfully
                print("\nerror: image not read from file \n\n")  # print error message to std out
                os.system("pause")  # pause so user can see error message
                return  # and exit program
            # end if

            for n in range(1):
                cv2.imwrite(f'IMGOUT\Main-1-{n:02}.png', imgOriginalScene)

            listOfPossiblePlates = DetectPlates.detectPlatesInScene(imgOriginalScene)  # detect plates

            listOfPossiblePlates = DetectChars.detectCharsInPlates(listOfPossiblePlates)  # detect chars in plates

            ######cv2.imshow("imgOriginalScene", imgOriginalScene)            # show scene image >>>>>>>>>>IMG OUT PUT<<<<<<<<<<<<<<<

            if len(listOfPossiblePlates) == 0:  # if no plates were found
                print("\nno license plates were detected\n")  # inform user no plates were found
            else:  # else

                listOfPossiblePlates.sort(key=lambda possiblePlate: len(possiblePlate.strChars), reverse=True)

                licPlate = listOfPossiblePlates[0]

                if len(licPlate.strChars) == 0:  # if no chars were found in the plate
                    print("\nno characters were detected\n\n")  # show message
                    return  # and exit program

                # print("\nReg.no = " + licPlate.strChars + '  '+ now.strftime("Date=%d-%m-%y Time=%H:%M:%S"))     # write license plate text to std out#>>>>MAIN OUTPUT><<<<XD<
                print("Vehicle Registration:: " + licPlate.strChars)
                print(now.strftime("Date=%d-%m-%y Time=%H:%M:%S"))

                # DBMS CHECKING WITH AUTHO TABLE###

                outsting = licPlate.strChars
                # execute SQL query to select the rows from the table that match the string
                query = "SELECT * FROM testao WHERE lc_num = %s;"
                cur.execute(query, (outsting,))
                rows = cur.fetchall()
                if len(rows) == 0:
                    print("Unauthorized_Vehicle")
                    usernamedata = "Unknown User"
                    accessdata = "Unauthorized_Vehicle"
                    file = open("Data_PMS/Unauthorized_Vehicle_list.csv", "a")
                    A = []
                    w = csv.writer(file)
                    n = 1
                    while n <= 1:
                        r = str("Unauthorized_Vehicle_Number = " + licPlate.strChars + '  ' + now.strftime(
                            "Date=%d-%m-%y Time=%H:%M:%S"))
                        A.append(r)
                        n = n + 1
                        w.writerow(A)
                        file.close()

                    ##dbasses="Unauthorized_Vehicle">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                else:
                    for row in rows:
                        # print(row[0], row[1])><>>>>>>>>>>>>>TO PRINT OUT THE ROWS OF SELECTED TABLE
                        print("Authorized_Vehicle")
                        username = row[
                            1]  # the column number of data base table of authoti>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                        usernamedata = username
                        print("Owner_name:" + username)  # print the other attributes in the row
                        accessdata = "Authorized"

                def send_to_telegram(message):
                    apiToken = '6047129599:AAFqm2xkAkwE2NKw5G7DNhWs1C7bbEg5Wi8'

                    chatID=tele_ID
                    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

                    try:
                        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
                        # print(response.text)
                        print("Notified to the admin")
                    except Exception as e:
                        print(e)

                # accessdata="Unauthorized"
                # usernamedata="not defined"

                def generate_random_number():
                    return random.randint(1, 10)  # Parking lot number of lines

                def generate_random_string():
                    # letters = string.ascii_uppercase
                    letters = ['A', 'B', 'C']  # parking lot line
                    return ''.join(random.choice(letters) for i in range(1))

                fourdig = str(generate_random_number())
                twochar = generate_random_string()

                send_to_telegram("vehicle Number= " + licPlate.strChars + '' + '' + '' + now.strftime(
                    "\nDate=%d-%m-%y \nTime=%H:%M:%S") + "\nOwner name=" + usernamedata + "\nEntry Type=" + accessdata + "\nAssined parkingLot=" + twochar + "-" + fourdig)

                file = open("Data_PMS/OUTPUT_DATA.csv", "a")
                A = []
                w = csv.writer(file)
                # w.writerow(["Regn4um::"])
                n = 1
                while n <= 1:
                    # r = str("Reg.no = " + licPlate.strChars + '  '+ now.strftime("Date=%d-%m-%y Time=%H:%M:%S"))
                    r = str("vehicle Number= " + licPlate.strChars + '' + '' + '' + now.strftime(
                        "Date=%d-%m-%y Time=%H:%M:%S") + "Owner name=" + usernamedata + "Entry Type=" + '\033[91m' + accessdata + '\033[0m' + "Assined parkingLot=" + twochar + "-" + fourdig)
                    A.append(r)
                    n = n + 1
                    w.writerow(A)
                    file.close()
                    # print("recorded") to

            sql = "INSERT INTO test1 (reg_num, time, date,autho,owner,parking_lot) VALUES (%s, %s, %s,%s,%s,%s)"
            # current_time = now.strftime("%H:%M:%S")
            # current_date = now.strftime("%Y-%m-%d")
            string_value = licPlate.strChars
            Author = accessdata
            owner = usernamedata
            parklot = twochar + fourdig
            cur.execute(sql, (string_value, now.strftime("%H:%M:%S"), now.strftime("%Y-%m-%d"), Author, owner, parklot))
            print("Data added to Database!!")
            conn.commit()
            cur.close()

            # for android broadcast
            UDP_IP = "192.168.0.100"  # Change to a valid IP address on your network
            UDP_PORT = 5005  # Change to a different port number if needed
            MESSAGE = licPlate.strChars + "Allocated parking lot:" + parklot
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
            print("message send to driver!!")
        #------------------------------------------------
        #      content for main2 image preview section
        # preview, preview image in preview  frame

        img1 = Label(main2, text='IMAGE VIEWER', font=('Arial',14,'bold'), fg="white", bg="#0b0d1a")
        img1.place(x=85, y=7,)

        # no preview img, add image/size
        prw = Image.open("preview(300,350).png")
        prw = prw.resize((300, 350), Image.Resampling.LANCZOS)  # resize image
        preview = ImageTk.PhotoImage(prw)  # updated image size

        prev = Label(main2, image=preview, borderwidth=0, relief=SUNKEN)
        prev.image=preview
        prev.place(x=5, y=40)

        #           this image2 is for open saved image of vehicle from file directory and to show in window frame
        prev2 = Label(main2, bg='#08101b', borderwidth=0, relief=SUNKEN)

        # -------------------import image
        def file():
            global img
            filename = filedialog.askopenfilename(initialdir="G:/JPEG",filetypes=(("png images", "*.png"), ("jpg images", "*.jpg")))
            img = Image.open(filename)
            img = img.resize((300, 350), Image.Resampling.LANCZOS)  # resize image
            img = ImageTk.PhotoImage(img)  # updated image size
            prev2['image'] = img
        prev2.place(x=5, y=40)

        # -----------------button for image,to open image from file directory
        savedimg = Button(main2, text="Saved Image", padx=13, pady=6, command=file, fg="white", bg="#121b40", borderwidth=0, relief=RAISED)
        savedimg.place(x=10, y=439)


        # -----------button for video, to open image from file directory-----------Not Defined
        savedvid = Button(main2, text="Saved Video", padx=15, pady=6, fg="white", bg="#121b40", borderwidth=0, relief=RAISED)
        savedvid.place(x=10, y=400)

        # ------------button for open output, to open output from file directory(not finished)
        def csvv():
            # f = open("testing-1.csv")
            os.startfile('output_data.csv')
            time.sleep(1)
            print("Output data file is opened")

        otp = Button(main2, text="Output", padx=15, pady=6, command=csvv, fg="white", bg="#121b40", borderwidth=0,relief=RAISED)
        otp.place(x=225, y=439)
        ############

        #   button for exit
        exit = Button(borderbot, text='Exit',padx=15, pady=7,  fg="white", bg="#121b40", borderwidth=0,relief=RAISED,command=destroy)
        exit.pack(padx=10, pady=13,side=RIGHT)

        #   button for credit page
        crdt = Button(borderbot, text='Credit',  padx=15, pady=7, fg="white", bg="#121b40",borderwidth=0,relief=RAISED, command=lambda: controller.show_frame(credit))
        crdt.pack(padx=10, pady=13,side=LEFT)


#page3

class regdbms(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # images ________________
        img1 = Image.open("parkingtheme.jpg")  # theme for frame left and right

        img1 = img1.resize((170, 600), Image.Resampling.LANCZOS)  # resize image
        themeside = ImageTk.PhotoImage(img1)

        # image frametop
        img2 = Image.open("guitoptheme.jpg")
        img2 = img2.resize((657, 60), Image.Resampling.LANCZOS)
        themetop = ImageTk.PhotoImage(img2)

        # image frambot
        img3 = Image.open("guibottheme.jpg")
        img3 = img3.resize((660, 60), Image.Resampling.LANCZOS)
        themebot = ImageTk.PhotoImage(img3)

        # image register page
        img4 = Image.open("dbmspmss.jpg")
        img4 = img4.resize((660, 490), Image.Resampling.LANCZOS)
        thememain = ImageTk.PhotoImage(img4)




        #----------imglabels And frame

        #       left frame
        leftbord = tk.LabelFrame(self, width=170, height=600, bg="#051425", borderwidth=0, relief=RAISED)
        leftbord.pack(side=LEFT, fill="both")

        # imglabel
        imglil = tk.Label(leftbord, image=themeside, borderwidth=0)
        imglil.image = themeside
        imglil.place(x=0, y=0)

        #       right frame
        rightbord = tk.LabelFrame(self, width=170, height=600, bg="#051425", borderwidth=0, relief=RAISED)
        rightbord.pack(side=RIGHT, fill="both")

        # imglabel1
        imglil1 = tk.Label(rightbord, image=themeside, borderwidth=0)
        imglil1.image = themeside
        imglil1.place(x=0, y=0)

        #       top frame
        bordertop = tk.LabelFrame(self, width=660, height=50, bg="#051425", relief=SUNKEN, borderwidth=0)
        bordertop.pack(side=TOP, fill="both")

        # imglabel2
        imglil2 = tk.Label(bordertop, image=themetop, borderwidth=0)
        imglil2.image = themetop
        imglil2.place(x=0, y=0)

        #       bottom frame
        borderbot = tk.LabelFrame(self, width=660, height=60, bg="#051425", relief=SUNKEN, borderwidth=0)
        borderbot.pack(side=BOTTOM, fill="both")

        # imglabel3
        imglil3 = tk.Label(borderbot, image=themebot, borderwidth=0)
        imglil3.image = themebot
        imglil3.place(x=0, y=0)

        #image register main
        main = tk.LabelFrame(self, width=660, height=490, bg="#051425", relief=SUNKEN, borderwidth=0)
        main.pack(fill="both")

        # imglabel3
        imglil4 = tk.Label(main, image=thememain, borderwidth=0)
        imglil4.image = thememain
        imglil4.place(x=0, y=0)

        # ----------------label for database field

        # label1

        lil1 = Label(bordertop, text='Parking Management & Security System', font=("Arial", 16), fg="white",bg="#051425", borderwidth=0, )
        lil1.place(x=145, y=17)

        # label2  database info
        lil2 = Label(main, text='Add & Remove Vehicle and Owner details ', font=("Arial", 12, 'bold'), fg="white",bg="#0b1829", borderwidth=0, )
        lil2.place(x=190, y=40)


        # database np

        lil4 = Label(main, text='Enter Owner Name: ', font=('Arial', 10, 'bold'), fg="white", bg="#002036",borderwidth=0,pady=3, relief=GROOVE)
        lil4.place(x=80, y=115)

        # input databce np

        inp2 = Entry(main, width=35, justify=CENTER, fg="white", bg="#080914", borderwidth=8)  # input value
        inp2.place(x=310, y=110)

        # database

        lil5 = Label(main, text='Enter Vehicle Registration:', font=('Arial', 10, 'bold'), fg="white", bg="#002036",borderwidth=0, pady=3, relief=GROOVE)
        lil5.place(x=80, y=180)

        # input database
        inp3 = Entry(main, width=35, justify=CENTER, fg="white", bg="#080914", borderwidth=8)  # input value
        inp3.place(x=310, y=175)

        # ----------------buttons-----------------------------------------------------------------------------#

        # clear button, clear entry field
        def clearing():  ####Out put value


            inp2.delete(first=0, last=100)  # for clear from field after submit
            inp3.delete(first=0, last=100)  # for clear from field after submit


        cler = Button(main, text="Clear", padx=15, pady=10, fg="white", bg="#121b39", borderwidth=0,relief=RAISED,command=clearing)
        cler.place(x=480, y=240)

        # remove data button,dbms
        def remove_data():
            cur = conn.cursor()
            cur.execute("DELETE FROM testao WHERE  lc_num= %s;", (inp3.get(),))

            conn.commit()
            conn.commit()


        remve = Button(main, text="Remove Data", padx=15, pady=10, fg="white", bg="#121b39",borderwidth=0, relief=RAISED,command=remove_data)
        remve.place(x=310, y=300)  # 240)

        # submit button,dbms
        def add_data():

            cursor = conn.cursor()
            sql = """INSERT INTO testao (lc_num, owner_name)
                     VALUES (%s,%s)"""
            data = (inp3.get(),inp2.get())
            cursor.execute(sql, data)
            conn.commit()

        submt = Button(main, text="Add Data", padx=15, pady=10, fg="white", bg="#121b39", borderwidth=0,relief=RAISED,command=add_data)
        submt.place(x=465, y=300)

#           button for back to home pgae - PMSS
        button = tk.Button(borderbot, text='Back',padx=15, pady=7, fg="white", bg="#121b40",borderwidth=0,relief=RAISED, command=lambda: controller.show_frame(pmsshome))
        button.place(x=10, y=13)


#page4 for Credit

class credit(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # images ________________
        img1 = Image.open("parkingtheme.jpg")  # theme for frame left and right

        img1 = img1.resize((170, 600), Image.Resampling.LANCZOS)  # resize image
        themeside = ImageTk.PhotoImage(img1)

        # image frametop
        img2 = Image.open("guitoptheme.jpg")
        img2 = img2.resize((657, 60), Image.Resampling.LANCZOS)
        themetop = ImageTk.PhotoImage(img2)

        # image frambot
        img3 = Image.open("guibottheme.jpg")
        img3 = img3.resize((660, 60), Image.Resampling.LANCZOS)
        themebot = ImageTk.PhotoImage(img3)

        # image register page
        img4 = Image.open("creditpmss.jpg")
        img4 = img4.resize((660, 490), Image.Resampling.LANCZOS)
        thememain = ImageTk.PhotoImage(img4)

        # ----------imglabels And frame

        #       left frame
        leftbord = tk.LabelFrame(self, width=170, height=600, bg="#051425", borderwidth=0, relief=RAISED)
        leftbord.pack(side=LEFT, fill="both")

        # imglabel
        imglil = tk.Label(leftbord, image=themeside, borderwidth=0)
        imglil.image = themeside
        imglil.place(x=0, y=0)

        #       right frame
        rightbord = tk.LabelFrame(self, width=170, height=600, bg="#051425", borderwidth=0, relief=RAISED)
        rightbord.pack(side=RIGHT, fill="both")

        # imglabel1
        imglil1 = tk.Label(rightbord, image=themeside, borderwidth=0)
        imglil1.image = themeside
        imglil1.place(x=0, y=0)

        #       top frame
        bordertop = tk.LabelFrame(self, width=660, height=50, bg="#051425", relief=SUNKEN, borderwidth=0)
        bordertop.pack(side=TOP, fill="both")

        # imglabel2
        imglil2 = tk.Label(bordertop, image=themetop, borderwidth=0)
        imglil2.image = themetop
        imglil2.place(x=0, y=0)

        #       bottom frame
        borderbot = tk.LabelFrame(self, width=660, height=60, bg="#051425", relief=SUNKEN, borderwidth=0)
        borderbot.pack(side=BOTTOM, fill="both")

        # imglabel3
        imglil3 = tk.Label(borderbot, image=themebot, borderwidth=0)
        imglil3.image = themebot
        imglil3.place(x=0, y=0)

        # image register main
        main = tk.LabelFrame(self, width=660, height=490, bg="#051425", relief=SUNKEN, borderwidth=0)
        main.pack(fill="both")

        # imglabel3
        imglil4 = tk.Label(main, image=thememain, borderwidth=0)
        imglil4.image = thememain
        imglil4.place(x=0, y=0)

        # label1

        lil1 = Label(bordertop, text='Parking Management & Security System', font=("Arial", 16), fg="white", bg="#051425", borderwidth=0, )
        lil1.place(x=145, y=17)

#       button for back to home- PMSS
        button = tk.Button(borderbot, text='Back',padx=15, pady=7, fg="white", bg="#121b40",borderwidth=0,relief=RAISED,  command=lambda: controller.show_frame(pmsshome))
        button.place(x=10, y=13)


###################

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a window
        window = Frame(self)
        window.pack()


        window.grid_rowconfigure(0, minsize=600)
        window.grid_columnconfigure(0, minsize=1000)


        self.frames = {}
        for F in (userlogin, pmsshome,regdbms,credit):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(userlogin)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

app = Application()
app.resizable(width=False, height=False)  # to disable resize window
app.configure(bg="#08101b")
app.title('Parking Management & Security System')

#LOGO_GUI
image_icon= PhotoImage(file="pmsslogo.png")
app.iconphoto(False,image_icon)
#Force close gui



#root.bind('<Escape>', lambda e: root.quit())
app.bind('<Escape>', lambda e: sys.exit("Force Shutdown"))

app.mainloop()
