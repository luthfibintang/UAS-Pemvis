# Library
from customtkinter import *

main = CTk()
main.title("Ubah Password Page")
main.config(bg="#F4F6F9")
main_width = 841
main_height = 600

# Get the screen width and height (Monitor)
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x = (screen_width // 2) - (main_width // 2)
y = (screen_height // 2) - (main_height // 2)

# Set the geometry of the window to center it
main.geometry(f"{main_width}x{main_height}+{x}+{y}")
main.resizable(False, False)

# Frame
frame1 = CTkFrame(main, fg_color="#FFFFFF", bg_color="white")

# Page title
title = CTkLabel(frame1, text="Ubah Password", text_color="black", font=("", 24, "bold"))
title.grid(row=0, column=0, sticky="w", pady=(28.47, 7), padx=30)
subTitle_lbl = CTkLabel(frame1, text="Masukan code yang anda terima dari email dan ubah password Anda.", text_color="black", font=("", 15))
subTitle_lbl.grid(row=1, column=0, sticky="we", pady=(0, 10), padx=30)

# Code Entry
code_lbl = CTkLabel(frame1, text="Code", text_color="black", font=("", 12))
code_lbl.grid(row=2, column=0, sticky="w", padx=30)
code_entry = CTkEntry(frame1, text_color="black", fg_color="#F6F6F6", border_color="#B5B5B5",
                     font=("", 12), width=405, corner_radius=5, height=28)
code_entry.grid(row=3, column=0, sticky="nwe", padx=30, pady=(0, 5))

# Email Entry
email_lbl = CTkLabel(frame1, text="Email", text_color="black", font=("", 12))
email_lbl.grid(row=4, column=0, sticky="w", padx=30)
email_entry = CTkEntry(frame1, text_color="black", fg_color="#F6F6F6", border_color="#B5B5B5",
                     font=("", 12), width=405, corner_radius=5, height=28)
email_entry.grid(row=5, column=0, sticky="nwe", padx=30, pady=(0, 5))

# New Password Entry
newpassword_lbl = CTkLabel(frame1, text="Password Baru", text_color="black", font=("", 12))
newpassword_lbl.grid(row=6, column=0, sticky="w", padx=30)
newpassword_entry = CTkEntry(frame1, text_color="black", fg_color="#F6F6F6", border_color="#B5B5B5",
                     font=("", 12), width=405, corner_radius=5, height=28)
newpassword_entry.grid(row=7, column=0, sticky="nwe", padx=30, pady=(0, 5))

# Confirm New Password Entry
repeatPassword_lbl = CTkLabel(frame1, text="Ulangi Password Baru", text_color="black", font=("", 12))
repeatPassword_lbl.grid(row=8, column=0, sticky="w", padx=30)

repeatPassword_entry = CTkEntry(frame1, text_color="black", fg_color="#F6F6F6", border_color="#B5B5B5",
                     font=("", 12), width=405, corner_radius=5, height=28)
repeatPassword_entry.grid(row=9, column=0, sticky="nwe", padx=30, pady=(0, 18))

l_btn = CTkButton(frame1, text="Kirim Code", text_color="white", font=("", 12), height=28, width=72, fg_color="#5692EC", cursor="hand2",
                  corner_radius=5)
l_btn.grid(row=10, column=0, sticky="nwe", pady=(5, 10), padx=30)

register1_lbl = CTkLabel(frame1,text="Kembali",text_color="#4388F0",cursor="hand2",font=("",12))
register1_lbl.grid(row=11,column=0, sticky="we", pady=(0, 28.47))

frame1.pack(expand=True, anchor="center")

main.mainloop()