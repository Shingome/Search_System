import tkinter as tk
from tkinter import ttk


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


class TableWindow(Window):
    def __init__(self, width, height, title, resizable, columns):
        super().__init__(width, height, title, resizable)
        self.window.minsize(1200, 800)

        self.this_page = 1

        self.frame_search = tk.Frame(self.window, bg='silver')
        self.frame_database = tk.Frame(self.window)
        self.frame_pagination = tk.Frame(self.window, bg="silver")

        self.frame_search.place(relx=0, rely=0, relwidth=1, relheight=0.05)
        self.frame_pagination.place(relx=0.5, rely=0, relwidth=1, relheight=0.05)
        self.frame_database.place(relx=0, rely=0.05, relwidth=1, relheight=0.95)

        self.textbox_search = ttk.Entry(self.frame_search)
        self.button_search = tk.Button(self.frame_search, text="Поиск", command=lambda: self.search())
        self.textbox_search.grid(row=0, column=0, padx=20, ipadx=150, sticky="w", pady=12)
        self.button_search.grid(row=0, column=1, padx=10, sticky="w")

        self.page_prev = tk.Button(self.frame_pagination, text="<")
        self.page_start = tk.Button(self.frame_pagination, text="start")
        self.page_now = ttk.Entry(self.frame_pagination, width=6,
                                  justify='center',
                                  validate="focusout",
                                  validatecommand=self.update_date)
        self.page_end = tk.Button(self.frame_pagination, text="end")
        self.page_next = tk.Button(self.frame_pagination, text=">")

        self.page_prev.grid(row=0, column=0, ipadx=15, ipady=2.5, pady=5)
        self.page_start.grid(row=0, column=1, ipadx=15, ipady=2.5, pady=5)
        self.page_now.grid(row=0, column=2, ipadx=1, ipady=2.5, pady=5, padx=2)
        self.page_end.grid(row=0, column=3, ipadx=15, ipady=2.5, pady=5)
        self.page_next.grid(row=0, column=4, ipadx=15, ipady=2.5, pady=5)

        self.textbox_search = ttk.Entry(self.frame_search)
        self.button_search = tk.Button(self.frame_search, text="Поиск", command=lambda: self.search())
        self.textbox_search.grid(row=0, column=0, padx=20, ipadx=150, sticky="w", pady=12)
        self.button_search.grid(row=0, column=1, padx=10, sticky="w")

        self.table, self.scroll_pane = create_table(self.frame_database, columns)

        self.scroll_pane.pack(side=tk.RIGHT, fill=tk.Y)
        self.table.pack(expand=tk.YES, fill=tk.BOTH, side=tk.TOP)

    def update_date(self):
        pass

    def check_page(self):
        pass

    def search(self):
        pass


def create_table(frame, columns):
    table = ttk.Treeview(frame, show="headings")
    scroll_pane = ttk.Scrollbar(frame, command=table.yview)
    table.configure(yscrollcommand=scroll_pane.set)
    table['columns'] = columns
    for i in columns:
        table.heading(i, text=i, anchor="center")
    return table, scroll_pane
