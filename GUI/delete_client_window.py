import tkinter

from windows import *


class DeleteClientWindow(ChildWindow):
    def __init__(self, parent, width, height, title, resizable):
        super().__init__(parent, width, height, title, resizable)
        self.grab_focus()

        self.frame = tk.Frame(self.window)
        self.frame.place(relx=0.2, rely=0.2, relheight=0.9, relwidth=0.9)

        self.val_digit = (self.window.register(self.validate_digit))

        self.label_id = tk.Label(self.frame, text="ID:")

        self.textbox_id = ttk.Entry(self.frame,
                                    validate="key",
                                    validatecommand=(self.val_digit, "%S"))

        self.button_id = tkinter.Button(self.frame,
                                        text="Удалить",
                                        command=lambda: self.delete_field(self.textbox_id.get()))

        self.label_id.grid(row=0, column=0, sticky=tk.E)
        self.textbox_id.grid(row=0, column=1)
        self.button_id.grid(row=1, column=0, columnspan=2, pady=8)

    def delete_field(self, id):
        DataBase.Clients.delete(id)
        self.window.destroy()



