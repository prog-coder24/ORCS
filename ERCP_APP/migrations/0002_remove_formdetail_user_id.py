# Generated by Django 3.1.6 on 2021-02-04 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ERCP_APP', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formdetail',
            name='user_id',
        ),
    ]
