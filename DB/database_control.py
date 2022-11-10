import mysql.connector


def save(func):
    def saved(*args, **kwargs):
        func(*args, *kwargs)
        DataBase.database.commit()
    return saved

def change_string(func):
    def changed(*args):
        args = list(args)
        for i in range(len(args)):
            if type(args[i]) == str:
                args[i] = DataBase.string_to_MYSQL(args[i])
        func(*args)
    return changed


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

    @staticmethod
    def string_to_MYSQL(string):
        return "\"" + string + "\""

    class Clients:
        @staticmethod
        def max_index():
            DataBase.cursor.execute("SELECT max(client_id) FROM clients")
            index = (i for i in DataBase.cursor).__next__()[0]
            return index
        @save
        @staticmethod
        @change_string
        def add(fname, sname, adress, phone):
            def generate_card_id(client_id):
                import time
                return client_id + int(time.strftime("%m%d%y"))

            client_id = DataBase.Clients.max_index() + 1 if DataBase.Clients.max_index() is not None else 1

            card_id = generate_card_id(client_id)

            request = f"INSERT INTO clients(client_id, card_id, fname, sname, adress, phone)" \
                      f"VALUES ({client_id}, {card_id}, {fname}, {sname}, {adress}, {phone})"

            DataBase.execute(request)

            request = f"INSERT INTO cards(card_id, client_id) " \
                      f"VALUES ({card_id}, {client_id})"

            DataBase.execute(request)


        @save
        @change_string
        @staticmethod
        def update(client_id, fname, sname, adress, phone):
            request = f"UPDATE clients " \
                      f"SET fname = {fname}, sname = {sname}, adress = {adress}, phone = {phone}" \
                      f"where client_id = {client_id}"

            DataBase.cursor.execute(request)

        @save
        @staticmethod
        def delete(client_id):
            request = f"DELETE FROM clients " \
                      f"WHERE client_id = {client_id}"
            DataBase.cursor.execute(request)

            request = f"DELETE FROM cards " \
                      f"WHERE client_id = {client_id}"
            DataBase.cursor.execute(request)


        @staticmethod
        def get_info(page):
            request = f"SELECT * " \
                      f"FROM clients" \
                      f" where client_id BETWEEN {(page - 1) * 100} AND {page * 100 - 1}"
            DataBase.cursor.execute(request)
            info = (i for i in DataBase.cursor)
            return info

        @staticmethod
        def search(find):
            if not str.isdigit(find):
                request = f"SELECT * " \
                          f"FROM clients " \
                          f"WHERE (fname LIKE \"%{find}%\") OR" \
                          f"(sname LIKE \"%{find}%\") OR" \
                          f"(adress LIKE \"%{find}%\") OR" \
                          f"(phone LIKE \"{find}%\")" \
                          f"LIMIT 100"
            else:
                request = f"SELECT * " \
                          f"FROM clients " \
                          f"WHERE (client_id = {find}) OR" \
                          f"(card_id = {find}) OR" \
                          f"(fname LIKE \"%{find}%\") OR" \
                          f"(sname LIKE \"%{find}%\") OR" \
                          f"(adress LIKE \"%{find}%\") OR" \
                          f"(phone LIKE \"{find}%\")" \
                          f"LIMIT 100"
            DataBase.cursor.execute(request)
            info = (i for i in DataBase.cursor)
            return info
