from windows import *


class RequestsWindow(TableWindow):
    def __init__(self, width, height, title, resizable):
        super().__init__(width, height, title, resizable, ['request_id',
                                                           'client_id',
                                                           'name',
                                                           'author',
                                                           'registration_date'])

        books = ((i, i, i, i, i) for i in range(100))
        for i in books:
            self.table.insert('', tk.END, values=i)
