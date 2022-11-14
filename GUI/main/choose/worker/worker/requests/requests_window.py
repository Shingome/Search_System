from Base.windows import *


class RequestsWindow(TableWindow):
    def __init__(self, width, height, title, resizable):
        super().__init__(width, height, title, resizable, ['request_id',
                                                           'card_id',
                                                           'name',
                                                           'author',
                                                           'registration_date'])
        self.frame_buttons.place_forget()

    def fill_page(self):
        self.table.delete(*self.table.get_children())
        for i in DataBase.Requests.get_info(self.this_page):
            self.table.insert('', tk.END, values=i)

    def last_page(self):
        self.this_page = self.max_page()
        self.fill_entry()

    def max_page(self):
        return int(DataBase.Requests.max_index() / 100) + 1

    def search(self, find):
        self.table.delete(*self.table.get_children())
        for i in DataBase.Requests.search(find):
            self.table.insert('', tk.END, values=i)
