# Generated by Django 3.0.5 on 2020-05-03 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200503_1337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='ags',
            new_name='tags',
        ),
    ]
