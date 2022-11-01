import mysql.connector


# def save(func):
#     def saved(*args, **kwargs):
#         print(args, kwargs)
#         print(*args, sep="\n")
#         func(1, *args, *kwargs)
#         DataBase.database.commit()
#     return saved


class DataBase:
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="WNlrlrQ932MQj6Il0tJvheqnk1D?#|yfdwa~Hts",
        database="DB"
    )

    cursor = database.cursor(buffered=True)

    @staticmethod
    def execute(request):
        return DataBase.cursor.execute(request)

    class Clients:

        # @save
        @staticmethod
        def add(fname, sname, adress, phone):
            def generate_card_id(client_id):
                import time
                return client_id + int(time.strftime("%m%d"))

            def max_index():
                DataBase.cursor.execute("SELECT max(client_id) FROM clients")
                index = (i for i in DataBase.cursor)
                print(index)
                exit()
                return DataBase.cursor

            client_id = max_index() + 1 if max_index() is not None else 1

            print(max_index())

            card_id = generate_card_id(client_id)

            request = f"INSERT INTO clients" \
                      f" VALUES ({client_id}, {card_id}, {fname}, {sname}, {adress}, {phone})"

            DataBase.execute(request)

            request = f"INSERT INTO cards(card_id, client_id) " \
                      f"VALUES ({card_id}, {client_id})"

            DataBase.execute(request)

            DataBase.database.commit()

        # @save
        def change(self, client_id, fname, sname, adress, phone):
            DataBase.cursor.execute(f"UPDATE clients "
                                    f"SET fname = {fname},"
                                    f"    sname = {sname},"
                                    f"    adress = {adress},"
                                    f"    phone = {phone},"
                                    f"where client_id = {client_id}")
