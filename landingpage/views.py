from django.shortcuts import render, redirect
from crm.forms import AddRecordForm

def index(request):
    form = AddRecordForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'landingpage/index.html', {'form': form})
