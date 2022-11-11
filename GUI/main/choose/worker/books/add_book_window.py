from Base.windows import *


class AddBookWindow(SupportWindow):
    def __init__(self, parent, width, height, title, resizable):
        super().__init__(parent, width, height, title, resizable)

        self.label_id = tk.Label(self.frame, text="ID:")
        self.label_name = tk.Label(self.frame, text="Название:")
        self.label_author = tk.Label(self.frame, text="Автор:")
        self.label_publish = tk.Label(self.frame, text="Издательство:")
        self.label_year = tk.Label(self.frame, text="Год издания:")
        self.label_pages = tk.Label(self.frame, text="Количество страниц:")

        self.textbox_id = ttk.Entry(self.frame,
                                    validate="key",
                                    validatecommand=(self.val_digit, '%P'))
        self.textbox_name = ttk.Entry(self.frame,
                                      validate="key",
                                      validatecommand=(self.val_text, '%P'))
        self.textbox_author = ttk.Entry(self.frame,
                                        validate="key",
                                        validatecommand=(self.val_text, '%P'))
        self.textbox_publish = ttk.Entry(self.frame,
                                         validate="key",
                                         validatecommand=(self.val_text, '%P'))
        self.textbox_year = ttk.Entry(self.frame,
                                      validate="key",
                                      validatecommand=(self.val_digit, '%P'))
        self.textbox_pages = ttk.Entry(self.frame,
                                       validate="key",
                                       validatecommand=(self.val_digit, '%P'))

        self.button_add = tk.Button(self.frame,
                                    text="Создать",
                                    command=lambda: self.add_field(self.textbox_id.get(),
                                                                   self.textbox_name.get(),
                                                                   self.textbox_author.get(),
                                                                   self.textbox_publish.get(),
                                                                   self.textbox_year.get(),
                                                                   self.textbox_pages.get()))

        self.label_id.grid(row=0, column=0, sticky=tk.E)
        self.label_name.grid(row=1, column=0, sticky=tk.E)
        self.label_author.grid(row=2, column=0, sticky=tk.E)
        self.label_publish.grid(row=3, column=0, sticky=tk.E)
        self.label_year.grid(row=4, column=0, sticky=tk.E)
        self.label_pages.grid(row=5, column=0, sticky=tk.E)

        self.textbox_id.grid(row=0, column=1, padx=5, pady=5)
        self.textbox_name.grid(row=1, column=1, padx=5, pady=5)
        self.textbox_author.grid(row=2, column=1, padx=5, pady=5)
        self.textbox_publish.grid(row=3, column=1, padx=5, pady=5)
        self.textbox_year.grid(row=4, column=1, padx=5, pady=5)
        self.textbox_pages.grid(row=5, column=1, padx=5, pady=5)

        self.button_add.grid(row=6, columnspan=2, pady=10)

    def add_field(self, *args):
        try:
            DataBase.Books.add(*args)
        except:
            self.error()
            return
        self.window.destroy()
