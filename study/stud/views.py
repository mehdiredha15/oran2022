from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Room,Stade,Coor


# Create your views here.

def detail(request,pk):
    sport = Room.objects.get(id=pk)
    return render(request,'stud/detail.html',{'sport': sport})

def achat(request,pk):
    sport= Room.objects.get(id=pk)
    return render(request,'stud/achat.html',{'sport':sport})

def home(request,pk):
        ath = Room.objects.filter(category=pk)
        return render(request,'stud/PLAN.html',{'sport':ath})

def tennis(request):
    ath = Room.objects.filter(category=2)
    return render(request,'stud/PLAN.html',{'sport':ath})

def basketball(request):
    ath = Room.objects.filter(category=3)
    return render(request,'stud/PLAN.html',{'sport':ath})

def boules(request):
    ath = Room.objects.filter(category=4)
    return render(request,'stud/PLAN.html',{'sport':ath})

def boxe(request):
    ath = Room.objects.filter(category=5)
    return render(request,'stud/PLAN.html',{'sport':ath})

def football(request):
    ath = Room.objects.filter(category=6)
    return render(request,'stud/PLAN.html',{'sport':ath})

def cyclisme(request):
    ath = Room.objects.filter(category=7)
    return render(request,'stud/PLAN.html',{'sport':ath})

def natation(request):
    ath = Room.objects.filter(category=8)
    return render(request,'stud/PLAN.html',{'sport':ath})

def general(request):
    sport = Room.objects.all()
    return render(request,'stud/general.html',{'sport':sport})

def indexx(request):
    return render(request,'stud/indexx.html')

def oran(request):
    return render(request,'stud/Discover-Oran.html')

def update(request,pk):
    tickets=Stade.objects.get(id=pk)
    nb = tickets.nb_tickets -1
    return nb

def form(request,pk):
    sport = Room.objects.get(id=pk)
    return render(request,'stud/form.html',{'sport':sport})


def forum(request):
    if form.is_valid:
       form.save()
       return redirect('stud/indexx.html')
    return render(request,'stud/form.html')

def ticket(request,pk):
    sport = Room.objects.get(id=pk)
    return render(request,'stud/TICKET.html',{'sport':sport})

def planning(request):
    return render(request,'stud/PLANNING.html')