from django.shortcuts import render
from django.http import HttpResponse
from .models import Department, Doctor
from . forms import BookingForm

def index(request):
    return render(request,"index.html")
def department(request):
    department=Department.objects.all()
    return render(request,"department.html",{'department':department})
def home(request):
    return render(request,"home.html")
def booking(request):
    form=BookingForm()
    if request.method=='POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Thank You</h1>')
    return render(request,"booking.html",{'form':form})
def doctors(request):
    doctors=Doctor.objects.all()
    return render(request,"doctors.html",{'doctors':doctors})



