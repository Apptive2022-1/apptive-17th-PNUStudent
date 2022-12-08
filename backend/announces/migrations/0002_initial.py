# Generated by Django 4.1.3 on 2022-12-08 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('announces', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announce',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announces', to=settings.AUTH_USER_MODEL),
        ),
    ]
