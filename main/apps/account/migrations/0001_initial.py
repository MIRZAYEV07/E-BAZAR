# Generated by Django 4.1.1 on 2022-09-23 13:11

from django.db import migrations, models
import main.apps.account.models.user
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('phone_number', models.CharField(error_messages={'unique': 'User with this phone number already exists.'}, max_length=15, unique=True, verbose_name='Phone number')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('unique_identifier', models.PositiveIntegerField(blank=True, null=True, unique=True)),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('activating_code', models.CharField(blank=True, max_length=6, null=True)),
                ('profile_picture', models.ImageField(blank=True, upload_to=main.apps.account.models.user.upload_profile_images)),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('username', models.CharField(max_length=100, null=True, unique=True)),
                ('otp', models.CharField(max_length=6, null=True)),
                ('is_verified', models.BooleanField(default=False, null=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting account.', verbose_name='active')),
                ('is_moderator', models.BooleanField(default=False, verbose_name='moderator status')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=15)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'ordering': ('-id',),
            },
        ),
    ]
