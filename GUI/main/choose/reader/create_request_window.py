from Base.windows import *


class CreateRequestWindow(SupportWindow):
    def __init__(self, parent, width, height, title, resizable):
        super().__init__(parent, width, height, title, resizable)

        self.label_id = tk.Label(self.frame, text="ID читателя:")
        self.label_name = tk.Label(self.frame, text="Название:")
        self.label_author = tk.Label(self.frame, text="Автор:")

        self.textbox_id = ttk.Entry(self.frame,
                                    validate="key",
                                    validatecommand=(self.val_digit, '%P'))
        self.textbox_name = ttk.Entry(self.frame,
                                      validate="key",
                                      validatecommand=(self.val_text, '%P'))
        self.textbox_author = ttk.Entry(self.frame,
                                        validate="key",
                                        validatecommand=(self.val_text, '%P'))

        self.button_add = tk.Button(self.frame,
                                    text="Отправить",
                                    command=lambda: self.add_field(self.textbox_id.get(),
                                                                   self.textbox_name.get(),
                                                                   self.textbox_author.get()))

        self.label_id.grid(row=0, column=0, sticky=tk.E)
        self.label_name.grid(row=1, column=0, sticky=tk.E)
        self.label_author.grid(row=2, column=0, sticky=tk.E)

        self.textbox_id.grid(row=0, column=1, padx=5, pady=5)
        self.textbox_name.grid(row=1, column=1, padx=5, pady=5)
        self.textbox_author.grid(row=2, column=1, padx=5, pady=5)

        self.button_add.grid(row=3, columnspan=2, pady=10)

    def add_field(self, *args):
        try:
            DataBase.Requests.add(*args)
        except:
            self.error()
            return
        self.window.destroy()
