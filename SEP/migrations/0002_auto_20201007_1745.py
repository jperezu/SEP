# Generated by Django 3.1.2 on 2020-10-07 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SEP', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventrequest',
            old_name='client_id',
            new_name='client',
        ),
    ]
