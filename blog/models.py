from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# class = table
# attributes = fields
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)#if user is deleted, their post is also deleted
    image = models.ImageField(default='post-default.jpg',upload_to='post_images')
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    # def save(self, *args, **kwargs):
    #     super(Post, self).save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     #resizing image if its too large
    #     if img.height > 500 or img.width > 1000:
    #         output_size = (500, 1000)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
