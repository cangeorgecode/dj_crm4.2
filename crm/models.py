from django.db import models
from django.conf import settings

CHOICES = (
    ('prospect', 'prospect'),
    ('lead', 'lead'),
    ('customer', 'customer'),
    ('all', 'all'),
)

INTERACTIONS = (
    ('email', 'email'),
    ('phone', 'phone'),
    ('meeting', 'meeting'),
)

DEALS = (
    ('won', 'won'), 
    ('lost', 'lost'),
    ('wip', 'wip'),
    ('interested', 'interested'),
)

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=50)
    biz_name = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(max_length=50, choices=CHOICES, default="prospect", null=True, blank=True)
    ratings = models.IntegerField(null=True, blank=True)
    notes = models.TextField(max_length=1000, null=True, blank=True)
    deal = models.CharField(max_length=50, choices=DEALS, default="wip", null=True, blank=True)
    deal_close_date = models.DateField(null=True, blank=True)
    expected_revenue = models.IntegerField(null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return(f"{self.full_name}")

class Todos(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    todos = models.TextField(max_length=1000, null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Todos"

    def __str__(self):
        return(f"{self.user_id}")

class Interaction(models.Model):
    interaction_date = models.DateField(null=True, blank=True)
    interaction_type = models.CharField(max_length=100, choices=INTERACTIONS, default="email")
    notes = models.CharField(max_length=255)
    follow_up = models.CharField(max_length=255)
    client_id = models.IntegerField()

    def __str__(self):
        return(f"{self.interaction_date, self.notes}")

class Transaction(models.Model):
    transaction_date = models.DateField(auto_now_add=True)
    client_id = models.IntegerField()
    service = models.CharField(max_length=100)
    amount = models.FloatField()

    def __str__(self):
        return(f"{self.transaction_date, self.service, self.amount}")