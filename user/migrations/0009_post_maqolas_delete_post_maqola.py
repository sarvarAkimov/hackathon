# Generated by Django 4.0.5 on 2022-06-04 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_post_maqola'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_maqolas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('img', models.ImageField(upload_to='media')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.xamshira')),
            ],
        ),
        migrations.DeleteModel(
            name='Post_maqola',
        ),
    ]
