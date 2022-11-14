from Base.windows import *


class AddWorkerWindow(SupportWindow):
    def __init__(self, parent, width, height, title, resizable):
        super().__init__(parent, width, height, title, resizable)

        self.label_login = tk.Label(self.frame, text="Логин:")
        self.label_password = tk.Label(self.frame, text="Пароль:")
        self.label_level = tk.Label(self.frame, text="Уровень доступа:")

        self.val_level = (self.window.register(self.validate_level))

        self.textbox_login = ttk.Entry(self.frame)
        self.textbox_password = ttk.Entry(self.frame)
        self.textbox_level = ttk.Entry(self.frame,
                                       validate="key",
                                       validatecommand=(self.val_level, '%P'))

        self.button_add = tk.Button(self.frame,
                                    text="Создать",
                                    command=lambda: self.add_field(self.textbox_login.get(),
                                                                   self.textbox_password.get(),
                                                                   self.textbox_level.get()))

        self.label_login.grid(row=0, column=0, sticky=tk.E)
        self.label_password.grid(row=1, column=0, sticky=tk.E)
        self.label_level.grid(row=2, column=0, sticky=tk.E)

        self.textbox_login.grid(row=0, column=1, padx=5, pady=5)
        self.textbox_password.grid(row=1, column=1, padx=5, pady=5)
        self.textbox_level.grid(row=2, column=1, padx=5, pady=5)

        self.button_add.grid(row=3, columnspan=2, pady=10)

    @staticmethod
    def validate_level(P):
        return True if P in ("1", "2") or P == "" else False

    def add_field(self, *args):
        for i in args:
            if not i:
                self.error()
                return
        try:
            DataBase.Workers.add(*args)
        except:
            self.error()
            return
        self.window.destroy()

