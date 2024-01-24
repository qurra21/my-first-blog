from django.shortcuts import render
from django.utils import timezone
from .models import Post # . means current directory
# voth model.py and view.py are in the sam dir
# so can use .

def post_list(request) : 
    posts = Post.objects.filter(published_date_lte= timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})





# request the info form the model you create before
# then pass it to template
# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})