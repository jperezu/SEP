# Generated by Django 3.1.2 on 2020-10-10 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SEP', '0010_requestbudget_requestrecruitment_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='department',
        ),
    ]
