# Generated by Django 3.2.9 on 2021-12-02 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20211202_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='body',
            field=models.CharField(max_length=280),
        ),
    ]
