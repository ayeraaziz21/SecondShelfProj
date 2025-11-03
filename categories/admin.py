from django.contrib import admin  # Import Django's built-in admin interface tools
from .models import bookCategory # Import your model (from the same app)
#when importing within the same app, we use .models  (instead of categories.models)
#we only do categories.models when  importing it from another app

# Create a custom admin class for your model
#This class customizes how the 'bookCategory' model is displayed in the Django Admin interface
class bookCategoryAdmin(admin.ModelAdmin):
    # 'list_display' defines which fields appear in the list view in /admin
    # Here, we're showing the string representation of each object.
    # You can replace '__str__' with real field names like 'id', 'name', etc.
    list_display = ['__str__']

    class Meta:
        model = bookCategory

#register the model with the admin site
# This makes the model visible and manageable in Django's admin panel.
admin.site.register(bookCategory, bookCategoryAdmin)