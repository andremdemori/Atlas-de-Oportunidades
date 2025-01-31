# Generated by Django 4.0.6 on 2023-03-21 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('agency', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('name', models.CharField(default=None, max_length=255, primary_key=True, serialize=False)),
                ('id_sheet', models.CharField(blank=True, max_length=255, null=True)),
                ('description_en', models.TextField(blank=True, default=None, null=True)),
                ('description_ptbr', models.TextField(blank=True, default=None, null=True)),
                ('label_en', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('label_ptbr', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('Unit', models.CharField(blank=True, default=None, max_length=12, null=True)),
                ('format', models.CharField(blank=True, default='Int', max_length=12, null=True)),
                ('new_classification_ptbr', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('new_classification_en', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('comments_en', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('comments_ptbr', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('Spreadsheet_register', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='upload.spreadsheet_register')),
            ],
        ),
    ]
