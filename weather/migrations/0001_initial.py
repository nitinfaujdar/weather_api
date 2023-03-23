# Generated by Django 4.1.5 on 2023-03-23 13:00

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Shop Name')),
                ('city', models.CharField(blank=True, max_length=155, null=True, verbose_name='Address')),
                ('temperature', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created_at')),
                ('monday', models.CharField(blank=True, max_length=150)),
                ('tuesday', models.CharField(blank=True, max_length=150)),
                ('wednesday', models.CharField(blank=True, max_length=150)),
                ('thursday', models.CharField(blank=True, max_length=150)),
                ('friday', models.CharField(blank=True, max_length=150)),
                ('saturday', models.CharField(blank=True, max_length=150)),
                ('sunday', models.CharField(blank=True, max_length=150)),
                ('date', models.DateField(auto_now=True, db_index=True)),
            ],
            options={
                'verbose_name': 'weather_data',
                'verbose_name_plural': 'weather_data',
                'db_table': 'weather_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone')),
                ('username', models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='Username')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email Address')),
                ('password', models.CharField(blank=True, max_length=155, null=True, verbose_name='Password')),
                ('otp', models.CharField(blank=True, max_length=10, null=True, verbose_name='otp')),
                ('is_otp_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'app_user',
                'verbose_name_plural': 'app_user',
                'db_table': 'app_user',
                'managed': True,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]