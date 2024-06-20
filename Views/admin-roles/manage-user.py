from customtkinter import *
from tkinter import Canvas, Menu, messagebox
from spinBox import FloatSpinbox
from CTkTable import *
import os
from PIL import Image
import sys
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
    current_filename = os.path.basename(__file__)
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

def open_detail(user_id, id_pengaduan):
    main.destroy()
    os.system(f"python views/admin-roles/detail-pengaduan.py {user_id} {id_pengaduan} {current_filename}")

def proses_pengaduan(id_pengaduan):
    confirmation = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin Memroses pengaduan ini?")
    if confirmation:
        result = adminbcknd.proses_pengaduan(id_pengaduan)
        if result:
            messagebox.showinfo("Success", "Pengaduan berhasil diproses!")
            open_prosesPengaduan()  # Reload the page to reflect changes
        else:
            messagebox.showerror("Error", "Gagal memroses pengaduan.")

def tanggapi_pengaduan(id_pengaduan):
    main.destroy()
    os.system(f"python views/admin-roles/tanggapan-form.py {user_id} {id_pengaduan} {current_filename}")

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

# selectedmenu = CTkFrame(main, fg_color="#D2E2FF", bg_color="white", width=225.75, height=52.5, corner_radius=0)
# selectedmenu.place(x=0, y=108)

dashboard_img = CTkImage(dark_image=Image.open("Assets/icon/dashboard1.png"), size=(18,18))
dashboard_lab = CTkLabel(sidebar, image=dashboard_img, text="", cursor="hand2")
dashboard_lab.place(x=32, y=118)
dashboard_lab.bind("<Button-1>", lambda e: open_dashboard())

dashboard_lbl = CTkLabel(sidebar, text="Dashboard", text_color="black", font=("PlusJakartaSans", 12), cursor="hand2")
dashboard_lbl.place(x=64, y=118)
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

selectedmenu = CTkFrame(sidebar, fg_color="#D2E2FF", bg_color="white", width=225.75, height=52.5, corner_radius=0)
selectedmenu.place(x=0, y=247.5)

process_img = CTkImage(dark_image=Image.open("Assets/icon/process1.png"), size=(24, 24))
process_lab = CTkLabel(selectedmenu, image=process_img, text="", cursor="hand2")
process_lab.place(x=32, y=255 - 242.5)
process_lab.bind("<Button-1>", lambda e: open_prosesPengaduan())

process_lbl = CTkLabel(selectedmenu, text="Proses Pengaduan", text_color="black", font=("PlusJakartaSans", 12), cursor="hand2")
process_lbl.place(x=64, y=255 - 242.5)
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

logout_btn = CTkButton(sidebar, text="Logout", width=202.5, height=44, fg_color="#FC544B", hover_color="#CB4139", font=("PlusJakartaSans", 15), cursor="hand2", command=logout)
logout_btn.place(x=9.75, y=709.5)

# Content Title
content_title = CTkFrame(main, fg_color="#FFFFFF", bg_color="white", width=787.5, height=90)
content_title.place(x=253, y=90.75)

contentTitle_lbl = CTkLabel(content_title, text="Verifikasi Pengaduan", text_color="black", font=("PlusJakartaSans", 24, "bold"), cursor="hand2")
contentTitle_lbl.place(x=285 - 259, y=120 - 90.75)

# Content
content = CTkFrame(main, fg_color="#FFFFFF", bg_color="white", width=787.5, height=540)
content.place(x=253, y=198.75)

show_lbl = CTkLabel(content, text="Show", text_color="black", font=("PlusJakartaSans", 13))
show_lbl.place(x=308 - 259, y=220 - 203)

spinbox = FloatSpinbox(content, width=100, step_size=10)
spinbox.set(10)
spinbox.place(x=345 - 259, y=220 - 203)

entries_lbl = CTkLabel(content, text="Entries", text_color="black", font=("PlusJakartaSans", 13))
entries_lbl.place(x=450 - 259, y=220 - 203)

search_entry = CTkEntry(content, text_color="black", fg_color="#F6F6F6", border_color="#B5B5B5", placeholder_text="Search", font=("", 13), width=210.75, height=30.25, border_width=1)
search_entry.place(x=764.25 - 259, y=220 - 203)

search_img = CTkImage(dark_image=Image.open("Assets/frame0/button_1.png"), size=(30.25, 30.25))
search_lab = CTkLabel(content, image=search_img, text="", cursor="hand2")
search_lab.place(x=954 - 259, y=220 - 203)

# Table frame
# Scrollable frame for the table
table_frame = CTkScrollableFrame(content, fg_color="#F4F6F9", width=718.5, height=350, corner_radius=10)
table_frame.place(x=30, y=80)

# Columns for the table
columns = ["No", "NIK", "Judul Pengaduan", "Tanggal Pengaduan", "Action"]

# Fetch data from the database based on user_id
users_data = adminbcknd.get_all_user()

for i, col in enumerate(columns):
    label = CTkLabel(table_frame, text=col, text_color="black", font=("PlusJakartaSans", 13, "bold"), width=181.5, height=50, fg_color="#D3D3D3")
    label.grid(row=0, column=i, sticky="nsw")

# Populate the table with data
for row_idx, row_data in enumerate(users_data, start=1):
    label = CTkLabel(table_frame, text=str(row_idx), text_color="black", font=("PlusJakartaSans", 13), width=181.5, height=50)
    label.grid(row=row_idx, column=0, sticky="nsw")
    
    for col_idx, item in enumerate([users_data['id'], users_data['nik'], users_data['nama'], users_data['email'], users_data['telp']], start=1):
        label = CTkLabel(table_frame, text=item, text_color="black", font=("PlusJakartaSans", 13), width=181.5, height=50)
        label.grid(row=row_idx, column=col_idx, sticky="nsw")

    # Add button in the "Action" column
    button_frame = CTkFrame(table_frame, fg_color="#F4F6F9", width=120)
    button_frame.grid(row=row_idx, column=len(columns)-1, padx=(10, 10), sticky="nswe")

    # Tambahkan tombol Detail, Edit, dan Delete ke dalam button_frame
    edit_img = CTkImage(dark_image=Image.open("Assets/icon/edit.png"), size=(20, 20))
    edit_btn = CTkButton(button_frame, image=edit_img, text="", width=30, height=30, fg_color="#FFD700", hover_color="#FFC700")
    edit_btn.pack(side=LEFT, padx=2, pady=10)
        
    delete_img = CTkImage(dark_image=Image.open("Assets/icon/delete.png"), size=(20, 20))
    delete_btn = CTkButton(button_frame, image=delete_img, text="", width=30, height=30, fg_color="#FF6347", hover_color="#FF4500")
    delete_btn.pack(side=LEFT, padx=2, pady=10)

main.mainloop()
