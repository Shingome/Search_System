from Base.windows import *
import time


class BestsellerWindow(LabelWindow):
    def __init__(self, parent, width, height, title, resizable):
        super().__init__(parent, width, height, title, resizable)
        month, year = time.strftime("%m %Y").split(" ")
        name, count = Analytics.bestseller(int(month), int(year))
        self.label.configure(text=f'Самая популярная книга в этом месяце'
                                  f' - \"{name}\" \n'
                                  f'Всего заказов - {str(count)}')
