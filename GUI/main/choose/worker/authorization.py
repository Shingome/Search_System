import tkinter.messagebox

from Base.windows import *
from GUI.main.choose.worker.worker.worker_window import WorkerWindow
from GUI.main.choose.worker.admin.admin_window import AdminWindow


class AuthorizationWindow(ChildWindow):
    def __init__(self, parent, width, height, title, resizable):
        super().__init__(parent, width, height, title, resizable)
        self.grab_focus()
        self.parent = parent

        self.frame = tk.Frame(self.window)
        self.frame.place(relx=0, rely=0.05, relheight=1, relwidth=1)

        self.label_login = tk.Label(self.frame, text="Логин: ")
        self.label_password = tk.Label(self.frame, text="Пароль: ")
        self.textbox_login = ttk.Entry(self.frame)
        self.textbox_password = ttk.Entry(self.frame, show="*")
        self.button_accept = tk.Button(self.frame, text="ОК", command=lambda: self.check(self.textbox_login.get(),
                                                                                         self.textbox_password.get()))

        self.label_login.grid(row=0, column=0, padx=20, pady=20, sticky=tk.E)
        self.textbox_login.grid(row=0, column=1, pady=20, sticky=tk.W)
        self.label_password.grid(row=1, column=0, padx=20, pady=20, sticky=tk.E)
        self.textbox_password.grid(row=1, column=1, pady=20, sticky=tk.W)
        self.button_accept.place(anchor=tk.CENTER, rely=0.75, relx=0.5, relheight=0.15, relwidth=0.6)

        self.window.bind('<Return>', self.check_bind)

    def check_bind(self, *args):
        return self.check(self.textbox_login.get(), self.textbox_password.get())

    def check(self, login, password):
        if not login or not password:
            tkinter.messagebox.showerror(title="Ошибка", message="Введите данные")
            return
        level = DataBase.Workers.check(login, password)
        if level == 1:
            self.open_worker()
        elif level == 2:
            self.open_admin()
        else:
            tkinter.messagebox.showerror(title="Ошибка", message="Пользователь не был найден")

    def open_worker(self, width=300, height=400, title="Работник", resizable=(False, False)):
        self.parent.destroy()
        WorkerWindow(width, height, title, resizable)

    def open_admin(self, width=200, height=200, title="Администратор", resizable=(False, False)):
        self.parent.destroy()
        AdminWindow(width, height, title, resizable)
