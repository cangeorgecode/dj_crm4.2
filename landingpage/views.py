from django.shortcuts import render, redirect
from .forms import AddLeadForm

def index(request):
    form = AddLeadForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'landingpage/index.html', {'form': form})
