from django.shortcuts import render,HttpResponse
from .form import UserForms
from django.http import HttpResponse
from .models import  Person
from django.core.exceptions import ObjectDoesNotExist

people = Person.objects.all()
print(people.query)


def getData(request):
    tom = Person.objects.create(name="Tom",age=25,photo="bbv.jpg")
    try:
        men = Person.objects.get(name="MIke")
    except ObjectDoesNotExist:
        mike = Person(name='Mike',age=15,photo='fgdh.jpg')
        mike.save()

    # people= Person.objects.all()
    people = Person.objects.exclude(name = "name1")

    return render(request,'data.html',context = {'data':people})

def index(request):
    if request.method == 'POST':
        form = UserForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            return HttpResponse(f'name:{name}')
        else:
            return HttpResponse(f'Данные не валидны')
    else:
        form = UserForms()
        return render(request,'index.html',context={'form':form})