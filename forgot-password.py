from customtkinter import *

main = CTk()
main.title("Login Page")
main.config(bg="#F4F6F9")
main_width = 841
main_height = 600
main.geometry(f"{main_width}x{main_height}")
main.resizable(False, False)


frame1 = CTkFrame(main,fg_color="#FFFFFF", bg_color="white", height= 160, width=265)

pos_x = (main_width - frame1.winfo_reqwidth()) / 2
pos_y = (main_height - frame1.winfo_reqheight()) / 2

# Letakkan frame di tengah window secara horizontal
frame1.place(x=pos_x, y=pos_y)

title = CTkLabel(frame1,text="Lupa Password?",text_color="black",font=("",24,"bold"), )
title.grid(row=0,column=0,sticky="w", pady=(28.47, 18), padx=30)

subTitle_lbl = CTkLabel(frame1,text="Masukan email dan klik kirim code.",text_color="black", font=("",15), )
subTitle_lbl.grid(row=1,column=0, sticky="w", pady=(0, 40), padx=30)

nik_lbl = CTkLabel(frame1,text="Email",text_color="black",font=("",12))
nik_lbl.grid(row=1,column=0,sticky="w",padx=30)

nik_entry = CTkEntry(frame1,text_color="black", fg_color="#F6F6F6", border_color="#B5B5B5",
                         font=("",12), width=405, corner_radius=5, height=28)
nik_entry.grid(row=2,column=0,sticky="nwe",padx=30, pady=(0, 18))

l_btn = CTkButton(frame1,text="Kirim Code",text_color="white", font=("",12),height=28,width=72,fg_color="#5692EC",cursor="hand2",
                  corner_radius=5)
l_btn.grid(row=12,column=0,sticky="nwe",pady=(5,20), padx=30)

main.mainloop()