from django.shortcuts import render

def home(request):
    #return HttpResponse("hello home page")
     return render(request, 'home.html')
    
    
def about(request):
    #return HttpResponse("hello about page")
    return render(request, "about.html")