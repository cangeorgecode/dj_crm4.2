# Generated by Django 5.0.6 on 2024-06-30 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_record_deal_record_expected_revenue'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='deal_close_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
