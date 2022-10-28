from windows import *


class OrdersWindow(TableWindow):
    def __init__(self, width, height, title, resizable):
        super().__init__(width, height, title, resizable, ['order_id', 'book_id', 'card_id', 'get_date', 'return'])

        books = ((i, i, i, i, i) for i in range(100))
        for i in books:
            self.table.insert('', tk.END, values=i)
