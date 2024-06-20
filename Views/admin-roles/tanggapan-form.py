from customtkinter import *
import tkinter as tk
from tkinter import filedialog, Menu, Canvas, messagebox
from PIL import Image
import os
import sys
from datetime import datetime
sys.path.insert(1, 'C://Dev//UPJ//pemvis//uas')
import adminbcknd
import shutil

def logout():
    confirmation = messagebox.askyesno("Logout", "Apakah Anda yakin ingin logout?")
    if confirmation:
        main.destroy()
        os.system("python views/auth/login.py")

if len(sys.argv) > 2:
    user_id = sys.argv[1]
    id_pengaduan = sys.argv[2]
    back_fileName = sys.argv[3]
    user_name = adminbcknd.get_user_name(user_id)
    pengaduan_detail = adminbcknd.get_pengaduan_detail(id_pengaduan)
else:
    user_id = None
    id_pengaduan = None
    user_name = "User"
    pengaduan_detail = None

def back_button():
    main.destroy()
    os.system(f"python views/admin-roles/detail-pengaduan.py {user_id} {id_pengaduan} {back_fileName}")

def open_profile():
    main.destroy()  # Close the current window
    os.system(f"python Views/admin-roles/user-profile.py {user_id}")
    
def open_dashboard():
    main.destroy()  # Close the current window
    os.system(f"python Views/admin-roles/dashboard-admin.py {user_id}")
    
def open_verifikasiPengaduan():
    main.destroy()  # Close the current window
    os.system(f"python Views/admin-roles/verifikasi-pengaduan.py {user_id}")

def open_prosesPengaduan():
    main.destroy()  # Close the current window
    os.system(f"python Views/admin-roles/proses-pengaduan.py {user_id}")

def open_tanggapanPengaduan():
    main.destroy()  # Close the current window
    os.system(f"python Views/admin-roles/tanggapan-pengaduan.py {user_id}")
    
def open_manageUser():
    main.destroy()  # Close the current window
    os.system(f"python Views/admin-roles/manage-user.py {user_id}")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        filename = os.path.basename(file_path)
        strfilename.set(filename)
        global uploaded_file_path
        uploaded_file_path = file_path

def entry_clicked(event):
    browse_file()

def submit_tanggapan():
    description = responseDesc_txtb.get("1.0", tk.END).strip()
    date_reported = datetime.now().strftime('%Y-%m-%d')
    last_updated = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    attachment = strfilename.get()

    new_filename = None
    if 'uploaded_file_path' in globals() and uploaded_file_path:
        file_extension = attachment
        new_filename = f"{last_updated.replace(':', '-')}{file_extension}"
        storage_path = f"storage/img/tanggapan/{user_id}"
        if not os.path.exists(storage_path):
            os.makedirs(storage_path)
        destination_path = os.path.join(storage_path, new_filename)
        shutil.copy(uploaded_file_path, destination_path)

    adminbcknd.submit_tanggapan(id_pengaduan, user_id, date_reported, description, new_filename, last_updated)
    adminbcknd.update_status_selesai(id_pengaduan)
    messagebox.showinfo("Tanggapan Berhasil", "Pengaduan Berhasil Ditanggapi")
    main.destroy()
    os.system(f"python views/admin-roles/proses-pengaduan.py {user_id}")

main = CTk()
main.title("List Pengaduan")
main.config(bg="#F4F6F9")

main_width = 1080
main_height = 768

screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

x = (screen_width // 2) - (main_width // 2)
y = (screen_height // 2) - (main_height // 2)

main.geometry(f"{main_width}x{main_height}+{x}+{y}")
main.resizable(False, False)

navbar = CTkFrame(main, fg_color="#6777EF", bg_color="white", width=854.25, height=129.75, corner_radius=0)
navbar.place(x=225.75, y=0)

profile_img = CTkImage(dark_image=Image.open("Assets/frame0/image_1.png"), size=(45, 45))
profile_lab = CTkLabel(navbar, image=profile_img, text="")
profile_lab.place(x=830 - 225.75, y=23.25)

username_lbl = CTkLabel(navbar, text=f"Hi, {user_name}", text_color="white", font=("PlusJakartaSans", 18))
username_lbl.place(x=883 - 225.75, y=33)

menu = Menu(main, tearoff=0)
menu.add_command(label="Profile", command=open_profile)
menu.add_command(label="Logout", command=logout)

def show_menu(event):
    menu.post(event.x_root, event.y_root)

dropdown_trigger = CTkLabel(navbar, text="▼", text_color="white", font=("PlusJakartaSans", 18), cursor="hand2")
dropdown_trigger.place(x=1020 - 225.75, y=33)
dropdown_trigger.bind("<Button-1>", show_menu)

sidebar = CTkFrame(main, fg_color="#FFFFFF", bg_color="white", width=225.75, height=769.5)
sidebar.place(x=0, y=0)

appName_lbl = CTkLabel(sidebar, text="SuaraKu", text_color="black", font=("PlusJakartaSans", 28, "bold"))
appName_lbl.place(x=55, y=25.5)

submenu_lbl1 = CTkLabel(sidebar, text="MAIN", text_color="#8B8B8B", font=("PlusJakartaSans", 12))
submenu_lbl1.place(x=10.5, y=82.5)

dashboard_img = CTkImage(dark_image=Image.open("Assets/icon/dashboard1.png"), size=(18,18))
dashboard_lab = CTkLabel(sidebar, image=dashboard_img, text="", cursor="hand2")
dashboard_lab.place(x=32, y=118)
dashboard_lab.bind("<Button-1>", lambda e: open_dashboard())

dashboard_lbl = CTkLabel(sidebar, text="Dashboard", text_color="black", font=("PlusJakartaSans", 12), cursor="hand2")
dashboard_lbl.place(x=64, y=118)
dashboard_lbl.bind("<Button-1>", lambda e: open_dashboard())

submenu_lbl2 = CTkLabel(sidebar, text="PENGADUAN", text_color="#8B8B8B", font=("PlusJakartaSans", 12))
submenu_lbl2.place(x=10.5, y=168.75)

selectedmenu = CTkFrame(sidebar, fg_color="#D2E2FF", bg_color="white", width=225.75, height=52.5, corner_radius=0)
selectedmenu.place(x=0, y=192)

verifikasi_img = CTkImage(dark_image=Image.open("Assets/icon/check2.png"), size=(20, 20))
verifikasi_lab = CTkLabel(selectedmenu, image=verifikasi_img, text="", cursor="hand2")
verifikasi_lab.place(x=32, y=205 - 192)
verifikasi_lab.bind("<Button-1>", lambda e: open_verifikasiPengaduan())

verifikasi_lbl = CTkLabel(selectedmenu, text="Verifikasi Pengaduan", text_color="#6777EF", font=("PlusJakartaSans", 12), cursor="hand2")
verifikasi_lbl.place(x=64, y=205 - 192)
verifikasi_lbl.bind("<Button-1>", lambda e: open_verifikasiPengaduan())

process_img = CTkImage(dark_image=Image.open("Assets/icon/process1.png"), size=(24, 24))
process_lab = CTkLabel(sidebar, image=process_img, text="", cursor="hand2")
process_lab.place(x=32, y=261.75)
process_lab.bind("<Button-1>", lambda e: open_prosesPengaduan())

process_lbl = CTkLabel(sidebar, text="Proses Pengaduan", text_color="black", font=("PlusJakartaSans", 12), cursor="hand2")
process_lbl.place(x=64, y=261.75)
process_lbl.bind("<Button-1>", lambda e: open_prosesPengaduan())

response_img = CTkImage(dark_image=Image.open("Assets/icon/response1.png"), size=(24, 24))
response_lab = CTkLabel(sidebar, image=response_img, text="", cursor="hand2")
response_lab.place(x=32, y=311.75)
response_lab.bind("<Button-1>", lambda e: open_tanggapanPengaduan())

response_lbl = CTkLabel(sidebar, text="Tanggapan", text_color="black", font=("PlusJakartaSans", 12), cursor="hand2")
response_lbl.place(x=64, y=311.75)
response_lbl.bind("<Button-1>", lambda e: open_tanggapanPengaduan())

submenu_lbl3 = CTkLabel(sidebar, text="USER", text_color="#8B8B8B", font=("PlusJakartaSans", 12))
submenu_lbl3.place(x=10.5, y=353.75)

usermenu_img = CTkImage(dark_image=Image.open("Assets/icon/user1.png"), size=(18, 18))
usermenu_lab = CTkLabel(sidebar, image=usermenu_img, text="", cursor="hand2")
usermenu_lab.place(x=32, y=390.25)
usermenu_lab.bind("<Button-1>", lambda e: open_profile())

usermenu_lbl = CTkLabel(sidebar, text="Manage User", text_color="black", font=("PlusJakartaSans", 12), cursor="hand2")
usermenu_lbl.place(x=64, y=390.25)
usermenu_lbl.bind("<Button-1>", lambda e: open_profile())

submenu_lbl4 = CTkLabel(sidebar, text="LAPORAN", text_color="#8B8B8B", font=("PlusJakartaSans", 12))
submenu_lbl4.place(x=10.5, y=438)

generateLaporan_img = CTkImage(dark_image=Image.open("Assets/icon/file1.png"), size=(18, 18))
generateLaporan_lab = CTkLabel(sidebar, image=generateLaporan_img, text="", cursor="hand2")
generateLaporan_lab.place(x=32, y=479.75)

generateLaporan_lbl = CTkLabel(sidebar, text="Generate Laporan", text_color="black", font=("PlusJakartaSans", 12), cursor="hand2")
generateLaporan_lbl.place(x=64, y=479.75)

logout_btn = CTkButton(sidebar, text="Logout", width=202.5, height=44, fg_color="#FF372D", hover_color="#FC544B", font=("PlusJakartaSans", 15), cursor="hand2", command=logout)
logout_btn.place(x=9.75, y=709.5)

# Content Title
content_title = CTkFrame(main, fg_color="#FFFFFF", bg_color="white", width=787.5, height=90)
content_title.place(x=259, y=90.75)

contentTitle_lbl = CTkLabel(content_title, text="Tulis Tanggapan Pengaduan", text_color="black", font=("PlusJakartaSans", 24, "bold"), cursor="hand2")
contentTitle_lbl.place(x=80 - 41.25, y=153 - 121.5)

backButton_img = CTkImage(dark_image=Image.open("Assets/arrow.png"), size=(20, 20))
backButton_lab = CTkLabel(content_title, image=backButton_img, text="", cursor="hand2")
backButton_lab.place(x=56 - 41.25, y=153 - 121.5)
backButton_lab.bind("<Button-1>", lambda e: back_button())

# Content
content = CTkFrame(main, fg_color="#FFFFFF", bg_color="white", width=787.5, height=540)
content.place(x=259, y=203)

title_lbl = CTkLabel(content, text="ID Petugas/Admin", text_color="black", font=("PlusJakartaSans", 15))
title_lbl.place(x=284.25 - 259, y=230.25 - 203)

title_entry = CTkEntry(content, text_color="black", fg_color="#FDFDFF", border_color="#b5b5b5", border_width=1, font=("", 15), width=742.5, height=35)
title_entry.place(x=284.25 - 259, y=256.5 - 203)

responseDesc_lbl = CTkLabel(content, text="Isi Tanggapan", text_color="black", font=("PlusJakartaSans", 15))
responseDesc_lbl.place(x=283.5 - 259, y=300.75 - 203)

responseDesc_txtb = CTkTextbox(content, text_color="black", fg_color="#FDFDFF", border_color="#b5b5b5", border_width=1, font=("", 15), width=742.5, height=180)
responseDesc_txtb.place(x=284.25 - 259, y=334 - 203)

responseProv_lbl = CTkLabel(content, text="Bukti Tanggapan", text_color="black", font=("PlusJakartaSans", 13))
responseProv_lbl.place(x=284.25 - 259, y=537.75 - 203)

strfilename = tk.StringVar()
responseProv_entry = CTkEntry(content, text_color="black", fg_color="#FDFDFF", border_color="#b5b5b5", border_width=1, font=("", 15), width=670, height=35, textvariable=strfilename, state=DISABLED)
responseProv_entry.place(x=284 - 259, y=564 - 203)
responseProv_entry.bind("<Button-1>", entry_clicked)

responseProv_btn = CTkButton(content, text="Browse", width=93, height=35, fg_color="#888888", hover_color="#AEAEAE", font=("PlusJakartaSans", 15), cursor="hand2", command=browse_file)
responseProv_btn.place(x=933.75 - 259, y=564 - 203)

addTanggapan_btn = CTkButton(content, text="Kirim Tanggapan", width=156.75, height=42, fg_color="#6777EF", hover_color="#424D98", font=("PlusJakartaSans", 15), cursor="hand2", command=submit_tanggapan)
addTanggapan_btn.place(x=863.25 - 259, y=659.25 - 203)

if pengaduan_detail:
    title_entry.insert(0, pengaduan_detail['id_user'])
    title_entry.configure(state=DISABLED)

main.mainloop()
