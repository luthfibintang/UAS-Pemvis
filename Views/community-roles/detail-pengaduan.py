from customtkinter import *
import tkinter as tk
from tkinter import filedialog, Menu, Canvas, messagebox
from PIL import Image
import os
import sys
from datetime import datetime
sys.path.insert(1, 'C://Dev//UPJ//pemvis//uas')
import pengadubcknd

# Function to handle logout
def logout():
    confirmation = messagebox.askyesno("Logout", "Apakah Anda yakin ingin logout?")
    if confirmation:
        main.destroy()
        os.system("python views/auth/login.py")

if len(sys.argv) > 2:
    user_id = sys.argv[1]
    id_pengaduan = sys.argv[2]
    user_name = pengadubcknd.get_user_name(user_id)
    pengaduan_detail = pengadubcknd.get_pengaduan_detail(id_pengaduan)
    if pengaduan_detail['status'] == "Selesai":
        tanggapan_detail = pengadubcknd.get_tanggapan_detail(id_pengaduan)
else:
    user_id = None
    id_pengaduan = None
    user_name = "User"
    pengaduan_detail = None

def back_button():
    main.destroy()
    os.system(f"python views/community-roles/list-pengaduan.py {user_id}")

def open_profile():
    main.destroy()
    os.system(f"python Views/community-roles/user-profile.py {user_id}")

def open_pengaduan():
    main.destroy()
    os.system(f"python Views/community-roles/list-pengaduan.py {user_id}")

def open_dashboard():
    main.destroy()
    os.system(f"python Views/community-roles/dashboard-community.py {user_id}")

def display_image_with_fixed_height(image_path, desired_height):
    # Open the image
    image = Image.open(image_path)
    
    # Get the original dimensions
    original_width, original_height = image.size
    
    # Calculate the aspect ratio
    aspect_ratio = original_width / original_height
    
    # Calculate the new width based on the desired height and aspect ratio
    new_width = int(desired_height * aspect_ratio)
    
    # Resize the image
    resized_image = image.resize((new_width, desired_height), Image.Resampling.LANCZOS)
    
    return resized_image

main = CTk()
main.title("Detail Pengaduan")
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

dashboard_lbl = CTkLabel(navbar, text="Dashboard", text_color="white", font=("PlusJakartaSans", 18), cursor="hand2")
dashboard_lbl.place(x=323, y=34)
dashboard_lbl.bind("<Button-1>", lambda e: open_dashboard())

pengaduan_lbl = CTkLabel(navbar, text="Pengaduan", text_color="white", font=("PlusJakartaSans", 18), cursor="hand2")
pengaduan_lbl.place(x=482, y=34)
pengaduan_lbl.bind("<Button-1>", lambda e: open_pengaduan())

canvas = Canvas(navbar, width=151.5)
canvas.create_rectangle(455, 2, 607, 2, width=3)
canvas.place(x=450, y=82)

user_lbl = CTkLabel(navbar, text="User", text_color="white", font=("PlusJakartaSans", 18), cursor="hand2")
user_lbl.place(x=645, y=34)
user_lbl.bind("<Button-1>", lambda e: open_profile())

profile_img = CTkImage(dark_image=Image.open("Assets/frame0/image_1.png"), size=(45, 45))
profile_lab = CTkLabel(navbar, image=profile_img, text="")
profile_lab.place(x=830, y=23.25)

username_lbl = CTkLabel(navbar, text=f"Hi, {user_name}", text_color="white", font=("PlusJakartaSans", 18))
username_lbl.place(x=883, y=33)

# Dropdown menu
menu = Menu(main, tearoff=0)
menu.add_command(label="Profile", command=open_profile)
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

contentTitle_lbl = CTkLabel(content_title, text="Detail Pengaduan", text_color="black", font=("PlusJakartaSans", 24, "bold"), cursor="hand2")
contentTitle_lbl.place(x=105.5 - 41.25, y=153 - 121.5)

backButton_img = CTkImage(dark_image=Image.open("Assets/arrow.png"), size=(26.25, 26.25))
backButton_lab = CTkLabel(content_title, image=backButton_img, text="", cursor="hand2")
backButton_lab.place(x=62.75 - 41.25, y=153 - 121.5)
backButton_lab.bind("<Button-1>", lambda e: back_button())

# Content frame
if pengaduan_detail['status'] == "Selesai":
    content1 = CTkFrame(main, fg_color="#FFFFFF", bg_color="white", width= 474, height=522)
    content1.place(x=41.25, y=232.5)
    
    titlecontent_lbl = CTkLabel(content1, text="Pengaduan", text_color="black", font=("PlusJakartaSans", 18, "bold"))
    titlecontent_lbl.place(x=55 - 41.25, y=247.5 - 232.5)
    
    judul_lbl = CTkLabel(content1, text=pengaduan_detail['judul'], text_color="black", font=("PlusJakartaSans", 15, "bold"))
    judul_lbl.place(x=55 - 41.25, y=290 - 232.5)

    tgl_lbl = CTkLabel(content1, text=f"Tanggal dibuat : {pengaduan_detail['tgl_pengaduan']}", text_color="#616161", font=("PlusJakartaSans", 15))
    tgl_lbl.place(x=55 - 41.25, y=316.5 - 232.5)

    isiPengaduan_txtb = CTkTextbox(content1, text_color="black", fg_color="#FDFDFF", border_color="#b5b5b5", border_width=0, font=("", 15), width=435, height=112)
    isiPengaduan_txtb.insert("0.0", pengaduan_detail['isi_pengaduan'])
    isiPengaduan_txtb.configure(state=DISABLED)
    isiPengaduan_txtb.place(x=50 - 41.25, y=343.5 - 232.5)

    # Attachment
    attachment = pengaduan_detail['attachment']
    attachment_path = f"storage/img/{user_id}/{attachment}"
    if attachment:
        attachment_path = f"storage/img/{user_id}/{pengaduan_detail['attachment']}"
        desired_height = 240
        resized_image = display_image_with_fixed_height(attachment_path, desired_height)
        
        attachment_lbl = CTkLabel(content1, text="Lampiran :", text_color="black", font=("PlusJakartaSans", 15))
        attachment_lbl.place(x=55 - 41.25, y=475.25 - 232.5)

        attachment_img = CTkImage(dark_image=resized_image, size=(resized_image.width, desired_height))
        attachment_lab = CTkLabel(content1, image=attachment_img, text="")
        attachment_lab.place(x=55 - 41.25, y=500 - 232.5)
    
    content2 = CTkFrame(main, fg_color="#FFFFFF", bg_color="white", width= 474, height=522)
    content2.place(x=555, y=232.5)
    
    titlecontent_lbl = CTkLabel(content2, text="Tanggapan", text_color="black", font=("PlusJakartaSans", 18, "bold"))
    titlecontent_lbl.place(x=579 - 555, y=247.5 - 232.5)
    
    judul_lbl = CTkLabel(content2, text=f"Ditanggapi oleh : {tanggapan_detail["nama"]} - {tanggapan_detail['id_user']}", text_color="black", font=("PlusJakartaSans", 15, "bold"))
    judul_lbl.place(x=579 - 555, y=290 - 232.5)

    tgl_lbl = CTkLabel(content2, text=f"Tanggal dibuat : {tanggapan_detail['tgl_tanggapan']}", text_color="#616161", font=("PlusJakartaSans", 15))
    tgl_lbl.place(x=579 - 555, y=316.5 - 232.5)

    isiPengaduan_txtb = CTkTextbox(content2, text_color="black", fg_color="#FDFDFF", border_color="#b5b5b5", border_width=0, font=("", 15), width=435, height=112)
    isiPengaduan_txtb.insert("0.0", tanggapan_detail['isi_tanggapan'])
    isiPengaduan_txtb.configure(state=DISABLED)
    isiPengaduan_txtb.place(x=574 - 555, y=343.5 - 232.5)

    # Attachment
    attachment = tanggapan_detail['attachment']
    attachment_path = f"storage/img/tanggapan/{tanggapan_detail['id_user']}/{attachment}"
    if attachment:
        attachment_path = f"storage/img/tanggapan/{tanggapan_detail['id_user']}/{tanggapan_detail['attachment']}"
        desired_height = 240
        resized_image = display_image_with_fixed_height(attachment_path, desired_height)
        
        attachment_lbl = CTkLabel(content2, text="Lampiran :", text_color="black", font=("PlusJakartaSans", 15))
        attachment_lbl.place(x=579 - 555, y=475.25 - 232.5)

        attachment_img = CTkImage(dark_image=resized_image, size=(resized_image.width, desired_height))
        attachment_lab = CTkLabel(content2, image=attachment_img, text="")
        attachment_lab.place(x=579 - 555, y=500 - 232.5)
else:
    content = CTkFrame(main, fg_color="#FFFFFF", bg_color="white", width=990.75, height=484.5)
    content.place(x=41.25, y=250.5)

    judul_lbl = CTkLabel(content, text=pengaduan_detail['judul'], text_color="black", font=("PlusJakartaSans", 18, "bold"))
    judul_lbl.place(x=68 - 41.25, y=267 - 250.5)

    tgl_lbl = CTkLabel(content, text=f"Tanggal dibuat : {pengaduan_detail['tgl_pengaduan']}", text_color="#616161", font=("PlusJakartaSans", 15))
    tgl_lbl.place(x=820 - 41.25, y=270.75 - 250.5)

    isiPengaduan_txtb = CTkTextbox(content, text_color="black", fg_color="#FDFDFF", border_color="#b5b5b5", border_width=0, font=("", 15), width=940.5, height=95)
    isiPengaduan_txtb.insert("0.0", pengaduan_detail['isi_pengaduan'])
    isiPengaduan_txtb.configure(state=DISABLED)
    isiPengaduan_txtb.place(x=67 - 41.25, y=312.75 - 250.5)

    # Attachment
    attachment = pengaduan_detail['attachment']
    attachment_path = f"storage/img/{user_id}/{attachment}"
    if attachment:
        attachment_path = f"storage/img/{user_id}/{pengaduan_detail['attachment']}"
        desired_height = 240
        resized_image = display_image_with_fixed_height(attachment_path, desired_height)
        
        attachment_lbl = CTkLabel(content, text="Lampiran :", text_color="black", font=("PlusJakartaSans", 15))
        attachment_lbl.place(x=67 - 41.25, y=417.75 - 250.5)

        attachment_img = CTkImage(dark_image=resized_image, size=(resized_image.width, desired_height))
        attachment_lab = CTkLabel(content, image=attachment_img, text="")
        attachment_lab.place(x=66.75 - 41.25, y=443.25 - 250.5)

main.mainloop()
