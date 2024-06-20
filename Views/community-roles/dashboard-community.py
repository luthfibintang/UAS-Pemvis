import sys
from customtkinter import *
from tkinter import Canvas, Menu, messagebox
from spinBox import FloatSpinbox
from CTkTable import *
import os
from PIL import Image
sys.path.insert(1, 'C://Dev//UPJ//pemvis//uas')
import pengadubcknd

def logout():
    confirmation = messagebox.askyesno("Logout", "Apakah Anda yakin ingin logout?")
    if confirmation:
        main.destroy()
        os.system("python views/auth/login.py")

if len(sys.argv) > 1:
    user_id = sys.argv[1]
    user_name = pengadubcknd.get_user_name(user_id)
else:
    user_id = None
    user_name = "User"
    
def open_profile():
    main.destroy()  # Close the current window
    os.system(f"python Views/community-roles/user-profile.py {user_id}")

def open_pengaduan():
    main.destroy()  # Close the current window
    os.system(f"python Views/community-roles/list-pengaduan.py {user_id}")

def open_dashboard():
    main.destroy()  # Close the current window
    os.system(f"python Views/community-roles/dashboard-community.py {user_id}")

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

navbar = CTkFrame(main, fg_color="#6777EF", bg_color="white", width=main_width, height=88.5, corner_radius=0)
navbar.place(x=0, y=0)

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
canvas.place(x=287, y=82)

user_lbl = CTkLabel(navbar, text="User", text_color="white", font=("PlusJakartaSans", 18), cursor="hand2")
user_lbl.place(x=645, y=34)
user_lbl.bind("<Button-1>", lambda e: open_profile())

profile_img = CTkImage(dark_image=Image.open("Assets/frame0/image_1.png"), size=(45, 45))
profile_lab = CTkLabel(navbar, image=profile_img, text="")
profile_lab.place(x=830, y=23.25)

username_lbl = CTkLabel(navbar, text=f"Hi, {user_name}", text_color="white", font=("PlusJakartaSans", 18))
username_lbl.place(x=883, y=33)

menu = Menu(main, tearoff=0)
menu.add_command(label="Profile", command=open_profile)
menu.add_command(label="Logout", command=logout)

def show_menu(event):
    menu.post(event.x_root, event.y_root)

dropdown_trigger = CTkLabel(navbar, text="▼", text_color="white", font=("PlusJakartaSans", 18), cursor="hand2")
dropdown_trigger.place(x=1020, y=33)
dropdown_trigger.bind("<Button-1>", show_menu)

content_title = CTkFrame(main, fg_color="#FFFFFF", bg_color="white", width=990.75, height=96.75)
content_title.place(x=41.25, y=121.5)

contentTitle_lbl = CTkLabel(content_title, text="Dashboard", text_color="black", font=("PlusJakartaSans", 24, "bold"), cursor="hand2")
contentTitle_lbl.place(x=56 - 41.25, y=153 - 121.5)

content = CTkFrame(main, fg_color="#FFFFFF", bg_color="white", width=990.75, height=484.5)
content.place(x=41.25, y=250.5)

backButton_img = CTkImage(dark_image=Image.open("Assets/icon/dshbrd.png"), size=(976.21, 111.46))
backButton_lab = CTkLabel(content, image=backButton_img, text="", cursor="hand2")
backButton_lab.place(x=50.25 - 41.25, y=254.25 - 250.5)

# show_lbl = CTkLabel(content, text="IDK about this one", text_color="black", font=("PlusJakartaSans", 15))
# show_lbl.place(x=81.5 - 41.25, y=288 - 250.5)

main.mainloop()
