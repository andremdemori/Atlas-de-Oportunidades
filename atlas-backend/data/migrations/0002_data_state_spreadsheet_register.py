# Generated by Django 4.0.6 on 2023-03-21 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_state',
            name='Spreadsheet_register',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='upload.spreadsheet_register'),
        ),
    ]