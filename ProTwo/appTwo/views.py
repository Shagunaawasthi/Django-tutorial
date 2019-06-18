from django.shortcuts import render
from appTwo.models import User
#from django.http import HttpResponse

#earlier we had HttpResponse now we can only have render
# Create your views here.
#def index(request):
    # return HttpResponse("hola")

def index(request):
    return render(request,'appTwo/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'appTwo/users.html', context= user_dict)
