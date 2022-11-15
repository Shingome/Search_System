from Base.windows import *
from GUI.main.choose.worker.worker.books.books_window import BooksWindow
from GUI.main.choose.worker.worker.clients.clients_window import ClientsWindow
from GUI.main.choose.worker.worker.orders.orders_window import OrdersWindow
from GUI.main.choose.worker.worker.requests.requests_window import RequestsWindow


class WorkerWindow(Window):
    def __init__(self, width, height, title, resizable):
        super().__init__(width, height, title, resizable)
        self.button_books = tk.Button(text="Книжный фонд", command=lambda: self.open_books())
        self.button_clients = tk.Button(text="Читатели", command=lambda: self.open_clients())
        self.button_orders = tk.Button(text="Заказы", command=lambda: self.open_orders())
        self.button_requests = tk.Button(text="Заявки", command=lambda: self.open_requests())

        self.button_books.place(relx=0.25, rely=0.025, relwidth=0.5, relheight=0.20)
        self.button_clients.place(relx=0.25, rely=0.275, relwidth=0.5, relheight=0.20)
        self.button_orders.place(relx=0.25, rely=0.525, relwidth=0.5, relheight=0.20)
        self.button_requests.place(relx=0.25, rely=0.775, relwidth=0.5, relheight=0.20)

    @staticmethod
    def open_books(width=1600, height=600, title="Книжный фонд", resizable=(True, True)):
        BooksWindow(width, height, title, resizable)

    @staticmethod
    def open_clients(width=1600, height=600, title="Клиенты", resizable=(True, True)):
        ClientsWindow(width, height, title, resizable)

    @staticmethod
    def open_orders(width=1600, height=600, title="Заказы", resizable=(True, True)):
        OrdersWindow(width, height, title, resizable)

    @staticmethod
    def open_requests(width=1600, height=600, title="Заявки", resizable=(True, True)):
        RequestsWindow(width, height, title, resizable)
