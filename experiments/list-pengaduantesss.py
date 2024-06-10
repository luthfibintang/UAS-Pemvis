
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Dev\UPJ\pemvis\New folder\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1920x1040")
window.configure(bg = "#F4F6F9")


canvas = Canvas(
    window,
    bg = "#F4F6F9",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.375,
    0.0,
    1920.375,
    124.0,
    fill="#6777EF",
    outline="")

canvas.create_text(
    46.375,
    38.0,
    anchor="nw",
    text="SuaraKu",
    fill="#FFFFFF",
    font=("PlusJakartaSansRoman Bold", 37 * -1)
)

canvas.create_text(
    679.375,
    48.0,
    anchor="nw",
    text="Dashboard",
    fill="#FFFFFF",
    font=("Inter", 25 * -1)
)

canvas.create_text(
    928.375,
    48.0,
    anchor="nw",
    text="Pengaduan",
    fill="#FFFFFF",
    font=("Inter", 25 * -1)
)

canvas.create_text(
    1179.375,
    48.0,
    anchor="nw",
    text="User",
    fill="#FFFFFF",
    font=("Inter", 25 * -1)
)

canvas.create_text(
    1671.375,
    47.0,
    anchor="nw",
    text="Hi, Pengadu",
    fill="#FFFFFF",
    font=("Inter", 25 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    1630.4140625,
    62.0,
    image=image_image_1
)

canvas.create_rectangle(
    58.375,
    171.0,
    1886.375,
    307.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    59.375,
    352.0,
    1887.375,
    1034.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    160.3125,
    438.75,
    229.921875,
    488.3203125,
    fill="#F6F6F6",
    outline="")

canvas.create_text(
    91.375,
    449.0,
    anchor="nw",
    text="Show",
    fill="#000000",
    font=("Inter", 21 * -1)
)

canvas.create_text(
    167.375,
    451.0,
    anchor="nw",
    text="10",
    fill="#000000",
    font=("Inter", 21 * -1)
)

canvas.create_text(
    238.375,
    449.0,
    anchor="nw",
    text="Entries",
    fill="#000000",
    font=("Inter", 21 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    212.28125,
    463.296875,
    image=image_image_2
)

canvas.create_text(
    80.375,
    215.0,
    anchor="nw",
    text="Pengaduan",
    fill="#000000",
    font=("PlusJakartaSansRoman Bold", 37 * -1)
)

canvas.create_text(
    78.375,
    370.0,
    anchor="nw",
    text="Tabel Pengaduan",
    fill="#000000",
    font=("Inter", 25 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1805.7421875,
    y=429.0,
    width=48.515621185302734,
    height=49.5703125
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1657.558578491211,
    453.78515625,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=1509.375,
    y=429.0,
    width=296.3671569824219,
    height=47.5703125
)

canvas.create_rectangle(
    110.375,
    540.0,
    1854.375,
    603.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    352.375,
    558.0,
    anchor="nw",
    text="Judul Pengaduan",
    fill="#484848",
    font=("Inter", 21 * -1)
)

canvas.create_text(
    261.375,
    624.0,
    anchor="nw",
    text="Contoh Pengaduan oleh user Pengadu",
    fill="#606060",
    font=("Inter", 21 * -1)
)

canvas.create_text(
    776.375,
    632.0,
    anchor="nw",
    text="2024-03-22",
    fill="#606060",
    font=("Inter", 21 * -1)
)

canvas.create_text(
    1153.375,
    630.0,
    anchor="nw",
    text="Belum Diverifikasi",
    fill="#606060",
    font=("Inter", 21 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=1484.5401611328125,
    y=629.6484375,
    width=137.83482360839844,
    height=39.023433685302734
)

canvas.create_text(
    805.375,
    558.0,
    anchor="nw",
    text="Tanggal Pengaduan",
    fill="#484848",
    font=("Inter", 21 * -1)
)

canvas.create_text(
    1213.375,
    558.0,
    anchor="nw",
    text="Status",
    fill="#484848",
    font=("Inter", 21 * -1)
)

canvas.create_text(
    1554.375,
    558.0,
    anchor="nw",
    text="Action ",
    fill="#484848",
    font=("Inter", 21 * -1)
)

canvas.create_text(
    138.375,
    558.0,
    anchor="nw",
    text="No",
    fill="#484848",
    font=("Inter", 21 * -1)
)

canvas.create_text(
    141.375,
    639.0,
    anchor="nw",
    text="1",
    fill="#606060",
    font=("Inter", 21 * -1)
)

canvas.create_text(
    261.375,
    701.0,
    anchor="nw",
    text="Contoh Pengaduan 2 oleh user Pengadu",
    fill="#606060",
    font=("Inter", 21 * -1)
)

canvas.create_text(
    777.375,
    701.0,
    anchor="nw",
    text="2024-04-22",
    fill="#606060",
    font=("Inter", 21 * -1)
)

canvas.create_text(
    1154.375,
    701.0,
    anchor="nw",
    text="Sedang Diproses",
    fill="#606060",
    font=("Inter", 21 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=1484.375,
    y=700.0,
    width=137.83863830566406,
    height=39.023433685302734
)

canvas.create_text(
    140.375,
    701.0,
    anchor="nw",
    text="2",
    fill="#606060",
    font=("Inter", 21 * -1)
)

canvas.create_text(
    262.375,
    778.0,
    anchor="nw",
    text="Contoh Pengaduan 3 oleh user Pengadu",
    fill="#606060",
    font=("Inter", 21 * -1)
)

canvas.create_text(
    776.375,
    778.0,
    anchor="nw",
    text="2024-05-22",
    fill="#606060",
    font=("Inter", 21 * -1)
)

canvas.create_text(
    1154.375,
    778.0,
    anchor="nw",
    text="Selesai",
    fill="#606060",
    font=("Inter", 21 * -1)
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=1481.375,
    y=771.0,
    width=137.5708770751953,
    height=39.023433685302734
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=1804.375,
    y=212.0,
    width=52.734371185302734,
    height=53.7890625
)

canvas.create_text(
    136.375,
    778.0,
    anchor="nw",
    text="3",
    fill="#606060",
    font=("Inter", 21 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1845.375,
    61.0,
    image=image_image_3
)

canvas.create_rectangle(
    890.1015625,
    118.7265625,
    1108.421875,
    124.0000001215592,
    fill="#FFFFFF",
    outline="")
window.resizable(False, False)
window.mainloop()
