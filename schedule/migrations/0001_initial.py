# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-19 18:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DaySchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(choices=[('1', '1'), ('2', '2')], max_length=5, verbose_name='Неделя')),
                ('day', models.CharField(choices=[('mon', 'Понедельник'), ('tue', 'Вторник'), ('wed', 'Среда'), ('thu', 'Четверг'), ('fri', 'Пятница'), ('sat', 'Суббота')], max_length=20, verbose_name='День')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('key', models.CharField(max_length=10, verbose_name='Кодовое название')),
            ],
            options={
                'verbose_name_plural': 'факультеты',
                'verbose_name': 'факультет',
            },
        ),
        migrations.CreateModel(
            name='LectureRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_number', models.IntegerField(choices=[(0, '8:00 - 9:35'), (1, '9:50 - 11:25'), (2, '11:40 - 13:15'), (3, '13:30 - 15:05'), (4, '15:20 - 16:55'), (5, '17:10 - 18:45'), (6, '19:00 - 20:35'), (7, '20:50 - 22:25')], verbose_name='Пара')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.DaySchedule')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'должности',
                'verbose_name': 'должность',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Position', verbose_name='Должность')),
            ],
            options={
                'verbose_name_plural': 'преподаватели',
                'verbose_name': 'преподаватель',
            },
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'звания',
                'verbose_name': 'звание',
            },
        ),
        migrations.CreateModel(
            name='StudyGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Faculty', verbose_name='Факультет')),
            ],
        ),
        migrations.CreateModel(
            name='StudySubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('type', models.CharField(choices=[('lect', 'Лекция'), ('pract', 'Практика')], max_length=20, verbose_name='Вид')),
            ],
        ),
        migrations.AddField(
            model_name='professor',
            name='rank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Rank', verbose_name='Звание'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.StudySubject', verbose_name='Предмет'),
        ),
        migrations.AddField(
            model_name='dayschedule',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.StudyGroup', verbose_name='Группа'),
        ),
    ]
