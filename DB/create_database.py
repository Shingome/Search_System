import mysql.connector

database = mysql.connector.connect(
  host="localhost",
  user="root",
  password="WNlrlrQ932MQj6Il0tJvheqnk1D?#|yfdwa~Hts",
  database="DB"
)

cursor = database.cursor()

cursor.execute("CREATE DATABASE DB")

cursor.execute("CREATE TABLE books (book_id INT PRIMARY KEY,"
               "name varchar(60),"
               "author varchar(60),"
               "publish varchar(60),"
               "year year,"
               "pages smallint)")

cursor.execute("CREATE TABLE clients (client_id INT PRIMARY KEY ,"
               "card_id INT UNIQUE,"
               "fname varchar(60),"
               "sname varchar(60),"
               "adress varchar(60),"
               "phone varchar(60))")

cursor.execute("CREATE TABLE cards (card_id INT PRIMARY KEY,"
               "client_id INT UNIQUE,"
               "registration DATETIME NOT NULL DEFAULT NOW(),"
               "FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE SET NULL)")

cursor.execute("CREATE TABLE orders (order_id INT PRIMARY KEY AUTO_INCREMENT,"
               "book_id INT NOT NULL,"
               "card_id INT NOT NULL,"
               "get_date DATETIME NOT NULL DEFAULT NOW(),"
               "return_date DATETIME DEFAULT NULL,"
               "FOREIGN KEY (book_id) REFERENCES books(book_id),"
               "FOREIGN KEY (card_id) REFERENCES cards(card_id))")

cursor.execute("CREATE TABLE requests (request_id INT PRIMARY KEY AUTO_INCREMENT,"
               "card_id INT NOT NULL,"
               "name varchar(60) NOT NULL,"
               "author varchar(60) NOT NULL,"
               "registration_date DATETIME NOT NULL DEFAULT NOW(),"
               "FOREIGN KEY (card_id) REFERENCES cards(card_id))")

cursor.execute("CREATE TABLE workers (id INT PRIMARY KEY AUTO_INCREMENT, "
               "login VARCHAR(60) NOT NULL, "
               "password VARCHAR(60) NOT NULL, "
               "level INT DEFAULT 0)")

database.commit()
