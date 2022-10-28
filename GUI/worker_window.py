from windows import *
from books_window import BooksWindow
from clients_window import ClientsWindow
from orders_windows import OrdersWindow
from requests_windows import RequestsWindow


class WorkerWindow(Window):
    def __init__(self, width, height, title, resizable):
        super().__init__(width, height, title, resizable)
        self.window.minsize(300, 400)
        button_books = tk.Button(text="Книжный фонд", command=lambda: self.open_books())
        button_clients = tk.Button(text="Читатели", command=lambda: self.open_clients())
        button_orders = tk.Button(text="Заказы", command=lambda: self.open_orders())
        button_requests = tk.Button(text="Заявки", command=lambda: self.open_requests())

        button_books.place(relx=0.25, rely=0.025, relwidth=0.5, relheight=0.20)
        button_clients.place(relx=0.25, rely=0.275, relwidth=0.5, relheight=0.20)
        button_orders.place(relx=0.25, rely=0.525, relwidth=0.5, relheight=0.20)
        button_requests.place(relx=0.25, rely=0.775, relwidth=0.5, relheight=0.20)

    def open_books(self, width=1600, height=600, title="Книжный фонд", resizable=(True, True)):
        BooksWindow(width, height, title, resizable)

    def open_clients(self, width=1600, height=600, title="Клиенты", resizable=(True, True)):
        ClientsWindow(width, height, title, resizable)

    def open_orders(self, width=1600, height=600, title="Заказы", resizable=(True, True)):
        OrdersWindow(width, height, title, resizable)

    def open_requests(self, width=1600, height=600, title="Заказы", resizable=(True, True)):
        RequestsWindow(width, height, title, resizable)