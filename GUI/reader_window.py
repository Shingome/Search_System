from windows import *


class ReaderWindow(TableWindow):
    def __init__(self, width, height, title, resizable):
        super().__init__(width, height, title, resizable, ['name', 'author', 'publish', 'year', 'pages'])

        frame_request = tk.Frame(self.window, bg="silver")
        frame_request.place(relx=0.75, relwidth=0.25, relheight=0.05)

        button_request = tk.Button(frame_request, text="Не нашел книгу?", command=lambda: self.open_request())
        button_request.pack(side=tk.RIGHT, padx=30)

        books = ((i, i, i, i, i) for i in range(100))
        for i in books:
            self.table.insert('', tk.END, values=i)

    def open_request(self, width=200, height=200, title="Работник", resizable=(False, False)):
        pass
