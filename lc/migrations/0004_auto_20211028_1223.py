# Generated by Django 3.2.7 on 2021-10-28 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lc', '0003_auto_20211021_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='lc',
            name='bank',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lc',
            name='branch',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lc',
            name='pqaPayorder',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]