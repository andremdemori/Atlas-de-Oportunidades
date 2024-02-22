# Generated by Django 4.0.6 on 2023-04-17 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sectors', '0004_sectorssensus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sectorssensus',
            old_name='cd_dist',
            new_name='cd_geocodb',
        ),
        migrations.RenameField(
            model_name='sectorssensus',
            old_name='cd_mun',
            new_name='cd_geocodd',
        ),
        migrations.RenameField(
            model_name='sectorssensus',
            old_name='cd_sit',
            new_name='cd_geocodi',
        ),
        migrations.RenameField(
            model_name='sectorssensus',
            old_name='cd_subdist',
            new_name='cd_geocodm',
        ),
        migrations.RenameField(
            model_name='sectorssensus',
            old_name='cd_uf',
            new_name='cd_geocods',
        ),
        migrations.RenameField(
            model_name='sectorssensus',
            old_name='nm_dist',
            new_name='nm_bairro',
        ),
        migrations.RenameField(
            model_name='sectorssensus',
            old_name='nm_mun',
            new_name='nm_distrit',
        ),
        migrations.RenameField(
            model_name='sectorssensus',
            old_name='nm_sit',
            new_name='nm_meso',
        ),
        migrations.RenameField(
            model_name='sectorssensus',
            old_name='nm_uf',
            new_name='nm_micro',
        ),
        migrations.RenameField(
            model_name='sectorssensus',
            old_name='sigla_uf',
            new_name='nm_municip',
        ),
        migrations.RemoveField(
            model_name='sectorssensus',
            name='cd_setor',
        ),
        migrations.AddField(
            model_name='sectorssensus',
            name='tipo',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sectorssensus',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]