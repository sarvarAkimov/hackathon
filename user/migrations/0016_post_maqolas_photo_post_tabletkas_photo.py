# Generated by Django 4.0.5 on 2022-06-04 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_xamshira_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_maqolas',
            name='photo',
            field=models.ImageField(default=1, upload_to='media'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post_tabletkas',
            name='photo',
            field=models.ImageField(default=1, upload_to='media'),
            preserve_default=False,
        ),
    ]