from django.db import models

# Create your models here.

class Column(models.Model):
	title = models.CharField(max_length=50)
	def __unicode__(self):
		return self.title

class News(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	column = models.ForeignKey(Column, default='')
	counter = models.IntegerField(default=0)
	pubDate = models.DateField(auto_now_add=True)
	author = models.CharField(max_length=60)
	def __unicode__(self):
		return self.title
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=3)

class Photo(models.Model):
	title = models.CharField(max_length=50)
	content = models.CharField(max_length=50)
	column = models.ForeignKey(Column, default='')
	photo = models.ImageField(upload_to='photos')
	def __unicode__(self):  
		return self.title