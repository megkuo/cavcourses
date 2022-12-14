# Generated by Django 4.1.3 on 2022-11-24 03:41

import classlist.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USERNAME_FIELD', models.CharField(default='User', max_length=150)),
                ('first_name', models.CharField(blank=True, default='User', max_length=150)),
                ('last_name', models.CharField(blank=True, default='Name', max_length=150)),
                ('email', models.EmailField(default='none@gmail.com', max_length=150)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last date logged in')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_authenticated', models.BooleanField(default=True)),
                ('is_anonymous', models.BooleanField(default=False)),
                ('avatar', models.URLField(default='/static/classlist/default_account_image.png')),
                ('account_created', models.BooleanField(default=False)),
                ('major', models.CharField(default=True, max_length=100)),
                ('year', models.IntegerField(choices=[(1, 'First year'), (2, 'Second year'), (3, 'Third year'), (4, 'Fourth year'), (5, 'Other')], default=5)),
                ('friends', models.ManyToManyField(blank=True, related_name='my_friends', to='classlist.account')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date updated')),
                ('catalog_number', models.CharField(max_length=100)),
                ('semester_code', models.IntegerField(default=0)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('units', models.CharField(blank=True, max_length=100)),
                ('subject', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_abbr', models.CharField(max_length=100)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last updated')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('email', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('course_dept', models.CharField(blank=True, max_length=100)),
                ('course_num', models.CharField(blank=True, max_length=100)),
                ('section_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('section_number', models.CharField(blank=True, max_length=100)),
                ('component', models.CharField(blank=True, max_length=100)),
                ('capacity', models.IntegerField(default=0)),
                ('wait_list', models.IntegerField(default=0)),
                ('wait_cap', models.IntegerField(default=0)),
                ('enrollment_total', models.IntegerField(default=0)),
                ('enrollment_available', models.IntegerField(default=0)),
                ('topic', models.CharField(blank=True, max_length=200)),
                ('course', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='classlist.course')),
                ('instructor', models.ForeignKey(default=classlist.models.Instructor.get_default_instructor, on_delete=django.db.models.deletion.CASCADE, to='classlist.instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Meetings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(blank=True, max_length=100)),
                ('start_time', models.CharField(blank=True, max_length=100)),
                ('end_time', models.CharField(blank=True, max_length=100)),
                ('facility_description', models.CharField(blank=True, max_length=200)),
                ('monday', models.BooleanField(blank=True, default=False)),
                ('tuesday', models.BooleanField(blank=True, default=False)),
                ('wednesday', models.BooleanField(blank=True, default=False)),
                ('thursday', models.BooleanField(blank=True, default=False)),
                ('friday', models.BooleanField(blank=True, default=False)),
                ('section', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='classlist.section')),
            ],
        ),
        migrations.CreateModel(
            name='Friend_Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='classlist.account')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='classlist.account')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(default=classlist.models.Department.get_default_dept, on_delete=django.db.models.deletion.CASCADE, to='classlist.department'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250)),
                ('from_user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_comments', to='classlist.account')),
                ('to_user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedule_comments', to='classlist.account')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('scheduleUser', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='classlist.account')),
                ('classRoster', models.ManyToManyField(blank=True, default=None, related_name='user_course', to='classlist.section')),
            ],
        ),
    ]
