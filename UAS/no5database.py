import mysql.connector



# Fungsi untuk menampilkan semua data dari tabel 'employees'
def show_employees():
    # Koneksi ke database
    cnx = mysql.connector.connect(user='username', password='password', host='host', database='database_name')
    cursor = cnx.cursor()



    # Eksekusi perintah SQL
    cursor.execute("SELECT * FROM employees")



    # Ambil semua data dari tabel 'employees'
    data = cursor.fetchall()



    # Tampilkan data
    print("ID\tNama\t\tGaji")
    print("---------------------------------")
    for row in data:
        print(row[0], "\t", row[1], "\t", row[2])



    # Tutup koneksi
    cnx.close()



# Fungsi untuk menambahkan data karyawan baru ke tabel 'employees'
def add_employee(name, salary):
    # Koneksi ke database
    cnx = mysql.connector.connect(user='username', password='password', host='host', database='database_name')
    cursor = cnx.cursor()



    # Eksekusi perintah SQL
    cursor.execute("INSERT INTO employees (name, salary) VALUES (%s, %s)", (name, salary))



    # Commit perubahan
    cnx.commit()



    # Tampilkan pesan berhasil
    print("Data karyawan berhasil ditambahkan.")



    # Tutup koneksi
    cnx.close()



# Panggil fungsi show_employees()
show_employees()



# Tambahkan data karyawan baru
add_employee("SADAT ARDIANSYAH", 5000000)



# Tampilkan data karyawan kembali
show_employees()