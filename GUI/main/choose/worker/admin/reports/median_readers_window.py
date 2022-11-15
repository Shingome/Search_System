from Base.windows import *
import time


class MedianReadersWindow(LabelWindow):
    def __init__(self, parent, width, height, title, resizable):
        super().__init__(parent, width, height, title, resizable)
        month, year = time.strftime("%m %Y").split(" ")
        self.label.configure(text="Среднее количество зарегистрированных абонементов в этом месяце - "
                                  + str(Analytics.median_readers(int(month), int(year))))
