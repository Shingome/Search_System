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

        @staticmethod
        def check_index(client_id):
            DataBase.cursor.execute(f"SELECT COUNT(*) FROM clients WHERE client_id = {client_id}")
            index = (i for i in DataBase.cursor).__next__()[0]
            return bool(index)

        @staticmethod
        def card_from_client(client_id):
            DataBase.cursor.execute(f"SELECT card_id FROM clients WHERE client_id = {client_id}")
            index = (i for i in DataBase.cursor).__next__()[0]
            return index

        @save
        @staticmethod
        @change_string
        def add(fname, sname, adress, phone):
            def generate_card_id(client_id):
                import time
                return client_id + int(time.strftime("%m%d%M%S"))

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


        @staticmethod
        def get_info(page):
            request = f"SELECT * FROM clients ORDER BY client_id LIMIT {(page - 1) * 100}, {page * 100 - 1}"
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

    class Books:
        @staticmethod
        def check_index(book_id):
            DataBase.cursor.execute(f"SELECT COUNT(*) FROM books WHERE book_id = {book_id}")
            index = (i for i in DataBase.cursor).__next__()[0]
            return bool(index)

        @staticmethod
        def length():
            request = f"SELECT COUNT(*) FROM books"
            DataBase.execute(request)
            index = (i for i in DataBase.cursor).__next__()[0]
            return index

        @save
        @staticmethod
        @change_string
        def add(book_id, name, author, publish, year, pages):
            request = f"INSERT INTO books(book_id, name, author, publish, year, pages)" \
                      f"VALUES ({book_id}, {name}, {author}, {publish}, {year}, {pages})"

            DataBase.execute(request)


        @save
        @change_string
        @staticmethod
        def update(book_id, name, author, publish, year, pages):
            request = f"UPDATE books " \
                      f"SET book_id = {book_id}," \
                      f" name = {name}," \
                      f" author = {author}," \
                      f" publish = {publish}," \
                      f" year = {year}, " \
                      f" pages = {pages}" \
                      f"where book_id = {book_id}"

            DataBase.cursor.execute(request)

        @save
        @staticmethod
        def delete(book_id):
            request = f"DELETE FROM books " \
                      f"WHERE book_id = {book_id}"
            DataBase.cursor.execute(request)

        @staticmethod
        def get_info(page):
            request = f"SELECT * FROM books ORDER BY book_id LIMIT {(page - 1) * 100}, {page * 100 - 1}"
            DataBase.cursor.execute(request)
            info = (i for i in DataBase.cursor)
            return info

        @staticmethod
        def search(find):
            if not str.isdigit(find):
                request = f"SELECT * " \
                          f"FROM books " \
                          f"WHERE (name LIKE \"%{find}%\") OR" \
                          f"(author LIKE \"%{find}%\") OR" \
                          f"(publish LIKE \"%{find}%\")" \
                          f"LIMIT 100"
            else:
                request = f"SELECT * " \
                          f"FROM books " \
                          f"WHERE (book_id = {find}) OR" \
                          f"(year = {find}) OR" \
                          f"(name LIKE \"%{find}%\") OR" \
                          f"(author LIKE \"%{find}%\") OR" \
                          f"(publish LIKE \"%{find}%\") OR" \
                          f"(pages = {find})" \
                          f"LIMIT 100"
            DataBase.cursor.execute(request)
            info = (i for i in DataBase.cursor)
            return info

    class Requests:
        @save
        @change_string
        @staticmethod
        def add(client_id, name, author):
            request = f"INSERT INTO requests(card_id, name, author)" \
                      f"VALUES ({DataBase.Clients.card_from_client(client_id)}, {name}, {author})"

            DataBase.execute(request)

        @staticmethod
        def get_info(page):
            request = f"SELECT * FROM requests ORDER BY request_id LIMIT {(page - 1) * 100}, {page * 100 - 1}"
            DataBase.cursor.execute(request)
            info = (i for i in DataBase.cursor)
            return info

        @staticmethod
        def max_index():
            DataBase.cursor.execute("SELECT max(request_id) FROM requests")
            index = (i for i in DataBase.cursor).__next__()[0]
            return index

        @staticmethod
        def search(find):
            if not str.isdigit(find):
                request = f"SELECT * " \
                          f"FROM requests " \
                          f"WHERE (name LIKE \"%{find}%\") OR" \
                          f"(author LIKE \"%{find}%\") OR" \
                          f"(registration_date LIKE \"%{find}%\")" \
                          f"LIMIT 100"
            else:
                request = f"SELECT * " \
                          f"FROM requests " \
                          f"WHERE (request_id = {find}) OR" \
                          f"(card_id = {find}) OR" \
                          f"(name LIKE \"%{find}%\") OR" \
                          f"(author LIKE \"%{find}%\") OR" \
                          f"(registration_date LIKE \"{find}%\")" \
                          f"LIMIT 100"
            DataBase.cursor.execute(request)
            info = (i for i in DataBase.cursor)
            return info

    class Orders:
        @save
        @change_string
        @staticmethod
        def add(book_id, client_id):
            request = f"INSERT INTO orders(book_id, card_id)" \
                      f"VALUES ({book_id}, {DataBase.Clients.card_from_client(client_id)})"

            DataBase.execute(request)

        @staticmethod
        def get_info(page):
            request = f"SELECT * FROM orders ORDER BY order_id LIMIT {(page - 1) * 100}, {page * 100 - 1}"
            DataBase.cursor.execute(request)
            info = (i for i in DataBase.cursor)
            return info

        @staticmethod
        def max_index():
            DataBase.cursor.execute("SELECT max(order_id) FROM orders")
            index = (i for i in DataBase.cursor).__next__()[0]
            return index

        @staticmethod
        def search(find):
            request = f"SELECT * " \
                      f"FROM orders " \
                      f"WHERE (order_id = {find}) OR" \
                      f"(card_id = {find}) OR" \
                      f"(book_id = {find})" \
                      f"LIMIT 100"
            DataBase.cursor.execute(request)
            info = (i for i in DataBase.cursor)
            return info

