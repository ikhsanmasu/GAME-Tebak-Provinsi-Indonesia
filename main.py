import turtle
from turtle import Screen, Turtle
import pandas as pd
import os
import sys

# use this directory when generating exe file
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

csv_dir = application_path + "/indonesia_province.csv"
image_dir = application_path + "/indonesia_map.gif"
guessed_dir = application_path + "/guessed_province.csv"

# # use this file to simulate this file using IDE
# csv_dir = "indonesia_province.csv"
# image_dir = "indonesia_map.gif"
# guessed_dir = "guessed_province.csv"

provinces = pd.read_csv(csv_dir)

screen = Screen()
screen.setup(width=1280, height=720)
screen.title("Indonesia Province")
screen.addshape(image_dir)
turtle.shape(image_dir)

instruction = Turtle()
instruction.penup()
instruction.hideturtle()
instruction.color("black")
instruction.goto((0, 300))
instruction.write("ketik 'exit' untuk keluar\nketik 'reset' untuk mengulang", move=False, align="center",
                  font=("Arial", 12, "bold"))


def add_province_name_to_map(name):
    province_data = provinces[provinces.province == name]
    x_cor = int(province_data.x.values)
    y_cor = int(province_data.y.values)
    name_write = Turtle()
    name_write.penup()
    name_write.hideturtle()
    name_write.color("black")
    name_write.goto((x_cor, y_cor))
    name_write.write(f"{name.upper()}", move=False, align="center", font=("Arial", 8, "bold"))


guessed_province = []

try:
    update_last_guessed = pd.read_csv(guessed_dir)
    guessed_province = [x for x in update_last_guessed["0"]]
except KeyError:
    guessed_province = []

for province in guessed_province:
    add_province_name_to_map(province)

all_province = provinces["province"].to_list()
len_province = len(all_province)

is_on = True
while is_on:
    try:
        len_guessed = len(guessed_province)
        answered_province = screen.textinput(title=f"{len_guessed}/{len_province} provinsi benar",
                                             prompt="Ketik nama provinsi lainnya").upper()
        if answered_province in all_province:
            add_province_name_to_map(answered_province)
            if answered_province not in guessed_province:
                guessed_province.append(answered_province)
        elif answered_province == "RESET":
            guessed_province = []
            screen.clear()
            screen.addshape(image_dir)
            turtle.shape(image_dir)
            instruction.write("ketik 'exit' untuk keluar\nketik 'reset' untuk mengulang", move=False, align="center",
                              font=("Arial", 12, "bold"))
        elif answered_province.lower() == "exit":
            new_data = pd.DataFrame(guessed_province)
            new_data.to_csv(guessed_dir)
            is_on = False

    except AttributeError:
        new_data = pd.DataFrame(guessed_province)
        new_data.to_csv(guessed_dir)
        is_on = False
