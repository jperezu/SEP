# Generated by Django 3.1.2 on 2020-10-12 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SEP', '0011_remove_task_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestbudget',
            name='status',
            field=models.CharField(default='requested', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requestrecruitment',
            name='status',
            field=models.CharField(default='requested', max_length=20),
            preserve_default=False,
        ),
    ]
