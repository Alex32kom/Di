# Generated by Django 5.0.6 on 2024-10-24 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmsslider',
            name='cms_text',
            field=models.CharField(max_length=500, verbose_name='Текст'),
        ),
    ]