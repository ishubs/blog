from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=20)

class images(models.Model):

	image = models.ImageField(upload_to='static/blog/images/')
	


class Post(models.Model):
	title = models.CharField(max_length=255)
	body = models.TextField()
	categories = models.ManyToManyField('category',related_name='posts')
	image = models.ImageField(upload_to='static/blog/images/')
	i = models.ManyToManyField('images', related_name='images')
	created_on = models.DateTimeField(auto_now_add=True)





class emailid(models.Model):
	email= models.EmailField()
class Comments(models.Model):
	author = models.CharField(max_length=60)
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey('Post', on_delete=models.CASCADE)
