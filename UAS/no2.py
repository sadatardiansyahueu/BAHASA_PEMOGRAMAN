####### Contoh Penanganan Exception #######



try:
            number = int(input("Enter a number: "))
            print(50/ number)



except ZeroDivisionError:
            print("Tidak bisa dibagi dengan 0")


except ValueError:
            print("Input harus berupa angka")


