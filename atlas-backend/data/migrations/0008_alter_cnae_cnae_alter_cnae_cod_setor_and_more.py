# Generated by Django 4.0.6 on 2023-09-14 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_cnae_spreadsheet_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cnae',
            name='cnae',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cnae',
            name='cod_setor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cnae',
            name='descricao',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cnae',
            name='nome_setor',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
