from django.db import models
#models lets us describe database tables as Python classes, not SQL code.

#defining a model(database table)
#class name bookCategory will become a table db (categories_bookcategory)
#It inherits from models.Model, which gives it all the database behavior (saving, updating, querying, etc.) 
class bookCategory(models.Model):
    # Django automatically adds an 'id' field (AutoField) as the primary key unless we define one ourselves                   
    title = models.CharField(max_length = 150)
    #defining a column in table, named title (in SQL, django will make field: title VARCHAR(150))

    #defines what Django should display when we print the object
    #eg in admin panel or when printed, without it we would see object reference: 'bookCategory object (1)'
    #but with it we'll see the actual book title (like 'science fiction')
    def __str__(self): 
        return self.title



#eg being used in code:
#from categories.models import bookCategory
#new_cat = bookCategory(title="Science Fiction")
#new_cat.save()
