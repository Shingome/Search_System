from Base.windows import *
from GUI.main.choose.worker.admin.workers.workers_window import WorkersWindow
from GUI.main.choose.worker.admin.reports.reports_window import ReportsWindow


class AdminWindow(Window):
    def __init__(self, width, height, title, resizable):
        super().__init__(width, height, title, resizable)
        self.button_books = tk.Button(text="Работники", command=lambda: self.workers_window())
        self.button_clients = tk.Button(text="Отчеты", command=lambda: self.reports())

        self.button_books.pack(padx=20, pady=20, ipady=20, ipadx=20)
        self.button_clients.pack(padx=20, pady=20, ipady=20, ipadx=30)

    @staticmethod
    def workers_window(width=1600, height=600, title="Работники", resizable=(True, True)):
        WorkersWindow(width, height, title, resizable)

    @staticmethod
    def reports(width=615, height=215, title="Отчеты", resizable=(True, True)):
        ReportsWindow(width, height, title, resizable)
