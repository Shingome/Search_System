from Base.windows import *
from GUI.main.choose.worker.admin.workers.workers_window import WorkersWindow

class AdminWindow(Window):
    def __init__(self, width, height, title, resizable):
        super().__init__(width, height, title, resizable)
        button_books = tk.Button(text="Работники", command=lambda: self.workers_window())
        button_clients = tk.Button(text="Отчеты", command=lambda: self.reports())

        button_books.pack(padx=20, pady=20, ipady=20, ipadx=20)
        button_clients.pack(padx=20, pady=20, ipady=20, ipadx=30)

    def workers_window(self, width=1600, height=600, title="Работники", resizable=(True, True)):
        WorkersWindow(width, height, title, resizable)

    def reports(self):
        pass
