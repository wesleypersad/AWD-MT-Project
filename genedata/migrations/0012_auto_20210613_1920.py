# Generated by Django 3.0.3 on 2021-06-13 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genedata', '0011_auto_20210613_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organism',
            name='taxa_id',
            field=models.CharField(max_length=200),
        ),
    ]