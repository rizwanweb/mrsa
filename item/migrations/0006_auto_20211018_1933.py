# Generated by Django 3.2.8 on 2021-10-18 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_auto_20211018_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemdutystructure',
            name='acdType',
            field=models.CharField(choices=[('%', '%'), ('F', 'F')], default='%', max_length=5),
        ),
        migrations.AlterField(
            model_name='itemdutystructure',
            name='cdType',
            field=models.CharField(choices=[('%', '%'), ('F', 'F')], default='F', max_length=5),
        ),
    ]
