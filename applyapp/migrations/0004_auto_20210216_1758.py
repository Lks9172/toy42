# Generated by Django 3.1.5 on 2021-02-16 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applyapp', '0003_apply_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='comment',
            field=models.TextField(default='대기중입니다.', max_length=200, null=True),
        ),
    ]