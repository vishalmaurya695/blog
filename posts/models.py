from django.db import models


# Create your models here.

class audienceuser(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(unique=True, max_length=50)
	mobile = models.CharField(max_length=13)
	password = models.CharField(max_length=20)
	profile = models.ImageField(upload_to="audience_profile", blank=True)

	def __str__(self):
		return self.name


class user(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(unique = True, max_length=80)
	mobile = models.IntegerField()
	profile = models.ImageField(upload_to='profile_pics', blank=True)
	password = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class topic (models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=500)

	def __str__(self):
		return self.name


class post(models.Model):
	title = models.CharField(max_length=200)
	topic = models.ForeignKey(topic, on_delete=models.CASCADE)
	description = models.TextField(max_length=30000)
	datepublished = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(user, on_delete=models.CASCADE)

	def __str__(self):
		return self.title


class comments(models.Model):
	user = models.ForeignKey(audienceuser, on_delete=models.CASCADE)
	post = models.ForeignKey(post, on_delete=models.CASCADE)
	commentdescription = models.TextField(max_length=1000)
	verified = models.BooleanField(default=False)
	date = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.commentdescription
