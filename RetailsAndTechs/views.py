from django.shortcuts import render, redirect, get_object_or_404
from .models import Retailer, Technician
from .forms import RetailerForm, TechnicianForm, RatingForm

def add_retailer(request):
    if request.method == 'POST':
        form = RetailerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_retailers')
    else:
        form = RetailerForm()
    return render(request, 'add_retailer.html', {'form': form})

def add_technician(request):
    if request.method == 'POST':
        form = TechnicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_technicians')
    else:
        form = TechnicianForm()
    return render(request, 'add_technician.html', {'form': form})

def rate_retailer(request, retailer_id):
    retailer = get_object_or_404(Retailer, id=retailer_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.retailer = retailer
            rating.save()
            return redirect('list_retailers')
    else:
        form = RatingForm()
    return render(request, 'rate_retailer.html', {'form': form, 'retailer': retailer})

def rate_technician(request, technician_id):
    technician = get_object_or_404(Technician, id=technician_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.technician = technician
            rating.save()
            return redirect('list_technicians')
    else:
        form = RatingForm()
    return render(request, 'rate_technician.html', {'form': form, 'technician': technician})

def list_retailers(request):
    retailers = Retailer.objects.all()
    return render(request, 'list_retailers.html', {'retailers': retailers})

def list_technicians(request):
    technicians = Technician.objects.all()
    return render(request, 'list_technicians.html', {'technicians': technicians})
