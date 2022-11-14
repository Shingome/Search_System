from Base.windows import *


class AddOrderWindow(SupportWindow):
    def __init__(self, parent, width, height, title, resizable):
        super().__init__(parent, width, height, title, resizable)

        self.label_book_id = tk.Label(self.frame, text="ID книги:")
        self.label_client_id = tk.Label(self.frame, text="ID клиента:")

        self.textbox_book_id = ttk.Entry(self.frame,
                                    validate="key",
                                    validatecommand=(self.val_digit, '%P'))
        self.textbox_client_id = ttk.Entry(self.frame,
                                      validate="key",
                                      validatecommand=(self.val_digit, '%P'))

        self.button_add = tk.Button(self.frame,
                                    text="Создать",
                                    command=lambda: self.add_field(self.textbox_book_id.get(),
                                                                   self.textbox_client_id.get()))

        self.label_book_id.grid(row=0, column=0, sticky=tk.E)
        self.label_client_id.grid(row=1, column=0, sticky=tk.E)

        self.textbox_book_id.grid(row=0, column=1, padx=5, pady=5)
        self.textbox_client_id.grid(row=1, column=1, padx=5, pady=5)

        self.button_add.grid(row=3, columnspan=2, pady=10)

    def add_field(self, *args):
        try:
            DataBase.Orders.add(*args)
        except:
            self.error()
            return
        self.window.destroy()

    def error(self):
        label_error = tk.Label(self.frame,
                               text=f"Ошибка(X{self.error_x})",
                               foreground=["red", "blue"][self.error_x % 2])
        label_error.grid(row=4, columnspan=2)
        self.error_x += 1
