# Generated by Django 3.2.8 on 2021-10-16 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lc', '0002_alter_lc_pqacharges'),
    ]

    operations = [
        migrations.CreateModel(
            name='BL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blNo', models.CharField(max_length=100)),
                ('blDate', models.DateField()),
                ('index', models.IntegerField()),
                ('quantity', models.FloatField()),
                ('insurance', models.FloatField(blank=True)),
                ('usd', models.FloatField(blank=True)),
                ('landingCharges', models.FloatField(blank=True)),
                ('importValuePKR', models.FloatField(blank=True)),
                ('whRate', models.FloatField(default=0.25)),
                ('warehousingCharges', models.FloatField(blank=True)),
                ('exciseRate', models.FloatField(default=1.25)),
                ('excise', models.FloatField(blank=True)),
                ('stampCharges', models.FloatField(blank=True)),
                ('lc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lc.lc')),
            ],
        ),
    ]
