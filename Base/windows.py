import tkinter as tk
from tkinter import ttk
from DB.database_control import DataBase


class Window:
    def __init__(self, width, height, title="Window", resizable=(False, False)):
        self.window = tk.Tk()
        self.window.geometry(f'{width}x{height}')
        self.window.resizable(*resizable)
        self.window.title(title)


class ChildWindow:
    def __init__(self, parent, width, height, title, resizable):
        self.window = tk.Toplevel(parent)
        self.window.geometry(f'{width}x{height}')
        self.window.resizable(*resizable)
        self.window.title(title)

    def grab_focus(self):
        self.window.grab_set()
        self.window.focus_set()

    @staticmethod
    def validate_text(P):
        return True if str.isalpha(P) or P == "" else False

    @staticmethod
    def validate_digit(P):
        return True if str.isdigit(P) or P == "" else False


class TableWindow(Window):
    def __init__(self, width, height, title, resizable, columns):
        super().__init__(width, height, title, resizable)
        self.window.minsize(1200, 800)

        self.this_page = 1

        self.frame_search = tk.Frame(self.window, bg='silver')
        self.frame_database = tk.Frame(self.window)
        self.frame_pagination = tk.Frame(self.window, bg="silver")
        self.frame_buttons = tk.Frame(self.window, bg="silver")

        self.frame_search.place(relx=0, rely=0, relwidth=1, relheight=0.05)
        self.frame_pagination.place(relx=0.5, rely=0, relwidth=1, relheight=0.05)
        self.frame_database.place(relx=0, rely=0.05, relwidth=1, relheight=0.95)
        self.frame_buttons.place(relx=0.75, rely=0, relwidth=1, relheight=0.05)

        self.textbox_search = ttk.Entry(self.frame_search)
        self.button_search = tk.Button(self.frame_search,
                                       text="Поиск",
                                       command=lambda: self.search(self.textbox_search.get()))
        self.textbox_search.grid(row=0, column=0, padx=20, ipadx=150, sticky="w", pady=12)
        self.button_search.grid(row=0, column=1, padx=10, sticky="w")

        self.validate = (self.window.register(self.update_date))

        self.page_prev = tk.Button(self.frame_pagination, text="<", command=lambda: self.prev_page())
        self.page_start = tk.Button(self.frame_pagination, text="start", command=lambda: self.start_page())
        self.page_now = ttk.Entry(self.frame_pagination, width=6,
                                  justify='center',
                                  validate="key",
                                  validatecommand=(self.validate, '%P'))
        self.page_end = tk.Button(self.frame_pagination, text="end", command=lambda: self.last_page())
        self.page_next = tk.Button(self.frame_pagination, text=">", command=lambda: self.next_page())

        self.page_prev.grid(row=0, column=0, ipadx=15, ipady=2.5, pady=5)
        self.page_start.grid(row=0, column=1, ipadx=15, ipady=2.5, pady=5)
        self.page_now.grid(row=0, column=2, ipadx=1, ipady=2.5, pady=5, padx=2)
        self.page_end.grid(row=0, column=3, ipadx=15, ipady=2.5, pady=5)
        self.page_next.grid(row=0, column=4, ipadx=15, ipady=2.5, pady=5)

        self.table, self.scroll_pane = create_table(self.frame_database, columns)

        self.scroll_pane.pack(side=tk.RIGHT, fill=tk.Y)
        self.table.pack(expand=tk.YES, fill=tk.BOTH, side=tk.TOP)

        self.button_add_client = tk.Button(self.frame_buttons,
                                           text="Новая запись",
                                           command=lambda: self.add())

        self.button_update_client = tk.Button(self.frame_buttons,
                                              text="Изменить запись",
                                              command=lambda: self.update())

        self.button_delete_client = tk.Button(self.frame_buttons,
                                              text="Удалить запись",
                                              command=lambda: self.delete())

        self.button_add_client.grid(row=0, column=0, pady=8, padx=10)
        self.button_update_client.grid(row=0, column=1, pady=8, padx=10)
        self.button_delete_client.grid(row=0, column=2, pady=8, padx=10)

        self.fill_entry()

    def update_date(self, P):
        if str.isdigit(P):
            page = int(P)
            self.this_page = page if 1 <= page <= self.max_page() else self.this_page
            self.fill_entry()
            return True
        else:
            self.page_now.delete(0, tk.END)
            self.page_now.insert(0, "")
            return False

    def fill_entry(self):
        self.page_now.delete(0, tk.END)
        self.page_now.insert(0, str(self.this_page))
        self.fill_page()

    def start_page(self):
        self.this_page = 1
        self.fill_entry()

    def prev_page(self):
        self.this_page -= 1 if self.this_page > 1 else 0
        self.fill_entry()

    def next_page(self):
        self.this_page = self.this_page + 1 if self.this_page < self.max_page() else self.max_page()
        self.fill_entry()

    def max_page(self) -> int:
        pass

    def last_page(self):
        pass

    def fill_page(self):
        pass

    def search(self, find):
        pass

    def add(self, width, height, title, resizable):
        pass

    def update(self, width, height, title, resizable):
        pass

    def delete(self, width, height, title, resizable):
        pass


class SupportWindow(ChildWindow):
    def __init__(self, parent, width, height, title, resizable):
        super().__init__(parent, width, height, title, resizable)
        self.grab_focus()

        self.error_x = 1

        self.frame = tk.Frame(self.window)
        self.frame.place(relx=0.1, rely=0.1, relheight=0.85, relwidth=0.8)

        self.val_text = (self.window.register(self.validate_text))
        self.val_digit = (self.window.register(self.validate_digit))

    def error(self):
        label_error = tk.Label(self.frame,
                               text=f"Ошибка(X{self.error_x})",
                               foreground=["red", "blue"][self.error_x % 2])
        label_error.place(relx=0.3, rely=0.9, relwidth=0.4)
        self.error_x += 1

    def add_field(self, *args):
        pass


class DeleteWindow(SupportWindow):
    def __init__(self, parent, width, height, title, resizable):
        super().__init__(parent, width, height, title, resizable)

        self.frame.place(relx=0.2, rely=0.2, relheight=0.9, relwidth=0.9)

        self.label_id = tk.Label(self.frame, text="ID:")

        self.textbox_id = ttk.Entry(self.frame,
                                    validate="key",
                                    validatecommand=(self.val_digit, "%S"))

        self.button_del = tk.Button(self.frame,
                                        text="Удалить",
                                        command=lambda: self.delete_field(self.textbox_id.get()))

        self.label_id.grid(row=0, column=0, sticky=tk.E)
        self.textbox_id.grid(row=0, column=1)
        self.button_del.grid(row=1, column=0, columnspan=2, pady=8)

    def delete_field(self, id):
        pass



def create_table(frame, columns):
    table = ttk.Treeview(frame, show="headings")
    scroll_pane = ttk.Scrollbar(frame, command=table.yview)
    table.configure(yscrollcommand=scroll_pane.set)
    table['columns'] = columns
    for i in columns:
        table.heading(i, text=i, anchor="center")
    return table, scroll_pane
