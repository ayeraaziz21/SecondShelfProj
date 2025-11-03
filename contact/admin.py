from django.contrib import admin
from .models import contactUs

#Define a custom admin class for the contactUs model 
# This class customizes how contactUs entries are displayed and managed in the admin panel.
class contactAdmin(admin.ModelAdmin):
    # Fields to display as columns in the list view (the table on the admin page)
    list_display = ['__str__', 'full_name', 'is_read']
     # Add a sidebar filter to filter messages by their 'is_read' status
    list_filter = ['is_read']
    # Make the 'is_read' field editable directly from the list view
    list_editable = ['is_read']
    # Allow searching through specific fields
    search_fields = ['subject', 'message']

#Register the contactUs model with the custom admin configuration ---
# his tells Django to use contactAdmin when displaying contactUs in the admin interface.
admin.site.register(contactUs, contactAdmin)