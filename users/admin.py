from django.contrib import admin
from django.contrib.auth.admin import UserAdmin #import the default UserAdmin class (so we can extend it)
from django.contrib.auth.models import User, Group # Import the default User and Group models
from users.models import user_profile # Import your custom user profile model

# Remove the 'Group' model from the admin site
# This hides the default "Groups" section (not needed if you don’t use permissions/groups)
admin.site.unregister(Group)

#Define an inline admin for the user_profile model (Define what to show inline)
# This makes the 'user_profile' (profile info) appear directly inside the User page in the admin panel.
# So when you edit a User in /admin, you'll also see and edit their profile fields on the same page
# instead of going to a separate 'user_profile' section.
class accountInline(admin.StackedInline):
  model = user_profile  # Link to your related profile model
  can_delete = False # Prevent deleting the inline profile from admin
  verbose_name_plural = "Accounts"  # Custom plural label in the admin UI

# Create a custom admin class for the User model (Attach it to the User page)
#class accountInLine defines the rules for displaying the profile,
#and class customUserAdmin connects it to the User admin page
class customUserAdmin(UserAdmin):
  inlines = (accountInline, )

#Re-register the User model using your custom admin
# Django already registers the default User model by default,
# so we first unregister it, then re-register it with our custom admin.
admin.site.unregister(User)
admin.site.register(User, customUserAdmin)

# Optional:
# You could register user_profile separately if you want it to appear
# as its own standalone section in the admin site as well:
# admin.site.register(user_profile)

