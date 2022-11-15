import pandas as pd
import calendar
from matplotlib import pyplot as plt
from DB.database_control import DataBase

class Analytics:
    @staticmethod
    def median_orders(month, year):
        return sum(int(i[1]) for i in DataBase.Orders.new_orders(month, year)) / calendar.monthrange(year, month)[1]

    @staticmethod
    def new_orders(month, year):
        mon = {1: 0}
        for i in range(1, calendar.monthrange(year, month)[1] + 1):
            mon[i] = 0
        for i in DataBase.Orders.new_orders(month, year):
            key = str(i[0])
            key = int(key[len(key) - 2:])
            value = i[1]
            mon[key] = value
        series = pd.Series(mon)
        series.plot()
        plt.text(25, series.max(), "Всего: " + str(series.sum()), fontsize=15, bbox=dict(boxstyle="square, pad=0.5"))
        plt.xlabel("Дни")
        plt.ylabel("Заказы")
        plt.show()

    @staticmethod
    def median_readers(month, year):
        return sum(int(i[1]) for i in DataBase.Clients.new_clients(month, year)) / calendar.monthrange(year, month)[1]

    @staticmethod
    def new_readers(month, year):
        mon = {1: 0}
        for i in range(1, calendar.monthrange(year, month)[1] + 1):
            mon[i] = 0
        for i in DataBase.Clients.new_clients(month, year):
            key = str(i[0])
            key = int(key[len(key) - 2:])
            value = i[1]
            mon[key] = value
        series = pd.Series(mon)
        series.plot()
        plt.text(25, series.max(), "Всего: " + str(series.sum()), fontsize=15, bbox=dict(boxstyle="square, pad=0.5"))
        plt.xlabel("Дни")
        plt.ylabel("Читатели")
        plt.show()

    @staticmethod
    def bestseller(month, year):
        df = pd.DataFrame(DataBase.Books.count(month, year), columns=("name", "count"))
        return tuple(i for i in df.max())

    @staticmethod
    def db_to_excel(path:str):
        tables = DataBase.get_tables()
        for i in tables:
            pd.DataFrame(tables[i]).to_excel(f"{path}/{i}.xlsx", sheet_name=i)
