from Base.windows import *
from GUI.main.choose.reader.create_request_window import CreateRequestWindow


class ReaderWindow(TableWindow):
    def __init__(self, width, height, title, resizable):
        super().__init__(width, height, title, resizable, ['name', 'author', 'publish', 'year', 'pages'])

        self.frame_request = tk.Frame(self.window, bg="silver")
        self.frame_request.place(relx=0.75, relwidth=0.25, relheight=0.05)

        self.button_request = tk.Button(self.frame_request, text="Не нашел книгу?", command=lambda: self.request_window())
        self.button_request.pack(side=tk.RIGHT, padx=30)

    @staticmethod
    def hide_index(table):
        hiden = []
        for i in table:
            hiden.append(i[1:])
        return hiden

    def fill_page(self):
        self.table.delete(*self.table.get_children())
        for i in self.hide_index(DataBase.Books.get_info(self.this_page)):
            self.table.insert('', tk.END, values=i)

    def last_page(self):
        self.this_page = self.max_page()
        self.fill_entry()

    def max_page(self):
        return int(DataBase.Books.length() / 100) + 1

    def search(self, find):
        self.table.delete(*self.table.get_children())
        for i in self.hide_index(DataBase.Books.search(find)):
            self.table.insert('', tk.END, values=i)

    def request_window(self, width=280, height=180, title="Работник", resizable=(False, False)):
        CreateRequestWindow(self.window, width, height, title, resizable)
