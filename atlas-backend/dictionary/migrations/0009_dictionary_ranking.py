# Generated by Django 4.0.6 on 2023-04-10 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0008_remove_dictionary_comments_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictionary',
            name='ranking',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
