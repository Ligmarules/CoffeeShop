# from django.shortcuts import redirect, render
# from django.http import HttpResponse
# from django.contrib.auth import authenticate, at
# from operator import attrgetter
# from coffee.models import Coffee
# from coffee.views import get_blog_queryset



# def home_screen_view(request):
#     context = {}
    
#     query =""
#     if request.GET:
#         query = request.GET['q']
#         context["query"] = str(query)
        
#     else:
#         return HttpResponse("Not Found")
#     blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)
#     context['blog_posts'] = blog_posts
    
#     return render(request, "coffee/home.html", context)
    
