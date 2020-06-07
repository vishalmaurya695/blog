from django.shortcuts import render
from .models import *

# Create your views here.

def index (request):
	posts = post.objects
	return render(request,'index.html',{'post':posts})



def posts(request):
	posts = post.objects(get,id=pk_s)

	return render(request, 'post.html')


def postactive (request, pk_id):
	posts = post.objects.get(id=pk_id)
	comment = comments.objects.filter(post=pk_id)
	
	return render(request,'post.html', {'comments':comment, 'post':posts })