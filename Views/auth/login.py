from customtkinter import *
from PIL import Image
sys.path.insert(1, 'C://Dev//UPJ//pemvis//uas')
import auth
import os
from tkinter import messagebox

def open_register():
    main.destroy()  # Close the current window
    os.system("python Views/auth/register.py")
    

def login():
    email = email_entry.get()
    password = passwd_entry.get()
    # print(email, password)
    user = auth.check_credentials(email, password)
    if user['id']:
        # If login is successful, open the dashboard and pass the user_id
        messagebox.showinfo("Login Successful", "Login berhasil!")
        if user['role'] == 'masyarakat':
            main.destroy()
            os.system(f"python views/community-roles/dashboard-community.py {user['id']}")
        else:
            main.destroy()
            os.system(f"python views/admin-roles/dashboard-admin.py {user['id']}")
    else:
        messagebox.showwarning("Login Failed", "Email atau Password Salah")
        print("Invalid credentials")

main = CTk()
main.title("Login Page")
main.config(bg="white")
main_width = 841
main_height = 600

screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

x = (screen_width // 2) - (main_width // 2)
y = (screen_height // 2) - (main_height // 2)

main.geometry(f"{main_width}x{main_height}+{x}+{y}")
main.resizable(False, False)

bg_img = CTkImage(dark_image=Image.open("Assets/img1.jpg"), size=(505.77, 600))

bg_lab = CTkLabel(main, image=bg_img, text="")
bg_lab.grid(row=0, column=1)

imgt_1 = CTkLabel(main, text="Selamat Pagi!", text_color="white", font=("", 24, "bold"), fg_color='transparent')
imgt_1.grid(row=0, column=1, pady=(48.47, 75), padx=43.22, sticky="sw")
imgt_2 = CTkLabel(main, text="Indonesia", text_color="white", font=("", 14))
imgt_2.grid(row=0, column=1, pady=(48.47, 50), padx=43.22, sticky="sw")

imgt_3 = CTkLabel(main, text="Image dari Unsplash oleh. Azhar J ", text_color="white", font=("", 12), fg_color='transparent')
imgt_3.grid(row=0, column=1, pady=(48.47, 5), padx=43.22, sticky="sw")

frame1 = CTkFrame(main, fg_color="white", bg_color="white", height=600, width=100)
frame1.grid(row=0, column=0, padx=40, sticky="nsew")

title = CTkLabel(frame1, text="Welcome!", text_color="black", font=("", 24, "bold"), )
title.grid(row=0, column=0, sticky="w", pady=(48.47, 5), padx=30)
subTitle_lbl = CTkLabel(frame1, text="Login untuk mulai mengadu.", text_color="black", font=("", 15), )
subTitle_lbl.grid(row=1, column=0, sticky="w", pady=(0, 40), padx=30)

email_lbl = CTkLabel(frame1, text="Email", text_color="black", cursor="hand2", font=("", 12))
email_lbl.grid(row=2, column=0, sticky="w", padx=30)

email_entry = CTkEntry(frame1, text_color="black", fg_color="#F6F6F6", border_color="#B5B5B5", border_width=1,
                       font=("", 12), width=229.52, corner_radius=5, height=28)
email_entry.grid(row=3, column=0, sticky="nwe", padx=30, pady=(0, 20))

password_lbl = CTkLabel(frame1, text="Password", text_color="black", cursor="hand2", font=("", 12))
password_lbl.grid(row=4, column=0, sticky="w", padx=30)

passwd_entry = CTkEntry(frame1, text_color="black", fg_color="#F6F6F6", border_color="#B5B5B5", border_width=1,
                        font=("", 12), width=229, corner_radius=5, height=28, show="*")
passwd_entry.grid(row=5, column=0, sticky="nwe", padx=30)

cr_acc = CTkLabel(frame1, text="Forgot Password!", text_color="#4388F0", cursor="hand2", font=("", 12))
cr_acc.grid(row=6, column=0, sticky="w", pady=20, padx=30)

l_btn = CTkButton(frame1, text="Login", text_color="white", font=("", 12), height=26, width=72, fg_color="#5692EC", cursor="hand2",
                  corner_radius=5, command=login)
l_btn.grid(row=6, column=0, sticky="ne", pady=20, padx=35)

register1_lbl = CTkLabel(frame1, text="Tidak punya akun?", text_color="black", font=("", 12))
register1_lbl.grid(row=7, column=0, pady=20, sticky="w", padx=(65, 0))
register1_lbl = CTkLabel(frame1, text=" Buat", text_color="#4388F0", cursor="hand2", font=("", 12))
register1_lbl.grid(row=7, column=0, sticky="ne", pady=20, padx=(0, 90))
register1_lbl.bind("<Button-1>", lambda e: open_register())

register1_lbl = CTkLabel(frame1, text="Copyright © Universitas Pembangunan Jaya. Made by\n Bintang, Widi, & Halvino", text_color="black", font=("", 11))
register1_lbl.grid(row=8, column=0, sticky="we", pady=(130, 0))

main.mainloop()