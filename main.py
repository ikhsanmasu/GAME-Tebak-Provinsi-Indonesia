import turtle
from turtle import Screen, Turtle
import pandas as pd
import os
import sys


if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

# csv_dir = application_path + "/indonesia_province_coordinate.csv"
# image_dir = application_path + "/indonesia_resized.gif"

csv_dir = "indonesia_province_coordinate.csv"
image_dir = "indonesia_resized.gif"

curdir = os.getcwd()
provinces = pd.read_csv(csv_dir)
provinces_name = provinces.province.to_list()

screen = Screen()
screen.setup(width=1280, height=720)
screen.title("Indonesia Province")
screen.addshape(image_dir)
turtle.shape(image_dir)

instruction = Turtle()
instruction.penup()
instruction.hideturtle()
instruction.color("black")
instruction.goto((0, 330))
instruction.write("ketik 'exit' untuk keluar", move=False, align="center", font=("Arial", 8, "bold"))

def add_province_name_to_map(name):
    x_cor = float(provinces[provinces.province == name.upper()].coordinate.to_list()[0].split(",")[0][1:])
    y_cor = float(provinces[provinces.province == name.upper()].coordinate.to_list()[0].split(",")[1][:-1])
    name_write = Turtle()
    name_write.penup()
    name_write.hideturtle()
    name_write.color("black")
    name_write.goto((x_cor, y_cor))
    name_write.write(f"{name.upper()}", move=False, align="center", font=("Arial", 8, "bold"))

is_on = True
while is_on:
    answer_state = screen.textinput(title="Tebak semua nama provinsi", prompt="Ketik nama provinsi lainnya")
    if answer_state.upper() in provinces_name:
        add_province_name_to_map(answer_state)
    elif answer_state.lower() == "exit":
        is_on = False

