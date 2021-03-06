from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=101)
    desc = models.CharField(max_length=250)
    image = models.ImageField(upload_to="portfolio/images/",blank=True,default='portfolio/images/portfolio_header.jpg')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title