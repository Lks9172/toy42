# Generated by Django 3.1.5 on 2021-02-02 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0004_auto_20210202_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='designer',
        ),
        migrations.RemoveField(
            model_name='article',
            name='dev',
        ),
        migrations.RemoveField(
            model_name='article',
            name='pd',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='now_designer',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='now_dev',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='now_pd',
        ),
        migrations.AddField(
            model_name='article',
            name='now_designer',
            field=models.IntegerField(choices=[(0, '0'), (4, '4'), (8, '8'), (6, '6'), (7, '7'), (3, '3'), (1, '1'), (9, '9'), (5, '5'), (10, '10'), (2, '2')], default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='now_dev',
            field=models.IntegerField(choices=[(0, '0'), (4, '4'), (8, '8'), (6, '6'), (7, '7'), (3, '3'), (1, '1'), (9, '9'), (5, '5'), (10, '10'), (2, '2')], default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='now_pd',
            field=models.IntegerField(choices=[(0, '0'), (4, '4'), (8, '8'), (6, '6'), (7, '7'), (3, '3'), (1, '1'), (9, '9'), (5, '5'), (10, '10'), (2, '2')], default=0),
        ),
        migrations.AddField(
            model_name='teammember',
            name='designer',
            field=models.IntegerField(choices=[(0, '0'), (4, '4'), (8, '8'), (6, '6'), (7, '7'), (3, '3'), (1, '1'), (9, '9'), (5, '5'), (10, '10'), (2, '2')], default=0),
        ),
        migrations.AddField(
            model_name='teammember',
            name='dev',
            field=models.IntegerField(choices=[(0, '0'), (4, '4'), (8, '8'), (6, '6'), (7, '7'), (3, '3'), (1, '1'), (9, '9'), (5, '5'), (10, '10'), (2, '2')], default=0),
        ),
        migrations.AddField(
            model_name='teammember',
            name='pd',
            field=models.IntegerField(choices=[(0, '0'), (4, '4'), (8, '8'), (6, '6'), (7, '7'), (3, '3'), (1, '1'), (9, '9'), (5, '5'), (10, '10'), (2, '2')], default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='lapse',
            field=models.IntegerField(choices=[(1, '팀빌딩'), (3, '기획완료'), (2, '아이디어 구상')]),
        ),
        migrations.AlterField(
            model_name='article',
            name='local',
            field=models.CharField(choices=[('061', '전라남도'), ('031', '경기도'), ('053', '대구광역시'), ('064', '제주특별자치도'), ('044', '세종특별자치시'), ('054', '경상북도'), ('051', '부산광역시'), ('02', '서울특별시'), ('033', '강원도'), ('042', '대전광역시'), ('041', '충청남도'), ('043', '충청북도'), ('032', '인천광역시'), ('052', '울산광역시'), ('055', '경상남도'), ('063', '전라북도'), ('062', '광주광역시')], max_length=3),
        ),
    ]
