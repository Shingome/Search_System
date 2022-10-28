from windows import *


class ClientsWindow(TableWindow):
    def __init__(self, width, height, title, resizable):
        super().__init__(width, height, title, resizable, ['client_id',
                                                           'card_id',
                                                           'fname',
                                                           'cname',
                                                           'adress',
                                                           'phone',
                                                           'registration_date'])

        books = ((i, i, i, i, i, i, i) for i in range(100))
        for i in books:
            self.table.insert('', tk.END, values=i)
