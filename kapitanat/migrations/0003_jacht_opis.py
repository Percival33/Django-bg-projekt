# Generated by Django 3.2.6 on 2021-08-25 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kapitanat', '0002_auto_20210825_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='jacht',
            name='opis',
            field=models.TextField(default='#'),
        ),
    ]