# Generated by Django 3.2 on 2021-05-29 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='genre',
            field=models.CharField(default='drama', max_length=200),
        ),
    ]
