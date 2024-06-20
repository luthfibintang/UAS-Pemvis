import sys
from customtkinter import *
from tkinter import Canvas, Menu, messagebox
from CTkTable import *
import os
from PIL import Image
sys.path.insert(1, 'C://Dev//UPJ//pemvis//uas')
import adminbcknd

def logout():
    confirmation = messagebox.askyesno("Logout", "Apakah Anda yakin ingin logout?")
    if confirmation:
        main.destroy()
        os.system("python views/auth/login.py")

if len(sys.argv) > 1:
    user_id = sys.argv[1]
    user_name = adminbcknd.get_user_name(user_id)
else:
    user_id = None
    user_name = "User"

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

selectedmenu = CTkFrame(sidebar, fg_color="#D2E2FF", bg_color="white", width=225.75, height=52.5, corner_radius=0)
selectedmenu.place(x=0, y=108)

dashboard_img = CTkImage(dark_image=Image.open("Assets/icon/dashboard2.png"), size=(18,18))
dashboard_lab = CTkLabel(selectedmenu, image=dashboard_img, text="", cursor="hand2")
dashboard_lab.place(x=32, y=118 - 106.5)
dashboard_lab.bind("<Button-1>", lambda e: open_dashboard())

dashboard_lbl = CTkLabel(selectedmenu, text="Dashboard", text_color="#6777EF", font=("PlusJakartaSans", 12), cursor="hand2")
dashboard_lbl.place(x=64, y=118 - 106.5)
dashboard_lbl.bind("<Button-1>", lambda e: open_dashboard())

submenu_lbl2 = CTkLabel(sidebar, text="PENGADUAN", text_color="#8B8B8B", font=("PlusJakartaSans", 12))
submenu_lbl2.place(x=10.5, y=168.75)

verifikasi_img = CTkImage(dark_image=Image.open("Assets/icon/check1.png"), size=(20, 20))
verifikasi_lab = CTkLabel(sidebar, image=verifikasi_img, text="", cursor="hand2")
verifikasi_lab.place(x=32, y=209.25)
verifikasi_lab.bind("<Button-1>", lambda e: open_verifikasiPengaduan())

verifikasi_lbl = CTkLabel(sidebar, text="Verifikasi Pengaduan", text_color="black", font=("PlusJakartaSans", 12), cursor="hand2")
verifikasi_lbl.place(x=64, y=209.25)
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

contentTitle_lbl = CTkLabel(content_title, text="Dashboard", text_color="black", font=("PlusJakartaSans", 24, "bold"), cursor="hand2")
contentTitle_lbl.place(x=56 - 41.25, y=153 - 121.5)

content = CTkFrame(main, fg_color="#FFFFFF", bg_color="white", width=787.5, height=540)
content.place(x=259, y=203)

show_lbl = CTkLabel(content, text="IDK about this one", text_color="black", font=("PlusJakartaSans", 15))
show_lbl.place(x=273 - 259, y=230 - 203)

main.mainloop()
