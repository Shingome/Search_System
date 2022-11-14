from Base.windows import *


class AddClientWindow(SupportWindow):
    def __init__(self, parent, width, height, title, resizable):
        super().__init__(parent, width, height, title, resizable)

        self.label_sname = tk.Label(self.frame, text="Имя:")
        self.label_fname = tk.Label(self.frame, text="Фамилия:")
        self.label_adress = tk.Label(self.frame, text="Адрес:")
        self.label_phone = tk.Label(self.frame, text="Телефон:")

        self.textbox_sname = ttk.Entry(self.frame,
                                       validate="key",
                                       validatecommand=(self.val_text, '%P'))
        self.textbox_fname = ttk.Entry(self.frame,
                                       validate="key",
                                       validatecommand=(self.val_text, '%P'))
        self.textbox_adress = ttk.Entry(self.frame)
        self.textbox_phone = ttk.Entry(self.frame,
                                       validate="key",
                                       validatecommand=(self.val_digit, '%P'))

        self.button_add = tk.Button(self.frame,
                                    text="Создать",
                                    command=lambda: self.add_field(self.textbox_sname.get(), self.textbox_fname.get(),
                                                                   self.textbox_phone.get(), self.textbox_adress.get()))

        self.label_sname.grid(row=0, column=0, sticky=tk.E)
        self.label_fname.grid(row=1, column=0, sticky=tk.E)
        self.label_adress.grid(row=2, column=0, sticky=tk.E)
        self.label_phone.grid(row=3, column=0, sticky=tk.E)

        self.textbox_sname.grid(row=0, column=1, padx=5, pady=5)
        self.textbox_fname.grid(row=1, column=1, padx=5, pady=5)
        self.textbox_adress.grid(row=2, column=1, padx=5, pady=5)
        self.textbox_phone.grid(row=3, column=1, padx=5, pady=5)

        self.button_add.grid(row=4, columnspan=2, pady=10)

    def add_field(self, *args):
        for i in args:
            if not i:
                self.error()
                return
        try:
            DataBase.Clients.add(*args)
        except:
            self.error()
            return
        self.window.destroy()


