from django.db import models  #lets us define tables
from django.db.models import Q    #for building complex queries(like “title OR description contains …”)
from django.contrib.auth.models import User  #built in Django model for users (who can add/upload books)
import os  #for working with file names and paths for images

#imports model from categories app (so books can belong to categories)
from categories.models import bookCategory

# helper function to split a file name into name and extension
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

# defines the upload path and naming format for book images
# example book with id=4, title='dune': products/4-Dune.jpg
def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"

# custom model manager for Book
# allows adding extra query functions beyond the default .objects
class productManager(models.Manager):

    # returns only books that are marked active
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    # get a single book by ID (returns None if not found)
    def get_by_id(self, book_id):
        qs = self.get_queryset().filter(id=book_id)

        if qs.count() == 1:
            return qs.first()
        return None

    # search for books by title, description, or author (case-insensitive)
    def search(self, query):
        lookup = Q(title__icontains=query) | Q(
            description__icontains=query) | Q(Author__icontains=query)
        return self.get_queryset().filter(lookup, active=True).distinct()

    # get all active books that belong to a specific category
    def get_by_category(self, category_name):
        return self.get_queryset().filter(category__title__iexact=category_name, active=True)


# defines main table to store book details (Books.book table created in db.sqlite)
class Book(models.Model):
    #link to the built-in table auth_user
    #link to the user who added the book 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 

    title = models.CharField(max_length=150)
    description = models.TextField()
    Author = models.CharField(max_length=150, null=True)
    publisher = models.CharField(max_length=150, null=True)
    language = models.CharField(max_length=150, blank=True, null=True)
    edition = models.CharField(max_length=150, blank=True, null=True)
    Date = models.DateTimeField(null=True)
    price = models.IntegerField()

    #connect each book to one or more categories
    #books_book_category (auto-created join table) created 
    #(Django automatically creates a third table to link books ↔ categories)
    category = models.ManyToManyField(bookCategory, blank=True,)    
    
    image = models.ImageField(    
        upload_to=upload_image_path, null=True, blank=True)
    active = models.BooleanField(default=True)     #control visibility
    visit_count = models.IntegerField(default=0)   #track visits

    objects = productManager() 
    #Replaces default .objects with custom manager (giving all those helper methods)
    #so now we can do:
    #Book.objects.get_active_products()
    #Book.objects.search("fiction")
    #Book.objects.get_by_category("Science Fiction") 

    def __str__(self):
        return self.title     # how the book appears in Django admin or print() ->by title

     # returns a clean URL for each book (used for detail pages)
    def get_absolute_url(self):
        return f'/books/{self.id}/{self.title.replace(" ", "-")}'
