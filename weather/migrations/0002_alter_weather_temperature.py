# Generated by Django 4.1.5 on 2023-03-24 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='temperature',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]