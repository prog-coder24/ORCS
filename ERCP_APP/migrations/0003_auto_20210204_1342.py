# Generated by Django 3.1.6 on 2021-02-04 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERCP_APP', '0002_remove_formdetail_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carddetail',
            name='journey_to',
            field=models.CharField(default='Matunga Road', max_length=50),
        ),
    ]
