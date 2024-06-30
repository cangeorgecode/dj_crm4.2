from django.shortcuts import render, redirect
from .forms import AddLeadForm

def landing(request):
    form = AddLeadForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('landing')
    return render(request, 'landingpage/landing.html', {'form': form})
