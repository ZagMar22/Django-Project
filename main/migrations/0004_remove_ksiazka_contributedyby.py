# Generated by Django 4.1.2 on 2023-01-07 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_ksiazka'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ksiazka',
            name='contributedyby',
        ),
    ]
