from django.db import models
from django.utils import timezone

class Post(models.Model):
      author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
      title = models.CharField(max_length=200, null=True)
      text = models.TextField()
      category = models.ManyToManyField('blog.Category', blank=True, null=True)  # Corrected reference
      image = models.FileField(blank=True, upload_to='images/')
      created_date = models.DateTimeField(default=timezone.now)
      published_date = models.DateTimeField(blank=True, null=True)

      def __str__(self):
            return self.title

class Category(models.Model):  # Moved out of the Post model class
      title = models.CharField(max_length=200)
      slug = models.SlugField(max_length=200)
      parent = models.ForeignKey('blog.Category', blank=True, null=True, on_delete=models.CASCADE)

      @staticmethod
      def list_categories():
            return Category.objects.all()

      def __str__(self):
        return self.title
