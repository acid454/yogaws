# Generated by Django 3.2.19 on 2024-01-23 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ywsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWorkoutProps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prop_id', models.CharField(max_length=120)),
                ('value', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
