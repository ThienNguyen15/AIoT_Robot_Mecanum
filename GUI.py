from pathlib import Path

from tkinter import *
from tkinter.font import Font
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk
import cv2
from AI_Detection_Traffic_Signs import *
from main import *
from datetime import datetime

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Project HDL\Tkinter-Designer-master\build_core\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title("Project HDL - AI Detection UI")
window.iconbitmap('C:/Users/thien/OneDrive/Máy tính/Project HDL/cse.ico')

window.geometry("1200x700")
window.configure(bg="#FFFFFF")

canvas = Canvas(window, bg="#FFFFFF", height=700, width=1200, bd=0, highlightthickness=0, relief="ridge")

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(600.0, 350.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(907.0, 497.0, image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(907.0, 270.0, image=image_image_3)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(907.0, 170.0, image=image_image_4)

image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(907.0, 70.0, image=image_image_5)

image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(439.0, 587.0, image=image_image_6)

image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(257.0, 587.0, image=image_image_7)

image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(277.0, 495.0, image=image_image_8)

image_image_9 = PhotoImage(file=relative_to_assets("image_15.png"))
image_9 = canvas.create_image(277.0, 230.0, image=image_image_9)


# History
custom_font1 = Font(family="Times", size=26, weight="normal")
# slant="italic", underline=0, overstrike=0
history1 = ""
history2 = ""
history3 = ""
history4 = ""
history5 = ""
history6 = ""

def fix_time(current_time):
    day = str(current_time.day)
    month = str(current_time.month)
    hour = str(current_time.hour)
    minute = str(current_time.minute)
    second = str(current_time.second)
    if int(day) < 10:
        day = "0" + day
    if int(month) < 10:
        month = "0" + month
    if int(hour) < 10:
        hour = "0" + hour
    if int(minute) < 10:
        minute = "0" + minute
    if int(second) < 10:
        second = "0" + second
    return day, month, hour, minute, second

def change_history(new_value):
    global history1, history2, history3, history4, history5, history6
    current_time = datetime.now()
    day, month, hour, minute, second = fix_time(current_time)

    if (history1 != "" and history2 != "" and history3 != ""
        and history4 != "" and history5 != "" and history6 != ""):
        history1 = history2
        history2 = history3
        history3 = history4
        history4 = history5
        history5 = history6
        history6 = day + "/" + month + "/" + "24" + " " + hour + ":" + minute + ":" + second + " " + new_value
    elif history1 == "":
        history1 = day + "/" + month + "/" + "24" + " " + hour + ":" + minute + ":" + second + " " + new_value
    elif history1 != "" and history2 == "":
        history2 = day + "/" + month + "/" + "24" + " " + hour + ":" + minute + ":" + second + " " + new_value
    elif history1 != "" and history2 != "" and history3 == "":
        history3 = day + "/" + month + "/" + "24" + " " + hour + ":" + minute + ":" + second + " " + new_value
    elif history1 != "" and history2 != "" and history3 != "" and history4 == "":
        history4 = day + "/" + month + "/" + "24" + " " + hour + ":" + minute + ":" + second + " " + new_value
    elif history1 != "" and history2 != "" and history3 != "" and history4 != "" and history5 == "":
        history5 = day + "/" + month + "/" + "24" + " " + hour + ":" + minute + ":" + second + " " + new_value
    elif history1 != "" and history2 != "" and history3 != "" and history4 != "" and history5 != "" and history6 == "":
        history6 = day + "/" + month + "/" + "24" + " " + hour + ":" + minute + ":" + second + " " + new_value

    history.config(text=history1+"\n"+history2+"\n"+history3+"\n"+history4+"\n"+history5+"\n"+history6,)

history = Label(font=custom_font1, text=history1+"\n"+history2+"\n"+history3+"\n"+history4+"\n"+history5+"\n"+history6,
                 borderwidth=0, anchor="w", justify=LEFT, highlightthickness=0, bg="#E1F1FD")

history.place(x=652.0, y=368.0, width=510.0, height=290.0)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, bg="#E1F1FD")
button_1.place(x=659.0, y=330.0, width=150.0, height=62.0)


custom_font = Font(family="Times", size=35, weight="normal")


# Accuracy
def change_accuracy(new_value):
    global accuracy_UI
    accuracy_UI = new_value
    button_2.config(text="Accuracy: " + accuracy_UI + "%")

accuracy_UI = "0"
button_2 = Button(font=custom_font, text="Accuracy: " + accuracy_UI + "%",
                  borderwidth=0, highlightthickness=0, bg="#E1F1FD")
button_2.place(x=658.0, y=239.0, width=500.0, height=62.0)


# Traffic Signs
def change_traffic_sign(new_value):
    global traffic_sign
    traffic_sign = new_value
    button_3.config(text=traffic_sign)

traffic_sign = "Không hình ảnh"
button_3 = Button(font=custom_font, text=traffic_sign,
                  borderwidth=0, highlightthickness=0, bg="#E1F1FD")
button_3.place(x=658.0, y=139.0, width=500.0, height=62.0)


button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(image=button_image_4, borderwidth=0, highlightthickness=0, bg="#E1F1FD")
button_4.place(x=698.0, y=39.0, width=420.0, height=62.0)


# Cam_Mode
button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(image=button_image_5, borderwidth=0, highlightthickness=0, bg="#E1F1FD")
button_5.place(x=124.0, y=560.0, width=265.0, height=55.0)


# Automatic_On_Off
Flag = 0
def Automatic_On_Off():
    global button_image_4, button_4, Flag, Flag_UI, button_image_6, button_6, Flag1, button_image_7, button_7
    if Flag == 0:
        button_image_4 = PhotoImage(file=relative_to_assets("button_15.png"))
        button_image_6 = PhotoImage(file=relative_to_assets("button_17.png"))
        Flag = 1
        Flag_UI = 1
        Generate_UI()
    elif Flag == 1:
        button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
        button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
        Flag = 0
        Flag_UI = 0
        if Flag1 == 1:
            button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
            Flag1 = 0
            toggle_camera()
            button_7.config(image=button_image_7)

    button_4.config(image=button_image_4)
    button_6.config(image=button_image_6)


# Cam_IP
button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
button_6 = Button(image=button_image_6, borderwidth=0, highlightthickness=0,
                  bg="#E1F1FD", command=lambda: Automatic_On_Off(), relief="flat")
button_6.place(x=124.0, y=464.0, width=308.0, height=62.0)


# Frame Cam
camera_active = True
def toggle_camera():
    global camera_active
    camera_active = not camera_active

def update_frame():
    if camera_active:
        frame = get_data()
        label = Label(width=519, height=394)
        label.place(x=16.0, y=31.0)

        frame = cv2.resize(frame, (519, 394)) # resize the frame to 200x200
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.configure(image=imgtk)
        window.after(500, update_frame)


# Cam_On_Off
Flag1 = 0
def Cam_On_Off():
    global button_image_7, button_7, Flag1, camera_active, Flag_UI
    if Flag_UI == 1:
        if Flag1 == 0:
            button_image_7 = PhotoImage(file=relative_to_assets("button_16.png"))
            Flag1 = 1
            camera_active = True
            update_frame()
        elif Flag1 == 1:
            button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
            Flag1 = 0
            toggle_camera()
    else:
        button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
        Flag1 = 0
        camera_active = False

    button_7.config(image=button_image_7)

button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
button_7 = Button(image=button_image_7, borderwidth=0, highlightthickness=0,
                  bg="#E1F1FD", command=lambda: Cam_On_Off(), relief="flat")
button_7.place(x=420.0, y=568.0, width=40.0, height=40.0)


Flag_UI = 0
def Generate_UI():
    global counter_ai, ai_res, prev_res, accuracy, prev_accuracy
    if Flag_UI == 1:
        counter_ai = counter_ai - 1
        if counter_ai <= 0:
            counter_ai = 1
            prev_accuracy = accuracy
            if int(prev_accuracy) >= 75:
                prev_res = ai_res
            new_state, ai_res, image, accuracy = image_detector()
            print("AI Output: ", ai_res.strip() + " " + accuracy + "%")
            if prev_res != ai_res and int(accuracy) >= 75:
                # Publish data to Adafruit Server
                client.publish("p.ai", ai_res)
                client.publish("p.image", image)
                client.publish("p.tile", accuracy + "%")
                client.publish("ai", new_state)
                change_history(ai_res.strip())
                change_accuracy(accuracy)
                change_traffic_sign(ai_res.strip())
            # getkey_input(new_state)
            window.after(1000, Generate_UI)


window.resizable(False, False)
window.mainloop()
