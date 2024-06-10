import customtkinter
from Views.bin.spinBox import FloatSpinbox

app = customtkinter.CTk()

spinbox_1 = FloatSpinbox(app, width=100, step_size=10)
spinbox_1.pack(padx=20, pady=20)

spinbox_1.set(10)
print(spinbox_1.get())

app.mainloop()