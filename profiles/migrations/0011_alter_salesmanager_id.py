# Generated by Django 3.2.3 on 2022-03-11 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_salesmanager_total_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesmanager',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
