# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44 * 2**20 # Объём дискеты в байтах
number_pages = 100
strings_on_page = 50
number_symbols_on_string = 25
count_symbols = number_pages * strings_on_page * number_symbols_on_string * 4
number_books = int((volume // count_symbols ))
print("Количество книг, помещающихся на дискету:", number_books)
