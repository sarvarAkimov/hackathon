# Generated by Django 4.0.5 on 2022-06-04 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_kassallik_post_tabletkas'),
    ]

    operations = [
        migrations.AddField(
            model_name='xamshira',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
