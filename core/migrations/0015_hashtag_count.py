# Generated by Django 3.2.9 on 2021-12-02 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_hashtag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='hashtag',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
