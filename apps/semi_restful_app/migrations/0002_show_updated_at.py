# Generated by Django 2.2.1 on 2019-07-25 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi_restful_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]