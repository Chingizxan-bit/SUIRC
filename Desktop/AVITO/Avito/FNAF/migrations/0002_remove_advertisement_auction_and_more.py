# Generated by Django 4.2.4 on 2023-08-16 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FNAF', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='auction',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='author',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='category',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='creatied_at',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='description',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='location',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='price',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='title',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='updated_at',
        ),
        migrations.AlterModelTable(
            name='advertisement',
            table='advertisements',
        ),
    ]