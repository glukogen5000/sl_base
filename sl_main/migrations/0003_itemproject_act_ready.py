# Generated by Django 3.1.7 on 2021-03-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sl_main', '0002_auto_20210310_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemproject',
            name='act_ready',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Нет', 'Нет')], max_length=250, null=True, verbose_name='ИД загружена'),
        ),
    ]
