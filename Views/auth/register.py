# library
from customtkinter import *

# idk to descibe this, basically this is the think you need to do
main = CTk()
main.title("Registrasi Page")
main.config(bg="#F4F6F9")

#Main window that we use
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


frame1 = CTkFrame(main,fg_color="#FFFFFF", bg_color="white")

title = CTkLabel(frame1,text="Registerasi",text_color="black",font=("",24,"bold"), )
title.grid(row=0,column=0,sticky="w", pady=(28.47, 18), padx=30)

nik_lbl = CTkLabel(frame1,text="NIK",text_color="black",cursor="hand2",font=("",12))
nik_lbl.grid(row=1,column=0,sticky="w",padx=30)

nik_entry = CTkEntry(frame1,text_color="black", fg_color="#F6F6F6", border_color="#B5B5B5",
                         font=("",12), width=405, corner_radius=5, height=28)
nik_entry.grid(row=2,column=0,sticky="nwe",padx=30, pady=(0, 18))

name_lbl = CTkLabel(frame1,text="nama",text_color="black",cursor="hand2",font=("",12))
name_lbl.grid(row=3,column=0,sticky="w",padx=30)

name_entry = CTkEntry(frame1,text_color="black", fg_color="#F6F6F6", border_color="#B5B5B5",
                         font=("",12), width=229.52, corner_radius=5, height=28)
name_entry.grid(row=4,column=0,sticky="nwe",padx=30, pady=(0, 18))

email_lbl = CTkLabel(frame1,text="Email",text_color="black",cursor="hand2",font=("",12))
email_lbl.grid(row=5,column=0,sticky="w",padx=30)

email_entry = CTkEntry(frame1,text_color="black", fg_color="#F6F6F6", border_color="#B5B5B5",
                         font=("",12), width=229.52, corner_radius=5, height=28)
email_entry.grid(row=6,column=0,sticky="nwe",padx=30, pady=(0, 18))

password_lbl = CTkLabel(frame1,text="Password",text_color="black",cursor="hand2",font=("",12))
password_lbl.grid(row=7,column=0,sticky="w",padx=30)

password_lbl = CTkLabel(frame1,text="Ulangi Password",text_color="black",cursor="hand2",font=("",12))
password_lbl.grid(row=7,column=0,sticky="e",padx=(0, 125))

passwd_entry = CTkEntry(frame1,text_color="black",fg_color="#F6F6F6", border_color="#B5B5B5",
                         font=("",12), width=190,corner_radius=5, height=28, show="*")
passwd_entry.grid(row=8,column=0,sticky="w",padx=30, pady=(0, 18))
passwd_entry = CTkEntry(frame1,text_color="black",fg_color="#F6F6F6", border_color="#B5B5B5",
                         font=("",12), width=190,corner_radius=5, height=28, show="*")
passwd_entry.grid(row=8,column=0,sticky="e",padx=30, pady=(0, 18))

phoneNumber_lbl = CTkLabel(frame1,text="Nomor Telepon",text_color="black",cursor="hand2",font=("",12))
phoneNumber_lbl.grid(row=9,column=0,sticky="w",padx=30)

phoneNumber_entry = CTkEntry(frame1,text_color="black", fg_color="#F6F6F6", border_color="#B5B5B5",
                         font=("",12), width=229.52, corner_radius=5, height=28)
phoneNumber_entry.grid(row=10,column=0,sticky="nwe",padx=30, pady=(0, 18))

checkbox = CTkCheckBox(frame1, text="I agree with terms and conditions.", text_color="black", onvalue="on", offvalue="off", checkbox_width=20, checkbox_height=20,
                       border_width=2, border_color="#B5B5B5", fg_color="#5692EC", hover_color="#5692EC")
checkbox.grid(row=11, sticky="w", column=0, padx=30)

l_btn = CTkButton(frame1,text="Register",text_color="white", font=("",12),height=26,width=72,fg_color="#5692EC",cursor="hand2",
                  corner_radius=5)
l_btn.grid(row=12,column=0,sticky="ne",pady=(5,0), padx=35)

register1_lbl = CTkLabel(frame1,text="Sudah punya akun?",text_color="black",font=("",12))
register1_lbl.grid(row=13,column=0, sticky="w", padx=(150, 0))
register1_lbl = CTkLabel(frame1,text=" Login",text_color="#4388F0",cursor="hand2",font=("",12))
register1_lbl.grid(row=13,column=0, sticky="ne", pady=5, padx=(0, 170))

frame1.pack(expand=True, anchor="center")

main.mainloop()