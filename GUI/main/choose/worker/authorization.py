from Base.windows import *
from GUI.main.choose.worker.worker_window import WorkerWindow

class AuthorizationWindow(ChildWindow):
    def __init__(self, parent, width, height, title, resizable):
        super().__init__(parent, width, height, title, resizable)
        self.grab_focus()
        self.parent = parent
        self.error_x = 1

        self.frame = tk.Frame(self.window)
        self.frame.place(relx=0, rely=0, relheight=1, relwidth=1)

        label_id = tk.Label(self.frame, text="Логин: ")
        label_password = tk.Label(self.frame, text="Пароль: ")
        textbox_id = ttk.Entry(self.frame, )
        textbox_password = ttk.Entry(self.frame, show="*")
        button_accept = tk.Button(self.frame, text="ОК", command=lambda: self.open_worker())

        label_id.grid(row=0, column=0, padx=20, pady=20, sticky=tk.E)
        textbox_id.grid(row=0, column=1, pady=20, sticky=tk.W)
        label_password.grid(row=1, column=0, padx=20, pady=20, sticky=tk.E)
        textbox_password.grid(row=1, column=1, pady=20, sticky=tk.W)
        button_accept.place(anchor=tk.CENTER, rely=0.7, relx=0.5, relheight=0.15, relwidth=0.6)

    def error(self):
        label_error = tk.Label(self.frame,
                               text=f"Ошибка(X{self.error_x})",
                               foreground=["red", "blue"][self.error_x % 2])
        label_error.place(anchor=tk.CENTER, rely=0.9, relx=0.5, relheight=0.15, relwidth=0.6)
        self.error_x += 1

    def check(self):
        pass

    def open_worker(self, width=300, height=400, title="Работник", resizable=(True, True)):
        self.parent.destroy()
        WorkerWindow(width, height, title, resizable)
