from django.shortcuts import render, redirect
from .models import Record, Interaction
from .forms import AddRecordForm, AddInteractions
from django.db.models import Sum
from datetime import datetime, timedelta, date

current_date = date.today()
past_date = current_date - timedelta(days=7)

def index(request):
    records = Record.objects.all()
    interactions = Interaction.objects.filter(interaction_date__range=(past_date, current_date))
    return render(request, 'crm/index.html', {
        'records': records,
        'interactions': interactions,
        })

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

def client_interactions(request, pk):
    record = Record.objects.get(id=pk)
    form = AddInteractions(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect('table')
    return render(request, 'crm/interactions.html', {
        'form': form,
        'record': record,
        })

def reporting(request):
    total_revenue = Record.objects.aggregate(s=Sum("expected_revenue"))["s"]
    total_revenue = f"{total_revenue:,.2f}"

    revenue_won_jan = Record.objects.filter(deal="won").filter(deal_close_date__month='01').aggregate(s=Sum("expected_revenue"))["s"]
    if str(revenue_won_jan) == "None":
        revenue_won_jan = 0

    revenue_won_feb = Record.objects.filter(deal="won").filter(deal_close_date__month='02').aggregate(s=Sum("expected_revenue"))["s"]
    if str(revenue_won_feb) == "None":
        revenue_won_feb = 0

    revenue_won_mar = Record.objects.filter(deal="won").filter(deal_close_date__month='03').aggregate(s=Sum("expected_revenue"))["s"]
    if str(revenue_won_mar) == "None":
        revenue_won_mar = 0
    
    revenue_won_apr = Record.objects.filter(deal="won").filter(deal_close_date__month='04').aggregate(s=Sum("expected_revenue"))["s"]
    if str(revenue_won_apr) == "None":
        revenue_won_apr = 0

    revenue_won_may = Record.objects.filter(deal="won").filter(deal_close_date__month='05').aggregate(s=Sum("expected_revenue"))["s"]
    if str(revenue_won_may) == "None":
        revenue_won_may = 0

    revenue_won_jun = Record.objects.filter(deal="won").filter(deal_close_date__month='06').aggregate(s=Sum("expected_revenue"))["s"]
    if str(revenue_won_jun) == "None":
        revenue_won_jun = 0

    revenue_won_jul = Record.objects.filter(deal="won").filter(deal_close_date__month='07').aggregate(s=Sum("expected_revenue"))["s"]
    if str(revenue_won_jul) == "None":
        revenue_won_jul = 0

    revenue_won_aug = Record.objects.filter(deal="won").filter(deal_close_date__month='08').aggregate(s=Sum("expected_revenue"))["s"]
    if str(revenue_won_aug) == "None":
        revenue_won_aug = 0

    revenue_won_sep = Record.objects.filter(deal="won").filter(deal_close_date__month='09').aggregate(s=Sum("expected_revenue"))["s"]
    if str(revenue_won_sep) == "None":
        revenue_won_sep = 0

    revenue_won_oct = Record.objects.filter(deal="won").filter(deal_close_date__month='10').aggregate(s=Sum("expected_revenue"))["s"]
    if str(revenue_won_oct) == "None":
        revenue_won_oct = 0

    revenue_won_nov = Record.objects.filter(deal="won").filter(deal_close_date__month='11').aggregate(s=Sum("expected_revenue"))["s"]
    if str(revenue_won_nov) == "None":
        revenue_won_nov = 0

    revenue_won_dec = Record.objects.filter(deal="won").filter(deal_close_date__month='12').aggregate(s=Sum("expected_revenue"))["s"]
    if str(revenue_won_dec) == "None":
        revenue_won_dec = 0

    case_won = Record.objects.filter(deal="won").count()
    case_loss = Record.objects.filter(deal="lost").count()
    case_wip = Record.objects.filter(deal="wip").count()
    return render(request, 'crm/reporting.html', {
        'total_revenue': total_revenue,
        'case_won': case_won,
        'case_loss': case_loss,
        'case_wip': case_wip,
        'revenue_won_jan': revenue_won_jan,
        'revenue_won_feb': revenue_won_feb,
        'revenue_won_mar': revenue_won_mar,
        'revenue_won_apr': revenue_won_apr,
        'revenue_won_may': revenue_won_may,
        'revenue_won_jun': revenue_won_jun,
        'revenue_won_jul': revenue_won_jul,
        'revenue_won_aug': revenue_won_aug,
        'revenue_won_sep': revenue_won_sep,
        'revenue_won_oct': revenue_won_oct,
        'revenue_won_nov': revenue_won_nov,
        'revenue_won_dec': revenue_won_dec,
    })
