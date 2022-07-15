from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='blog_images/')
    text = models.TextField(max_length=10000000)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('date',)
        verbose_name = 'article'
        verbose_name_plural = 'Articles'

    def get_summary(self):
        return self.text[:150]

    def __str__(self):
        return self.title
