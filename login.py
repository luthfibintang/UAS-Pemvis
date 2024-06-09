from customtkinter import *
from PIL import Image

main = CTk()
main.title("Login Page")
main.config(bg="white")
main.geometry("841x600")
main.resizable(False, False)

bg_img = CTkImage(dark_image=Image.open("Assets/img1.jpg"), size=(505.77, 600))

bg_lab = CTkLabel(main, image=bg_img, text="")
bg_lab.grid(row=0, column=1)

imgt_1 = CTkLabel(main,text="Selamat Pagi!",text_color="white",font=("",24,"bold"), fg_color='transparent')
imgt_1.grid(row=0,column=1, pady=(48.47, 75), padx=43.22, sticky="sw")
imgt_2 = CTkLabel(main,text="Indonesia",text_color="white",font=("",14))
imgt_2.grid(row=0,column=1, pady=(48.47, 50), padx=43.22, sticky="sw")

imgt_3 = CTkLabel(main,text="Image dari Unsplash oleh. Azhar J ",text_color="white",font=("",12), fg_color='transparent')
imgt_3.grid(row=0,column=1, pady=(48.47, 5), padx=43.22, sticky="sw")

frame1 = CTkFrame(main,fg_color="white", bg_color="white", height=600, width=100)
frame1.grid(row=0, column=0,padx=40, sticky="nsew")

title = CTkLabel(frame1,text="Welcome!",text_color="black",font=("",24,"bold"), )
title.grid(row=0,column=0,sticky="w", pady=(48.47, 5), padx=30)
subTitle_lbl = CTkLabel(frame1,text="Login untuk mulai mengadu.",text_color="black", font=("",15), )
subTitle_lbl.grid(row=1,column=0, sticky="w", pady=(0, 40), padx=30)

username_lbl = CTkLabel(frame1,text="username",text_color="black",cursor="hand2",font=("",15))
username_lbl.grid(row=2,column=0,sticky="w",padx=30)

usrname_entry = CTkEntry(frame1,text_color="black", fg_color="#F6F6F6", border_color="#B5B5B5",
                         font=("",12), width=229.52, corner_radius=5, height=28)
usrname_entry.grid(row=3,column=0,sticky="nwe",padx=30, pady=(0, 20))

password_lbl = CTkLabel(frame1,text="password",text_color="black",cursor="hand2",font=("",12))
password_lbl.grid(row=4,column=0,sticky="w",padx=30)

passwd_entry = CTkEntry(frame1,text_color="black",fg_color="#F6F6F6", border_color="#B5B5B5",
                         font=("",12), width=229,corner_radius=5, height=28, show="*")
passwd_entry.grid(row=5,column=0,sticky="nwe",padx=30)

cr_acc = CTkLabel(frame1,text="Forgot Password!",text_color="#4388F0",cursor="hand2",font=("",12))
cr_acc.grid(row=6,column=0,sticky="w",pady=20,padx=30)

l_btn = CTkButton(frame1,text="Login",text_color="white", font=("",12),height=26,width=72,fg_color="#5692EC",cursor="hand2",
                  corner_radius=5)
l_btn.grid(row=6,column=0,sticky="ne",pady=20, padx=35)

register1_lbl = CTkLabel(frame1,text="Tidak punya akun?",text_color="black",font=("",12))
register1_lbl.grid(row=7,column=0, pady=20, sticky="w", padx=(65, 0))
register1_lbl = CTkLabel(frame1,text=" Buat",text_color="#4388F0",cursor="hand2",font=("",12))
register1_lbl.grid(row=7,column=0, sticky="ne", pady=20, padx=(0, 90))

register1_lbl = CTkLabel(frame1,text="Copyright © Universitas Pembangunan Jaya. Made by\n Bintang, Widi, & Halvino",text_color="black",font=("",11))
register1_lbl.grid(row=8,column=0, sticky="we", pady=(130, 0))

main.mainloop()