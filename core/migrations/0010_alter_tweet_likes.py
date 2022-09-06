# Generated by Django 3.2.9 on 2021-12-02 06:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0009_alter_tweet_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='likes',
            field=models.ManyToManyField(blank=True, default=0, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]