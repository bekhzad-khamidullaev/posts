# Generated by Django 4.2 on 2023-05-02 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_auto_20230502_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(default='Lorem epsum', max_length=255, verbose_name='Заголовок'),
        ),
    ]