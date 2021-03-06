# Generated by Django 4.0.5 on 2022-06-04 13:47

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254)),
                ('full_name', models.CharField(blank=True, max_length=450)),
                ('password', models.CharField(max_length=150)),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('followers', models.ManyToManyField(related_name='followed', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('savol', models.TextField()),
                ('is_closed', models.BooleanField(default=False)),
                ('from_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='chat_from_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hospitals',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=250)),
                ('longitud', models.CharField(max_length=150)),
                ('latitud', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Xamshira',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('passport', models.FileField(blank=True, null=True, upload_to='pasports')),
                ('minut_10', models.BigIntegerField()),
                ('minut_20', models.BigIntegerField()),
                ('kasb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='occupations', to='medbro.occupation')),
                ('shifoxona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospital', to='medbro.hospitals')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('from_card', models.BigIntegerField()),
                ('to_card', models.BigIntegerField()),
                ('summ', models.BigIntegerField()),
                ('to_us', models.BigIntegerField()),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='money_from', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('text', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('chat', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nft_chat', to='medbro.chat')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nft_to', to=settings.AUTH_USER_MODEL)),
                ('xamshira', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='del_xamshira', to='medbro.xamshira')),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='from_users', to=settings.AUTH_USER_MODEL)),
                ('like', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='hospitals',
            name='main_nurse',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='medbro.xamshira'),
        ),
        migrations.AddField(
            model_name='hospitals',
            name='tez_yordam',
            field=models.ManyToManyField(blank=True, related_name='tezyordam', to='medbro.xamshira'),
        ),
        migrations.CreateModel(
            name='Check_time',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField()),
                ('from_user_check', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='check_from', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='time', to='medbro.xamshira')),
                ('vaqt', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='time', to='medbro.time')),
            ],
        ),
        migrations.AddField(
            model_name='chat',
            name='messages',
            field=models.ManyToManyField(related_name='all_messages', to='medbro.messages'),
        ),
        migrations.AddField(
            model_name='chat',
            name='to_users',
            field=models.ManyToManyField(related_name='xamshiras', to='medbro.xamshira'),
        ),
    ]
