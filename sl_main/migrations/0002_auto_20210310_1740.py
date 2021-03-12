# Generated by Django 3.1.7 on 2021-03-10 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sl_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemproject',
            name='data_ready_from_dogovor',
            field=models.DateField(blank=True, null=True, verbose_name='Срок завершения работ по договору'),
        ),
        migrations.AddField(
            model_name='itemproject',
            name='foto_montaj_upload',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Нет', 'Нет')], max_length=250, null=True, verbose_name='ФОТО монтажа + схемы для ИД приложены'),
        ),
        migrations.AddField(
            model_name='itemproject',
            name='id_ready',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Нет', 'Нет')], max_length=250, null=True, verbose_name='ИД загружена'),
        ),
        migrations.AddField(
            model_name='itemproject',
            name='komentariy',
            field=models.TextField(blank=True, null=True, verbose_name='Коментарий'),
        ),
        migrations.AddField(
            model_name='itemproject',
            name='plan_data_ready_smr',
            field=models.DateField(blank=True, null=True, verbose_name='Плановая дата завершение СМР'),
        ),
        migrations.AddField(
            model_name='itemproject',
            name='rtk_ready',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Нет', 'Нет')], max_length=250, null=True, verbose_name='Примека РТК проведена'),
        ),
        migrations.AddField(
            model_name='itemproject',
            name='smr_ready',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Нет', 'Нет')], max_length=250, null=True, verbose_name='СМР выполнены'),
        ),
    ]
