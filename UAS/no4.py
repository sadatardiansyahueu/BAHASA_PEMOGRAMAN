import mysql.connector
# koneksi ke database
cnx = mysql.connector(user='username', password='password', host='host', database='database_name')



# membuat cursor
cursor = cnx.cursor()



# mengeksekusi perintah SQL
cursor.execute("SELECT * FROM table_name")



# mengambil data dari database
data = cursor.fetchall()



# menampilkan data
for row in data:
    print(row)
    


# menutup koneksi
cnx.close()

