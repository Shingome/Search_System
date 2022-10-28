from windows import *


class BooksWindow(TableWindow):
    def __init__(self, width, height, title, resizable):
        super().__init__(width, height, title, resizable, ['id', 'name', 'author', 'publish', 'year', 'pages'])

        books = ((i, i, i, i, i, i) for i in range(100))
        for i in books:
            self.table.insert('', tk.END, values=i)
