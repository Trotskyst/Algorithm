# Generated by Django 2.2.1 on 2019-05-06 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alg_list', '0003_auto_20190506_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupalgorithm',
            name='slug',
            field=models.CharField(blank=True, max_length=200, verbose_name='ЧПУ'),
        ),
    ]