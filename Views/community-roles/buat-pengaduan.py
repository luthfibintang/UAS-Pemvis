from customtkinter import *
from tkinter import Canvas, Menu
from spinBox import FloatSpinbox
from CTkTable import *
import os
from PIL import Image

# Function to open detail
def open_detail():
    print("Detail button clicked!")

# Function to handle logout
def logout():
    main.destroy()
    os.system("python views/auth/login.py")

# Function to handle profile
def profile():
    print("Profile clicked!")

def back_button():
    main.destroy()
    os.system("python views/community-roles/list-pengaduan.py")

main = CTk()
main.title("List Pengaduan")
main.config(bg="#F4F6F9")

# Main window dimensions
main_width = 1080
main_height = 768

# Get screen dimensions
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

# Calculate x and y coordinates to center the window
x = (screen_width // 2) - (main_width // 2)
y = (screen_height // 2) - (main_height // 2)

# Set the geometry of the window
main.geometry(f"{main_width}x{main_height}+{x}+{y}")
main.resizable(False, False)

# Navbar frame
navbar = CTkFrame(main, fg_color="#6777EF", bg_color="white", width=main_width, height=88.5, corner_radius=0)
navbar.place(x=0, y=0)

# Title label in the navbar
appName_lbl = CTkLabel(navbar, text="SuaraKu", text_color="white", font=("PlusJakartaSans", 27, "bold"))
appName_lbl.place(x=27, y=27)

dashboard_lbl = CTkLabel(navbar, text="Dashboard", text_color="white", font=("PlusJakartaSans", 18))
dashboard_lbl.place(x=323, y=34)

pengaduan_lbl = CTkLabel(navbar, text="Pengaduan", text_color="white", font=("PlusJakartaSans", 18))
pengaduan_lbl.place(x=482, y=34)

canvas = Canvas(navbar, width=151.5)
canvas.create_rectangle(455, 2, 607, 2, width=3)
canvas.place(x=450, y=82)

user_lbl = CTkLabel(navbar, text="User", text_color="white", font=("PlusJakartaSans", 18))
user_lbl.place(x=645, y=34)

profile_img = CTkImage(dark_image=Image.open("Assets/frame0/image_1.png"), size=(45, 45))
profile_lab = CTkLabel(navbar, image=profile_img, text="")
profile_lab.place(x=830, y=23.25)

username_lbl = CTkLabel(navbar, text="Hi, Marcus Miles", text_color="white", font=("PlusJakartaSans", 18))
username_lbl.place(x=883, y=33)

# Dropdown menu
menu = Menu(main, tearoff=0)
menu.add_command(label="Profile", command=profile)
menu.add_command(label="Logout", command=logout)

# Function to show the dropdown menu
def show_menu(event):
    menu.post(event.x_root, event.y_root)

# Dropdown trigger
dropdown_trigger = CTkLabel(navbar, text="▼", text_color="white", font=("PlusJakartaSans", 18), cursor="hand2")
dropdown_trigger.place(x=1020, y=33)
dropdown_trigger.bind("<Button-1>", show_menu)

# Content title frame
content_title = CTkFrame(main, fg_color="#FFFFFF", bg_color="white", width=990.75, height=96.75)
content_title.place(x=41.25, y=121.5)

contentTitle_lbl = CTkLabel(content_title, text="Tulis Pengaduan", text_color="black", font=("PlusJakartaSans", 24, "bold"), cursor="hand2")
contentTitle_lbl.place(x=105.5 - 41.25, y=153 - 121.5)

backButton_img = CTkImage(dark_image=Image.open("Assets/arrow.png"), size=(26.25, 26.25))
search_lab = CTkLabel(content_title, image=backButton_img, text="", cursor="hand2")
search_lab.place(x=62.75 - 41.25, y=153 - 121.5)
search_lab.bind("<Button-1>", lambda e: back_button())

# Content frame
content = CTkFrame(main, fg_color="#FFFFFF", bg_color="white", width=990.75, height=484.5)
content.place(x=41.25, y=250.5)

title_lbl = CTkLabel(content, text="Judul", text_color="black", font=("PlusJakartaSans", 15))
title_lbl.place(x=69 - 41.25, y=271 - 250.5)

title_entry = CTkEntry(content, text_color="black", fg_color="#FDFDFF", border_color="#b5b5b5", border_width=1, font=("", 15), width=938.25, height=35)
title_entry.place(x=69 - 41.25, y=295 - 250.5)

reportDesc_lbl = CTkLabel(content, text="Isi Pengaduan", text_color="black", font=("PlusJakartaSans", 15))
reportDesc_lbl.place(x=69 - 41.25, y=346 - 250.5)

reportDesc_txtb = CTkTextbox(content, text_color="black", fg_color="#FDFDFF", border_color="#b5b5b5", border_width=1, font=("", 15), width=938.25, height=132)
reportDesc_txtb.place(x=69 - 41.25, y=374 - 250.5)

reportDate_lbl = CTkLabel(content, text="Tanggal Laporan", text_color="black", font=("PlusJakartaSans", 15))
reportDate_lbl.place(x=69 - 41.25, y=520 - 250.5)

reportDate_entry = CTkEntry(content, text_color="black", fg_color="#FDFDFF", border_color="#b5b5b5", border_width=1, font=("", 15), width=938.25, height=35)
reportDate_entry.place(x=69 - 41.25, y=546 - 250.5)

complaintProv_lbl = CTkLabel(content, text="Foto Profile", text_color="black", font=("PlusJakartaSans", 13))
complaintProv_lbl.place(x=69 - 41.25, y=593 - 250.5)

complaintProv_entry = CTkEntry(content, text_color="black", fg_color="#FDFDFF", border_color="#b5b5b5", border_width=1, font=("", 15), width=798.25, height=35, state=DISABLED)
complaintProv_entry.place(x=69 - 41.25, y=621 - 250.5)

complaintProv_btn = CTkButton(content, text="Browse", width=150, height=35, fg_color="#888888", hover_color="#AEAEAE", font=("PlusJakartaSans", 15), cursor="hand2")
complaintProv_btn.place(x=855.75 - 41.25, y=621 - 250.5)

addPengaduan_btn = CTkButton(content, text="Kirim Pengaduan", width=156.75, height=42, fg_color="#6777EF", hover_color="#424D98", font=("PlusJakartaSans", 15), cursor="hand2")
addPengaduan_btn.place(x=849 - 41.25, y=677.25 - 250.5)

main.mainloop()