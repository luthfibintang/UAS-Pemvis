# Library
from customtkinter import *

main = CTk()
main.title("Lupa Password Page")
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

#frame
frame1 = CTkFrame(main,fg_color="#FFFFFF", bg_color="white")

# Label Title
title = CTkLabel(frame1,text="Lupa Password?",text_color="black",font=("",24,"bold"), )
title.grid(row=0,column=0,sticky="w", pady=(28.47, 18), padx=30)
subTitle_lbl = CTkLabel(frame1,text="Masukan email dan klik kirim code.",text_color="black", font=("",15), )
subTitle_lbl.grid(row=1,column=0, sticky="w", pady=(0, 10), padx=30)

# Email input
email_lbl = CTkLabel(frame1,text="Email",text_color="black",font=("",12))
email_lbl.grid(row=2,column=0,sticky="w",padx=30)
email_entry = CTkEntry(frame1,text_color="black", fg_color="#F6F6F6", border_color="#B5B5B5",
                    font=("",12), width=405, corner_radius=5, height=28)
email_entry.grid(row=3,column=0,sticky="nwe",padx=30, pady=(0, 15))

# Button to send Code
confirm_btn = CTkButton(frame1,text="Kirim Code",text_color="white", font=("",12),height=28,width=72,fg_color="#5692EC",cursor="hand2",
                  corner_radius=5)
confirm_btn.grid(row=4,column=0,sticky="nwe",pady=(5,5), padx=30)

# Button to go back to Login
back_lbl = CTkLabel(frame1,text="Kembali",text_color="#4388F0",cursor="hand2",font=("",12))
back_lbl.grid(row=5,column=0, sticky="we", pady=(0, 28.47))

# Make frame in the middle of the main window
frame1.pack(expand=True, anchor="center")

# To display tkinter and not closed
main.mainloop()