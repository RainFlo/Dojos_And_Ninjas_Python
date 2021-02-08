from django.shortcuts import render, HttpResponse, redirect
from .models import Dojo, Ninja

# Create your views here.
def index(request):
    context = {
        'dojos': Dojo.objects.all()
    }
    return render(request, "index.html", context)


def process(request):
    if request.POST['process_type'] == 'dojo':
        Dojo.objects.create(
            name = request.POST['name'],
            city = request.POST['city'],
            state = request.POST['state']
        )
    else:
        Ninja.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            dojo = Dojo.objects.get(id=request.POST['dojo'])
        )
        print(Dojo.objects.get(id=request.POST['dojo']))
    return redirect('/')