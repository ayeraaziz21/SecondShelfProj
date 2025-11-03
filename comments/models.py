from django.db import models
from django.contrib.auth.models import User #built-in Django user mode
from books.models import Book
#imported from your books app, so each comment can be linked to a specific book.

#defines a db table called comments_comments (its named like: appname_model name)
class Comments(models.Model):
  # link each comment to the user who wrote it
  #on_delete=models.CASCADE: if the user or book is deleted, all their comments are deleted too.
  user = models.ForeignKey(User, on_delete=models.CASCADE,)
  #link each comment to a specific book
  book = models.ForeignKey(Book, on_delete=models.CASCADE,)
  comment = models.TextField()  #actual text contents
  date = models.DateTimeField(null=True)    # date/time the comment was made (can be null)

  class Meta:
        # names used for admin panel display
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
    
  # what to show when a comment object is shown in admin or printed
  def __str__(self):
        return str(self.user.username)
