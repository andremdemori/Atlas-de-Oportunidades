# Generated by Django 4.0.6 on 2023-04-15 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sectors', '0002_alter_sectors_cd_dist_alter_sectors_cd_mun_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectors',
            name='cd_dist',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sectors',
            name='cd_mun',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sectors',
            name='cd_setor',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='sectors',
            name='cd_sit',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sectors',
            name='cd_subdist',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sectors',
            name='cd_uf',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sectors',
            name='nm_dist',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sectors',
            name='nm_mun',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sectors',
            name='nm_sit',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sectors',
            name='nm_subdist',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sectors',
            name='nm_uf',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sectors',
            name='sigla_uf',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
