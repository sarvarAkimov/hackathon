# Generated by Django 4.0.5 on 2022-06-04 07:43

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_xamshira_passport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_maqola',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('post', django_quill.fields.QuillField()),
            ],
        ),
    ]
