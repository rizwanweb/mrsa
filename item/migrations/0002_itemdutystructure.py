# Generated by Django 3.2.8 on 2021-10-18 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemDutyStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customeDutyRate', models.FloatField()),
                ('customDuty', models.FloatField()),
                ('rdRate', models.FloatField()),
                ('rd', models.FloatField()),
                ('acdRate', models.FloatField()),
                ('acd', models.FloatField()),
                ('stRate', models.FloatField()),
                ('salesTax', models.FloatField()),
                ('itRate', models.FloatField()),
                ('incomeTax', models.FloatField()),
                ('fed', models.FloatField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.item')),
            ],
        ),
    ]
