# Generated by Django 3.1.6 on 2021-02-04 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ERCP_APP', '0004_auto_20210204_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdetail',
            name='journey_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source', to='ERCP_APP.carddetail'),
        ),
    ]