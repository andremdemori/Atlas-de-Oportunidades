# Generated by Django 4.0.6 on 2023-04-17 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sectors', '0006_sectorssensus_geo_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sectorssensus',
            name='id',
        ),
        migrations.AddField(
            model_name='sectorssensus',
            name='ID',
            field=models.BigIntegerField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sectorssensus',
            name='cd_geocodi',
            field=models.CharField(default=1, max_length=255, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]