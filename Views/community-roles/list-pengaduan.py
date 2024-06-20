from customtkinter import *
from tkinter import Canvas, Menu, messagebox
from spinBox import FloatSpinbox
from customtkinter import filedialog  
from CTkTable import *
import os
from PIL import Image
import sys
sys.path.insert(1, 'C://Dev//UPJ//pemvis//uas')
import pengadubcknd

# Function to open detail
def open_detail(user_id, id_pengaduan):
    main.destroy()
    os.system(f"python views/community-roles/detail-pengaduan.py {user_id} {id_pengaduan}")

def open_edit(user_id, id_pengaduan):
    main.destroy()
    os.system(f"python views/community-roles/edit-pengaduan.py {user_id} {id_pengaduan}")

# Function to handle logout
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

def open_buatPengaduan():
    main.destroy()
    os.system(f"python Views/community-roles/buat-pengaduan.py {user_id}")
      
def selectfile():
        filename = filedialog.askopenfilename()
        print(filename)

def delete_data(id_pengaduan, attachment):
    confirmation = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus pengaduan ini?")
    if confirmation:
        # Hapus pengaduan dari database
        pengadubcknd.delete_pengaduan_by_id(id_pengaduan)
        
        # Hapus attachment jika ada
        if attachment:
            attachment_path = f"storage/img/{user_id}/{attachment}"
            try:
                os.remove(attachment_path)
                messagebox.showinfo("Sukses", "Pengaduan beserta attachment berhasil dihapus.")
            except FileNotFoundError:
                messagebox.showwarning("Peringatan", f"Attachment tidak ditemukan: {attachment_path}")
        else:
            messagebox.showinfo("Sukses", "Pengaduan berhasil dihapus.")
        
        # Tutup jendela detail pengaduan setelah penghapusan
        main.destroy()
        os.system(f"python views/community-roles/list-pengaduan.py {user_id}")

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

contentTitle_lbl = CTkLabel(content_title, text="List Pengaduan", text_color="black", font=("PlusJakartaSans", 24, "bold"), cursor="hand2")
contentTitle_lbl.place(x=56 - 41.25, y=153 - 121.5)

addPengaduan_btn = CTkButton(content_title, text="Buat Pengaduan", width=100, height=30, fg_color="#6777EF", hover_color="#424D98", font=("PlusJakartaSans", 15))
addPengaduan_btn.place(x=857.75 - 41.25, y=156 - 121.5)
addPengaduan_btn.bind("<Button-1>", lambda e: open_buatPengaduan())

# Content frame
content = CTkFrame(main, fg_color="#FFFFFF", bg_color="white", width=990.75, height=484.5)
content.place(x=41.25, y=250.5)

show_lbl = CTkLabel(content, text="Show", text_color="black", font=("PlusJakartaSans", 13))
show_lbl.place(x=81.5 - 41.25, y=288 - 250.5)

# Spinbox
spinbox = FloatSpinbox(content, width=100, step_size=10)
spinbox.set(10)
spinbox.place(x=118.5 - 41.25, y=285 - 250.5)

entries_lbl = CTkLabel(content, text="Entries", text_color="black", font=("PlusJakartaSans", 13))
entries_lbl.place(x=223 - 41.25, y=288 - 250.5)

search_entry = CTkEntry(content, text_color="black", fg_color="#F6F6F6", border_color="#B5B5B5", placeholder_text="Search", font=("", 13), width=210.75, height=30.25)
search_entry.place(x=750 - 41.25, y=285 - 250.5)

search_img = CTkImage(dark_image=Image.open("Assets/frame0/button_1.png"), size=(30.25, 30.25))
search_lab = CTkLabel(content, image=search_img, text="", cursor="hand2")
search_lab.place(x=954 - 41.25, y=285 - 250.5)

# Table frame
# Scrollable frame for the table
table_frame = CTkScrollableFrame(content, fg_color="#F4F6F9", width=912, height=350, corner_radius=10)
table_frame.place(x=30, y=100)

# Columns for the table
columns = ["No", "Judul Pengaduan", "Tanggal Pengaduan", "Status", "Action"]

# Fetch data from the database based on user_id
pengaduan_data = pengadubcknd.get_pengaduan_by_user_id(user_id)

# Create header labels
for i, col in enumerate(columns):
    label = CTkLabel(table_frame, text=col, text_color="black", font=("PlusJakartaSans", 13, "bold"), width=181.5, height=50, fg_color="#D3D3D3")
    label.grid(row=0, column=i, sticky="nsw")

# Populate the table with data
for row_idx, row_data in enumerate(pengaduan_data, start=1):
    label = CTkLabel(table_frame, text=str(row_idx), text_color="black", font=("PlusJakartaSans", 13), width=181.5, height=50)
    label.grid(row=row_idx, column=0, sticky="nsw")
    
    for col_idx, item in enumerate([row_data['judul'], row_data['tgl_pengaduan'], row_data['status']], start=1):
        label = CTkLabel(table_frame, text=item, text_color="black", font=("PlusJakartaSans", 13), width=181.5, height=50)
        label.grid(row=row_idx, column=col_idx, sticky="nsw")

    # Add button in the "Action" column
    button_frame = CTkFrame(table_frame, fg_color="#F4F6F9", width=120)
    button_frame.grid(row=row_idx, column=len(columns)-1, padx=(10, 10), sticky="nswe")

    # Tambahkan tombol Detail, Edit, dan Delete ke dalam button_frame
    detail_img = CTkImage(dark_image=Image.open("Assets/icon/info.png"), size=(20, 20))
    detail_btn = CTkButton(button_frame, image=detail_img, text="", command=lambda user_id=user_id, id_pengaduan=row_data['id_pengaduan']: open_detail(user_id, id_pengaduan), width=30, height=30, fg_color="#6777EF", hover_color="#424D98")
    detail_btn.pack(side=LEFT, padx=(20, 2), pady=10)

    if row_data['status'] == "Belum Diverifikasi":
        edit_img = CTkImage(dark_image=Image.open("Assets/icon/edit.png"), size=(20, 20))
        edit_btn = CTkButton(button_frame, image=edit_img, text="", command=lambda user_id=user_id, id_pengaduan=row_data['id_pengaduan']: open_edit(user_id, id_pengaduan), width=30, height=30, fg_color="#FFD700", hover_color="#FFC700")
        edit_btn.pack(side=LEFT, padx=2, pady=10)
        
        delete_img = CTkImage(dark_image=Image.open("Assets/icon/delete.png"), size=(20, 20))
        delete_btn = CTkButton(button_frame, image=delete_img, text="", command=lambda id_pengaduan=row_data['id_pengaduan'], attachment=row_data['attachment']: delete_data(id_pengaduan, attachment), width=30, height=30, fg_color="#FF6347", hover_color="#FF4500")
        delete_btn.pack(side=LEFT, padx=2, pady=10)

main.mainloop()