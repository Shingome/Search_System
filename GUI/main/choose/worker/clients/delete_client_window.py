from Base.windows import *


class DeleteClientWindow(DeleteWindow):
    def __init__(self, parent, width, height, title, resizable):
        super().__init__(parent, width, height, title, resizable)

    def delete_field(self, id):
        try:
            DataBase.Clients.delete(id)
        finally:
            self.window.destroy()
            return
