import customtkinter
from typing import Union, Callable
from customtkinter import CTkFrame, CTkButton, CTkEntry

from customtkinter import CTkFrame, CTkButton, CTkEntry

class FloatSpinbox(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 step_size: int = 10,
                 command: Callable = None,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.command = command

        self.configure(fg_color="transparent")  # set frame color

        self.grid_columnconfigure((0, 2), weight=0)  # buttons don't expand
        self.grid_columnconfigure(1, weight=1)  # entry expands

        self.subtract_button = CTkButton(self, text="-", width=height-6, height=height-6, fg_color="#6777EF", hover_color="#424D98",
                                         command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = CTkEntry(self, width=width-(2*height), height=height-6, fg_color="transparent", text_color="black", font=("PlusJakartaSans", 12), border_color="#B5B5B5")
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="ew")

        self.add_button = CTkButton(self, text="+", width=height-6, height=height-6, fg_color="#6777EF", hover_color="#424D98",
                                    command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)

        # default value
        self.entry.insert(0, "10")  # Nilai awal menjadi 10

    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = min(int(self.entry.get()) + self.step_size, 50)  # Batasan nilai maksimal 50
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = max(int(self.entry.get()) - self.step_size, 10)  # Batasan nilai minimal 10
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def get(self) -> Union[float, None]:
        try:
            return float(self.entry.get())
        except ValueError:
            return None

    def set(self, value: float):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(int(value)))
