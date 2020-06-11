from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def authpass(request):
    user=request.GET['user']
    pass1=request.GET['pass']
    if(user=='admin' and pass1=='123'):
        return render(request,'success.html')
    else:
        return render(request,'forbidden.html')    
