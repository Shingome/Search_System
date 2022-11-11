from Base.windows import *
from GUI.main.choose.worker.orders.add_order_window import AddOrderWindow


class OrdersWindow(TableWindow):
    def __init__(self, width, height, title, resizable):
        super().__init__(width, height, title, resizable, ['order_id', 'book_id', 'card_id', 'get_date', 'return_date'])

        self.button_return = self.button_update_client
        self.button_unreturned = self.button_delete_client

        self.button_return.configure(text="Возврат")
        self.button_unreturned.configure(text="Невернувшие")

    def fill_page(self):
        self.table.delete(*self.table.get_children())
        for i in DataBase.Orders.get_info(self.this_page):
            self.table.insert('', tk.END, values=i)

    def last_page(self):
        self.this_page = self.max_page()
        self.fill_entry()

    def max_page(self):
        return int(DataBase.Orders.max_index() / 100) + 1

    def search(self, find):
        self.table.delete(*self.table.get_children())
        for i in DataBase.Orders.search(find):
            self.table.insert('', tk.END, values=i)

    def add(self, width=250, height=150, title="Добавить запись", resizable=(False, False)):
        AddOrderWindow(self.window, width, height, title, resizable)

