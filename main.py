from book import Book
import datetime

buku1 = Book(1, "Belajar Python", "Affan", 2025)
buku2 = Book(2, "belajar java", "dika", 2026)

print(buku1.judul)
print(buku1.get_update_treakhir())

buku1.update_judul("belajar python part 1")

print(buku1.judul)
print(buku1.get_update_treakhir())


