import pandas as pd
import calendar
from matplotlib import pyplot as plt
from DB.database_control import DataBase

class Analytics:
    @staticmethod
    def median_orders(month, year):
        pass

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
        plt.show()

    @staticmethod
    def median_readers(month, year):
        pass

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
        plt.show()

    @staticmethod
    def besseller(month, year):
        df = pd.DataFrame(DataBase.Books.count(month, year), columns=("name", "count"))
        print(df.max()['name'])
        print(df)
