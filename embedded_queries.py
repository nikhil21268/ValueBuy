import mysql.connector

# connect to a database
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MySQL2023",
  database="final_final"
)

# create a table
cursor = conn.cursor()
#cursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), age INT)")

# insert data into the table
#cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("John", 25))
#cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Mary", 30))

# select data from the table

cursor.execute("SELECT count(*) FROM product WHERE net_weight IS NOT NULL;")
result = cursor.fetchall()
for row in result:
    print(row)

cursor.execute("SELECT count(*) FROM consumables WHERE (date_of_expiry IS NOT NULL and ingredients is not null);")
result = cursor.fetchall()
for row in result:
    print(row)

cursor.execute("SELECT count(*) FROM electronics WHERE (voltage IS NOT NULL and warranty is not null);")
result = cursor.fetchall()
for row in result:
    print(row)

cursor.execute("SELECT count(*) FROM cosmetics WHERE (date_of_expiry IS NOT NULL  and composition is not null and directions_of_use is not null);")
result = cursor.fetchall()
for row in result:
    print(row)

cursor.execute("SELECT count(*) FROM clothing WHERE (category IS NOT NULL  and size is not null and type_of_clothing is not null);")
result = cursor.fetchall()
for row in result:
    print(row)


# close the connection
conn.close()
