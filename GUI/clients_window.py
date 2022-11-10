from windows import *
from add_client_window import AddClientWindow
from update_client_window import UpdateClientWindow
from delete_client_window import DeleteClientWindow


class ClientsWindow(TableWindow):
    def __init__(self, width, height, title, resizable):
        super().__init__(width, height, title, resizable, ['client_id',
                                                           'card_id',
                                                           'fname',
                                                           'cname',
                                                           'adress',
                                                           'phone'])

        self.frame_buttons = tk.Frame(self.window, bg="silver")
        self.frame_buttons.place(relx=0.75, rely=0, relwidth=1, relheight=0.05)

        self.button_add_client = tk.Button(self.frame_buttons,
                                    text="Новая запись",
                                    command=lambda: self.add_client_window())

        self.button_update_client = tk.Button(self.frame_buttons,
                                       text="Изменить запись",
                                       command=lambda: self.update_client_window())

        self.button_delete_client = tk.Button(self.frame_buttons,
                                              text="Удалить запись",
                                              command=lambda: self.delete_client_window())

        self.button_add_client.grid(row=0, column=0, pady=8, padx=10)
        self.button_update_client.grid(row=0, column=1, pady=8, padx=10)
        self.button_delete_client.grid(row=0, column=2, pady=8, padx=10)

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

    def add_client_window(self, width=250, height=200, title="Добавить запись", resizable=(False, False)):
        AddClientWindow(self.window, width, height, title, resizable)

    def update_client_window(self, width=250, height=250, title="Добавить запись", resizable=(False, False)):
        UpdateClientWindow(self.window, width, height, title, resizable)

    def delete_client_window(self, width=250, height=100, title="Добавить запись", resizable=(False, False)):
        DeleteClientWindow(self.window, width, height, title, resizable)

