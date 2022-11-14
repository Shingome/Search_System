from Base.windows import *


class UpdateClientWindow(SupportWindow):
    def __init__(self, parent, width, height, title, resizable):
        super().__init__(parent, width, height, title, resizable)

        self.label_id = tk.Label(self.frame, text="Id:")
        self.label_sname = tk.Label(self.frame, text="Имя:")
        self.label_fname = tk.Label(self.frame, text="Фамилия:")
        self.label_adress = tk.Label(self.frame, text="Адрес:")
        self.label_phone = tk.Label(self.frame, text="Телефон:")

        self.val_text = (self.window.register(self.validate_text))
        self.val_digit = (self.window.register(self.validate_digit))

        self.textbox_id = ttk.Entry(self.frame,
                                    validate="key",
                                    validatecommand=(self.val_digit, "%P"))
        self.textbox_sname = ttk.Entry(self.frame,
                                       validate="key",
                                       validatecommand=(self.val_text, '%P'))
        self.textbox_fname = ttk.Entry(self.frame,
                                       validate="key",
                                       validatecommand=(self.val_text, '%P'))
        self.textbox_phone = ttk.Entry(self.frame,
                                       validate="key",
                                       validatecommand=(self.val_digit, '%P'))
        self.textbox_adress = ttk.Entry(self.frame)

        self.button_add = tk.Button(self.frame,
                                    text="Изменить",
                                    command=lambda: self.update_field(self.textbox_id.get(),
                                                                      self.textbox_fname.get(),
                                                                      self.textbox_sname.get(),
                                                                      self.textbox_adress.get(),
                                                                      self.textbox_phone.get()))

        self.label_id.grid(row=0, column=0, sticky=tk.E)
        self.label_sname.grid(row=1, column=0, sticky=tk.E)
        self.label_fname.grid(row=2, column=0, sticky=tk.E)
        self.label_adress.grid(row=3, column=0, sticky=tk.E)
        self.label_phone.grid(row=4, column=0, sticky=tk.E)

        self.textbox_id.grid(row=0, column=1, padx=5, pady=5)
        self.textbox_sname.grid(row=1, column=1, padx=5, pady=5)
        self.textbox_fname.grid(row=2, column=1, padx=5, pady=5)
        self.textbox_adress.grid(row=3, column=1, padx=5, pady=5)
        self.textbox_phone.grid(row=4, column=1, padx=5, pady=5)

        self.button_add.grid(row=5, columnspan=2, pady=8)

    def update_field(self, client_id, fname, sname, adress, phone):
        try:
            error = False
            if not fname \
                    or not sname \
                    or not adress \
                    or not phone \
                    or not client_id \
                    or not DataBase.Clients.check_index(client_id):
                error = True
            else:
                DataBase.Clients.update(client_id, fname, sname, adress, phone)
        except:
            error = True
        if error:
            self.error()
        else:
            self.window.destroy()
