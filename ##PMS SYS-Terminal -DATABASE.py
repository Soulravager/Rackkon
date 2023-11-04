# PMS_SYSTEM_TERMINAL_WORKING
import requests
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
import cv2
import multiprocessing

# module level variables ##########################################################################
SCALAR_BLACK = (0.0, 0.0, 0.0)
SCALAR_WHITE = (255.0, 255.0, 255.0)
SCALAR_YELLOW = (0.0, 255.0, 255.0)
SCALAR_GREEN = (0.0, 255.0, 0.0)
SCALAR_RED = (0.0, 0.0, 255.0)
showSteps = False

###################################################################################################
# connecting DBMS
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="alpha123"
)
cur = conn.cursor()
max_attempts = 5  # maximum attempts for user login

# Prompt the user for their username and password
for attempt in range(1, max_attempts + 1):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    cur.execute("SELECT * FROM login WHERE user_id = %s AND password = %s", (username, password))
    result = cur.fetchone()

    if result:
        print("\033[34mLogin successful!!\033[0m")
        print("Starting PMS system..")
        break
    else:
        print("\033[31mInvalid username or password\033[0m")
        if attempt == max_attempts:
            print("\033[31mMaximum attempts reached. Exiting program...\033[0m")
            sys.exit()
        else:
            print(f"\033[31mYou have {max_attempts - attempt} attempt(s) remaining. Please try again.\033[0m")

ip_camera_num = input("Enter Ip-camera IP Adders:")
ip_camera_port = input("Enter Ip-camera port Number:")
print("Current Ip-camera IP adders selected    :" + ip_camera_num)
print("Current Ip-camera Ip port selected      :" + ip_camera_port)
camera_ip = "http://" + ip_camera_num + ":" + ip_camera_port + "/video"  # For input as video frames

# camera_ip = "http://" + ip_camera_num + ":" + ip_camera_port + "/shot.jpg"  # For input as frame by frame

print("Camera connected to " + " " + camera_ip)

# Android Broadcast ip
Ip_broadcast = "192.168.0.100"
# Telegram chat id
print("Please select an Telegram User :")
print("1. Alwin ")
print("2. Suhail")
print("3. adithya")

while True:
    choice = input("Please select a Telegram User : ")
    if choice == "1":
        print("\033[34mYou selected Alwin.\033[0m")
        tele_chat_id = '754112013'
        break  # Exit the loop
    elif choice == "2":
        print("\033[34mYou selected Suhail.\033[0m")
        tele_chat_id = '766494078'
        break  # Exit the loop
    elif choice == "3":
        print("\033[34mYou selected Adithya.\033[0m")
        print("User id not present.")
    else:
        print("\033[31mInvalid choice. Please select a Telegram user.\033[0m")


def main():
    camera()
    cur = conn.cursor()
    now = datetime.datetime.now()
    blnKNNTrainingSuccessful = DetectChars.loadKNNDataAndTrainKNN()  # attempt KNN training

    if not blnKNNTrainingSuccessful:  # if KNN training was not successful
        print("\nerror: KNN training was not successful\n")  # show error message
        return  # and exit program
    # end if

    url = camera_ip
    now = datetime.datetime.now()
    time_str = now.strftime("TIME=%H-%M-%S_Date=%d-%m-%Y")
    time_str = time_str

    def generate():
        return random.randint(1, 9999)  # Parking lot number of lines

    # Input camera
    cap = cv2.VideoCapture(url)
    while (1):
        time.sleep(1)
        ret, frame = cap.read()
        key = cv2.waitKey(1)
        # img_name = f'img_out/image_output_{time_str}.jpg'
        # cv2.imwrite(img_name, frame)
        if key:
            break
    cap.release()
    cv2.destroyAllWindows()
    imgOriginalScene = frame  # cv2.imread(IMAGE_OUTPUT)               # open image

    if imgOriginalScene is None:  # if image was not read successfully
        print("\nerror: image not read from file \n\n")  # print error message to std out
        os.system("pause")  # pause so user can see error message
        return  # and exit program
    # end if

    listOfPossiblePlates = DetectPlates.detectPlatesInScene(imgOriginalScene)  # detect plates

    listOfPossiblePlates = DetectChars.detectCharsInPlates(listOfPossiblePlates)  # detect chars in plates

    # #####cv2.imshow("imgOriginalScene", imgOriginalScene)            # show scene image >>>>>>>>>>IMG OUT
    # PUT<<<<<<<<<<<<<<<

    if len(listOfPossiblePlates) == 0:  # if no plates were found
        print("\nno license plates were detected\n")  # inform user no plates were found
        print("system is idling ")

    else:  # else

        listOfPossiblePlates.sort(key=lambda possiblePlate: len(possiblePlate.strChars), reverse=True)

        licPlate = listOfPossiblePlates[0]

        if len(licPlate.strChars) < 6:  # if no chars were found in the plate
            print("\nno characters were detected\n\n")  # show message
            return  # and exit program

        print("Vehicle Registration:: " + licPlate.strChars)
        print(now.strftime("Date=%d-%m-%y Time=%H:%M:%S"))

        # DBMS CHECKING WITH AUTH TABLE###
        lc_num = licPlate.strChars
        # execute SQL query to select the rows from the table that match the string
        query = "SELECT * FROM users WHERE lc_number = %s;"
        cur.execute(query, (lc_num,))
        rows = cur.fetchall()
        if len(rows) == 0:
            print("Unauthorized_Vehicle")
            user_name_data = "Unknown User"
            access_data = "Unauthorized_Vehicle"

            def generate_random_number():
                return random.randint(1, 20)  # Parking lot number of lines

            def generate_random_string():
                # letters = string.ascii_uppercase
                letters = ['TEMP']  # parking lot line
                return ''.join(random.choice(letters) for i in range(1))

            file = open("Unauthorized_Vehicle_list.csv", "a")
            A = []
            w = csv.writer(file)
            n = 1
            while n <= 1:
                r = str("Unauthorized_Vehicle_Number = " + lc_num + ',' + now.strftime(
                    "Date=%d-%m-%y Time=%H:%M:%S"))
                A.append(r)
                n = n + 1
                w.writerow(A)
                file.close()

        else:
            for row in rows:
                print("Authorized_Vehicle")

                def generate_random_number():
                    return random.randint(1, 10)  # Parking lot number of lines

                def generate_random_string():
                    # letters = string.ascii_uppercase
                    letters = ['A', 'B']  # parking lot line
                    return ''.join(random.choice(letters) for i in range(1))

                user_name = row[1]
                user_name_data = user_name
                print("Owner_name:" + user_name)  # print the other attributes in the row
                access_data = "Authorized"
        check_entry = lc_num

        cur = conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM output WHERE reg_num  = '{check_entry}'")
        count = cur.fetchone()[0]
        if count % 2 == 0:
            car_entry = "Entered"
        else:
            car_entry = "Exited"

        def send_to_telegram(message):
            apiToken = '6047129599:AAFqm2xkAkwE2NKw5G7DNhWs1C7bbEg5Wi8'
            chatID = tele_chat_id
            apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

            try:
                response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
                # print(response.text)
                print("Notified to the admin !!")
            except Exception as e:
                print(e)

        def random_number():
            return random.randint(1, 20)  # Parking lot number of lines

        def random_string():
            # letters = string.ascii_uppercase
            letters = ['A', 'B', 'C']  # parking lot line
            return ''.join(random.choice(letters) for i in range(1))

        num_park = str(generate_random_number())
        char_park = generate_random_string()

        #   for data insertion to output csv file

        file = open("Data_PMS/OUTPUT_DATA.csv", "a")
        A = []
        w = csv.writer(file)
        n = 1
        while n <= 1:
            r = str("vehicle Number= " + lc_num + ',' + now.strftime(
                "Date=%d-%m-%y Time=%H:%M:%S") + "," + "Owner name=" + user_name_data + "," + "Entry Type=" + access_data + "," + "Assigned parkingLot=" + char_park + "-" + num_park + "," + "Car Entry:" + check_entry)
            A.append(r)
            n = n + 1
            w.writerow(A)
            file.close()

        if len(lc_num) == 0:
            print("no data")

        else:
            sql = "INSERT INTO output (reg_num, time, date,authentication,user_name,parking_lot,entry) VALUES (%s, " \
                  "%s, %s,%s,%s,%s,%s) "
            lc_number = lc_num
            car_stat = car_entry
            Authentication = access_data
            owner = user_name_data
            Parking_lot = char_park + num_park
            cur.execute(sql,
                        (lc_number, now.strftime("%H:%M:%S"), now.strftime("%Y-%m-%d"), Authentication, owner,
                         Parking_lot,
                         car_stat))
            print("Data added to Database!!")
            conn.commit()
            data_to_delete = Parking_lot
            if car_entry == 'Exited':
                print("vehicle exited!")
                cur = conn.cursor()
                cur.execute(f"UPDATE output SET parking_lot = NULL WHERE parking_lot = '{data_to_delete}'")
                conn.commit()
                cur.close()
                if user_name_data == "Unknown User":
                    send_to_telegram(lc_num + " " + "Exited the parking lot")
                else:
                    send_to_telegram(owner + " " + lc_num + " " + "Exited the parking lot ")
            else:
                camera_record()
                print("Vehicle entered!")
                send_to_telegram("vehicle Number= " + lc_num + '' + '' + '' + now.strftime(
                    "\nDate=%d-%m-%y \nTime=%H:%M:%S") + "\nOwner name=" + user_name_data + "\nEntry Type=" + access_data + "\nAssigned parkingLot=" + char_park + "-" + num_park)

            # for android broadcast
            if car_stat == "Entered":
                UDP_IP = Ip_broadcast  # Change to a valid IP address on your network
                UDP_PORT = 5005  # Change to a different port number if needed
                MESSAGE = lc_num + "Allocated parking lot:" + Parking_lot
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
                print("message send to driver!!")

                cap = cv2.VideoCapture(url)
                while (1):
                    time.sleep(1)
                    ret, frame = cap.read()
                    key = cv2.waitKey(1)
                    img_name = f'vehicle_img_out/Entered_vehicle {time_str}.jpg'
                    cv2.imwrite(img_name, frame)
                    if key:
                        break


def camera_record():
    # Define the codec and output video parameters
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_folder = "vehicle_Entry_recording"  # specify the folder to save the video in
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # create the folder if it doesn't exist
    current_time = time.strftime("TIME=%H-%M-%S_Date=%d-%m-%Y", time.localtime())
    output_filename = f"vehicle_Entry {current_time}.avi"  # append timestamp to filename
    output_path = os.path.join(output_folder, output_filename)  # specify the output video path
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (1280, 720))

    # Capture video from IP camera
    cap = cv2.VideoCapture(camera_ip)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Record the start time
    start_time = time.time()

    while (cap.isOpened()):
        # Read a frame from the camera
        ret, frame = cap.read()

        if ret == True:
            # Write the frame to the output video file
            frame = cv2.resize(frame, (1280, 720))
            out.write(frame)

            # Exit if 'q' is pressed or if 10 seconds have passed
            elapsed_time = time.time() - start_time
            if cv2.waitKey(1) & 0xFF == ord('q') or elapsed_time >= 3:
                break
        else:
            break

    # Release the resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def camera():
    # Define the codec and output video parameters
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_folder = "video_output"  # specify the folder to save the video in
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # create the folder if it doesn't exist
    current_time = time.strftime("TIME=%H-%M-%S_Date=%d-%m-%Y", time.localtime())
    output_filename = f"PMS_OUT_{current_time}.avi"  # append timestamp to filename
    output_path = os.path.join(output_folder, output_filename)  # specify the output video path
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (1280, 720))

    # Capture video from IP camera
    cap = cv2.VideoCapture(camera_ip)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Record the start time
    start_time = time.time()

    while (cap.isOpened()):
        # Read a frame from the camera
        ret, frame = cap.read()

        if ret == True:
            # Write the frame to the output video file
            frame = cv2.resize(frame, (1280, 720))
            out.write(frame)

            # Exit if 'q' is pressed or if 10 seconds have passed
            elapsed_time = time.time() - start_time
            if cv2.waitKey(1) & 0xFF == ord('q') or elapsed_time >= 4:
                break
        else:
            break

    # Release the resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()


try:

    while True:
        main()

except KeyboardInterrupt:
    print("\033[31mPMS system is stopped by user!!\033[0m")
    sys.exit()

# cur.close()
conn.close()
###################################################################################################
if __name__ == "__main__":
    main()
