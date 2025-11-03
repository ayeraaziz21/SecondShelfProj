from django.contrib import admin
from .models import Comments

# Register the Comments model with the admin site
# This makes it visible and editable through the Django admin interface (/admin).
admin.site.register(Comments)
