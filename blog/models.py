from django.db import models
from accounts.models import Profile

class category(models.Model):
    name = models.CharField(max_length =100 ,unique=True)
    
    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200)
    image =models.ImageField(upload_to='blog_images/',blank=True,null=True)
    category =models.ForeignKey(category,on_delete=models.CASCADE)
    summary = models.TextField()
    content = models.TextField()
    is_draft = models.BooleanField(default =False)
    author =models.ForeignKey(Profile,on_delete=models.CASCADE,related_name ='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def short_summary(self):
        words = self.summary.split()
        return ' '.join(words[0:15])+('...' if len(words)>15 else '')
    
    def __str__(self):
        return self.title