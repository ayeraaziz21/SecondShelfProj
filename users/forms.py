from django import forms   #for making HTML forms in Python
from django.contrib.auth.models import User
# importing pre-built Django forms we're customizing later:
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm 

#This file defines all the HTML forms related to user management:
# Login form
# Register form
# Edit profile form
# Change password form
# Password reset forms (for “Forgot Password”)
# (Each form controls input validation and styling of fields)


# Login form
# Displays two input boxes: username + password
# Adds placeholders and CSS classes for styling (class="box")
class login_form(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={"class":"box","placeholder":"Enter your username"}),
        label="Username"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class":"box","placeholder":"Enter your password"}),
        label="Password"
    )

    #validation
    #This checks whether the entered username exists in the database.
    #If not, Django will display an error message on the form.
    #These clean_...() methods are special Django hooks that run automatically when you call form.is_valid()
    def clean_user_name(self):
        username = self.cleaned_data.get("user_name")
        username_is_exist = User.objects.filter(username=username).exists()
        if username_is_exist:
            return username
        raise forms.ValidationError("Username does not exist")
    
#helper widget that changes the input type to a date picker
#can reuse it in other forms (e.g. for book publishing date) later
class dateInput(forms.DateTimeInput):
    input_type = 'date'

#register form: handles user sign-up.
class register_form(forms.Form):
    #textboxes
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your username"}),
        
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter your email"}),
        
    )
    #password boxes
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter your password"}),
        
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter your password again"}),
        
    )
    #These clean_...() methods are special Django hooks that run automatically when you call form.is_valid().
    #Email must be unique
    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_is_exist = User.objects.filter(email=email).exists()
        if email_is_exist:
            raise forms.ValidationError("Email exists")
        return email
    
    #Username must be unique
    def clean_user_name(self):
        username = self.cleaned_data.get("user_name")
        username_is_exist = User.objects.filter(username=username).exists()
        if username_is_exist:
            raise forms.ValidationError("Username exists")
        return username
    
    #Passwords must match
    def clean_re_password(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")

        if not password or not re_password:
            raise forms.ValidationError("Both password fields are required")

        if password != re_password:
            raise forms.ValidationError("Passwords does not match")
        
        return password

#This form is used for editing profile info (inside the user account page).
class editRegisterForm(forms.Form):
    
    profile_pic = forms.ImageField(
        widget=forms.FileInput(attrs={"id":"file"}),
        required=False
    )
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your username"}),
        
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter your email","style":"text-transform:lowercase"}),
        
    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your city"}),
        required=False
    )
    address = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your address"}),
        required=False
    )
    CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=CHOICES, 
        
    )
    phone_num = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your phone number"}),
        required=False
    )
    whatsapp_num = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your whatsapp number"}),
        required=False
    )
    
    # methods to validate uniqueness handled by view so not needed here
    # def clean_user_name(self):
    #     username = self.cleaned_data.get('user_name', '')

    #     try:
    #         user = User.objects.get(username__iexact=username)
    #         if(user):
    #             raise forms.ValidationError("This username is already exist")
    #     except User.DoesNotExist:
    #         return username

    # def clean_user_name(self):
    #     username = self.cleaned_data.get("user_name")
    #     username_is_exist = User.objects.filter(username=username).exists()
    #     if username_is_exist:
    #         raise forms.ValidationError("This username is already exist")
    #     return username

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     email_is_exist = User.objects.filter(email=email).exists()
    #     if email_is_exist:
    #         raise forms.ValidationError("This email is already exist")
    #     return email


#This is just a styling override for Django’s built-in password change form(that we imported at start)
#it adds Bootstrap classes so it looks nice on the front-end
class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['old_password', 'new_password1', 'new_password2']:
            self.fields[fieldname].widget.attrs = {'class': 'form-control w-50'}

#reusable mixin that applies Bootstrap styles to multiple forms
#This allows you to inherit it in other forms (like MyResetPassForm and MySetPassForm) to quickly add styles.
class bootstrapStyleMixin:
    field_names = None 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.field_names:
            for fieldname in self.field_names:
                self.fields[fieldname].widget.attrs = {'class': 'form-control'}
        
        else:
            raise ValueError('The field names must be set')


#these classes are for password reset via email (Forgot Password flow)
#They both inherit from Django’s built-in password forms
#but get their CSS styling from bootstrapStyleMixin
class MyResetPassForm(bootstrapStyleMixin, PasswordResetForm):
    field_names = ['email']
    
class MySetPassForm(bootstrapStyleMixin, SetPasswordForm):
    field_names = ['new_password1', 'new_password2']