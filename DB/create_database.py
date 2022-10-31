import mysql.connector

database = mysql.connector.connect(
  host="localhost",
  user="root",
  password="WNlrlrQ932MQj6Il0tJvheqnk1D?#|yfdwa~Hts",
  database="mydatabase"
)

cursor = database.cursor()

cursor.execute("CREATE DATABASE mydatabase")

cursor.execute("CREATE TABLE books (book_id INT PRIMARY KEY,"
               "name varchar(60),"
               "author varchar(60),"
               "publish varchar(60),"
               "year year,"
               "pages smallint)")

cursor.execute("CREATE TABLE cards (card_id INT PRIMARY KEY,"
               "client_id INT,"
               "fname varchar(60),"
               "registration date)")

cursor.execute("CREATE TABLE clients (client_id INT PRIMARY KEY,"
               "card_id INT NOT NULL,"
               "fname varchar(60),"
               "sname varchar(60),"
               "adress varchar(60),"
               "phone varchar(60),"
               "FOREIGN KEY (card_id) REFERENCES cards(card_id))")

cursor.execute("ALTER TABLE cards ADD FOREIGN KEY (client_id) REFERENCES clients(client_id)")

cursor.execute("CREATE TABLE orders (order_id INT PRIMARY KEY,"
               "book_id INT NOT NULL,"
               "card_id INT NOT NULL,"
               "get_date DATE NOT NULL,"
               "return_date DATE DEFAULT NULL,"
               "FOREIGN KEY (book_id) REFERENCES books(book_id),"
               "FOREIGN KEY (card_id) REFERENCES cards(card_id))")

cursor.execute("CREATE TABLE requests (request_id INT PRIMARY KEY,"
               "card_id INT NOT NULL,"
               "name varchar(60) NOT NULL,"
               "author varchar(60) NOT NULL,"
               "registration_date DATE DEFAULT NULL,"
               "FOREIGN KEY (card_id) REFERENCES cards(card_id))")

database.commit()
