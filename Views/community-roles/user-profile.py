from customtkinter import *
from tkinter import Canvas, Menu
from spinBox import FloatSpinbox
from CTkTable import *
import os
from PIL import Image

# Function to open detail
def browse():
    print("browse button clicked!")

# Function to handle logout
def logout():
    main.destroy()
    os.system("python views/auth/login.py")

# Function to handle profile
def profile():
    print("Profile clicked!")
    
def change_profile():
    print("Change Profile clicked")

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
canvas.create_rectangle(547, 2, 607, 2, width=3)
canvas.place(x=589, y=82)

user_lbl = CTkLabel(navbar, text="User", text_color="white", font=("PlusJakartaSans", 18))
user_lbl.place(x=645, y=34)

profile_img = CTkImage(dark_image=Image.open("Assets/frame0/image_1.png"), size=(45, 45))
profile_lab = CTkLabel(navbar, image=profile_img, text="")
profile_lab.place(x=834, y=23.25)

username_lbl = CTkLabel(navbar, text="Hi, Masyarakat", text_color="white", font=("PlusJakartaSans", 18))
username_lbl.place(x=887, y=33)

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

contentTitle_lbl = CTkLabel(content_title, text="User Profile", text_color="black", font=("PlusJakartaSans", 24, "bold"), cursor="hand2")
contentTitle_lbl.place(x=56 - 41.25, y=153 - 121.5)

# Content frame

profileInformation = CTkFrame(main, fg_color="#FFFFFF", bg_color="white", width=347, height=177)
profileInformation.place(x=41, y=238)

bg_img = CTkImage(dark_image=Image.open("Assets/frame0/image_1.png"), size=(90, 90))
bg_lab = CTkLabel(profileInformation, image=bg_img, text="")
bg_lab.place(x=51-41, y=250 - 238)

name_lbl = CTkLabel(profileInformation, text="Marcus Miles", text_color="black", font=("PlusJakartaSans", 15))
name_lbl.place(x=156 - 41, y=265 - 238)

email_lbl = CTkLabel(profileInformation, text="marcusmiles911@example.com", text_color="black", font=("PlusJakartaSans", 13))
email_lbl.place(x=156 - 41, y=288 - 238)

phoneNumber_lbl = CTkLabel(profileInformation, text="08134567890", text_color="black", font=("PlusJakartaSans", 13))
phoneNumber_lbl.place(x=156 - 41, y=313 - 238)

bio_lbl = CTkLabel(profileInformation, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque eu diam mauris. Duis ante leo, tristique nec nunc at, ornare.",
                   text_color="black", font=("PlusJakartaSans", 13), wraplength=315, justify="left")
bio_lbl.place(x=61 - 41, y=351 - 238)

formEditProfile = CTkFrame(main, fg_color="#FFFFFF", bg_color="white", width=628, height=511)
formEditProfile.place(x=404, y=238)

card_lbl = CTkLabel(formEditProfile, text="Edit Profile", text_color="#6777EF", font=("PlusJakartaSans", 18))
card_lbl.place(x=422.25 - 404, y=258.75 - 238)

profile_lbl = CTkLabel(formEditProfile, text="Foto Profile", text_color="black", font=("PlusJakartaSans", 13))
profile_lbl.place(x=426 - 404, y=305.5 - 238)

profile_entry = CTkEntry(formEditProfile, text_color="black", fg_color="#FDFDFF", border_color="#b5b5b5", border_width=1, font=("", 13), width=453, height=39, state=DISABLED)
profile_entry.place(x=22, y=94)

placeholder_lbl = CTkLabel(formEditProfile, text="Choose to change profile", text_color="#B0B0B0", font=("", 13))
placeholder_lbl.place(x=28, y=98)

browse_btn = CTkButton(formEditProfile, text="Browse", width=132, height=39, fg_color="#888888", hover_color="#AEAEAE", command=browse, font=("PlusJakartaSans", 15))
browse_btn.place(x=873 - 404, y=332 - 238)

name_lbl = CTkLabel(formEditProfile, text="Nama Lengkap", text_color="black", font=("PlusJakartaSans", 13))
name_lbl.place(x=427 - 404, y=391 - 238)

name_entry = CTkEntry(formEditProfile, placeholder_text="Marcus Miles", text_color="black", fg_color="#FDFDFF", border_color="#b5b5b5", border_width=1, font=("", 13), width=267.75, height=39)
name_entry.place(x=426 - 404, y=414.75 - 238)

username_lbl = CTkLabel(formEditProfile, text="Username", text_color="black", font=("PlusJakartaSans", 13))
username_lbl.place(x=715.5 - 404, y=391 - 238)

username_entry = CTkEntry(formEditProfile, placeholder_text="marcusmiles911", text_color="black", fg_color="#FDFDFF", border_color="#b5b5b5", border_width=1, font=("", 13), width=285.75, height=39)
username_entry.place(x=712.5 - 404, y=414.75 - 238)

email_lbl = CTkLabel(formEditProfile, text="Email", text_color="black", font=("PlusJakartaSans", 13))
email_lbl.place(x=427 - 404, y=475 - 238)

email_entry = CTkEntry(formEditProfile, placeholder_text="marcusmiles911@example.com", text_color="black", fg_color="#FDFDFF", border_color="#b5b5b5", border_width=1, font=("", 13), width=330, height=39)
email_entry.place(x=426 - 404, y=498 - 238)

Phone_lbl = CTkLabel(formEditProfile, text="Nomor Telepon", text_color="black", font=("PlusJakartaSans", 13))
Phone_lbl.place(x=773.25 - 404, y=475 - 238)

Phone_entry = CTkEntry(formEditProfile, placeholder_text="081234567890", text_color="black", fg_color="#FDFDFF", border_color="#b5b5b5", border_width=1, font=("", 13), width=225, height=39)
Phone_entry.place(x=773.25 - 404, y=498 - 238)

bio_lbl = CTkLabel(formEditProfile, text="Bio", text_color="black", font=("PlusJakartaSans", 13))
bio_lbl.place(x=427.5 - 404, y=559.75 - 238)

# bio_entry = CTkTextbox(formEditProfile, text_color="black", fg_color="#FDFDFF", border_color="#b5b5b5", border_width=1, font=("", 13), width=572.25, height=85.5,
#                        placeholder_text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque eu diam mauris. Duis ante leo, tristique nec nunc at, ornare.")
# bio_entry.place(x=427.5 - 404, y=583.5 - 238)

placeholder_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque eu diam mauris. Duis ante leo, tristique nec nunc at, ornare."

def add_placeholder(event=None):
    if bio_textBox.get("1.0", "end-1c") == "":
        bio_textBox.insert("1.0", placeholder_text)
        bio_textBox.configure(text_color="grey")

    # Function to remove placeholder
def remove_placeholder(event):
    if bio_textBox.get("1.0", "end-1c") == placeholder_text:
        bio_textBox.delete("1.0", "end")
        bio_textBox.configure(text_color="black")

# Profile entry (now as a textbox)
bio_textBox = CTkTextbox(formEditProfile, text_color="grey", fg_color="#FDFDFF", border_color="#b5b5b5", border_width=1, font=("", 13), width=572.25, height=85.5)
bio_textBox.place(x=427.5 - 404, y=583.5 - 238)
# Insert placeholder text initially
bio_textBox.insert("1.0", placeholder_text)

# Bind events to remove/add placeholder
bio_textBox.bind("<FocusIn>", remove_placeholder)
bio_textBox.bind("<FocusOut>", add_placeholder)

changeProfile_btn = CTkButton(formEditProfile, text="Ubah Profile", width=134, height=41, fg_color="#6777EF", hover_color="#424D98", command=change_profile, font=("PlusJakartaSans", 13))
changeProfile_btn.place(x=866 - 404, y=689 - 238)
    
main.mainloop() 