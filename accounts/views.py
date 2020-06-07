from django.shortcuts import render
from django.http import HttpResponse
from posts.models import audienceuser

# Create your views here.
def register(request):
	return render(request,'account.html')


def registeraudience(request):
	return HttpResponse(request,'registered')