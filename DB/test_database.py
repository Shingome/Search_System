import mysql.connector

database = mysql.connector.connect(
  host="localhost",
  user="root",
  password="WNlrlrQ932MQj6Il0tJvheqnk1D?#|yfdwa~Hts",
  database="mydatabase"
)

cursor = database.cursor()

# cursor.execute("CREATE DATABASE mydatabase")

cursor.execute("drop table books")
# cursor.execute("drop table orders")

cursor.execute("CREATE TABLE books (book_id INT PRIMARY KEY,"
               "name varchar(60),"
               "author varchar(60),"
               "publish varchar(60),"
               "year year,"
               "pages smallint)")

cursor.execute("CREATE TABLE orders (order_id INT PRIMARY KEY,"
               "book_id INT,"
               "get_date DATE,"
               "return TINYINT(1),"
               "FOREIGN KEY (book_id) REFERENCES books (book_id)")

# cursor.execute("SHOW DATABASES")

# database.commit()

for i in cursor:
  print(i)