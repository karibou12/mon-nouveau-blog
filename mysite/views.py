from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse('Hello world')
    return render(request, 'main/index.html')



# Create your views here.
# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_list.html', {'posts': posts})
#
