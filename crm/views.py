from django.shortcuts import render, redirect
from .models import Record
from .forms import AddRecordForm

def index(request):
    records = Record.objects.all()
    return render(request, 'crm/index.html', {'records': records})

def account_profile(request):
    return render(request, 'crm/account-profile.html')

def table(request):
    records = Record.objects.all()
    return render(request, 'crm/table-datatable.html', {'records': records})

# Update and view individual client's record
def client_record(request, pk):
    record = Record.objects.get(id=pk)
    form = AddRecordForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect('table')
    return render(request, 'crm/form-layout.html', {
        'form': form,
        'record': record,
        })

def delete_record(request, pk):
    delete_record = Record.objects.get(id=pk)
    delete_record.delete()
    return redirect('table')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('table')
    else:
        return render(request, 'crm/add.html', {'form': form})
