from django.db import models

#creates db table contact_contactUs
class contactUs(models.Model):

    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=100) #subject line of the contact message
    message = models.TextField()
    is_read = models.BooleanField()  # marks whether the admin has read the message or not

    class Meta:
         # how the model name appears in Django admin
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
    
    #  display name in admin or print() = subject
    def __str__(self):
        return self.subject
