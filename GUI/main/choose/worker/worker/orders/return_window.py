from Base.windows import *


class ReturnOrderWindow(DeleteWindow):
    def __init__(self, parent, width, height, title, resizable):
        super().__init__(parent, width, height, title, resizable)

        self.label_book_id = tk.Label(self.frame, text="ID книги:")

        self.label_id.configure(text="ID клиента:")

        self.textbox_book_id = ttk.Entry(self.frame,
                                         validate="key",
                                         validatecommand=(self.val_digit, "%S"))

        self.button_return = self.button_del
        self.button_return.configure(text="Возврат",
                                     command=lambda: self.returned(self.textbox_id.get(),
                                                                   self.textbox_book_id.get()))

        self.label_id.grid(row=0, column=0, sticky=tk.E, pady=5)
        self.textbox_id.grid(row=0, column=1, pady=5)
        self.label_book_id.grid(row=1, column=0, sticky=tk.E, pady=5)
        self.textbox_book_id.grid(row=1, column=1, pady=5)
        self.button_return.grid(row=2, column=0, columnspan=2, pady=5)

    def returned(self, client_id, book_id):
        if not client_id or not book_id :
            return
        try:
            DataBase.Orders.returned(client_id, book_id)
        finally:
            self.window.destroy()
