from Base.windows import *
from GUI.main.choose.worker.worker.books.add_book_window import AddBookWindow
from GUI.main.choose.worker.worker.books.delete_book_window import DeleteBookWindow
from GUI.main.choose.worker.worker.books.update_book_window import UpdateBookWindow


class BooksWindow(TableWindow):
    def __init__(self, width, height, title, resizable):
        super().__init__(width, height, title, resizable, ['ID Книги',
                                                           'Название',
                                                           'Автор',
                                                           'Издательство',
                                                           'Год',
                                                           'Страницы'])

    def fill_page(self):
        self.table.delete(*self.table.get_children())
        for i in DataBase.Books.get_info(self.this_page):
            self.table.insert('', tk.END, values=i)

    def last_page(self):
        self.this_page = self.max_page()
        self.fill_entry()

    def max_page(self):
        return int(DataBase.Books.length() / 100) + 1

    def search(self, find):
        self.table.delete(*self.table.get_children())
        for i in DataBase.Books.search(find):
            self.table.insert('', tk.END, values=i)

    def add(self, width=350, height=300, title="Добавить запись", resizable=(False, False)):
        AddBookWindow(self.window, width, height, title, resizable)

    def update(self, width=350, height=300, title="Изменить запись", resizable=(False, False)):
        UpdateBookWindow(self.window, width, height, title, resizable)

    def delete(self, width=250, height=100, title="Удалить запись", resizable=(False, False)):
        DeleteBookWindow(self.window, width, height, title, resizable)

