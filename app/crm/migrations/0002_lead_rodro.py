# Generated by Django 3.2.4 on 2022-06-22 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='rodro',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]