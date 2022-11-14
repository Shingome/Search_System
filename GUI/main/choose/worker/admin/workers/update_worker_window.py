from Base.windows import *
from GUI.main.choose.worker.admin.workers.add_worker_window import AddWorkerWindow


class UpdateWorkerWindow(AddWorkerWindow):
    def __init__(self, parent, width, height, title, resizable):
        super().__init__(parent, width, height, title, resizable)

        self.label_id = tk.Label(self.frame, text="ID:")

        self.textbox_id = ttk.Entry(self.frame,
                                       validate="key",
                                       validatecommand=(self.val_digit, '%P'))

        self.button_update = self.button_add

        self.button_update.configure(text="Изменить",
                                     command=lambda: self.update_field(self.textbox_id.get(),
                                                                       self.textbox_login.get(),
                                                                       self.textbox_password.get(),
                                                                       self.textbox_level.get()))

        self.label_id.grid(row=0, column=0, sticky=tk.E)
        self.label_login.grid(row=1, column=0, sticky=tk.E)
        self.label_password.grid(row=2, column=0, sticky=tk.E)
        self.label_level.grid(row=3, column=0, sticky=tk.E)

        self.textbox_id.grid(row=0, column=1, padx=5, pady=5)
        self.textbox_login.grid(row=1, column=1, padx=5, pady=5)
        self.textbox_password.grid(row=2, column=1, padx=5, pady=5)
        self.textbox_level.grid(row=3, column=1, padx=5, pady=5)

        self.button_add.grid(row=4, columnspan=2, pady=10)

    def update_field(self, worker_id, login, password, level):
        try:
            error = False
            if not worker_id \
                    or not login \
                    or not password \
                    or not level \
                    or not DataBase.Workers.check_index(worker_id):
                error = True
            else:
                DataBase.Workers.update(worker_id, login, password, level)
        except:
            error = True
        if error:
            self.error()
        else:
            self.window.destroy()
