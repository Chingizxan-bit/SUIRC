# Generated by Django 4.2.4 on 2023-08-17 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FNAF', '0013_advertisement_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='description',
            new_name='content',
        ),
    ]
