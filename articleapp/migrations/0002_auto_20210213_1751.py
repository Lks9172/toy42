# Generated by Django 3.1.5 on 2021-02-13 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Introduce',
            new_name='introduce',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='',
            new_name='',
        ),
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
