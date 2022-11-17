from Base.windows import *
from GUI.main.choose.worker.admin.workers.add_worker_window import AddWorkerWindow
from GUI.main.choose.worker.admin.workers.update_worker_window import UpdateWorkerWindow
from GUI.main.choose.worker.admin.workers.delete_worker_window import DeleteWorkerWindow


class WorkersWindow(TableWindow):
    def __init__(self, width, height, title, resizable):
        super().__init__(width, height, title, resizable, ['ID Сотрудника',
                                                           'Логин',
                                                           'Пароль',
                                                           'Доступ'])

    def fill_page(self):
        self.table.delete(*self.table.get_children())
        for i in DataBase.Workers.get_info(self.this_page):
            self.table.insert('', tk.END, values=i)

    def last_page(self):
        self.this_page = self.max_page()
        self.fill_entry()

    def max_page(self):
        return int(DataBase.Workers.max_index() / 100) + 1

    def search(self, find):
        self.table.delete(*self.table.get_children())
        for i in DataBase.Workers.search(find):
            self.table.insert('', tk.END, values=i)

    def add(self, width=300, height=180, title="Добавить запись", resizable=(False, False)):
        AddWorkerWindow(self.window, width, height, title, resizable)

    def update(self, width=300, height=200, title="Изменить запись", resizable=(False, False)):
        UpdateWorkerWindow(self.window, width, height, title, resizable)

    def delete(self, width=250, height=100, title="Удалить запись", resizable=(False, False)):
        DeleteWorkerWindow(self.window, width, height, title, resizable)
