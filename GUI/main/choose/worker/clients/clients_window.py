from Base.windows import *
from GUI.main.choose.worker.clients.add_client_window import AddClientWindow
from GUI.main.choose.worker.clients.update_client_window import UpdateClientWindow
from GUI.main.choose.worker.clients.delete_client_window import DeleteClientWindow


class ClientsWindow(TableWindow):
    def __init__(self, width, height, title, resizable):
        super().__init__(width, height, title, resizable, ['client_id',
                                                           'card_id',
                                                           'fname',
                                                           'cname',
                                                           'adress',
                                                           'phone'])

    def fill_page(self):
        self.table.delete(*self.table.get_children())
        for i in DataBase.Clients.get_info(self.this_page):
            self.table.insert('', tk.END, values=i)

    def last_page(self):
        self.this_page = self.max_page()
        self.fill_entry()

    def max_page(self):
        return int(DataBase.Clients.max_index() / 100) + 1

    def search(self, find):
        self.table.delete(*self.table.get_children())
        for i in DataBase.Clients.search(find):
            self.table.insert('', tk.END, values=i)

    def add(self, width=250, height=220, title="Добавить запись", resizable=(False, False)):
        AddClientWindow(self.window, width, height, title, resizable)

    def update(self, width=250, height=250, title="Изменить запись", resizable=(False, False)):
        UpdateClientWindow(self.window, width, height, title, resizable)

    def delete(self, width=250, height=100, title="Удалить запись", resizable=(False, False)):
        DeleteClientWindow(self.window, width, height, title, resizable)
