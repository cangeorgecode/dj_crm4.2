from django.shortcuts import render
from dotenv import load_dotenv
from mailjet_rest import Client
import os
from crm.models import Record

load_dotenv()

MJ_API_KEY = os.environ['MJ_APIKEY_PUBLIC']
MJ_API_SECRET = os.environ['MJ_APIKEY_PRIVATE']
mailjet = Client(auth=(MJ_API_KEY, MJ_API_SECRET), version='v3.1')

def index(request):
    records = Record.objects.filter(ratings__gte=75)
    return render(request, 'sendmail/index.html', {'records': records})

# get a list of the email to send email to
# plug each email into mailjet template
# plug the corresponding receiptient's name 
# run the function somewhere in django
