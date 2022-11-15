import tkinter.messagebox

from Base.windows import *
import tkinter.filedialog as tf
from GUI.main.choose.worker.admin.reports.median_orders_window import MedianOrdersWindow
from GUI.main.choose.worker.admin.reports.median_readers_window import MedianReadersWindow
from GUI.main.choose.worker.admin.reports.bestseller_window import BestsellerWindow
import time


class ReportsWindow(Window):
    def __init__(self, width, height, title, resizable):
        super().__init__(width, height, title, resizable)

        self.frame = tk.Frame(self.window)

        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.button_new_readers = tk.Button(self.frame,
                                            text="Новые читатели",
                                            command=lambda: self.new_readers_plot(),
                                            width=25,
                                            height=5)
        
        self.button_median_readers = tk.Button(self.frame,
                                               text="Среднее количество читателей",
                                               command=lambda: self.median_readers_window(),
                                               width=25,
                                               height=5)
        
        self.button_new_orders = tk.Button(self.frame,
                                           text="Новые заказы",
                                           command=lambda: self.new_orders_plot(),
                                           width=25,
                                           height=5)
        
        self.button_median_orders = tk.Button(self.frame,
                                              text="Среднее количество заказов",
                                              command=lambda: self.median_orders_window(),
                                              width=25,
                                              height=5)
        
        self.button_db_to_excel = tk.Button(self.frame,
                                            text="БД в Excel",
                                            command=lambda: self.db_to_excel(),
                                            width=25,
                                            height=5)
        
        self.button_bestseller = tk.Button(self.frame,
                                           text="Самая популярная книга",
                                           command=lambda: self.bestseller_window(),
                                           width=25,
                                           height=5)

        self.button_new_readers.grid(row=0, column=0, padx=10, pady=10)
        self.button_new_orders.grid(row=0, column=1, padx=10, pady=10)
        self.button_db_to_excel.grid(row=0, column=2, padx=10, pady=10)
        self.button_median_readers.grid(row=1, column=0, padx=10, pady=10)
        self.button_median_orders.grid(row=1, column=1, padx=10, pady=10)
        self.button_bestseller.grid(row=1, column=2, padx=10, pady=10)

    def median_orders_window(self, width=450, height=50, title="Среднее", resizable=(False, False)):
        MedianOrdersWindow(self.window, width, height, title, resizable)

    def median_readers_window(self, width=550, height=50, title="Среднее", resizable=(False, False)):
        MedianReadersWindow(self.window, width, height, title, resizable)

    def bestseller_window(self, width=400, height=70, title="Бестселлер", resizable=(False, False)):
        BestsellerWindow(self.window, width, height, title, resizable)

    @staticmethod
    def new_orders_plot():
        month, year = time.strftime("%m %Y").split(" ")
        return Analytics.new_orders(int(month), int(year))

    @staticmethod
    def new_readers_plot():
        month, year = time.strftime("%m %Y").split(" ")
        return Analytics.new_readers(int(month), int(year))

    @staticmethod
    def db_to_excel():
        Analytics.db_to_excel(tf.askdirectory())
        tkinter.messagebox.showinfo(message="Успешно сохранено", title="Успех")
