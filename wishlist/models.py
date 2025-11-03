from django.db import models
from django.contrib.auth.models import User

from books.models import Book


# creates db table wishlist_wish
class Wish(models.Model):
    # links each wishlist to a specific user (1 user → many wishlists possible)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # readable name shown in admin or print()
    def __str__(self):
        return self.owner.get_username()

# creates db table wishlist_wishdetail
class wishDetail(models.Model):
    # connects to Wish table (many books per wishlist)
    wish = models.ForeignKey(Wish, on_delete=models.CASCADE)
     # connects to Book table (each entry represents a wished book)
    wishBook = models.ForeignKey(Book, on_delete=models.CASCADE)
    # stores price of the wished book at the time it was added
    price = models.IntegerField()


    # readable name (shows the book title)
    def __str__(self):
        return self.wishBook.title
