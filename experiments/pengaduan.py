import tkinter as tk
from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkEntry, CTkImage
from tkinter import Menu, Canvas
from PIL import Image
import os
from spinBox import FloatSpinbox
from CTkTable import *

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("List Pengaduan")
        self.config(bg="#F4F6F9")

        # Main window dimensions
        main_width = 1080
        main_height = 768

        # Get screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate x and y coordinates to center the window
        x = (screen_width // 2) - (main_width // 2)
        y = (screen_height // 2) - (main_height // 2)

        # Set the geometry of the window
        self.geometry(f"{main_width}x{main_height}+{x}+{y}")
        self.resizable(False, False)

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (ListPengaduanPage, BuatPengaduanPage):
            frame = F(parent=self.container, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(ListPengaduanPage)

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()

class ListPengaduanPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#F4F6F9")

        navbar = CTkFrame(self, fg_color="#6777EF", bg_color="white", width=1080, height=88.5, corner_radius=0)
        navbar.pack(side="top", fill="x")

        appName_lbl = CTkLabel(navbar, text="SuaraKu", text_color="white", font=("PlusJakartaSans", 27, "bold"))
        appName_lbl.place(x=27, y=27)

        dashboard_lbl = CTkLabel(navbar, text="Dashboard", text_color="white", font=("PlusJakartaSans", 18))
        dashboard_lbl.place(x=323, y=34)

        pengaduan_lbl = CTkLabel(navbar, text="Pengaduan", text_color="white", font=("PlusJakartaSans", 18))
        pengaduan_lbl.place(x=482, y=34)

        canvas = Canvas(navbar, width=151.5)
        canvas.create_rectangle(455, 2, 607, 2, width=3)
        canvas.place(x=450, y=82)

        user_lbl = CTkLabel(navbar, text="User", text_color="white", font=("PlusJakartaSans", 18))
        user_lbl.place(x=645, y=34)

        profile_img = CTkImage(dark_image=Image.open("Assets/frame0/image_1.png"), size=(45, 45))
        profile_lab = CTkLabel(navbar, image=profile_img, text="")
        profile_lab.place(x=830, y=23.25)

        username_lbl = CTkLabel(navbar, text="Hi, Marcus Miles", text_color="white", font=("PlusJakartaSans", 18))
        username_lbl.place(x=883, y=33)

        menu = Menu(self.controller, tearoff=0)
        menu.add_command(label="Profile", command=self.profile)
        menu.add_command(label="Logout", command=self.logout)

        dropdown_trigger = CTkLabel(navbar, text="▼", text_color="white", font=("PlusJakartaSans", 18), cursor="hand2")
        dropdown_trigger.place(x=1020, y=33)
        dropdown_trigger.bind("<Button-1>", self.show_menu)

        content_title = CTkFrame(self, fg_color="#FFFFFF", bg_color="white", width=990.75, height=96.75)
        content_title.pack(pady=(88.5, 0))

        contentTitle_lbl = CTkLabel(content_title, text="List Pengaduan", text_color="black", font=("PlusJakartaSans", 24, "bold"), cursor="hand2")
        contentTitle_lbl.place(x=56 - 41.25, y=153 - 121.5)

        addPengaduan_btn = CTkButton(content_title, text="Buat Pengaduan", width=100, height=30, fg_color="#6777EF", hover_color="#424D98", command=self.open_buat_pengaduan, font=("PlusJakartaSans", 15))
        addPengaduan_btn.place(x=857.75 - 41.25, y=156 - 121.5)

        content = CTkFrame(self, fg_color="#FFFFFF", bg_color="white", width=990.75, height=484.5)
        content.pack(pady=(0, 41.25))

        show_lbl = CTkLabel(content, text="Show", text_color="black", font=("PlusJakartaSans", 13))
        show_lbl.place(x=81.5 - 41.25, y=288 - 250.5)

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

        table_frame = CTkFrame(content, fg_color="#F4F6F9", width=922.75, height=196.5)
        table_frame.place(x=40, y=100)

        columns = ["No", "Judul Pengaduan", "Tanggal Pengaduan", "Status", "Action"]
        data = [
            ["1", "Contoh Pengaduan 1", "2024-03-22", "Belum Diverifikasi"],
            ["2", "Contoh Pengaduan 2", "2024-04-22", "Sedang Diproses"],
            ["3", "Contoh Pengaduan 3", "2024-05-22", "Selesai"]
        ]

        for i, col in enumerate(columns):
            label = CTkLabel(table_frame, text=col, text_color="black", font=("PlusJakartaSans", 13, "bold"), width=181.5, height=50, fg_color="#D3D3D3")
            label.grid(row=0, column=i, sticky="nsw")

        for row_idx, row_data in enumerate(data, start=1):
            for col_idx, item in enumerate(row_data):
                label = CTkLabel(table_frame, text=item, text_color="black", font=("PlusJakartaSans", 13), width=181.5, height=50)
                label.grid(row=row_idx, column=col_idx, sticky="nsw")

            # Add button in the "Action" column
            button = CTkButton(table_frame, text="Detail", command=open_detail, width=100, height=30, fg_color="#6777EF", hover_color="#424D98")
            button.grid(row=row_idx, column=len(columns)-1, padx=(37.5, 37.5), pady=(10, 10))

    def profile(self):
        print("Profile clicked!")

    def logout(self):
        self.controller.destroy()
        os.system("python views/auth/login.py")

    def show_menu(self, event):
        menu = Menu(self.controller, tearoff=0)
        menu.add_command(label="Profile", command=self.profile)
        menu.add_command(label="Logout", command=self.logout)
        menu.post(event.x_root, event.y_root)
    
    def open_buat_pengaduan(self):
        self.controller.show_frame(BuatPengaduanPage)

class BuatPengaduanPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#F4F6F9")

        navbar = CTkFrame(self, fg_color="#6777EF", bg_color="white", width=1080, height=88.5, corner_radius=0)
        navbar.pack(side="top", fill="x")

        appName_lbl = CTkLabel(navbar, text="SuaraKu", text_color="white", font=("PlusJakartaSans", 27, "bold"))
        appName_lbl.place(x=27, y=27)

        dashboard_lbl = CTkLabel(navbar, text="Dashboard", text_color="white", font=("PlusJakartaSans", 18))
        dashboard_lbl.place(x=323, y=34)

        pengaduan_lbl = CTkLabel(navbar, text="Pengaduan", text_color="white", font=("PlusJakartaSans", 18))
        pengaduan_lbl.place(x=482, y=34)

        canvas = Canvas(navbar, width=151.5)
        canvas.create_rectangle(455, 2, 607, 2, width=3)
        canvas.place(x=450, y=82)

        user_lbl = CTkLabel(navbar, text="User", text_color="white", font=("PlusJakartaSans", 18))
        user_lbl.place(x=645, y=34)

        profile_img = CTkImage(dark_image=Image.open("Assets/frame0/image_1.png"), size=(45, 45))
        profile_lab = CTkLabel(navbar, image=profile_img, text="")
        profile_lab.place(x=830, y=23.25)

        username_lbl = CTkLabel(navbar, text="Hi, Marcus Miles", text_color="white", font=("PlusJakartaSans", 18))
        username_lbl.place(x=883, y=33)

        menu = Menu(self.controller, tearoff=0)
        menu.add_command(label="Profile", command=self.profile)
        menu.add_command(label="Logout", command=self.logout)

        dropdown_trigger = CTkLabel(navbar, text="▼", text_color="white", font=("PlusJakartaSans", 18), cursor="hand2")
        dropdown_trigger.place(x=1020, y=33)
        dropdown_trigger.bind("<Button-1>", self.show_menu)

        content_title = CTkFrame(self, fg_color="#FFFFFF", bg_color="white", width=990.75, height=96.75)
        content_title.pack(pady=(88.5, 0))

        contentTitle_lbl = CTkLabel(content_title, text="Buat Pengaduan", text_color="black", font=("PlusJakartaSans", 24, "bold"), cursor="hand2")
        contentTitle_lbl.place(x=105.5 - 41.25, y=153 - 121.5)

        backButton_img = CTkImage(dark_image=Image.open("Assets/arrow.png"), size=(26.25, 26.25))
        backButton_lab = CTkLabel(content_title, image=backButton_img, text="", cursor="hand2")
        backButton_lab.place(x=62.75 - 41.25, y=153 - 121.5)
        backButton_lab.bind("<Button-1>", lambda e: self.controller.show_frame(ListPengaduanPage))

        # Your Buat Pengaduan Page content here
    def profile(self):
        print("Profile clicked!")

    def logout(self):
        self.controller.destroy()
        os.system("python views/auth/login.py")

    def show_menu(self, event):
        menu = Menu(self.controller, tearoff=0)
        menu.add_command(label="Profile", command=self.profile)
        menu.add_command(label="Logout", command=self.logout)
        menu.post(event.x_root, event.y_root)

def open_detail():
    print("Detail button clicked!")


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
