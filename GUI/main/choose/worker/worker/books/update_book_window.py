from Base.windows import *
from GUI.main.choose.worker.worker.books.add_book_window import AddBookWindow


class UpdateBookWindow(AddBookWindow):
    def __init__(self, parent, width, height, title, resizable):
        super().__init__(parent, width, height, title, resizable)

        self.button_add.configure(text="Изменить", command=lambda: self.update_field(self.textbox_id.get(),
                                                                                     self.textbox_name.get(),
                                                                                     self.textbox_author.get(),
                                                                                     self.textbox_publish.get(),
                                                                                     self.textbox_year.get(),
                                                                                     self.textbox_pages.get()))

    def update_field(self, book_id, name, author, publish, year, pages):
        try:
            error = False
            if not book_id \
                    or not name \
                    or not author \
                    or not publish \
                    or not year \
                    or not pages \
                    or not DataBase.Books.check_index(book_id):
                error = True
            else:
                DataBase.Books.update(book_id, name, author, publish, year, pages)
        except:
            error = True
        if error:
            self.error()
        else:
            self.window.destroy()
