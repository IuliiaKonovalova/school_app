# Generated by Django 3.2.3 on 2022-03-11 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_alter_salesmanager_id'),
        ('students', '0007_auto_20220310_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='sales_manager',
        ),
        migrations.AddField(
            model_name='student',
            name='sales_manager',
            field=models.ManyToManyField(related_name='student', to='profiles.SalesManager'),
        ),
    ]