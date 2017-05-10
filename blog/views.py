from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
	#Below returns a list called posts
	#published_date is a field in our model. The '-' in front means reverse the order
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	#Here we are passing a dictionary with the key of 'posts' and the value of our created list above

	return render(request, 'blog/post_list.html', {'posts': posts})
