from Base.windows import *
from GUI.main.choose.worker.worker.worker_window import WorkerWindow
from GUI.main.choose.worker.admin.admin_window import AdminWindow


class AuthorizationWindow(ChildWindow):
    def __init__(self, parent, width, height, title, resizable):
        super().__init__(parent, width, height, title, resizable)
        self.grab_focus()
        self.parent = parent
        self.error_x = 1

        self.frame = tk.Frame(self.window)
        self.frame.place(relx=0, rely=0, relheight=1, relwidth=1)

        label_login = tk.Label(self.frame, text="Логин: ")
        label_password = tk.Label(self.frame, text="Пароль: ")
        textbox_login = ttk.Entry(self.frame)
        textbox_password = ttk.Entry(self.frame, show="*")
        button_accept = tk.Button(self.frame, text="ОК", command=lambda: self.check(textbox_login.get(),
                                                                                    textbox_password.get()))
        button_accept.configure(command=lambda: self.open_worker())

        label_login.grid(row=0, column=0, padx=20, pady=20, sticky=tk.E)
        textbox_login.grid(row=0, column=1, pady=20, sticky=tk.W)
        label_password.grid(row=1, column=0, padx=20, pady=20, sticky=tk.E)
        textbox_password.grid(row=1, column=1, pady=20, sticky=tk.W)
        button_accept.place(anchor=tk.CENTER, rely=0.7, relx=0.5, relheight=0.15, relwidth=0.6)

    def error(self):
        label_error = tk.Label(self.frame,
                               text=f"Ошибка(X{self.error_x})",
                               foreground=["red", "blue"][self.error_x % 2])
        label_error.place(anchor=tk.CENTER, rely=0.9, relx=0.5, relheight=0.15, relwidth=0.6)
        self.error_x += 1

    def check(self, login, password):
        if not login or not password:
            self.error()
            return
        level = DataBase.Workers.check(login, password)
        if level == 1:
            self.open_worker()
        elif level == 2:
            self.open_admin()
        else:
            self.error()

    def open_worker(self, width=300, height=400, title="Работник", resizable=(False, False)):
        self.parent.destroy()
        WorkerWindow(width, height, title, resizable)

    def open_admin(self, width=200, height=200, title="Администратор", resizable=(False, False)):
        self.parent.destroy()
        AdminWindow(width, height, title, resizable)
