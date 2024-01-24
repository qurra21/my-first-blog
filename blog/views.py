from django.shortcuts import render



# request the info form the model you create before
# then pass it to template
# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})