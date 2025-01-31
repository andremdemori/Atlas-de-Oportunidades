# Generated by Django 4.0.6 on 2023-03-17 00:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Spreadsheet_register',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Sheet_name', models.TextField(blank=True, null=True, verbose_name='Sheet_name')),
                ('Date', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Spreadsheet_register',
                'verbose_name_plural': 'Spreadsheet_register',
            },
        ),
    ]
