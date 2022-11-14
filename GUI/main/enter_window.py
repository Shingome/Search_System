from Base.windows import *
from GUI.main.choose.reader.reader_window import ReaderWindow
from GUI.main.choose.worker.authorization import AuthorizationWindow


class EnterWindow(Window):
    def __init__(self, width, height, title="Меню", resizable=(False, False)):
        super().__init__(width, height, title, resizable)
        but_reader = tk.Button(text='Читатель', command=lambda: self.open_reader())
        but_reader.pack(side=tk.RIGHT, expand=True, padx=20, pady=20, fill=tk.BOTH)
        but_worker = tk.Button(text='Работник', command=lambda: self.authorization())
        but_worker.pack(side=tk.LEFT, expand=True, padx=20, pady=20, fill=tk.BOTH)
        self.window.mainloop()

    def open_reader(self, width=1600, height=600, title="Читатель", resizable=(True, True)):
        self.window.destroy()
        ReaderWindow(width, height, title, resizable)

    def authorization(self, width=250, height=200, title="Авторизация", resizable=(False, False)):
        AuthorizationWindow(self.window, width, height, title, resizable)


if __name__ == "__main__":
    app = EnterWindow(400, 200)
