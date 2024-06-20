from django.shortcuts import render

def index(request):
    return render(request, 'crm/index.html')

def account_profile(request):
    return render(request, 'crm/account-profile.html')

def table(request):
    return render(request, 'crm/table-datatable.html')